Summary:	Enlightened Thumbnail Generator
Summary(pl):	O�wiecony generator miniaturek obraz�w
Name:		epsilon
Version:	0.3.0.004
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	10118c712b42d00b332c6fe1d9257661
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje-devel
BuildRequires:	epeg-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Epsilon to ma�a, niezale�na od ekranu i szybka biblioteka do
generowania miniaturek obraz�w. Sama biblioteka jest zgodna ze
standardem opracowanym przez freedesktop.org . Wi�cej informacji
mo�na znale�� pod adresem
http://triq.net/~jens/thumbnail-spec/index.html .

Epeg oferuje bardzo zauwa�alne przyspieszenie w stosunku do tego
standardu, ale jest ono dost�pne tylko je�li obrazek jest plikiem
JPEG. Je�li plik jest innego typu, zostanie u�yte tradycyjne
zachowanie freedesktop.org . Aby pokaza� przyspieszenie oferowane
przez epeg, Epsilon mo�e by� zbudowany z lub bez epeg.

%package devel
Summary:	Epsilon header file
Summary(pl):	Plik nag��wkowy Epsilon
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Epsilon thumbnailer development header.

%description devel -l pl
Plik nag��wkowy biblioteki Epsilon generuj�cej miniaturki obraz�w.

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
%attr(755,root,root) %{_bindir}/epsilon
%attr(755,root,root) %{_libdir}/libepsilon.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/epsilon-config
%attr(755,root,root) %{_libdir}/libepsilon.so
%{_libdir}/libepsilon.la
%{_includedir}/Epsilon.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libepsilon.a
