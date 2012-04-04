%define pkgversion %(echo %version|sed s/[a-z]//g|sed s/\\\\.//)
%define pkgrelease %(echo %version|sed s/[^a-z]//g)

Name: Nestopia
Version: 1.40h
Release: 6%{?dist}
Summary: A portable open source NES/Famicom emulator       

Group: Applications/Emulators
License: GPLv2+
URL: http://nestopia.sourceforge.net/
Source0: http://dl.sf.net/sourceforge/nestopia/%{name}%{pkgversion}src.zip
# Source1 is not downloadable without a valid browser user agent
Source1: http://rbelmont.mameworld.info/nst%{pkgversion}_lnx_release_%{pkgrelease}.zip
Source2: Nestopia.desktop
Source3: nestopia.sh
Patch0: Nestopia-1.40-fixmakefile.patch
Patch1: Nestopia-1.36-nesntsc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gtk2-devel >= 2.4.0
BuildRequires: SDL-devel >= 1.2.12
BuildRequires: alsa-lib-devel
BuildRequires: zlib-devel
BuildRequires: nes_ntsc-devel
BuildRequires: pkgconfig
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme

%description
Nestopia is a portable open source NES/Famicom emulator written in C++. It's 
designed to be as accurate as possible and supports a large number of 
peripherals. The hardware is emulated at cycle-by-cycle granularity, ensuring 
full support for software that do mid-scanline and other timing trickery. 

Linux porting by R. Belmont.

%prep
%setup -q -c
%setup -q -T -D -a 1

%patch0 -p1
%patch1 -p0

# Fix end-of-line encoding
sed -i 's/\r//' changelog.txt
sed -i 's/\r//' source/linux/7zip/*

# Fix file permissions
chmod 644 source/linux/7zip/*

# Compile with system zlib
sed -i 's/\"..\/zlib\/zlib.h\"/\<zlib.h\>/' source/core/NstZlib.cpp

%build
# It does not compile with smp_mflags
make RPMFLAGS="-c $RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}

# Install main executable
install -d %{buildroot}%{_bindir}
install -m 755 nst %{buildroot}%{_bindir}

# Install data files
install -d %{buildroot}%{_datadir}/%{name}
install -m 644 {nstcontrols,NstDatabase.xml} %{buildroot}%{_datadir}/%{name}

# Install wrapper script
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor dribble        \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert source/win32/resource/window.ico \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/Nestopia.png

%clean
rm -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root)
%{_bindir}/nst
%{_bindir}/nestopia.sh
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/applications/dribble-%{name}.desktop
%doc changelog.txt COPYING README.Linux readme.html

%changelog
* Wed Apr 04 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.40h-6
- Rebuilt

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.40h-5
- Rebuilt for c++ ABI breakage

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.40h-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.40h-3
- rebuild for new F11 features

* Thu Dec 04 2008 Andrea Musuruane <musuruan@gmail.com> 1.40h-2
- Fixed unowned directory (BZ #216)

* Sun Oct 25 2008 Andrea Musuruane <musuruan@gmail.com> 1.40h-1
- updated to 1.40 release h

* Tue Jul 15 2008 Andrea Musuruane <musuruan@gmail.com> 1.40g-1
- updated to 1.40 release g

* Tue Feb 26 2008 Andrea Musuruane <musuruan@gmail.com> 1.37-0.3.pre5
- fixed gcc 4.3 patch with the help of Ian Chapman

* Mon Feb 25 2008 Andrea Musuruane <musuruan@gmail.com> 1.37-0.2.pre5
- added a patch to compile with gcc 4.3

* Sat Feb 23 2008 Andrea Musuruane <musuruan@gmail.com> 1.37-0.1.pre5
- updated to 1.37 preview 5
- removed %%{?_smp_mflags} from make invocation
- changed license due to new guidelines
- removed %%{?dist} tag from changelog
- updated icon cache scriptlets to be compliant to new guidelines

* Sun May 06 2007 Andrea Musuruane <musuruan@gmail.com> 1.36-0.1.pre4
- updated to 1.36 preview 4
- added gtk2-devel, pkgconfig, ImageMagick and desktop-file-utils to BR
- updated SDL-devel version in BR
- added hicolor-icon-theme to Requires
- added desktop file and icon
- added a wrapper script to copy data files under ~/.nestopia and run the
  main executable
- cosmetic changes

* Sat Nov 11 2006 Andrea Musuruane <musuruan@gmail.com> 1.32-0.2.pre1
- added Source1 full URL
- replaced %%{__sed} with sed
- versioning now follows Fedora guidelines
- added a patch from Ian Chapman to increase verbosity and use $RPM_OPT_FLAGS
  in Makefile
- added a patch from Ian Chapman to use the system nes_ntsc instead of bundled
  nes_ntsc
- now using system zlib instead of bundled zlib

* Wed Oct 25 2006 Andrea Musuruane <musuruan@gmail.com> 1.32-0.1.pre1
- initial package

