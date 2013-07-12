Summary:	Library to read DWARF debug information of an ELF object
Summary(pl.UTF-8):	Biblioteka do odczytu informacji debugowych DWARF z obiektów ELF
Name:		libdwarf
%define		snap	20130207
Version:	0.%{snap}.1
Release:	2
License:	LGPL v2.1 (library), GPL v2 (utilities)
Group:		Libraries
#Source0Download:	http://reality.sgiweb.org/davea/dwarf.html
Source0:	http://reality.sgiweb.org/davea/%{name}-%{snap}.tar.gz
# Source0-md5:	64b42692e947d5180e162e46c689dfbf
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-link.patch
URL:		http://reality.sgiweb.org/davea/dwarf.html
BuildRequires:	elfutils-devel
BuildRequires:	libstdc++-devel
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
%setup -q -n dwarf-%{snap}
%patch0 -p1
%patch1 -p1

%build
cd libdwarf
%configure \
	--enable-shared
%{__make}

cd ../dwarfdump
%configure
# build races found
%{__make} -j1

cd ../dwarfdump2
%configure
# build races found
%{__make} -j1

cd ../dwarfgen
%configure
%{__make}

%{__make}
%if 0
cd libdwarf
%configure \
	CFLAGS="%{rpmcflags} -fPIC"
%{__make} libdwarf.a libdwarf.so
cd ..
cd dwarfdump
%configure
%{__make} -j1
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_includedir},%{_libdir},%{_mandir}/man1}

install libdwarf/libdwarf.so $RPM_BUILD_ROOT%{_libdir}/libdwarf.so.0.%{snap}
ln -sf libdwarf.so.0.%{snap} $RPM_BUILD_ROOT%{_libdir}/libdwarf.so.0
ln -sf libdwarf.so.0.%{snap} $RPM_BUILD_ROOT%{_libdir}/libdwarf.so
install libdwarf/libdwarf.a $RPM_BUILD_ROOT%{_libdir}
cp -p libdwarf/libdwarf.h $RPM_BUILD_ROOT%{_includedir}

for d in dwarfdump ; do
# dwarfdump2 is just a C++ version of dwarfdump
# dwarfgen is not really useful yet (just test/example program)
%{__make} -C $d install \
	DESTDIR=$RPM_BUILD_ROOT
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc libdwarf/CHANGES libdwarf/COPYING libdwarf/ChangeLog* libdwarf/NEWS libdwarf/README
%attr(755,root,root) %{_libdir}/libdwarf.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libdwarf.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdwarf.so
%{_includedir}/libdwarf.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdwarf.a

%files -n dwarfdump
%defattr(644,root,root,755)
%doc dwarfdump/COPYING dwarfdump/ChangeLog* dwarfdump/NEWS dwarfdump/README
%{_sysconfdir}/dwarfdump.conf
%attr(755,root,root) %{_bindir}/dwarfdump
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
