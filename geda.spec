%define __noautoreq '.*/bin/awk|.*/bin/gawk'
%define libmajor 42

Summary:	GPL Electronic Design Automation Project
Name:		geda
Epoch:		1
Version:	1.8.1
Release:	5
License:	GPLv2
Group:		Office
Url:		https://www.gpleda.org/
Source:		ftp://ftp.geda-project.org/geda-gaf/stable/v1.8/%{version}/geda-gaf-%{version}.tar.gz
Patch0:		geda-gaf-1.8.1-linkage.patch
Patch1:		geda-gaf-1.8.1-desktop.patch
BuildRequires:	shared-mime-info
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(guile-2.0)
BuildRequires:	libstroke-devel
BuildRequires:	guile
Requires:	geda-gattrib
Requires:	geda-gschem
Requires:	geda-gnetlist
Requires:	geda-gsymcheck
Requires:	geda-symbols
Requires:	geda-utils
Suggests:	geda-docs
Suggests:	geda-examples

%description
The GPL Electronic Design Automation (gEDA) project has produced and
continues working on a full GPL'd suite and toolkit of Electronic
Design Automation tools. These tools are used for electrical circuit
design, schematic capture, simulation, prototyping, and
production. Currently, the gEDA project offers a mature suite of free
software applications for electronics design, including schematic
capture, attribute management, bill of materials (BOM) generation,
net listing into over 20 net list formats, analog and digital
simulation, and printed circuit board (PCB) layout.

%files

#--------------------------------------------------------------------------
%package -n lib%{name}-data
Summary:	Static data from %{name}
Group:		Sciences/Other
Conflicts:	%{name}-symbols < 1:1.6.0-2

%description -n lib%{name}-data
This packages contains some help files and other
static stuff.

The gEDA project is working on producing a full GPL'd suite of
Electronic Design Automation tools. These tools are used for electrical
circuit design, simulation, prototyping, and production.

%files -n lib%{name}-data -f lib%{name}%{libmajor}.lang
%dir %{_datadir}/gEDA
%{_datadir}/gEDA/prolog.ps
%{_datadir}/gEDA/scheme/geda.scm
%{_datadir}/gEDA/scheme/color-map.scm
%{_datadir}/gEDA/system-gafrc
%{_datadir}/gEDA/print-colormap-*
%{_iconsdir}/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/*

#--------------------------------------------------------------------------
%define libname %mklibname %{name} %{libmajor}

%package -n %{libname}
Summary:	Libraries for the gEDA project
Group:		Sciences/Other
Requires:	lib%{name}-data = %{EVRD}

%description -n %{libname}
This package contains libgeda%{libmajor} (library needed by gEDA applications).

The gEDA project is working on producing a full GPL'd suite of
Electronic Design Automation tools. These tools are used for electrical
circuit design, simulation, prototyping, and production.

%files -n %{libname}
%{_libdir}/*.so.%{libmajor}
%{_libdir}/*.so.%{libmajor}.*

#--------------------------------------------------------------------------
%define develname %mklibname -d %{name}

%package -n %{develname}
Summary:	Development libraries for the gEDA project
Group:		Sciences/Other
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
This package contains libgeda%{libmajor} development libraries needed
by gEDA applications) and the necessary header files for development.

The gEDA project is working on producing a full GPL'd suite of
Electronic Design Automation tools. These tools are used for electrical
circuit design, simulation, prototyping, and production.

%files -n %{develname}
%{_libdir}/libgeda.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libgeda

#--------------------------------------------------------------------------
%package symbols
Summary:	Electronic symbols for gEDA
Group:		Sciences/Other

%description symbols
This package contains a bunch of symbols of electronic devices
used by gschem, the gEDA project schematic editor.

%files symbols
%dir %{_datadir}/gEDA/sym
%dir %{_datadir}/gEDA/sym/*/
%{_datadir}/gEDA/sym/*/*
%{_datadir}/gEDA/gafrc.d
%{_datadir}/doc/geda-gaf/nc.pdf

#--------------------------------------------------------------------------
%package gattrib
Summary:	Electronics schematics editor
Group:		Sciences/Other
Requires:	%{name}-symbols = %{EVRD}

%description gattrib
Gattrib is gEDA's attribute editor.  It reads a set of gschem .sch
files (schematic files), and creates a spreadsheet showing all
components in rows, with the associated component attributes listed in
the columns.  It allows the user to add, modify, or delete component
attributes outside of gschem, and then save the .sch files back
out.  When it is completed, it will allow the user to edit attributes
attached to components, nets, and pins.  (Currently, only component
attribute editing is implemented; pin and net attributes are displayed
only.)

%files gattrib -f %{name}-gattrib.lang
%{_bindir}/gattrib
%{_datadir}/gEDA/system-gattribrc
%{_datadir}/gEDA/gattrib-menus.xml
%{_datadir}/applications/geda-gattrib.desktop
%{_iconsdir}/hicolor/*/apps/geda-gattrib.*
%{_datadir}/doc/geda-gaf/man/gattrib.html
%{_mandir}/man1/gattrib.1.xz

