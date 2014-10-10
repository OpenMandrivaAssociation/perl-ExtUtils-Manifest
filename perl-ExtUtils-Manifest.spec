%define upstream_name    ExtUtils-Manifest
%define upstream_version 1.63
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Utilities for managing MANIFEST files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-Manifest-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildArch:	noarch

%description
Functions
    ExtUtils::Manifest exports no functions by default. The following are
    exported on request

    * mkmanifest

          mkmanifest();

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.600.0-1
+ Revision: 759429
- version update 1.60

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.580.0-5
+ Revision: 656910
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.580.0-4mdv2011.0
+ Revision: 597095
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.580.0-3mdv2011.0
+ Revision: 562423
- rebuild

* Sat Jul 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.580.0-2mdv2011.0
+ Revision: 558159
- rebuild

* Fri Dec 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.580.0-1mdv2010.1
+ Revision: 473268
- update to 1.58

* Mon Sep 21 2009 Jérôme Quelin <jquelin@mandriva.org> 1.570.0-1mdv2010.0
+ Revision: 446430
- update to 1.57

* Mon Aug 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.560.0-2mdv2010.0
+ Revision: 417169
- force rebuild

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.560.0-1mdv2010.0
+ Revision: 381060
- import perl-ExtUtils-Manifest



