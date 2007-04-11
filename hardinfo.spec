#
# Conditional build:
#

Summary:	Hardinfo
Summary(pl):	Hardinfo
Name:		hardinfo
Version:	0.4.2.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://download.berlios.de/hardinfo/%{name}-%{version}.tar.bz2
# Source0-md5:	6eaa923cc2051d6ab1bb7a7350c27699
URL:		-
BuildRequires:	gtk+2-devel >= 2.6.0
BuildRequires:	libsoup-devel >= 2.2.7
Requires:	/sbin/lspci
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

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
%{_libdir}/hardinfo/*
%{_datadir}/*
#%{_examplesdir}/%{name}-%{version}
