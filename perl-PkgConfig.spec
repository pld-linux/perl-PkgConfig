#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	PkgConfig
Summary:	PkgConfig - Pure-Perl Core-Only replacement for pkg-config
Summary(pl.UTF-8):	PkgConfig - czysto perlowy zamiennik programu pkg-config
Name:		perl-PkgConfig
Version:	0.25026
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PL/PLICEASE/PkgConfig-%{version}.tar.gz
# Source0-md5:	1f6e26df235d3aa6123a8f1849cd1903
URL:		https://metacpan.org/release/PkgConfig
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.56
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.94
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PkgConfig provides a pure-perl, core-only replacement for the
pkg-config utility.

%description -l pl.UTF-8
Moduł PkgConfig zawiera czysto perlowy, nie korzystający z
zewnętrznych modułów zamiennik programu pkg-config.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/pkg-config.pl
%attr(755,root,root) %{_bindir}/ppkg-config
%{perl_vendorlib}/PkgConfig.pm
%{_mandir}/man1/pkg-config.pl.1p*
%{_mandir}/man1/ppkg-config.1p*
%{_mandir}/man3/PkgConfig.3pm*
