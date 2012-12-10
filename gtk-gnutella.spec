%define name	gtk-gnutella
%define version	0.98.3
%define release	1
%define summary	Gnutella GTK client

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	%{summary}
License: 	GPLv2
Group: 		Networking/File transfer
Source0: 	http://downloads.sourceforge.net/project/gtk-gnutella/gtk-gnutella/%{version}/%{name}-%{version}.tar.bz2
Source1:	%{name}-remote-shell.txt.bz2
Source10:	%{name}.16.png
Source11:	%{name}.32.png
Source12:	%{name}.48.png
URL: 		http://gtk-gnutella.sourceforge.net
Buildrequires:	gtk+2-devel
Buildrequires:	libxml2-devel
BuildRequires:	gnutls-devel
BuildRequires:	glib2-devel
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
%setup -q -n %{name}-%{version}

%build
./Configure -Dprefix=%{_prefix}/ -Dbindir=%{_bindir}/ -Dprivlib=%{_datadir}/%{name}/ \
        -Dsysman=%{_mandir}/man1/ -Ucc="$CC" -Dccflags="-Wall $CFLAGS" \
        -Doptimize="%{optflags}" -Dgtkversion=2 -Dremotectrl=true \
        -Dofficial=true -ders 
#perl -p -i -e 's/SQuoTe\(a\)\"a/SQuoTe\(a\)\"a\"/g' config.h
#perl -p -i -e 's/EQuoTe\(a\)a\"/EQuoTe\(a\)\"a\"/g' config.h
#perl -p -i -e 's/usr\/local/usr/g' src/Makefile
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}/%{_mandir}/man1
make install INSTALL_PREFIX=%{buildroot}
chmod 755 %{buildroot}%{_bindir}/%{name}

# extra docs
bunzip2 -c %{SOURCE1} > remote-shell.txt

# icons
install -D -m 644 %{SOURCE10} %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 644 %{SOURCE11} %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 %{SOURCE12} %{buildroot}%{_liconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO AUTHORS LICENSE ChangeLog
%doc remote-shell.txt
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/gtk-gnutella.desktop



%changelog
* Tue Jun 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.98.3-1
+ Revision: 802705
- version update 0.98.3

* Fri Aug 12 2011 Andrey Bondrov <abondrov@mandriva.org> 0.97-1
+ Revision: 694190
- imported package gtk-gnutella

