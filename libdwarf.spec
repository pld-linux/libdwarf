Summary:	Library to read DWARF debug information of an ELF object
Name:		libdwarf
%define		_snap	20070703
Version:	0.%{_snap}.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://reality.sgiweb.org/davea/%{name}-%{_snap}.tar.gz
# Source0-md5:	3c67d1df89f05421267ede59feec8152
Patch0:		%{name}-makefile.patch
URL:		http://reality.sgiweb.org/davea/dwarf.html
BuildRequires:	elfutils-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fPIC

%description
Library to read DWARF debug information of an ELF object.

%package devel
Summary:	Header files for libdwarf library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdwarf library.

%package static
Summary:	Static libdwarf library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdwarf library.

%package -n dwarfdump
Summary:	Tool for dumps DWARF debug information of an ELF object
License:	GPL v2
Group:		Development/Tools

%description -n dwarfdump
Tool for dumps DWARF debug information of an ELF object.

%prep
%setup -q -n dwarf-%{_snap}
%patch -p1

%build
cd libdwarf
%configure
%{__make} libdwarf.a libdwarf.so
cd ..
cd dwarfdump
%configure
%{__make}
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
%doc dwarfdump/COPYING dwarfdump/ChangeLog* dwarfdump/NEWS dwarfdump/README
%{_sysconfdir}/dwarfdump.conf
%attr(755,root,root) %{_bindir}/dwarfdump
%{_mandir}/man1/*
