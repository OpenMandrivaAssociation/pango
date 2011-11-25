%define enable_gtkdoc	1

# Define biarch packages
%define biarches_32 %{ix86} ppc
%define biarches_64 x86_64 ppc64
%define query_modules_suffix %{nil}
%ifarch %{biarches_32}
%define query_modules_suffix -32
%endif
%ifarch %{biarches_64}
%define query_modules_suffix -64
%endif
%define query_modules pango-querymodules%{query_modules_suffix}

%define api_version	1.0
%define module_version	1.6.0
%define lib_major	0
%define gir_major	1.0

%define modulesname	%mklibname %{name}-modules %{api_version}
%define lib_name	%mklibname %{name} %{api_version} %{lib_major}
%define caironame	%mklibname %{name}cairo %{api_version} %{lib_major}
%define ft2name		%mklibname %{name}ft2_ %{api_version} %{lib_major}
%define xname		%mklibname %{name}x %{api_version} %{lib_major}
%define xftname		%mklibname %{name}xft %{api_version} %{lib_major}

%define girname		%mklibname %{name}-gir %{gir_major}
%define gircairo	%mklibname %{name}cairo-gir %{gir_major}
%define girft2		%mklibname %{name}ft2-gir %{gir_major}
%define girxft		%mklibname %{name}xft-gir %{gir_major}

%define develname	%mklibname -d %{name} %{api_version} 
%define develcairo	%mklibname -d %{name}cairo %{api_version} 
%define develft2	%mklibname -d %{name}ft2_ %{api_version} 
%define develx		%mklibname -d %{name}x %{api_version} 
%define develxft	%mklibname -d %{name}xft %{api_version} 

Summary:	System for layout and rendering of internationalized text
Name:		pango
Version:	1.29.5
Release:	1
License:	LGPLv2+
Group:		System/Internationalization
URL:		http://www.pango.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pango/%{name}-%{version}.tar.xz
# (gb) 1.4.0-2mdk biarch support
Patch5:		pango-1.29.5-lib64.patch

BuildRequires: pkgconfig(glib-2.0) >= 2.24
BuildRequires: pkgconfig(freetype2) >= 2.1.3
BuildRequires: pkgconfig(xft) >= 2.0
BuildRequires: pkgconfig(fontconfig) >= 2.5.0
BuildRequires: pkgconfig(cairo) >= 1.7.6
BuildRequires: pkgconfig(libthai) >= 0.1.9
BuildRequires: pkgconfig(gobject-introspection-1.0)
%if %{enable_gtkdoc}
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtd412-xml
BuildRequires: gtk-doc >= 0.10
BuildRequires: libxslt-proc
%endif

%description
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%package -n %{lib_name} 
Summary: %{summary}
Group:	%{group}

%description -n %{lib_name}
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%package -n %{caironame} 
Summary: %{summary} - cairo
Group:	%{group}

%description -n %{caironame}
Library for %{name} - cairo.

%package -n %{ft2name} 
Summary: %{summary} - ft2
Group:	%{group}

%description -n %{ft2name}
Library for %{name} - ft2.

%package -n %{xname} 
Summary: %{summary} - x
Group:	%{group}

%description -n %{xname}
Library for %{name} - x

%package -n %{xftname} 
Summary: %{summary} - xft
Group:	%{group}

%description -n %{xftname}
Library for %{name} - xft

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Conflicts:	gir-repository < 0.6.5

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{gircairo}
Summary:	GObject Introspection interface description for %{name} - cairo
Group:		System/Libraries
Requires:	%{caironame} = %{version}-%{release}
Conflicts:	gir-repository < 0.6.5

%description -n %{gircairo}
GObject Introspection interface description for %{name} - cairo.

%package -n %{girft2}
Summary:	GObject Introspection interface description for %{name} - ft2
Group:		System/Libraries
Requires:	%{ft2name} = %{version}-%{release}
Conflicts:	gir-repository < 0.6.5

%description -n %{girft2}
GObject Introspection interface description for %{name} - ft2.

%package -n %{girxft}
Summary:	GObject Introspection interface description for %{name} - xft
Group:		System/Libraries
Requires:	%{ft2name} = %{version}-%{release}
Conflicts:	gir-repository < 0.6.5

%description -n %{girxft}
GObject Introspection interface description for %{name} - xft.

%package -n %{modulesname}
Summary:	%{summary}
Group:		%{group}
Provides:	lib%{name}%{api_version} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}
%rename %{lib_name}-modules
#need this since we launch pango-querymodules in %post
Provides:	pango-modules = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description -n %{modulesname}
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%package -n %{develname}
Summary:  %{summary}
Group: Development/GNOME and GTK+
%rename	%{name}-devel
%rename	%{name}-doc
Requires:	%{lib_name} = %{version}-%{release}
Conflicts:	%{_lib}pango1.0_0 < 1.28.1-2

%description -n %{develname}
This package includes the development library and header files
for the %{name} package.

%package -n %{develcairo}
Summary:  %{summary} - cairo
Group: Development/GNOME and GTK+
Requires:	%{caironame} = %{version}-%{release}

%description -n %{develcairo}
This package includes the development library and header files
for the %{name}cairo package.

%package -n %{develft2}
Summary:  %{summary} - ft2
Group: Development/GNOME and GTK+
Requires:	%{ft2name} = %{version}-%{release}

%description -n %{develft2}
This package includes the development library and header files
for the %{name}ft2 package.

