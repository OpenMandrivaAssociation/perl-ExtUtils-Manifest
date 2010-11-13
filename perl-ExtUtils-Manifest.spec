%define upstream_name    ExtUtils-Manifest
%define upstream_version 1.58

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Utilities for managing MANIFEST files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Functions
    ExtUtils::Manifest exports no functions by default. The following are
    exported on request

    * mkmanifest

          mkmanifest();

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
