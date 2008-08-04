Name:           yum-arch
Version:        2.2.2
Release:        %mkrel 4
Summary:        Extract headers from rpm in a old yum repository
License:        GPL
Group:          System/Configuration/Packaging
URL:            http://linux.duke.edu/yum/
Source0:        http://linux.duke.edu/projects/yum/download/2.2/yum-%{version}.tar.gz
Patch1:         yum-arch-folder.patch
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

