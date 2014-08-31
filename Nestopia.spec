%global realname nestopia

Name: Nestopia
Version: 1.45
Release: 2%{?dist}
Summary: A portable open source NES/Famicom emulator       

License: GPLv2+
URL: http://0ldsk00l.ca/nestopia.html
Source0: http://downloads.sourceforge.net/nestopiaue/%{version}/%{realname}-%{version}.tgz
# Install to FHS-compliant locations and handle DESTDIR
Patch0: %{name}-1.45-install-location.patch
# Use a format specifier with gtk_message_dialog_new
Patch1: %{name}-1.45-format-security.patch
# Use system nes_ntsc
Patch2: Nestopia-1.36-nesntsc.patch

BuildRequires: gtk3-devel
BuildRequires: SDL-devel >= 1.2.12
BuildRequires: alsa-lib-devel
BuildRequires: libarchive-devel
BuildRequires: zlib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: nes_ntsc-devel
BuildRequires: pkgconfig
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme

%description
Nestopia is a portable open source NES/Famicom emulator written in C++. It's 
designed to be as accurate as possible and supports a large number of 
peripherals. The hardware is emulated at cycle-by-cycle granularity, ensuring 
full support for software that do mid-scanline and other timing trickery. 

%prep
%setup -q -n %{realname}-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p0

# Fix end-of-line encoding
sed -i 's/\r//' changelog.txt

# Clean up sources
rm -rf dll lib source/kaillera source/unrar

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
# It does not compile with smp_mflags
make

%install
make install DESTDIR=%{buildroot}

# Validate desktop file
desktop-file-validate \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{realname}.desktop

%files
%{_bindir}/%{realname}
%{_datadir}/%{realname}
%{_datadir}/pixmaps/%{realname}.svg
%{_datadir}/applications/%{realname}.desktop
%doc changelog.txt COPYING README.unix readme.html

%changelog
* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Oct 31 2013 Andrea Musuruane <musuruan@gmail.com> - 1.45-1
- Switch to upstream by R. Danbrook
- Added two patches from Debian
- Updated %%description
- Dropped desktop vendor tag for F-19+
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Dropped cleaning at the beginning of %%install

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.40h-7
- Mass rebuilt for Fedora 19 Features

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

* Sun Oct 26 2008 Andrea Musuruane <musuruan@gmail.com> 1.40h-1
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

