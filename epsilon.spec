Summary:	Enlightened Thumbnail Generator
Name:		epsilon
Version:	0.3.0
%define _snap	20050106
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	5929b790a7b4864ad7e60e246cf662bf
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	epeg-devel
BuildRequires:	freetype-devel
BuildRequires:	imlib2-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epsilon is a small, display independent, and quick thumbnailing
library. The lib itself conforms to the standard put forth by
freedesktop.org You can find out more information about it at
http://triq.net/~jens/thumbnail-spec/index.html

Epeg offers very noticeable speed increases to this standard, but it
is only available if the input image is a jpeg file. If the file is
anything other than jpg, the traditional freedesktop.org thumbnailing
will occur. To show the speed increase epeg offers, Epsilon can be
built with and without epeg.

%package devel
Summary:	Epsilon headers and development libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Epsilon thumbnailer development headers and libraries.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libepsilon.so.*
%attr(755,root,root) %{_bindir}/epsilon

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepsilon.so
%{_libdir}/libepsilon.la
%attr(755,root,root) %{_bindir}/epsilon-config
%{_includedir}/Epsilon.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libepsilon.a
