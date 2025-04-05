Summary:	Library to read DWARF debug information of an ELF object
Summary(pl.UTF-8):	Biblioteka do odczytu informacji debugowych DWARF z obiektów ELF
Name:		libdwarf
Version:	0.12.0
Release:	1
Epoch:		1
License:	LGPL v2.1 (library), GPL v2 (utilities)
Group:		Libraries
#Source0Download: https://www.prevanders.net/dwarf.html#releases
Source0:	https://www.prevanders.net/%{name}-%{version}.tar.xz
# Source0-md5:	5253c12000053405b12734f1b8120c76
URL:		https://www.prevanders.net/dwarf.html
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to read DWARF debug information of an ELF object.

%description -l pl.UTF-8
Biblioteka do odczytu informacji debugowych DWARF z obiektów ELF.

%package devel
Summary:	Header files for libdwarf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdwarf
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zlib-devel
Requires:	zstd-devel

%description devel
Header files for libdwarf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdwarf.

%package static
Summary:	Static libdwarf library
Summary(pl.UTF-8):	Statyczna biblioteka libdwarf
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libdwarf library.

%description static -l pl.UTF-8
Statyczna biblioteka libdwarf.

%package apidocs
Summary:	API documentation for libdwarf library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libdwarf
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libdwarf library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libdwarf.

%package -n libdwarfp
Summary:	Library to produce DWARF debug symbols
Summary(pl.UTF-8):	Biblioteka do tworzenia symboli debugowych DWARF
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n libdwarfp
Library to produce DWARF debug symbols.

%description -n libdwarfp -l pl.UTF-8
Biblioteka do tworzenia symboli debugowych DWARF.

%package -n libdwarfp-devel
Summary:	Header files for libdwarfp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdwarfp
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	libdwarfp-devel = %{epoch}:%{version}-%{release}

%description -n libdwarfp-devel
Header files for libdwarfp library.

%description -n libdwarfp-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdwarfp.

%package -n libdwarfp-static
Summary:	Static libdwarfp library
Summary(pl.UTF-8):	Statyczna biblioteka libdwarfp
Group:		Development/Libraries
Requires:	libdwarfp-devel = %{epoch}:%{version}-%{release}

%description -n libdwarfp-static
Static libdwarf libraryp.

%description -n libdwarfp-static -l pl.UTF-8
Statyczna biblioteka libdwarfp.

%package -n libdwarfp-apidocs
Summary:	API documentation for libdwarf library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libdwarf
Group:		Documentation
BuildArch:	noarch

%description -n libdwarfp-apidocs
API documentation for libdwarf library.

%description -n libdwarfp-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libdwarf.

%package -n dwarfdump
Summary:	Tool for dumps DWARF debug information of an ELF object
Summary(pl.UTF-8):	Narzędzie wypisujące informacje debugowe DWARF z obiektów ELF
License:	GPL v2
Group:		Development/Tools

%description -n dwarfdump
Tool for dumps DWARF debug information of an ELF object.

%description -n dwarfdump -l pl.UTF-8
Narzędzie wypisujące informacje debugowe DWARF z obiektów ELF.

%package -n dwarfgen
Summary:	Example DWARF data generator
Summary(pl.UTF-8):	Przykładowy generator informacji DWARF
Group:		Development/Tools
Requires:	libdwarfp = %{epoch}:%{version}-%{release}

%description -n dwarfgen
dwarfgen creates DWARF sections as requested by specific options.

%description -n dwarfgen -l pl.UTF-8
dwarfgen tworzy sekcje DWARF zgodnie z konkretnymi opcjami.

%prep
%setup -q

%build
%configure \
	--enable-dwarfgen \
	--enable-shared \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdwarf*.la

# substitutions missing in configure
%{__sed} -e 's,@requirements_libdwarfp_pc@,,' \
	-e 's,@requirements_libdwarfp_libs@,,' \
	-i $RPM_BUILD_ROOT%{_pkgconfigdir}/libdwarfp.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md src/lib/libdwarf/{CHANGES,COPYING,NEWS,README}
%attr(755,root,root) %{_libdir}/libdwarf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdwarf.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdwarf.so
%dir %{_includedir}/libdwarf-0
%{_includedir}/libdwarf-0/dwarf.h
%{_includedir}/libdwarf-0/libdwarf.h
%{_pkgconfigdir}/libdwarf.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdwarf.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/libdwarf.pdf

%files -n libdwarfp
%defattr(644,root,root,755)
%doc src/lib/libdwarfp/{COPYING,NEWS,README}
%attr(755,root,root) %{_libdir}/libdwarfp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdwarfp.so.0

%files -n libdwarfp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdwarfp.so
%{_includedir}/libdwarf-0/libdwarfp.h
%{_pkgconfigdir}/libdwarfp.pc

%files -n libdwarfp-static
%defattr(644,root,root,755)
%{_libdir}/libdwarfp.a

%files -n libdwarfp-apidocs
%defattr(644,root,root,755)
%doc doc/libdwarfp.pdf

%files -n dwarfdump
%defattr(644,root,root,755)
%doc src/bin/dwarfdump/{COPYING,NEWS,README}
%attr(755,root,root) %{_bindir}/dwarfdump
%{_datadir}/dwarfdump
%{_mandir}/man1/dwarfdump.1*

%files -n dwarfgen
%defattr(644,root,root,755)
%doc src/bin/dwarfgen/{COPYING,NEWS,README}
%attr(755,root,root) %{_bindir}/dwarfgen
%{_mandir}/man1/dwarfgen.1*
