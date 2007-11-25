#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightened Thumbnail Generator
Summary(pl.UTF-8):	Oświecony generator miniaturek obrazów
Name:		epsilon
Version:	0.3.0.008
Release:	2
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	ba946584d90357f98402456e0fee9dcf
URL:		http://enlightenment.org/
# ecore-con ecore-evas ecore-file
BuildRequires:	ecore-devel >= 0.9.9.038
BuildRequires:	edje-devel >= 0.5.0.038
BuildRequires:	epeg-devel >= 0.9.0.008
BuildRequires:	evas-devel >= 0.9.9.038
BuildRequires:	imlib2-devel >= 1.0.0
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	xine-lib-devel >= 1:1.0.0
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Epsilon is a small, display independent, and quick thumbnailing
library. The lib itself conforms to the standard put forth by
freedesktop.org . You can find out more information about it at
http://triq.net/~jens/thumbnail-spec/index.html .

Epeg offers very noticeable speed increases to this standard, but it
is only available if the input image is a JPEG file. If the file is
anything other than jpg, the traditional freedesktop.org thumbnailing
will occur. To show the speed increase epeg offers, Epsilon can be
built with and without epeg.

%description -l pl.UTF-8
Epsilon to mała, niezależna od ekranu i szybka biblioteka do
generowania miniaturek obrazów. Sama biblioteka jest zgodna ze
standardem opracowanym przez freedesktop.org . Więcej informacji
można znaleźć pod adresem
http://triq.net/~jens/thumbnail-spec/index.html .

Epeg oferuje bardzo zauważalne przyspieszenie w stosunku do tego
standardu, ale jest ono dostępne tylko jeśli obrazek jest plikiem
JPEG. Jeśli plik jest innego typu, zostanie użyte tradycyjne
zachowanie freedesktop.org . Aby pokazać przyspieszenie oferowane
przez epeg, Epsilon może być zbudowany z lub bez epeg.

%package libs
Summary:	Epsilon library
Summary(pl.UTF-8):	Biblioteka Epsilon
Group:		X11/Libraries
Requires:	ecore-con >= 0.9.9.038
Requires:	ecore-evas >= 0.9.9.038
Requires:	ecore-file >= 0.9.9.038
Requires:	edje-libs >= 0.5.0.038
Requires:	epeg-libs >= 0.9.0.008
Requires:	evas >= 0.9.9.038
Requires:	imlib2 >= 1.0.0

%description libs
Epsilon library.

%description libs -l pl.UTF-8
Biblioteka Epsilon.

%package devel
Summary:	Epsilon header file
Summary(pl.UTF-8):	Plik nagłówkowy Epsilon
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
# ecore-con ecore-evas ecore-file
Requires:	ecore-devel >= 0.9.9.038
Requires:	edje-devel >= 0.5.0.038
Requires:	epeg-devel >= 0.9.0.008
Requires:	evas-devel >= 0.9.9.038
Requires:	imlib2-devel >= 1.0.0
Requires:	libpng-devel >= 1.2.0

%description devel
Epsilon thumbnailer development header.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki Epsilon generującej miniaturki obrazów.

%package static
Summary:	Static Epsilon library
Summary(pl.UTF-8):	Statyczna biblioteka Epsilon
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Epsilon library.

%description static -l pl.UTF-8
Statyczna biblioteka Epsilon.

%package plugin-xine
Summary:	XINE-based thumbnailer for Epsilon
Summary(pl.UTF-8):	Oparty na XINE generator miniaturek dla Epsilona
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	xine-lib >= 1:1.0.0

%description plugin-xine
XINE-based thumbnailer for Epsilon. It supports MPEG, AVI, WMV and
QuickTime files.

Oparty na XINE generator miniaturek dla Epsilona. Obsługuje pliki
MPEG, AVI, WMV i QuickTime.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/epsilon/plugins/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/epsilon
%attr(755,root,root) %{_bindir}/epsilon_thumbd
%attr(755,root,root) %{_bindir}/epsilon_thumb_test

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepsilon.so.*.*.*
%dir %{_libdir}/epsilon
%dir %{_libdir}/epsilon/plugins

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/epsilon-config
%attr(755,root,root) %{_libdir}/libepsilon.so
%{_libdir}/libepsilon.la
%{_includedir}/Epsilon*.h
%{_pkgconfigdir}/epsilon.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libepsilon.a
%endif

%files plugin-xine
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/epsilon/plugins/xine_thumbnailer.so
