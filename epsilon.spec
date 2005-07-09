Summary:	Enlightened Thumbnail Generator
Summary(pl):	O¶wiecony generator miniaturek obrazów
Name:		epsilon
Version:	0.3.0
%define _snap	20050701
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/snaps/enli/e17/libs/%{name}-%{_snap}.tar.gz
# Source0-md5:	b86833bb0c6190b93b99234d9d3a5311
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

%package devel
Summary:	Epsilon header file
Summary(pl):	Plik nag³ówkowy Epsilon
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
