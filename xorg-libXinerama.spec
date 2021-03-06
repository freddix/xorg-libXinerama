Summary:	Xinerama extension library
Name:		xorg-libXinerama
Version:	1.1.3
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2
# Source0-md5:	9336dc46ae3bf5f81c247f7131461efd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xinerama extension library.

%package devel
Summary:	Header files for libXinerama library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Xinerama extension library.

This package contains the header files needed to develop programs that
use libXinerama.

%prep
%setup -qn libXinerama-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXinerama.so.?
%attr(755,root,root) %{_libdir}/libXinerama.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXinerama.so
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xinerama.pc
%{_mandir}/man3/Xinerama*.3x*

