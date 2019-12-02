Summary:	Library to read DWARF debug information of an ELF object
Summary(pl.UTF-8):	Biblioteka do odczytu informacji debugowych DWARF z obiektów ELF
Name:		libdwarf
Version:	20191104
Release:	1
License:	LGPL v2.1 (library), GPL v2 (utilities)
Group:		Libraries
#Source0Download: https://www.prevanders.net/dwarf.html
Source0:	https://www.prevanders.net/%{name}-%{version}.tar.gz
# Source0-md5:	f5927304b32525f93bccefe2828e802d
URL:		https://www.prevanders.net/dwarf.html
BuildRequires:	elfutils-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to read DWARF debug information of an ELF object.

%description -l pl.UTF-8
Biblioteka do odczytu informacji debugowych DWARF z obiektów ELF.

%package devel
Summary:	Header files for libdwarf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdwarf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	elfutils-devel
Requires:	zlib-devel

%description devel
Header files for libdwarf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdwarf.

%package static
Summary:	Static libdwarf library
Summary(pl.UTF-8):	Statyczna biblioteka libdwarf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdwarf library.

%description static -l pl.UTF-8
Statyczna biblioteka libdwarf.

%package -n dwarfdump
Summary:	Tool for dumps DWARF debug information of an ELF object
Summary(pl.UTF-8):	Narzędzie wypisujące informacje debugowe DWARF z obiektów ELF
License:	GPL v2
Group:		Development/Tools

%description -n dwarfdump
Tool for dumps DWARF debug information of an ELF object.

%description -n dwarfdump -l pl.UTF-8
Narzędzie wypisujące informacje debugowe DWARF z obiektów ELF.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# (another implementation) provided by elfutils
%{__rm} $RPM_BUILD_ROOT%{_includedir}/dwarf.h

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/libdwarf/libdwarf-devel

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc libdwarf/{CHANGES,COPYING,ChangeLog*,NEWS,README}
%attr(755,root,root) %{_libdir}/libdwarf.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libdwarf.so.1

%files devel
%defattr(644,root,root,755)
%doc libdwarf/libdwarf*.pdf
%attr(755,root,root) %{_libdir}/libdwarf.so
%{_libdir}/libdwarf.la
%{_includedir}/libdwarf.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdwarf.a

%files -n dwarfdump
%defattr(644,root,root,755)
%doc dwarfdump/{COPYING,ChangeLog*,NEWS,README}
%attr(755,root,root) %{_bindir}/dwarfdump
%{_datadir}/dwarfdump
%{_mandir}/man1/dwarfdump.1*

%if 0
# not really useful yet
%files -n dwarfgen
%defattr(644,root,root,755)
%doc dwarfgen/{COPYING,ChangeLog,README}
%{_sysconfdir}/dwarfgen.conf
%attr(755,root,root) %{_bindir}/dwarfgen
%{_mandir}/man1/dwarfgen.1*
%endif
