Summary: Utility for getting and setting Xv attributes
Name: xvattr
Version: 1.3
Release: 18%{?dist}
License: GPLv2+
Group: User Interface/X
URL: http://www.dtek.chalmers.se/groups/dvd/
Source: http://www.dtek.chalmers.se/groups/dvd/dist/xvattr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libXt-devel, libXv-devel
BuildRequires: autoconf automake libtool

ExcludeArch: s390 s390x

Patch0: xvattr-1.3-no-gtk.patch

%description
This program is used for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY, etc.


%prep
%setup -q
%patch0 -p1 -b .jx
# Convert man page to UTF-8
iconv -f iso8859-1 -t utf-8 -o tmp xvattr.1
%{__mv} -f tmp xvattr.1


%build
autoreconf -v --install
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Thu Feb 25 2010 Adam Jackson <ajax@redhat.com> 1.3-18
- Add dist tag. Remove gtk1 dep. ExcludeArch: s390*. Build for EL6. (#216921)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-15
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 1.3-14
- Rebuild for new BuildID feature.
- Remove dist tag, since the package will seldom change.

* Fri Aug  3 2007 Matthias Saou <http://freshrpms.net/> 1.3-13
- Update License field.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 1.3-12
- Switch to using DESTDIR install method.
- Convert man page to UTF-8... not?

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.3-11
- FC6 rebuild.

* Tue May 23 2006 Matthias Saou <http://freshrpms.net/> 1.3-10
- Fix CFLAGS so that our optflags get used too (Ville, #192611).

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.3-9
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.3-8
- Rebuild for new gcc/glibc and modular X.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.3-7
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 1.3-5
- Bump release to provide Extras upgrade path.

* Wed Mar 24 2004 Matthias Saou <http://freshrpms.net/> 1.3-4
- Remove explicit XFree86 dependency for the binary package.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Oct 4 2002 Matthias Saou <http://freshrpms.net/>
- Initial rpm release.

