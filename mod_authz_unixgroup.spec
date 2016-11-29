Summary: External group accesss module for the Apache HTTP Server
Name: mod_authz_unixgroup
Version: 1.1.0
Release: 2%{?dist}
Group: System Environment/Daemons
License: Apache License
URL: http://code.google.com/p/mod-auth-external
Source0: http://mod-auth-external.googlecode.com/files/%{name}-%{version}.tar.gz
Source1: mod_authz_unixgroup.conf
Source2: 10-authz-unixgroup-webconfig.conf
BuildRequires: httpd-devel

%description
An Apache group access module.

%package webconfig
Summary: External group accesss module for the Webconfig Apache HTTP Server
Group: System Environment/Daemons
BuildRequires: webconfig-httpd-devel

%description webconfig
A Webconfig Apache group access module.

%prep
%setup -q
%build
/usr/clearos/sandbox%{_bindir}/apxs -c mod_authz_unixgroup.c
mv .libs .libs-webconfig

%{_bindir}/apxs -c mod_authz_unixgroup.c

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/httpd/modules
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d %{buildroot}/usr/clearos/sandbox%{_libdir}/httpd/modules
install -d %{buildroot}/usr/clearos/sandbox%{_sysconfdir}/httpd/conf.modules.d

install -m0755 .libs/*.so %{buildroot}%{_libdir}/httpd/modules/
install -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/authz_unixgroup.conf

install -m0755 .libs-webconfig/*.so %{buildroot}/usr/clearos/sandbox%{_libdir}/httpd/modules/
install -m0644 %{SOURCE2} %{buildroot}/usr/clearos/sandbox%{_sysconfdir}/httpd/conf.modules.d/10-authz-unixgroup.conf

%files webconfig
/usr/clearos/sandbox%{_sysconfdir}/httpd/conf.modules.d/10-authz-unixgroup.conf
/usr/clearos/sandbox%{_libdir}/httpd/modules/mod_authz_unixgroup.so

%files
%doc CHANGES INSTALL LICENSE NOTICE README
%config(noreplace) %{_sysconfdir}/httpd/conf.d/authz_unixgroup.conf
%{_libdir}/httpd/modules/mod_authz_unixgroup.so

%changelog
* Tue Nov 29 2016 ClearFoundation <developer@clearfoundation.com. 1.1.0-2
- Added webconfig support

* Wed Jun  4 2014 ClearFoundation <developer@clearfoundation.com> 1.1.0-1
- Updated to 1.1.0

* Thu Apr  5 2012 ClearFoundation <developer@clearfoundation.com> 1.0.3-1
- Import
