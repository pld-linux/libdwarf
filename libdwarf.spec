Summary:	Library to read DWARF debug information of an ELF object
Summary(pl.UTF-8):	Biblioteka do odczytu informacji debugowych DWARF z obiektów ELF
Name:		libdwarf
%define		snap	20120410
Version:	0.%{snap}.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://reality.sgiweb.org/davea/%{name}-%{snap}.tar.gz
# Source0-md5:	77c8b351f11738bc9fa50474a69d5b36
Patch0:		%{name}-makefile.patch
URL:		http://reality.sgiweb.org/davea/dwarf.html
BuildRequires:	elfutils-devel
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

%build
cd libdwarf
%configure \
	CFLAGS="%{rpmcflags} -fPIC"
%{__make} libdwarf.a libdwarf.so
cd ..
cd dwarfdump
%configure
%{__make} -j1
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_includedir},%{_libdir},%{_mandir}/man1}

install libdwarf/libdwarf.h $RPM_BUILD_ROOT%{_includedir}
install libdwarf/libdwarf.{a,so} $RPM_BUILD_ROOT%{_libdir}

%{__make} -C dwarfdump install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc libdwarf/CHANGES libdwarf/COPYING libdwarf/ChangeLog* libdwarf/NEWS libdwarf/README
%attr(755,root,root) %{_libdir}/libdwarf.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/libdwarf.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdwarf.a

%files -n dwarfdump
%defattr(644,root,root,755)
%doc dwarfdump/COPYING dwarfdump/ChangeLog* dwarfdump/NEWS dwarfdump/README
%{_sysconfdir}/dwarfdump.conf
%attr(755,root,root) %{_bindir}/dwarfdump
%{_mandir}/man1/*
