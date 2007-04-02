#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightened Thumbnail Generator
Summary(pl.UTF-8):	Oświecony generator miniaturek obrazów
Name:		epsilon
Version:	0.3.0.007
Release:	5
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	408d3c63f9efa06e93e29a691c28985e
Patch0:		%{name}-proto.patch
URL:		http://enlightenment.org/Libraries/Epsilon/
BuildRequires:	edje-devel
BuildRequires:	epeg-devel
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

%description libs
Epsilon library.

%description libs -l pl.UTF-8
Biblioteka Epsilon.

%package devel
Summary:	Epsilon header file
Summary(pl.UTF-8):	Plik nagłówkowy Epsilon
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	epeg-devel

%description devel
Epsilon thumbnailer development header.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki Epsilon generującej miniaturki obrazów.

%package static
Summary:	Static Epsilon library
Summary(pl.UTF-8):	Statyczna biblioteka Epsilon
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Epsilon library.

%description static -l pl.UTF-8
Statyczna biblioteka Epsilon.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/epsilon*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepsilon.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/epsilon-config
%attr(755,root,root) %{_libdir}/libepsilon.so
%{_libdir}/libepsilon.la
%{_includedir}/Epsilon*.h
%{_pkgconfigdir}/%{name}.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libepsilon.a
%endif
