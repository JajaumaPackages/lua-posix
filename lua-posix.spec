%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}
%global commit 58016bbba40b063e8a98a7e9f14acfcd46f103d4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           lua-posix
Version:        33.3.1
Release:        2%{?dist}
Summary:        A POSIX library for Lua
Group:          Development/Libraries
License:        Public Domain
URL:            http://luaforge.net/projects/luaposix/
Source0:        https://github.com/luaposix/luaposix/archive/release-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  lua-devel
BuildRequires:  ncurses-devel
BuildRequires:	lua-lunit
%if 0%{?fedora} || 0%{?rhel} >= 7
Requires:       lua(abi) = %{luaver}
%else
Requires:       lua >= %{luaver}
%endif

%description
This is a POSIX library for Lua which provides access to many POSIX features
to Lua programs.

%prep
%setup -q -n luaposix-release-v%{version}


%build
%configure --libdir=%{lualibdir} --datadir=/%{luapkgdir}
make V=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%check
make V=1 check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_defaultdocdir}/luaposix/
%{lualibdir}/*
%{luapkgdir}/*.lua
%{luapkgdir}/posix/


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 33.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 17 2015 Orion Poplawski <orion@cora.nwra.com> - 33.3.1-1
- Update to 33.3.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 26 2015 Orion Poplawski <orion@cora.nwra.com> - 33.2.1-1
- Update to 33.2.1

* Tue Feb 24 2015 Orion Poplawski <orion@cora.nwra.com> - 32-4
- Update spec to match packaging draft, rebuild for lua 5.3 (bug #1195707)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 4 2014 Orion Poplawski <orion@cora.nwra.com> - 32-1
- Update to version 32

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Tom Callaway <spot@fedoraproject.org> - 5.1.28-1
- update to 5.1.28, lua 5.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 27 2011 Michel Salim <salimma@fedoraproject.org> - 5.1.14-1
- Update to 5.1.14

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 15 2010 Tim Niemueller <tim@niemueller.de> - 5.1.7-1
- Update to 5.1.7
- Add -fPIC to CFLAGS

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Tim Niemueller <tim@niemueller.de> - 5.1.4-1
- Update to 5.1.4

* Sat Apr 05 2008 Tim Niemueller <tim@niemueller.de> - 5.1.2-2
- Set proper CFLAGS for valid debuginfo

* Fri Apr 04 2008 Tim Niemueller <tim@niemueller.de> - 5.1.2-1
- Initial package

