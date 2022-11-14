Summary:	Graphic for netCDF data file
Name:		ncview
Version:	2.1.8
Release:	1
License:	GPLv3
Group:		Sciences/Other
Source:		ftp://cirrus.ucsd.edu/pub/ncview/ncview-%{version}.tar.gz
URL:		http://meteora.ucsd.edu/~pierce/ncview_home_page.html
BuildRequires:  pkgconfig(netcdf)
BuildRequires:	netpbm-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xt)
BuildRequires:	udunits2-devel
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libpng)

%description
Ncview is a visual browser for netCDF format files.  Typically you
would use ncview to get a quick and easy, push-button look at your
netCDF files.  You can view simple movies of the data, view along
various dimensions, take a look at the actual data values, change
color maps, invert the data, etc.

%prep
%autosetup -p1
autoreconf -fi -Im4macros
%configure \
    --with-udunits2_incdir=%{_includedir}/udunits2

%build
%make_build

%install
%make_install

# Menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=Science;Education;
Name=%{name}
Comment=Graphic for netCDF data file
EOF

%files
%defattr(-, root, root, -)
%doc COPYING INSTALL README
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