#--------------------------------------------------------------------------
%package gschem
Summary:	Electronics schematics editor
Group:		Sciences/Other
Requires:	%{name}-symbols = %{EVRD}
Conflicts:	%{name}-symbols < 1:1.6.0-2

%description gschem
Gschem is an electronics schematic editor. It is part of the gEDA project.

%files gschem -f %{name}-gschem.lang
%{_bindir}/gschem
%{_mandir}/man1/gschem.*
%{_datadir}/gEDA/bitmap/gschem*
%{_datadir}/gEDA/system-gschemrc
%{_datadir}/gEDA/gschem-*
%{_datadir}/gEDA/scheme/auto-place-attribs.scm
%{_datadir}/gEDA/scheme/auto-uref.scm
%{_datadir}/gEDA/scheme/default-attrib-positions.scm 
%{_datadir}/gEDA/scheme/generate_netlist.scm
%{_datadir}/gEDA/scheme/gschem.scm
%{_datadir}/gEDA/scheme/image.scm
%{_datadir}/gEDA/scheme/list-keys.scm
%{_datadir}/gEDA/scheme/partslist-common.scm
%{_datadir}/gEDA/scheme/pcb.scm
%{_datadir}/gEDA/scheme/print.scm
%{_datadir}/gEDA/scheme/print-NB-attribs.scm
%{_datadir}/gEDA/scheme/geda/attrib.scm
%{_datadir}/gEDA/scheme/geda/core/gettext.scm
%{_datadir}/gEDA/scheme/geda/deprecated.scm
%{_datadir}/gEDA/scheme/geda/object.scm
%{_datadir}/gEDA/scheme/geda/os.scm
%{_datadir}/gEDA/scheme/geda/page.scm
%{_datadir}/gEDA/scheme/gschem/attrib.scm
%{_datadir}/gEDA/scheme/gschem/core/gettext.scm
%{_datadir}/gEDA/scheme/gschem/deprecated.scm
%{_datadir}/gEDA/scheme/gschem/gschemdoc.scm
%{_datadir}/gEDA/scheme/gschem/hook.scm
%{_datadir}/gEDA/scheme/gschem/keymap.scm
%{_datadir}/gEDA/scheme/gschem/selection.scm
%{_datadir}/gEDA/scheme/gschem/util.scm
%{_datadir}/gEDA/scheme/gschem/window.scm
%{_datadir}/doc/geda-gaf/man/gschem.html
%{_datadir}/applications/geda-gschem.desktop
%{_iconsdir}/hicolor/*/apps/geda-gschem.*
%{_infodir}/geda-scheme.info.*

#--------------------------------------------------------------------------
%package gsymcheck
Summary:	Electronics schematics editor
Group:		Sciences/Other
Requires:	%{name}-symbols = %{EVRD}

%description gsymcheck
Gsymcheck is a utility to check symbols for gschem. It is part
of the gEDA project.

%files gsymcheck
%{_bindir}/gsymcheck
%{_datadir}/gEDA/system-gsymcheckrc
%{_datadir}/doc/geda-gaf/man/gsymcheck.html
%{_mandir}/man1/gsymcheck.*

#--------------------------------------------------------------------------
%package utils
Summary:	Net lister for the gEDA project
Group:		Sciences/Other
Requires:	%{name}-symbols = %{EVRD}

%description utils
Several utilities for the gEDA project.

%files utils
%{_bindir}/gmk_sym
%{_bindir}/smash_megafile
%{_bindir}/convert_sym
%{_bindir}/sarlacc_schem
%{_bindir}/sarlacc_sym
%{_bindir}/gschlas
%{_bindir}/olib
%{_bindir}/refdes_renum
%{_bindir}/gsch2pcb
%{_bindir}/pads_backannotate
%{_bindir}/tragesym
%{_bindir}/garchive
%{_bindir}/grenum
%{_bindir}/gsymfix
%{_bindir}/schdiff
%{_bindir}/pcb_backannotate
%{_bindir}/gxyrs
%{_datadir}/gEDA/perl/lib/gxyrs.pm
%{_datadir}/gEDA/system-gschlasrc
%{_datadir}/doc/geda-gaf/man/grenum.html
%{_datadir}/doc/geda-gaf/man/convert_sym.html
%{_datadir}/doc/geda-gaf/man/garchive.html
%{_datadir}/doc/geda-gaf/man/gmk_sym.html
%{_datadir}/doc/geda-gaf/man/gsch2pcb.html
%{_datadir}/doc/geda-gaf/man/gschlas.html
%{_datadir}/doc/geda-gaf/man/gsymfix.html
%{_datadir}/doc/geda-gaf/man/gxyrs.html
%{_datadir}/doc/geda-gaf/man/olib.html
%{_datadir}/doc/geda-gaf/man/pads_backannotate.html
%{_datadir}/doc/geda-gaf/man/pcb_backannotate.html
%{_datadir}/doc/geda-gaf/man/refdes_renum.html
%{_datadir}/doc/geda-gaf/man/sarlacc_schem.html
%{_datadir}/doc/geda-gaf/man/sarlacc_sym.html
%{_datadir}/doc/geda-gaf/man/schdiff.html
%{_datadir}/doc/geda-gaf/man/smash_megafile.html
%{_datadir}/doc/geda-gaf/man/tragesym.html
%{_datadir}/doc/geda-gaf/readmes
%{_mandir}/man1/grenum.1*
%{_mandir}/man1/convert_sym.1*
%{_mandir}/man1/garchive.1*
%{_mandir}/man1/gmk_sym.1*
%{_mandir}/man1/gsch2pcb.1*
%{_mandir}/man1/gschlas.1*
%{_mandir}/man1/gsymfix.1*
%{_mandir}/man1/gxyrs.1*
%{_mandir}/man1/olib.1*
%{_mandir}/man1/pads_backannotate.1*
%{_mandir}/man1/pcb_backannotate.1*
%{_mandir}/man1/refdes_renum.1*
%{_mandir}/man1/sarlacc_schem.1*
%{_mandir}/man1/sarlacc_sym.1*
%{_mandir}/man1/schdiff.1*
%{_mandir}/man1/smash_megafile.1*
%{_mandir}/man1/tragesym.1*

#--------------------------------------------------------------------------
%package gnetlist
Summary:	Net lister for the gEDA project
Group:		Sciences/Other
Requires:	%{name}-symbols = %{EVRD}
Conflicts:	%{name}-symbols < 1:1.6.0-2

%description gnetlist
Gnetlist generates net lists from schematics drawn with gschem
(the gEDA schematic editor). Possible output formats are:
- spice net lists
- verilog
- tango

%files gnetlist
%dir %{_datadir}/gEDA
%{_bindir}/gnetlist
%{_bindir}/sw2asc
%{_mandir}/man1/gnetlist.*
%{_datadir}/gEDA/system-gnetlistrc
%{_datadir}/gEDA/scheme/gnet*.scm
%dir %{_datadir}/gEDA/scheme/gnetlist
%{_datadir}/gEDA/scheme/gnetlist/backend-getopt.scm
%{_datadir}/doc/geda-gaf/man/gnetlist.html
%{_datadir}/doc/geda-gaf/man/sw2asc.html
%{_mandir}/man1/sw2asc.1*

#--------------------------------------------------------------------------
%package examples
Summary:	Examples for the gEDA project
Group:		Sciences/Other

%description examples
This package provide example for the gEDA project.

%files examples
%{_datadir}/doc/geda-gaf/examples

#--------------------------------------------------------------------------
%package docs
Summary:	Doc for the gEDA project
Group:		Sciences/Other

%description docs
This package provides documentation for the gEDA project.

%files docs
%{_datadir}/doc/geda-gaf/wiki
%{_datadir}/doc/geda-gaf/gedadocs.html

#--------------------------------------------------------------------------

%prep
%setup -qn geda-gaf-%{version}
%autopatch -p1

%build
%configure2_5x \
	--disable-update-xdg-database \
	--disable-static \
	--disable-rpath
%make

%install
%makeinstall_std

%find_lang lib%{name}%{libmajor}
%find_lang %{name}-gattrib
%find_lang %{name}-gschem
#fix linting
sed -i 's/\r//' %{buildroot}%{_datadir}/doc/geda-gaf/examples/RF_Amp/{Q2,MSA-2643,Q1}.cir
sed -i 's/\r//' %{buildroot}%{_datadir}/doc/geda-gaf/examples/TwoStageAmp/spice.netlist





