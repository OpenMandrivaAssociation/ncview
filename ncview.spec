%define version 1.93c
%define release %mkrel 3

Summary: Graphic for netCDF data file 
Name: ncview
Version: %version
Release: %release
License: GPL
Group: Sciences/Other
Source: ftp://cirrus.ucsd.edu/pub/ncview/ncview-%{version}.tar.gz
Patch1:         ncview-1.92e-netpbm.patch
Patch0:         ncview-1.92e-Makefile.in.patch

URL: http://meteora.ucsd.edu/~pierce/ncview_home_page.html
BuildRequires:  netcdf-devel udunits-devel libnetpbm-devel
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
%patch0 -p1
%patch1 -p0

%build
%configure --with-netcdf-libdir=%{_libdir} --with-udunits_libdir=%{_libdir} \
  --with-ppm_libdir=%{_libdir} --datadir=%{_datadir}/%{name} \
  --x-includes=%{_includedir}/X11 \
  --x-libraries=%{_libdir} \
  --with-netcdf_incdir=%{_includedir}/netcdf-3

%make 

%install
rm -rf $RPM_BUILD_ROOT
export XAPPLRESDIR="${RPM_BUILD_ROOT}%{_sysconfdir}/X11/app-defaults"
mkdir -p "${RPM_BUILD_ROOT}%{_sysconfdir}/X11/app-defaults"
%makeinstall NCVIEW_LIB_DIR=${RPM_BUILD_ROOT}%{_datadir}/ncview BINDIR=${RPM_BUILD_ROOT}%{_bindir} MANDIR=${RPM_BUILD_ROOT}%{_mandir}/man1
chmod 644 ${RPM_BUILD_ROOT}%{_sysconfdir}/X11/app-defaults/Ncview
chmod 644 ${RPM_BUILD_ROOT}%{_mandir}/man1/*

%clean
[ $RPM_BUILD_ROOT != '/' ] && rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc COPYING INSTALL README
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/X11/app-defaults/*
%{_mandir}/man1/*

