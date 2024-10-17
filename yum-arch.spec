Name:           yum-arch
Version:        2.2.2
Release:        7
Summary:        Extract headers from rpm in a old yum repository
License:        GPL
Group:          System/Configuration/Packaging
URL:            https://linux.duke.edu/yum/
Source0:        http://linux.duke.edu/projects/yum/download/2.2/yum-%{version}.tar.gz
Patch1:         yum-arch-folder.patch
Patch2:         yum-arch-python26.patch
Requires:       python
Requires:       python-rpm
Requires:       python-libxml2
BuildRequires:  python
BuildRequires:  gettext
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Extract headers from rpm in a old yum repository.

This package only provides the old yum-arch command from yum-%{version}
It should be used to generate repository informations for Fedora Core  < 3
and RedHat Enterprise Linux < 4.

%prep
%setup -q -n yum-%{version}
%patch1 -p0 -b .folder
%patch2 -p0

# to avoid rpmlint warnings
for source in *.py {repomd,rpmUtils,yum}/*.py; do
    sed -i -e '/^#!\/usr/d' $source
done

%build
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
%doc README AUTHORS COPYING TODO INSTALL ChangeLog
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man8/%{name}*



%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.2.2-6mdv2010.0
+ Revision: 446313
- rebuild

* Wed Feb 18 2009 Michael Scherer <misc@mandriva.org> 2.2.2-5mdv2009.1
+ Revision: 342505
- fix usage on 2.6, reported by xrg_ on irc

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.2.2-4mdv2009.0
+ Revision: 262956
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.2.2-3mdv2009.0
+ Revision: 262806
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.2-1mdv2008.1
+ Revision: 115431
- import yum-arch


* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.2-1mdv2008.1
- initial mdv release
