#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	IPC
%define		pnam	Session
Summary:	Drive ssh or other interactive shell, local or remote (like 'expect')
Summary(pl.UTF-8):	Sterowanie ssh lub inną interaktywną powłoką lokalną lub zdalną (podobnie do expect)
Name:		perl-IPC-Session
Version:	0.05
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa56a95d08ebfc11edff3d9e9515d93c
URL:		http://search.cpan.org/dist/IPC-Session/
%{?with_tests:BuildRequires:	/bin/csh}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::Session encapsulates the open3() function call (see the
IPC::Open3 manpage) and its associated filehandles. This makes it easy
to maintain multiple interactive command sessions, such as multiple
persistent 'ssh' and/or 'rsh' sessions, within the same perl script.

%description -l pl.UTF-8
IPC::Session obudowuje funkcję open3() (zobacz stronę podręcznika
systemowego dla IPC::Open3) i związane z nią uchwyty plików. Pozwala
to na łatwe zarządzanie wieloma interaktywnymi sesjami, np. w
przypadku wielu przezroczystych sesji 'ssh' i/lub 'rsh' w jednym
skrypcie Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_vendorlib}/IPC/Session.pm
%{_mandir}/man3/*.3pm*
