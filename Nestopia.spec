%global realname nestopia

Name: Nestopia
Version: 1.53.0
Release: 1%{?dist}
Summary: A portable open source NES/Famicom emulator       

License: GPLv2+
URL: http://0ldsk00l.ca/nestopia/
Source0: https://github.com/0ldsk00l/%{realname}/archive/%{version}.tar.gz#/%{realname}-%{version}.tar.gz
# Debian man page
Source1: %{realname}.6
# AppData from Debian
Source2: %{realname}.appdata.xml
# Use system nes_ntsc
Patch0: %{name}-1.53.0-use-system-nes_ntsc.patch

BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: fltk-devel
BuildRequires: SDL2-devel
BuildRequires: libarchive-devel
BuildRequires: libsamplerate-devel
BuildRequires: zlib-devel
BuildRequires: libepoxy-devel
BuildRequires: nes_ntsc-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires: hicolor-icon-theme

%description
Nestopia is a portable open source NES/Famicom emulator written in C++. It's 
designed to be as accurate as possible and supports a large number of 
peripherals. The hardware is emulated at cycle-by-cycle granularity, ensuring 
full support for software that do mid-scanline and other timing trickery. 

%prep
%setup -q -n %{realname}-%{version}
%patch 0 -p1

# Fix end-of-line encoding
sed -i 's/\r//' ChangeLog

# Remove bundled libs
find source/nes_ntsc/ -type f -not -name "nes_ntsc_config.h" -delete


%build
autoreconf -fvi
%configure \
  --disable-silent-rules
%make_build


%install
%make_install

# Move docs to %%{_pkgdocdir}
mv %{buildroot}%{_docdir}/%{realname} %{buildroot}%{_pkgdocdir}

# Validate desktop file
desktop-file-validate \
   %{buildroot}%{_datadir}/applications/%{realname}.desktop

# Install man page
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man6/

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%{_bindir}/%{realname}
%{_datadir}/%{realname}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{realname}.desktop
%{_datadir}/metainfo/%{realname}.appdata.xml
%{_mandir}/man6/*
%license COPYING
%doc %{_pkgdocdir}

%changelog
* Wed Mar 19 2025 Leigh Scott <leigh123linux@gmail.com> - 1.53.0-1
- Update to 1.53.0

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.52.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 01 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.52.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 30 2024 Andrea Musuruane <musuruan@gmail.com> - 1.52.1-1
- Updated to new upstream release

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.52.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.52.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Dec 30 2022 Andrea Musuruane <musuruan@gmail.com> - 1.52.0-1
- Updated to new upstream release

* Sat Aug 06 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.51.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Tue Feb 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.51.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 28 2021 Andrea Musuruane <musuruan@gmail.com> - 1.51.1-1
- Updated to new upstream release

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.51.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Andrea Musuruane <musuruan@gmail.com> - 1.51.0-1
- Updated to new upstream release

* Tue Feb 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Andrea Musuruane <musuruan@gmail.com> - 1.50-1
- Updated to new upstream release

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jun 27 2018 Andrea Musuruane <musuruan@gmail.com> - 1.49-1
- Updated to new upstream release
- Added gcc-c++ dependency
- Used new AppData directory
- Removed obsolete scriptlets

* Wed Feb 28 2018 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 Andrea Musuruane <musuruan@gmail.com> - 1.48-1
- Updated to new upstream release
- Added AppData from Debian

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 24 2016 Andrea Musuruane <musuruan@gmail.com> - 1.47-1
- Updated to new upstream release
- Updated URL
- Added Debian man page
- Updated Debian patches
- Moved icons in %%{_datadir}/icons/hicolor

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

