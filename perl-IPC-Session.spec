%include	/usr/lib/rpm/macros.perl
%define	pdir	IPC
%define	pnam	Session
Summary:	IPC-Session perl module
Summary(pl):	Modu³ perla IPC-Session
Name:		perl-IPC-Session
Version:	0.05
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
#BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::Session encapsulates the open3() function call (see the IPC::Open3
manpage) and its associated filehandles.  This makes it easy to maintain
multiple interactive command sessions, such as multiple persistent 'ssh'
and/or 'rsh' sessions, within the same perl script.

%description -l pl
IPC::Session obudowuje funkcjê open3() (zobacz stronê podrêcznika
systemowego dla IPC::Open3) i zwi±zane z ni± uchwyty plików. Pozwala to
na ³atwe zarz±dzanie wieloma interaktywnymi sesjami, np. w przypadku
wielu przezroczystych sesji 'ssh' i/lub 'rsh' w jednym skrypcie perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_sitelib}/IPC/Session.pm
%{_mandir}/man3/*.3pm*
