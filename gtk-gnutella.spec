Name: 		gtk-gnutella
Version: 	1.1.15
Release: 	1
Summary: 	Gnutella GTK client
License: 	GPLv2
Group: 		Networking/File transfer
Source0: 	http://sourceforge.net/projects/gtk-gnutella/files/gtk-gnutella-%{version}.tar.xz
URL: 		http://gtk-gnutella.sourceforge.net
Patch0:         gtk-gnutella-1.1.15-malloc.patch
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libglade-2.0)
Buildrequires:	libxml2-devel
BuildRequires:	gnutls-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	dbus-devel
BuildRequires:	zlib-devel
Buildrequires:	bison
Buildrequires:	byacc
Buildrequires:	gettext

%description
Gtk-gnutella is a client of Gnutella network (http://www.gnutella.com/).
It's a fully-featured servent, designed to share any type of file.
Gtk-gnutella implements compressed connections, ultrapeer and leaf 
nodes, Passive/Active Remote Queueing (PARQ), and other modern 
gnutella network features.

%prep
%setup -q
%autopatch -p1

%build
export CC=gcc
export CXX=g++

./Configure -O -Dprefix=%{_prefix} -Dbindir=%{_bindir} \
        -Dglibpth="/%{_lib} %{_libdir}" \
        -Dprivlib=%{_datadir}/%{name} -Dsysman=%{_mandir}/man1 \
        -Dccflags="%{optflags}" -Dcc="%{__cc}" -Dyacc="byacc" \
        -Dgtkversion=%{?_with_gtk1:1}%{!?_with_gtk1:2} \
        -Dofficial=true -ders
make


%install
make install INSTALL_PREFIX=%{buildroot}
make install.man INSTALL_PREFIX=%{buildroot}

rm -f %{buildroot}%{_datadir}/pixmaps/*.svg
install -D -m 644 extra_files/gtk-gnutella.16.png \
        %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gtk-gnutella.png
install -D -m 644 extra_files/gtk-gnutella.32.png \
        %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gtk-gnutella.png
install -D -m 644 extra_files/gtk-gnutella.png \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gtk-gnutella.png
install -D -m 644 extra_files/gtk-gnutella.svg \
        %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/gtk-gnutella.svg

desktop-file-install --delete-original  \
        --dir %{buildroot}%{_datadir}/applications   \
        %{buildroot}%{_datadir}/applications/*

%find_lang %name

%files  -f %{name}.lang
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/gtk-gnutella/
%{_datadir}/applications/*
%{_datadir}/appdata/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*

%doc README TODO AUTHORS LICENSE GEO_LICENSE doc/other/shell.txt


%changelog
* Tue Jun 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.98.3-1
+ Revision: 802705
- version update 0.98.3

* Fri Aug 12 2011 Andrey Bondrov <abondrov@mandriva.org> 0.97-1
+ Revision: 694190
- imported package gtk-gnutella

