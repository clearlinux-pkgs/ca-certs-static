Name:           ca-certs-static
Version:        0.1
Release:        1
License:        MPL-2.0 GPL-2.0
Summary:        Default System Trust Store
Url:            https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/
Group:          base
BuildRequires:  ca-certs
BuildRequires:  /usr/bin/c_rehash

%description
Default System Trust store.

%prep
rm -rf build

%build
mkdir -p build
clrmakets build

%install
mkdir -p %{buildroot}/var/cache/ca-certs
cp -r --preserve=mode,links build/* %{buildroot}/var/cache/ca-certs

%files
/var/cache/ca-certs/*
