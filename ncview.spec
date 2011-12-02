Summary:	Graphic for netCDF data file
Name:		ncview
Version:	2.1.1
Release:	%mkrel 1
License:	GPLv3
Group:		Sciences/Other
Source:		ftp://cirrus.ucsd.edu/pub/ncview/ncview-%{version}.tar.gz
Patch0:		ncview-2.1-link.patch
URL:		http://meteora.ucsd.edu/~pierce/ncview_home_page.html
BuildRequires:	netcdf-devel
BuildRequires:	libnetpbm-devel
BuildRequires:	libx11-devel
BuildRequires:	libxaw-devel
BuildRequires:	libxt-devel
BuildRequires:	udunits2-devel
BuildRequires:	expat-devel
BuildRequires:	png-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Ncview is a visual browser for netCDF format files.  Typically you
would use ncview to get a quick and easy, push-button look at your
netCDF files.  You can view simple movies of the data, view along
various dimensions, take a look at the actual data values, change
color maps, invert the data, etc.

%prep
%setup -q
%patch0 -p0 -b .link

%build
autoreconf -fi -Im4macros
%configure2_5x --with-ppm_libdir=%{_libdir} --with-udunits2_libdir=%{_libdir} \
	--with-udunits2_incdir=%{_includedir}/udunits2 \
	--with-ppm_libdir=%{_libdir} --with-ppm_incdir=%{_includedir}/netpbm
%make

%install
rm -rf %{buildroot}
%makeinstall_std

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

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
[ %{buildroot} != '/' ] && rm -fr %{buildroot}

%files
%defattr(-, root, root, -)
%doc COPYING INSTALL README
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop

