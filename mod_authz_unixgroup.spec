Summary: External group accesss module for the Apache HTTP Server
Name: mod_authz_unixgroup
Version: 1.1.0
Release: 1%{?dist}
Group: System Environment/Daemons
License: Apache License
URL: http://code.google.com/p/mod-auth-external
Source0: http://mod-auth-external.googlecode.com/files/%{name}-%{version}.tar.gz
Source1: mod_authz_unixgroup.conf
BuildRequires: httpd-devel

%description
An apache group access module.

%prep
%setup -q
%build
%{_bindir}/apxs -c mod_authz_unixgroup.c

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/httpd/modules
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d

install -m0755 .libs/*.so %{buildroot}%{_libdir}/httpd/modules/
install -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/authz_unixgroup.conf

%files
%doc CHANGES INSTALL LICENSE NOTICE README
%config(noreplace) %{_sysconfdir}/httpd/conf.d/authz_unixgroup.conf
%{_libdir}/httpd/modules/mod_authz_unixgroup.so

%changelog
* Wed Jun  4 2014 ClearFoundation <developer@clearfoundation.com> 1.1.0-1
- Updated to 1.1.0

* Thu Apr  5 2012 ClearFoundation <developer@clearfoundation.com> 1.0.3-1
- Import
