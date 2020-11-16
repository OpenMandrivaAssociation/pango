# pango is used by gst-plugins-base, which is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif
%define url_ver %(echo %{version}|cut -d. -f1,2)
%define enable_gtkdoc 1

%define api 1.0
%define major 0

%define libname %mklibname %{name} %{api} %{major}
%define libcairo %mklibname %{name}cairo %{api} %{major}
%define libft2 %mklibname %{name}ft2_ %{api} %{major}
%define libxft %mklibname %{name}xft %{api} %{major}

%define lib32name %mklib32name %{name} %{api} %{major}
%define lib32cairo %mklib32name %{name}cairo %{api} %{major}
%define lib32ft2 %mklib32name %{name}ft2_ %{api} %{major}
%define lib32xft %mklib32name %{name}xft %{api} %{major}

%define girname %mklibname %{name}-gir %{api}
%define gircairo %mklibname %{name}cairo-gir %{api}
%define girft2 %mklibname %{name}ft2-gir %{api}
%define girxft %mklibname %{name}xft-gir %{api}
%define girfc %mklibname %{name}fc-gir %{api}
%define girot %mklibname %{name}ot-gir %{api}

%define devname %mklibname -d %{name} %{api}
%define devcairo %mklibname -d %{name}cairo %{api}
%define devft2 %mklibname -d %{name}ft2_ %{api}
%define devx %mklibname -d %{name}x %{api}
%define devxft %mklibname -d %{name}xft %{api}

%define dev32name %mklib32name -d %{name} %{api}
%define dev32cairo %mklib32name -d %{name}cairo %{api}
%define dev32ft2 %mklib32name -d %{name}ft2_ %{api}
%define dev32x %mklib32name -d %{name}x %{api}
%define dev32xft %mklib32name -d %{name}xft %{api}

%bcond_with	bootstrap

Summary:	System for layout and rendering of internationalized text
Name:		pango
Version:	1.48.0
Release:	1
License:	LGPLv2+
Group:		System/Internationalization
Url:		http://www.pango.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pango/%{url_ver}/%{name}-%{version}.tar.xz
# Added as Source: rather than Patch: so autosetup doesn't pick it up.
# This is an arch specific hack.
Source1:	pango-1.44.7-compile-with-our-cairo32.patch
Patch0:		pango-1.44.7-fallthrough.patch
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	git-core
BuildRequires:	pkgconfig(cairo) >= 1.7.6
BuildRequires:	pkgconfig(fontconfig) >= 2.5.0
BuildRequires:	pkgconfig(freetype2) >= 2.1.3
BuildRequires:	pkgconfig(glib-2.0) >= 2.24
BuildRequires:	pkgconfig(gio-2.0) >= 2.24
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libthai) >= 0.1.9
BuildRequires:	pkgconfig(harfbuzz) >= 0.9.3-3
BuildRequires:	pkgconfig(xft) >= 2.0
BuildRequires:	pkgconfig(fribidi) >= 0.19.7
BuildRequires:	atomic-devel
%if %{enable_gtkdoc}
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk-doc >= 0.10
BuildRequires:	xsltproc
%endif
Requires:	%{libname} = %{EVRD}
# (tpg) get rid of pango-modules
Obsoletes:	%{mklibname pango-modules 1.0} < 1.38.0-3
Provides:	pango-modules = %{EVRD}
Provides:	lib%{name}%{api} = %{EVRD}
Provides:	lib%{name} = %{EVRD}
%rename		%{_lib}pango1.0_0-modules
%if %{with compat32}
BuildRequires:	devel(libcairo)
BuildRequires:	devel(libfontconfig)
BuildRequires:	devel(libexpat)
BuildRequires:	devel(libuuid)
BuildRequires:	devel(libfreetype)
BuildRequires:	devel(libXft)
BuildRequires:	devel(libglib-2.0)
BuildRequires:	devel(libgio-2.0)
BuildRequires:	devel(libharfbuzz)
BuildRequires:	devel(libatomic)
BuildRequires:	devel(libfribidi)
BuildRequires:	devel(libz)
BuildRequires:	devel(libbz2)
BuildRequires:	devel(libpng16)
BuildRequires:	devel(libXrender)
BuildRequires:	devel(libgobject-2.0)
BuildRequires:	devel(libpixman-1)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
BuildRequires:	devel(libmount)
BuildRequires:	devel(libblkid)
%endif

%description
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%package -n %{libname}
Summary:	Internationalized text layout and rendering system
Group:		%{group}

%description -n %{libname}
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%package -n %{libcairo}
Summary:	Internationalized text layout and rendering system - cairo
Group:		%{group}

%description -n %{libcairo}
Library for %{name} - cairo.

%package -n %{libft2}
Summary:	Internationalized text layout and rendering system - ft2
Group:		%{group}

%description -n %{libft2}
Library for %{name} - ft2.

