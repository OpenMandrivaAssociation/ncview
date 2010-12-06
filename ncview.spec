%define version 1.93g
%define release %mkrel 3

Summary: Graphic for netCDF data file 
Name: ncview
Version: %version
Release: %release
License: GPLv3
Group: Sciences/Other
Source: ftp://cirrus.ucsd.edu/pub/ncview/ncview-%{version}.tar.gz
Patch0:	ncview-1.93g-as-needed.patch
Patch1: ncview-1.92e-netpbm.patch
URL: http://meteora.ucsd.edu/~pierce/ncview_home_page.html
BuildRequires:  netcdf-devel 
BuildRequires:	udunits-devel 
BuildRequires:	libnetpbm-devel
BuildRequires:  X11-devel
BuildRequires:  netcdf-static-devel
BuildRoot: %_tmppath/%name-%version-root

%description
Ncview is a visual browser for netCDF format files.  Typically you
would use ncview to get a quick and easy, push-button look at your
netCDF files.  You can view simple movies of the data, view along
various dimensions, take a look at the actual data values, change
color maps, invert the data, etc.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
# Makefile doesn't actually respect --with-ppm_incdir
CFLAGS="%optflags -I/usr/include/netpbm"  

%configure2_5x --with-netcdf-libdir=%{_libdir} --with-udunits_libdir=%{_libdir} \
  --with-ppm_libdir=%{_libdir} --with-ppm_incdir=%{_includedir}/netpbm \
  --datadir=%{_datadir}/%{name} \
  --x-includes=%{_includedir}/X11 \
  --x-libraries=%{_libdir}

%make 

%install
rm -rf %{buildroot}
export XAPPLRESDIR="%{buildroot}%{_sysconfdir}/X11/app-defaults"
mkdir -p "%{buildroot}%{_sysconfdir}/X11/app-defaults"
%makeinstall NCVIEW_LIB_DIR=%{buildroot}%{_datadir}/ncview BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1
chmod 644 %{buildroot}%{_sysconfdir}/X11/app-defaults/Ncview
chmod 644 %{buildroot}%{_mandir}/man1/*

# Menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=Science;Other;
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
%config(noreplace) %{_sysconfdir}/X11/app-defaults/*
%{_mandir}/man1/*

