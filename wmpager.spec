Summary:	Dockapp for changin active destop
Summary(pl):	Dockapp do zmiany aktywnego pulpitu
Name:		wmpager
Version:	1.2
Release:	2
License:	Free
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/sourceforge/wmpager/%{name}-%{version}.tar.gz
# Source0-md5:	402f6678bc29d5c355e9bc79a28faf59
Patch0:		%{name}-makefile.patch
URL:		http://wmpager.sourceforge.net
BuildRequires:	XFree86-devel
Requires:	XFree86
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dockapp application for changing active desktop.

%description -l pl
Aplikacja dokujaca do zmiany aktywnego pulpitu.

%prep
%setup -q 
%patch0 -p1
%{__perl} -pi -e 's@/lib@/%{_lib}@g' src/Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