%package -n %{develx}
Summary:  %{summary} - x
Group: Development/GNOME and GTK+
Requires:	%{xname} = %{version}-%{release}

%description -n %{develx}
This package includes the development library and header files
for the %{name}x package.

%package -n %{develxft}
Summary:  %{summary} - xft
Group: Development/GNOME and GTK+
Requires:	%{xname} = %{version}-%{release}

%description -n %{develxft}
This package includes the development library and header files
for the %{name}xft package.

%prep
%setup -q
%apply_patches

%build
#needed by patch5
autoreconf -fi
%configure2_5x \
	--enable-static=no \
%if !%enable_gtkdoc
	--disable-gtk-doc \
%endif

%make ARCH=%{_arch}

%check
#disabled for https://bugzilla.gnome.org/show_bug.cgi?id=610791
make check

%install
rm -rf %{buildroot}

%makeinstall_std
# remove unpackaged files
find %{buildroot} -name "*.la" -delete

# remove some quite annoying /usr/usr
perl -pi -e "s|/usr/usr/%{_lib}|%{_libdir}|g" %{buildroot}%{_libdir}/*.la

mkdir -p %{buildroot}%{_sysconfdir}/pango/%{_arch}
touch %{buildroot}%{_sysconfdir}/pango/%{_arch}/pango.modules

%ifarch %{biarches_32} %{biarches_64}
mv %{buildroot}%{_bindir}/pango-querymodules %{buildroot}%{_bindir}/%{query_modules}
%endif
%ifarch %{biarches_64}
mv %{buildroot}%{_bindir}/pango-view %{buildroot}%{_bindir}/pango-view%{query_modules_suffix}
%endif

cp -f pango/opentype/README README.opentype

%post -n %{modulesname}
if [ "$1" = "2" -a -r  %{_sysconfdir}/pango/pango.modules ]; then
  rm -f %{_sysconfdir}/pango/pango.modules 
fi
%{_bindir}/%{query_modules} > %{_sysconfdir}/pango/%{_arch}/pango.modules

%files
%doc README AUTHORS NEWS
%ifnarch %{biarches_32} %{biarches_64}
%{_bindir}/pango-querymodules
%endif
%{_mandir}/man1/*
%dir %{_sysconfdir}/pango
%config(noreplace) %{_sysconfdir}/pango/pango*.aliases

%files -n %{modulesname}
%ifarch %{biarches_32} %{biarches_64}
%{_bindir}/pango-querymodules-*
%endif
%dir %{_libdir}/pango
%dir %{_libdir}/pango/%{module_version}
%dir %{_libdir}/pango/%{module_version}/modules
%{_libdir}/pango/%{module_version}/modules/*.so
%dir %{_sysconfdir}/pango/%{_arch}
%ghost %verify (not md5 mtime size) %config(noreplace) %{_sysconfdir}/pango/%{_arch}/pango.modules

%files -n %{lib_name}
%{_libdir}/libpango-%{api_version}.so.%{lib_major}*

%files -n %{caironame}
%{_libdir}/libpangocairo-%{api_version}.so.%{lib_major}*

%files -n %{ft2name}
%{_libdir}/libpangoft2-%{api_version}.so.%{lib_major}*

%files -n %{xname}
%{_libdir}/libpangox-%{api_version}.so.%{lib_major}*

%files -n %{xftname}
%{_libdir}/libpangoxft-%{api_version}.so.%{lib_major}*

%files -n %{girname}
%_libdir/girepository-1.0/Pango-%{gir_major}.typelib

%files -n %{gircairo}
%_libdir/girepository-1.0/PangoCairo-%{gir_major}.typelib

%files -n %{girft2}
%_libdir/girepository-1.0/PangoFT2-%{gir_major}.typelib

%files -n %{girxft}
%_libdir/girepository-1.0/PangoXft-%{gir_major}.typelib

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/pango
%doc ChangeLog pango-view/HELLO.txt
%{_bindir}/pango-view*
%{_libdir}/libpango-*.so
%{_libdir}/pkgconfig/pango.pc
%_datadir/gir-1.0/Pango-%{gir_major}.gir
%{_includedir}/pango-1.0/pango/pango-*.h
%{_includedir}/pango-1.0/pango/pango.h
%{_includedir}/pango-1.0/pango/pangofc-*.h

%files -n %{develcairo}
%{_libdir}/libpangocairo*.so
%{_libdir}/pkgconfig/pangocairo.pc
%_datadir/gir-1.0/PangoCairo-%{gir_major}.gir
%{_includedir}/pango-1.0/pango/pangocairo.h

%files -n %{develft2}
%{_libdir}/libpangoft2-*.so
%{_libdir}/pkgconfig/pangoft2.pc
%_datadir/gir-1.0/PangoFT2-%{gir_major}.gir
%{_includedir}/pango-1.0/pango/pangoft2.h

%files -n %{develx}
%{_libdir}/libpangox-*.so
%{_libdir}/pkgconfig/pangox.pc
%{_includedir}/pango-1.0/pango/pangox.h

%files -n %{develxft}
%{_libdir}/libpangoxft-*.so
%{_libdir}/pkgconfig/pangoxft.pc
%_datadir/gir-1.0/PangoXft-%{gir_major}.gir
%{_includedir}/pango-1.0/pango/pangoxft.h
%{_includedir}/pango-1.0/pango/pangoxft-render.h