%package -n %{libxft}
Summary:	Internationalized text layout and rendering system - xft
Group:		%{group}

%description -n %{libxft}
Library for %{name} - xft.

%if !%{with bootstrap}
%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{gircairo}
Summary:	GObject Introspection interface description for %{name} - cairo
Group:		System/Libraries

%description -n %{gircairo}
GObject Introspection interface description for %{name} - cairo.

%package -n %{girft2}
Summary:	GObject Introspection interface description for %{name} - ft2
Group:		System/Libraries

%description -n %{girft2}
GObject Introspection interface description for %{name} - ft2.

%package -n %{girxft}
Summary:	GObject Introspection interface description for %{name} - xft
Group:		System/Libraries

%description -n %{girxft}
GObject Introspection interface description for %{name} - xft.

%package -n %{girfc}
Summary:	GObject Introspection interface description for %{name} - fc
Group:		System/Libraries

%description -n %{girfc}
GObject Introspection interface description for %{name} - fc.

%package -n %{girot}
Summary:	GObject Introspection interface description for %{name} - ot
Group:		System/Libraries

%description -n %{girot}
GObject Introspection interface description for %{name} - ot.
%endif

%package -n %{devname}
Summary:	Internationalized text layout and rendering system
Group:		Development/GNOME and GTK+
%rename		pango-devel
%rename		pango-doc
Requires:	%{libname} = %{EVRD}
%if !%{with bootstrap}
Requires:	%{girname} = %{EVRD}

%endif
Conflicts:	%{_lib}pango1.0_0 < 1.28.1-2

%description -n %{devname}
This package includes the development library and header files
for the %{name} package.

%package -n %{devcairo}
Summary:	Internationalized text layout and rendering system - cairo
Group:		Development/GNOME and GTK+
Requires:	%{libcairo} = %{version}-%{release}
%if !%{with bootstrap}
Requires:	%{gircairo} = %{version}-%{release}
%endif

%description -n %{devcairo}
This package includes the development library and header files
for the %{name}cairo package.

%package -n %{devft2}
Summary:	Internationalized text layout and rendering system - ft2
Group:		Development/GNOME and GTK+
Requires:	%{libft2} = %{version}-%{release}
%if !%{with bootstrap}
Requires:	%{girft2} = %{version}-%{release}
%endif

%description -n %{devft2}
This package includes the development library and header files
for the %{name}ft2 package.

%package -n %{devxft}
Summary:	Internationalized text layout and rendering system - xft
Group:		Development/GNOME and GTK+
Requires:	%{libxft} = %{version}-%{release}
%if !%{with bootstrap}
Requires:	%{girxft} = %{version}-%{release}
%endif

%description -n %{devxft}
This package includes the development library and header files
for the %{name}xft package.

%if %{with compat32}
%package -n %{lib32name}
Summary:	Internationalized text layout and rendering system (32-bit)
Group:		%{group}

%description -n %{lib32name}
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%package -n %{lib32cairo}
Summary:	Internationalized text layout and rendering system - cairo (32-bit)
Group:		%{group}

%description -n %{lib32cairo}
Library for %{name} - cairo.

%package -n %{lib32ft2}
Summary:	Internationalized text layout and rendering system - ft2 (32-bit)
Group:		%{group}

%description -n %{lib32ft2}
Library for %{name} - ft2.

%package -n %{lib32xft}
Summary:	Internationalized text layout and rendering system - xft (32-bit)
Group:		%{group}

%description -n %{lib32xft}
Library for %{name} - xft.

%package -n %{dev32name}
Summary:	Internationalized text layout and rendering system (32-bit)
Group:		Development/GNOME and GTK+
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}

%description -n %{dev32name}
This package includes the development library and header files
for the %{name} package.

%package -n %{dev32cairo}
Summary:	Internationalized text layout and rendering system - cairo (32-bit)
Group:		Development/GNOME and GTK+
Requires:	%{devcairo} = %{version}-%{release}
Requires:	%{lib32cairo} = %{version}-%{release}

%description -n %{dev32cairo}
This package includes the development library and header files
for the %{name}cairo package.

%package -n %{dev32ft2}
Summary:	Internationalized text layout and rendering system - ft2 (32-bit)
Group:		Development/GNOME and GTK+
Requires:	%{devft2} = %{version}-%{release}
Requires:	%{lib32ft2} = %{version}-%{release}

%description -n %{dev32ft2}
This package includes the development library and header files
for the %{name}ft2 package.

%package -n %{dev32xft}
Summary:	Internationalized text layout and rendering system - xft (32-bit)
Group:		Development/GNOME and GTK+
Requires:	%{devxft} = %{version}-%{release}
Requires:	%{lib32xft} = %{version}-%{release}

%description -n %{dev32xft}
This package includes the development library and header files
for the %{name}xft package.
%endif

