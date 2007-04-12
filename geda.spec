%define name geda
%define version 20060123
%define release %mkrel 2

Summary: A project manager
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source20: %name-16.png
Source21: %name-32.png
Source22: %name-48.png
License: GPL
Group: Office
Url: http://www.geda.seul.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libgtk+-devel
BuildRequires: libglib-devel
BuildRequires: libpng-devel
BuildRequires: gtk2-devel
Requires: geda-gschem

%description
The gEDA project is working on producing a full GPL'd
suite of Electronic Design Automation tools.

gEDA Suite Project Manager is a start point for everything what 
you may want to do. It is used to organize your files and easy 
running tools. It simplifies your job.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p %buildroot{%_menudir,%_liconsdir,%_iconsdir,%_miconsdir}
cat <<EOF >$RPM_BUILD_ROOT%{_menudir}/%name
?package(%name):\
needs="x11"\
section="More Applications/Sciences/Electricity"\
title="gEDA"\
longtitle="Geda project manager"\
icon="%name.png"\
command="%name"
EOF

install -D -m644 %{SOURCE20} $RPM_BUILD_ROOT%{_miconsdir}/%name.png
install -D -m644 %{SOURCE21} $RPM_BUILD_ROOT%{_iconsdir}/%name.png
install -D -m644 %{SOURCE22} $RPM_BUILD_ROOT%{_liconsdir}/%name.png

%find_lang %name

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README NEWS 
%_bindir/geda
%_bindir/raw2gw
%_bindir/graphman
%_menudir/%name
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png



