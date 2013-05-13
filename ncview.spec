Summary:	Graphic for netCDF data file
Name:		ncview
Version:	2.1.1
Release:	2
License:	GPLv3
Group:		Sciences/Other
Source:		ftp://cirrus.ucsd.edu/pub/ncview/ncview-%{version}.tar.gz
Patch0:		ncview-2.1-link.patch
URL:		http://meteora.ucsd.edu/~pierce/ncview_home_page.html
BuildRequires:	netcdf-devel
BuildRequires:	netpbm-devel = 10.57.01-2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xt)
BuildRequires:	udunits2-devel
BuildRequires:	expat-devel
BuildRequires:	png-devel

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



%changelog
* Fri Dec 02 2011 Andrey Bondrov <abondrov@mandriva.org> 2.1.1-1mdv2012.0
+ Revision: 737142
- New version 2.1.1

* Thu Mar 10 2011 Funda Wang <fwang@mandriva.org> 2.0-0.beta4.2
+ Revision: 643232
- rebuild to obsolete old packages

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 2.0-0.beta4.1
+ Revision: 636339
- 2.0 beta4

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1.93g-4
+ Revision: 636331
- correctly detect libname
- tighten BR

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.93g-3mdv2011.0
+ Revision: 613004
- the mass rebuild of 2010.1 packages

* Mon Jan 18 2010 Emmanuel Andry <eandry@mandriva.org> 1.93g-2mdv2010.1
+ Revision: 493338
- diff p0 to fix linking issue with hdf5
- use configure2_5x
- fix netpbm headers detection at compile time
- fix netcdf include path

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Mar 11 2009 Emmanuel Andry <eandry@mandriva.org> 1.93g-1mdv2009.1
+ Revision: 353802
- New version 1.93g
- drop patch 0
- add menu item

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.93c-3mdv2009.0
+ Revision: 253657
- rebuild

* Tue Feb 19 2008 Olivier Thauvin <nanardon@mandriva.org> 1.93c-1mdv2008.1
+ Revision: 172609
- 1.93c

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 20:54:47 (55139)
- 1.93b

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 20:15:11 (55121)
Import ncview

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.92e-2mdk
- Add X11-devel as BuildRequires for X11/Core.h

* Thu Sep 29 2005 Olivier Thauvin <nanardon@mandriva.org> 1.92e-1mdk
- From Philippe Weill <Philippe.Weill@aero.jussieu.fr>
    - Initial SPEC