%prep
%autosetup -p1
%if %{with compat32}
patch -p1 -b -z .1~ <%{S:1}
%meson32 \
	-Db_ndebug=true \
	-Dlibthai=disabled \
	-Dc_std=c11 \
	-Dgir=false \
	-Denable_docs=false \
	-Dintrospection=disabled
%endif

%meson \
	-Db_ndebug=true \
	-Dc_std=c11 \
%if %{with bootstrap}
	-Dgir=false \
%else
	-Dgir=true \
%endif
%if %enable_gtkdoc
	-Denable_docs=true \
%else
	-Denable_docs=false \
%endif

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%ninja_build -C build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%ninja_install -C build

# No need to package the tests, they aren't relevant
# for end users
rm -rf %{buildroot}%{_libexecdir}/installed-tests \
	%{buildroot}%{_datadir}/installed-tests

%files
%doc README.md THANKS NEWS
%{_bindir}/pango-view
%{_bindir}/pango-list
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libpango-%{api}.so.%{major}*

%files -n %{libcairo}
%{_libdir}/libpangocairo-%{api}.so.%{major}*

%files -n %{libft2}
%{_libdir}/libpangoft2-%{api}.so.%{major}*

%files -n %{libxft}
%{_libdir}/libpangoxft-%{api}.so.%{major}*

%if !%{with bootstrap}
%files -n %{girname}
%{_libdir}/girepository-1.0/Pango-%{api}.typelib

%files -n %{gircairo}
%{_libdir}/girepository-1.0/PangoCairo-%{api}.typelib

%files -n %{girft2}
%{_libdir}/girepository-1.0/PangoFT2-%{api}.typelib

%files -n %{girxft}
%{_libdir}/girepository-1.0/PangoXft-%{api}.typelib

%files -n %{girfc}
%{_libdir}/girepository-1.0/PangoFc-%{api}.typelib

%files -n %{girot}
%{_libdir}/girepository-1.0/PangoOT-%{api}.typelib

%endif

%files -n %{devname}
#doc %{_datadir}/gtk-doc/html/pango
%{_libdir}/libpango-*.so
%{_libdir}/pkgconfig/pango.pc
%{_libdir}/pkgconfig/pangofc.pc
%{_libdir}/pkgconfig/pangoot.pc
%if !%{with bootstrap}
%{_datadir}/gir-1.0/Pango-%{api}.gir
%{_datadir}/gir-1.0/PangoFc-%{api}.gir
%{_datadir}/gir-1.0/PangoOT-%{api}.gir
%endif
%dir %{_includedir}/pango-1.0
%dir %{_includedir}/pango-1.0/pango
%{_includedir}/pango-1.0/pango/pango-*.h
%{_includedir}/pango-1.0/pango/pango.h
%{_includedir}/pango-1.0/pango/pangofc-*.h

%files -n %{devcairo}
%{_libdir}/libpangocairo*.so
%{_libdir}/pkgconfig/pangocairo.pc
%if !%{with bootstrap}
%{_datadir}/gir-1.0/PangoCairo-%{api}.gir
%endif
%{_includedir}/pango-1.0/pango/pangocairo.h

%files -n %{devft2}
%{_libdir}/libpangoft2-*.so
%{_libdir}/pkgconfig/pangoft2.pc
%if !%{with bootstrap}
%{_datadir}/gir-1.0/PangoFT2-%{api}.gir
%endif
%{_includedir}/pango-1.0/pango/pangoft2.h

%files -n %{devxft}
%{_libdir}/libpangoxft-*.so
%{_libdir}/pkgconfig/pangoxft.pc
%if !%{with bootstrap}
%{_datadir}/gir-1.0/PangoXft-%{api}.gir
%endif
%{_includedir}/pango-1.0/pango/pangoxft.h
%{_includedir}/pango-1.0/pango/pangoxft-render.h

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libpango-%{api}.so.%{major}*

%files -n %{lib32cairo}
%{_prefix}/lib/libpangocairo-%{api}.so.%{major}*

%files -n %{lib32ft2}
%{_prefix}/lib/libpangoft2-%{api}.so.%{major}*

%files -n %{lib32xft}
%{_prefix}/lib/libpangoxft-%{api}.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libpango-*.so
%{_prefix}/lib/pkgconfig/pango.pc
%{_prefix}/lib/pkgconfig/pangofc.pc
%{_prefix}/lib/pkgconfig/pangoot.pc

%files -n %{dev32cairo}
%{_prefix}/lib/libpangocairo*.so
%{_prefix}/lib/pkgconfig/pangocairo.pc

%files -n %{dev32ft2}
%{_prefix}/lib/libpangoft2-*.so
%{_prefix}/lib/pkgconfig/pangoft2.pc

%files -n %{dev32xft}
%{_prefix}/lib/libpangoxft-*.so
%{_prefix}/lib/pkgconfig/pangoxft.pc
%endif
