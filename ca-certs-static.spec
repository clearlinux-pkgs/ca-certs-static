Name:           ca-certs-static
Version:        0.1
Release:        8
License:        MPL-2.0 GPL-2.0
Summary:        Default System Trust Store
Url:            https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/
Source0:        prebuilt-trust-store.service
Group:          base
BuildRequires:  ca-certs
BuildRequires:  openssl
Requires:       filesystem

%description
Default System Trust store.

%prep
rm -rf build

%build
mkdir -p build
CLR_TRUST_STORE=./build clrtrust generate

%install
mkdir -p %{buildroot}/usr/share/ca-certs/.prebuilt-store
cp -r --preserve=mode,links build/* %{buildroot}/usr/share/ca-certs/.prebuilt-store
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
install -m 0644 %{SOURCE0} %{buildroot}/usr/lib/systemd/system/prebuilt-trust-store.service
cd %{buildroot}/usr/lib/systemd/system/multi-user.target.wants && ln -s ../prebuilt-trust-store.service .

%files
/usr/share/ca-certs/.prebuilt-store/*
/usr/lib/systemd/system/prebuilt-trust-store.service
/usr/lib/systemd/system/multi-user.target.wants/prebuilt-trust-store.service
