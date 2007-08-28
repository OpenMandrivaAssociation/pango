# enable_gtkdoc: Toggle whether gtkdoc stuff should be rebuilt
#      0 = No
#      1 = Yes
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


# Version of libraries required
%define req_glib_version       2.9.0
%define req_freetype2_version  2.1.3-4mdk
%define req_fontconfig_version  2.1-4mdk
%define req_cairo_version  1.2.2

%define api_version	1.0
%define module_version	1.6.0
%define lib_major	0
%define lib_name    %mklibname %{name} %{api_version} %{lib_major}
%define libnamedev  %mklibname -d %{name} %{api_version} 

Summary:	System for layout and rendering of internationalized text
Name:		pango
Version:	1.18.1
Release: %mkrel 1
License:	LGPL
Group:		System/Internationalization
URL:		http://www.pango.org/
BuildRequires: glib2-devel >= %{req_glib_version} 
BuildRequires: freetype2-devel >= %{req_freetype2_version}
%if %mdkversion <= 200600
BuildRequires: libXft2-devel >= 2.0
%else
BuildRequires:libxft-devel >= 2.0
%endif
BuildRequires: fontconfig-devel >= %{req_fontconfig_version}
BuildRequires: libcairo-devel >= %req_cairo_version
BuildRequires: thai-devel >= 0.1.9
%if %enable_gtkdoc
BuildRequires: gtk-doc >= 0.10
BuildRequires: libxslt-proc docbook-style-xsl
BuildRequires: automake1.8
%endif
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pango/%{name}-%{version}.tar.bz2
# (gb) 1.4.0-2mdk biarch support
Patch5:		pango-1.2.5-lib64.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root


%description
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%package -n %{lib_name} 
Summary: %{summary}
Group:   %{group}
Provides:	lib%{name}%{api_version} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}
Requires:	%{name} = %{version}
Requires: freetype2 >= %{req_freetype2_version}
Requires: fontconfig >= %{req_fontconfig_version}
Requires: glib2 >= %{req_glib_version}
Requires:      %{lib_name}-modules = %{version}

%package -n %{lib_name}-modules
Summary:	%{summary}
Group:		%{group}
#need this since we launch pango-querymodules in %post
Requires(post):                %{lib_name} = %{version}
Provides:	pango-modules = %{version}-%{release}

%description -n %{lib_name}-modules
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%description -n %{lib_name}
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.
It is the next step on Gtk+ internationalization.

%package -n %{libnamedev}
Summary:  %{summary}
Group: Development/GNOME and GTK+
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{name}%{api_version}-devel = %{version}-%{release}
Requires:	%{name} = %{version}
Requires:	%{lib_name} = %{version}
Requires:	%{name}-doc >= %{version}
Obsoletes: %mklibname -d %{name} %{api_version} %{lib_major}
Conflicts:	%{name} < 1.18.0-3mdv

%description -n %{libnamedev}
This package includes the static libraries and header files
for the pango package.

%package doc
Summary:  %{summary}
Group: Development/GNOME and GTK+

%description doc
This package provides API documentation for Pango.

%prep
%setup -q
%patch5 -p1 -b .lib64
#needed by patch5
aclocal-1.8
automake-1.8
autoconf

%build

%configure2_5x \
	--enable-static=no \
%if %enable_gtkdoc
	--enable-gtk-doc=yes \
%endif

%make ARCH=%{_arch}

%check
make check

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pango/%{_arch}
touch $RPM_BUILD_ROOT%{_sysconfdir}/pango/%{_arch}/pango.modules

%ifarch %{biarches_32} %{biarches_64}
mv $RPM_BUILD_ROOT%{_bindir}/pango-querymodules $RPM_BUILD_ROOT%{_bindir}/%{query_modules}
%endif
%ifarch %{biarches_64}
mv $RPM_BUILD_ROOT%{_bindir}/pango-view $RPM_BUILD_ROOT%{_bindir}/pango-view%{query_modules_suffix}
%endif

cp -f pango/opentype/README README.opentype

# remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/pango/%{module_version}/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name}-modules
if [ "$1" = "2" -a -r  %{_sysconfdir}/pango/pango.modules ]; then
  rm -f %{_sysconfdir}/pango/pango.modules 
fi
%{_bindir}/%{query_modules} > %{_sysconfdir}/pango/%{_arch}/pango.modules

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README AUTHORS
%doc NEWS 
%ifnarch %{biarches_32} %{biarches_64}
%{_bindir}/pango-querymodules
%endif
%{_mandir}/man1/*
%dir %{_sysconfdir}/pango
%config(noreplace) %{_sysconfdir}/pango/pango*.aliases

%files -n %{lib_name}-modules
%defattr(-, root, root)
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
%defattr(-,root,root)
%{_libdir}/libpango-%{api_version}.so.%{lib_major}*
%{_libdir}/libpangoft2-%{api_version}.so.%{lib_major}*
%{_libdir}/libpangox-%{api_version}.so.%{lib_major}*
%{_libdir}/libpangoxft-%{api_version}.so.%{lib_major}*
%{_libdir}/libpangocairo-%{api_version}.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(-, root, root)
%{_bindir}/pango-view*
%{_libdir}/libpango-*.so
%{_libdir}/libpangox-*.so
%{_libdir}/libpangoxft-*.so
%{_libdir}/libpangoft2-*.so
%{_libdir}/libpangocairo*.so
%{_libdir}/pkgconfig/*
%attr(644,root,root) %{_libdir}/*.la
%{_includedir}/*

%files doc
%doc %{_datadir}/gtk-doc/html/pango
%doc ChangeLog
%doc pango-view/HELLO.txt
