%define url_ver %(echo %{version}|cut -d. -f1,2)
%define enable_gtkdoc 1

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

%define api 1.0
%define module_version 1.8.0
%define major 0

%define modules %mklibname %{name}-modules %{api}
%define libname %mklibname %{name} %{api} %{major}
%define libcairo %mklibname %{name}cairo %{api} %{major}
%define libft2 %mklibname %{name}ft2_ %{api} %{major}
%define libxft %mklibname %{name}xft %{api} %{major}

%define girname %mklibname %{name}-gir %{api}
%define gircairo %mklibname %{name}cairo-gir %{api}
%define girft2 %mklibname %{name}ft2-gir %{api}
%define girxft %mklibname %{name}xft-gir %{api}

%define develname %mklibname -d %{name} %{api}
%define develcairo %mklibname -d %{name}cairo %{api}
%define develft2 %mklibname -d %{name}ft2_ %{api}
%define develx %mklibname -d %{name}x %{api}
%define develxft %mklibname -d %{name}xft %{api}
%bcond_with	bootstrap

Summary:	System for layout and rendering of internationalized text
Name:		pango
Version:	1.33.7
Release:	1
License:	LGPLv2+
Group:		System/Internationalization
URL:		http://www.pango.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pango/%{url_ver}/%{name}-%{version}.tar.xz
# (gb) 1.4.0-2mdk biarch support
Patch5:		pango-1.32.0-lib64.patch

BuildRequires:	pkgconfig(cairo) >= 1.7.6
BuildRequires:	pkgconfig(fontconfig) >= 2.5.0
BuildRequires:	pkgconfig(freetype2) >= 2.1.3
BuildRequires:	pkgconfig(glib-2.0) >= 2.24
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libthai) >= 0.1.9
BuildRequires:	pkgconfig(xft) >= 2.0
BuildRequires:	pkgconfig(harfbuzz) >= 0.9.3-3
BuildRequires:	harfbuzz-devel
%if %{enable_gtkdoc}
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk-doc >= 0.10
BuildRequires:	xsltproc
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
%endif

%package -n %{modules}
Summary:	Internationalized text layout and rendering system
Group:		%{group}
Provides:	lib%{name}%{api} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}
%rename		%{_lib}pango1.0_0-modules
%rename		%{name}
#need this since we launch pango-querymodules in %post
Provides:	pango-modules = %{version}-%{release}

%description -n %{modules}
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%package -n %{develname}
Summary:	Internationalized text layout and rendering system
Group:		Development/GNOME and GTK+
%rename		pango-devel
%rename		pango-doc
Requires:	%{libname} = %{version}-%{release}
%if !%{with bootstrap}
Requires:	%{girname} = %{version}-%{release}
%endif
Conflicts:	%{_lib}pango1.0_0 < 1.28.1-2

%description -n %{develname}
This package includes the development library and header files
for the %{name} package.

%package -n %{develcairo}
Summary:	Internationalized text layout and rendering system - cairo
Group:		Development/GNOME and GTK+
Requires:	%{libcairo} = %{version}-%{release}
%if !%{with bootstrap}
Requires:	%{gircairo} = %{version}-%{release}
%endif

%description -n %{develcairo}
This package includes the development library and header files
for the %{name}cairo package.

%package -n %{develft2}
Summary:	Internationalized text layout and rendering system - ft2
Group:		Development/GNOME and GTK+
Requires:	%{libft2} = %{version}-%{release}
%if !%{with bootstrap}
Requires:	%{girft2} = %{version}-%{release}
%endif

%description -n %{develft2}
This package includes the development library and header files
for the %{name}ft2 package.

%package -n %{develxft}
Summary:	Internationalized text layout and rendering system - xft
Group:		Development/GNOME and GTK+
Requires:	%{libxft} = %{version}-%{release}
%if !%{with bootstrap}
Requires:	%{girxft} = %{version}-%{release}
%endif

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
	--with-included-modules=basic-fc \
%if %{with bootstrap}
        --enable-introspection=no \
%endif
%if !%enable_gtkdoc
	--disable-gtk-doc \
%endif

%make ARCH=%{_arch}

%check
#disabled for https://bugzilla.gnome.org/show_bug.cgi?id=610791
make check || true

%install
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

%post -n %{modules}
if [ "$1" = "2" -a -r  %{_sysconfdir}/pango/pango.modules ]; then
  rm -f %{_sysconfdir}/pango/pango.modules 
fi
%{_bindir}/%{query_modules} --system > %{_sysconfdir}/pango/%{_arch}/pango.modules

%postun -n %{modules}
if [ "$1" -gt "0" -a -r  %{_sysconfdir}/pango/pango.modules ]; then
  rm -f %{_sysconfdir}/pango/pango.modules 
fi
%{_bindir}/%{query_modules} > %{_sysconfdir}/pango/%{_arch}/pango.modules

%files -n %{modules}
%doc README AUTHORS NEWS
%dir %{_sysconfdir}/pango
%dir %{_sysconfdir}/pango/%{_arch}
%ghost %verify (not md5 mtime size) %config(noreplace) %{_sysconfdir}/pango/%{_arch}/pango.modules
%ifnarch %{biarches_32} %{biarches_64}
%{_bindir}/pango-querymodules
%else
%{_bindir}/pango-querymodules-*
%endif
%dir %{_libdir}/pango
%dir %{_libdir}/pango/%{module_version}
%dir %{_libdir}/pango/%{module_version}/modules
%{_libdir}/pango/%{module_version}/modules/*.so
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
%endif

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/pango
%doc ChangeLog pango-view/HELLO.txt
%{_bindir}/pango-view*
%{_libdir}/libpango-*.so
%{_libdir}/pkgconfig/pango.pc
%if !%{with bootstrap}
%{_datadir}/gir-1.0/Pango-%{api}.gir
%endif
%dir %{_includedir}/pango-1.0
%dir %{_includedir}/pango-1.0/pango
%{_includedir}/pango-1.0/pango/pango-*.h
%{_includedir}/pango-1.0/pango/pango.h
%{_includedir}/pango-1.0/pango/pangofc-*.h

%files -n %{develcairo}
%{_libdir}/libpangocairo*.so
%{_libdir}/pkgconfig/pangocairo.pc
%if !%{with bootstrap}
%{_datadir}/gir-1.0/PangoCairo-%{api}.gir
%endif
%{_includedir}/pango-1.0/pango/pangocairo.h

%files -n %{develft2}
%{_libdir}/libpangoft2-*.so
%{_libdir}/pkgconfig/pangoft2.pc
%if !%{with bootstrap}
%{_datadir}/gir-1.0/PangoFT2-%{api}.gir
%endif
%{_includedir}/pango-1.0/pango/pangoft2.h

%files -n %{develxft}
%{_libdir}/libpangoxft-*.so
%{_libdir}/pkgconfig/pangoxft.pc
%if !%{with bootstrap}
%{_datadir}/gir-1.0/PangoXft-%{api}.gir
%endif
%{_includedir}/pango-1.0/pango/pangoxft.h
%{_includedir}/pango-1.0/pango/pangoxft-render.h

