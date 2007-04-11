# TODO
# - fix amd64 build (*MUST USE* %{_libdir} for arch dependant files)
#   to do that  fix Makefile so that it will either install to /usr/lib if 32bit arch
#   or to /usr/lib64 if 64bit arch - we could then safely use %{_libdir} macro

Summary:	Hardinfo - benchmark tool
Summary(pl):	Hardinfo
Name:		hardinfo
Version:	0.4.2.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/hardinfo/%{name}-%{version}.tar.bz2
# Source0-md5:	6eaa923cc2051d6ab1bb7a7350c27699
URL:		http://hardinfo.berlios.de/web/HomePage
BuildRequires:	gtk+2-devel >= 2.6.0
BuildRequires:	libsoup-devel >= 2.2.7
BuildRequires:	pciutils
Requires:	pciutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HardInfo is a system information and benchmark tool for Linux systems.
This tool can gather information about your system's hardware and operating 
system, perform benchmarks and generate printable reports either in HTML or 
in plain text formats. 

#%description -l pl

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hardinfo
%dir %{_prefix}/lib/hardinfo
%{_prefix}/lib/hardinfo/*
%{_datadir}/*
