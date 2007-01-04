#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightened Thumbnail Generator
Summary(pl):	O¶wiecony generator miniaturek obrazów
Name:		epsilon
Version:	0.3.0.007
Release:	4
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

%description -l pl
Epsilon to ma³a, niezale¿na od ekranu i szybka biblioteka do
generowania miniaturek obrazów. Sama biblioteka jest zgodna ze
standardem opracowanym przez freedesktop.org . Wiêcej informacji
mo¿na znale¼æ pod adresem
http://triq.net/~jens/thumbnail-spec/index.html .

Epeg oferuje bardzo zauwa¿alne przyspieszenie w stosunku do tego
standardu, ale jest ono dostêpne tylko je¶li obrazek jest plikiem
JPEG. Je¶li plik jest innego typu, zostanie u¿yte tradycyjne
zachowanie freedesktop.org . Aby pokazaæ przyspieszenie oferowane
przez epeg, Epsilon mo¿e byæ zbudowany z lub bez epeg.

%package libs
Summary:	Epsilon library
Summary(pl):	Biblioteka Epsilon
Group:		X11/Libraries

%description libs
Epsilon library.

%description libs -l pl
Biblioteka Epsilon.

%package devel
Summary:	Epsilon header file
Summary(pl):	Plik nag³ówkowy Epsilon
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	epeg-devel

%description devel
Epsilon thumbnailer development header.

%description devel -l pl
Plik nag³ówkowy biblioteki Epsilon generuj±cej miniaturki obrazów.

%package static
Summary:	Static Epsilon library
Summary(pl):	Statyczna biblioteka Epsilon
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Epsilon library.

%description static -l pl
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
