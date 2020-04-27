%define		snap	20200427
Summary:	Hardinfo - benchmark tool
Summary(pl.UTF-8):	Hardinfo - narzędzie informujące o sprzęcie i jego wydajności
Name:		hardinfo
Version:	0.5.1.%{snap}
Release:	2
License:	GPL v2
Group:		X11/Applications
#Source0Download: https://github.com/lpereira/hardinfo/releases
Source0:	https://github.com/lpereira/hardinfo/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	9d7d9e00cb49579c4264b311a8232241
Patch0:		hwdata.patch
Patch1:		format-security.patch
URL:		http://hardinfo.berlios.de/web/HomePage
BuildRequires:	cmake >= 2.6
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	libsoup-devel >= 2.24
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	pciutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HardInfo is a system information and benchmark tool for Linux systems.
This tool can gather information about your system's hardware and
operating system, perform benchmarks and generate printable reports
either in HTML or in plain text formats.

%description -l pl.UTF-8
HardInfo to narzędzie dla systemów linuksowych informujące o systemie
i jego wydajności. Potrafi zbierać informacje o sprzęcie i systemie
operacyjnym, wykonywać testy wydajnościowe i generować nadające się do
druku raporty w formacie HTML lub czystym tekście.

%prep
%setup -q -n %{name}-master
%patch0 -p1
%patch1 -p1

%build
mkdir -p build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.md README.md TODO
%attr(755,root,root) %{_bindir}/hardinfo
%dir %{_libdir}/hardinfo
%dir %{_libdir}/hardinfo/modules
%attr(755,root,root) %{_libdir}/hardinfo/modules/benchmark.so
%attr(755,root,root) %{_libdir}/hardinfo/modules/computer.so
%attr(755,root,root) %{_libdir}/hardinfo/modules/devices.so
%attr(755,root,root) %{_libdir}/hardinfo/modules/network.so
%{_datadir}/hardinfo
%{_desktopdir}/hardinfo.desktop
%{_iconsdir}/hicolor/48x48/apps/hardinfo.png
%{_mandir}/man1/hardinfo.1*
