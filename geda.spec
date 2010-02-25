%define libmajor 38

Summary: GPL Electronic Design Automation Project
Name: geda
Epoch: 1
Version: 1.6.1
Release: %{mkrel 1}
License: GPLv2
Group: Office
Url: http://www.gpleda.org/
Source: http://geda.seul.org/release/v1.6/%version/geda-gaf-%version.tar.gz
Patch0: geda-gaf-1.6.0-fix-str-fmt.patch
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: gtk+2-devel
BuildRequires: shared-mime-info
BuildRequires: guile-devel
BuildRequires: libstroke-devel
Requires: geda-gattrib
Requires: geda-gschem
Requires: geda-gnetlist
Requires: geda-gsymcheck
Requires: geda-symbols
Requires: geda-utils
Suggests: geda-docs
Suggests: geda-examples

%description
The GPL Electronic Design Automation (gEDA) project has produced and
continues working on a full GPL'd suite and toolkit of Electronic
Design Automation tools. These tools are used for electrical circuit
design, schematic capture, simulation, prototyping, and
production. Currently, the gEDA project offers a mature suite of free
software applications for electronics design, including schematic
capture, attribute management, bill of materials (BOM) generation,
netlisting into over 20 netlist formats, analog and digital
simulation, and printed circuit board (PCB) layout.

%files 
%defattr(-,root,root)

#--------------------------------------------------------------------------
%package -n lib%{name}-data
Summary: Static data from %name
Group: Sciences/Other
Conflicts: %{name}-symbols < 1:1.6.0-2

%description -n lib%{name}-data
This packages contains some help files and other
static stuf.

The gEDA project is working on producing a full GPL'd suite of
Electronic Design Automation tools. These tools are used for electrical
circuit design, simulation, prototyping, and production.

%files -n lib%{name}-data -f lib%{name}%{libmajor}.lang
%defattr(-,root,root)
%dir %{_datadir}/gEDA
%{_datadir}/gEDA/prolog.ps
%{_datadir}/gEDA/scheme/geda.scm
%{_datadir}/gEDA/scheme/color-map.scm
%{_datadir}/gEDA/system-gafrc
%{_datadir}/gEDA/print-colormap-*
%{_iconsdir}/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/*

#--------------------------------------------------------------------------
%define libname %mklibname %name %libmajor

%package -n %libname
Summary: Libraries for the gEDA project
Group: Sciences/Other
Requires: lib%{name}-data = %epoch:%version

%description -n %libname
This package contains libgeda%{major} (library needed by gEDA applications).

The gEDA project is working on producing a full GPL'd suite of
Electronic Design Automation tools. These tools are used for electrical
circuit design, simulation, prototyping, and production.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{libmajor}
%{_libdir}/*.so.%{libmajor}.*

#--------------------------------------------------------------------------
%define develname %mklibname -d %name

%package -n %develname
Summary: Development libraries for the gEDA project
Group: Sciences/Other
Provides: %name-devel = %epoch:%version-%release
Requires: %{libname} = %epoch:%version

%description -n %develname
This package contains libgeda%{major} development libraries needed
by gEDA applications) and the necessary header files for development.

The gEDA project is working on producing a full GPL'd suite of
Electronic Design Automation tools. These tools are used for electrical
circuit design, simulation, prototyping, and production.

%files -n %develname
%defattr(-,root,root)
%{_libdir}/libgeda.so
%{_libdir}/libgeda.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libgeda

#--------------------------------------------------------------------------
%package symbols
Summary: Electronic symbols for gEDA
Group: Sciences/Other

%description symbols
This package contains a bunch of symbols of electronic devices
used by gschem, the gEDA project schematic editor.

%files symbols
%defattr(-,root,root)
%dir %{_datadir}/gEDA/sym
%dir %{_datadir}/gEDA/sym/*/
%{_datadir}/gEDA/sym/*/*
%{_datadir}/gEDA/gafrc.d
%{_datadir}/doc/geda-gaf/nc.pdf

#--------------------------------------------------------------------------
%package gattrib
Summary: Electronics schematics editor
Group: Sciences/Other
Requires: %{name}-symbols = %epoch:%version-%release

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
%defattr(-,root,root)
%_bindir/gattrib
%_datadir/gEDA/system-gattribrc
%_datadir/gEDA/gattrib-menus.xml
%_datadir/applications/geda-gattrib.desktop
%_iconsdir/hicolor/*/apps/geda-gattrib.*

#--------------------------------------------------------------------------
%package gschem
Summary: Electronics schematics editor
Group: Sciences/Other
Requires: %{name}-symbols = %epoch:%version-%release
Conflicts: %{name}-symbols < 1:1.6.0-2

%description gschem
Gschem is an electronics schematic editor. It is part of the gEDA project.

%files gschem -f %{name}-gschem.lang
%defattr(-,root,root)
%{_bindir}/gschem
%{_bindir}/gschemdoc
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
%{_datadir}/gEDA/scheme/pcb.scm
%{_datadir}/gEDA/scheme/print.scm
%{_datadir}/gEDA/scheme/print-NB-attribs.scm
%{_datadir}/doc/geda-gaf/man/gschem.html
%{_datadir}/applications/geda-gschem.desktop
%{_iconsdir}/hicolor/*/apps/geda-gschem.*

#--------------------------------------------------------------------------
%package gsymcheck
Summary: Electronics schematics editor
Group: Sciences/Other
Requires: %{name}-symbols = %epoch:%version-%release

%description gsymcheck
Gsymcheck is a utility to check symbols for gschem. It is part
of the gEDA project.

%files gsymcheck
%defattr(-,root,root)
%{_bindir}/gsymcheck
%{_datadir}/gEDA/system-gsymcheckrc
%{_datadir}/doc/geda-gaf/man/gsymcheck.html
%{_mandir}/man1/gsymcheck.*

#--------------------------------------------------------------------------
%package utils
Summary: Netlister for the gEDA project
Group: Sciences/Other
Requires: %{name}-symbols = %epoch:%version-%release

%description utils
Several utilities for the gEDA project.

%files utils
%defattr(-,root,root)
%{_bindir}/gmk_sym
%{_bindir}/smash_megafile
%{_bindir}/convert_sym
%{_bindir}/sarlacc_schem
%{_bindir}/sarlacc_sym
%{_bindir}/gschlas
%{_bindir}/gschupdate
%{_bindir}/gsymupdate
%{_bindir}/olib
%{_bindir}/refdes_renum
%{_bindir}/gsch2pcb
%{_bindir}/pads_backannotate
%{_bindir}/tragesym
%{_bindir}/garchive
%{_bindir}/grenum
%{_bindir}/gsymfix.pl
%{_bindir}/gnet_hier_verilog.sh
%{_bindir}/pcb_backannotate
%{_bindir}/gxyrs
%{_datadir}/gEDA/perl/lib/gxyrs.pm
%{_datadir}/gEDA/system-gschlasrc
%{_datadir}/doc/geda-gaf/man/grenum.html
%{_datadir}/doc/geda-gaf/readmes
%{_mandir}/man1/grenum.1*

#--------------------------------------------------------------------------
%package gnetlist
Summary: Netlister for the gEDA project
Group: Sciences/Other
Requires: %{name}-symbols = %epoch:%version-%release
Conflicts: %{name}-symbols < 1:1.6.0-2

%description gnetlist
Gnetlist generates netlists from schematics drawn with gschem
(the gEDA schematic editor). Possible output formats are:
- spice netlists
- verilog
- tango

%files gnetlist
%defattr(-,root,root)
%dir %{_datadir}/gEDA
%{_bindir}/gnetlist
%{_bindir}/mk_verilog_syms
%{_bindir}/sw2asc
%{_bindir}/sch2eaglepos.sh
%{_mandir}/man1/gnetlist.*
%{_datadir}/gEDA/system-gnetlistrc
%{_datadir}/gEDA/scheme/gnet*.scm
%{_datadir}/doc/geda-gaf/man/gnetlist.html

#--------------------------------------------------------------------------
%package examples
Summary: Examples for the gEDA project
Group: Sciences/Other

%description examples
This package provide example for the gEDA project.

%files examples
%defattr(-,root,root)
%{_datadir}/doc/geda-gaf/examples

#--------------------------------------------------------------------------
%package docs
Summary: Doc for the gEDA project
Group: Sciences/Other

%description docs
This package provides documentation for the gEDA project.

%files docs
%defattr(-,root,root)
%{_datadir}/doc/geda-gaf/wiki
%{_datadir}/doc/geda-gaf/gedadocs.html

#--------------------------------------------------------------------------

%prep
%setup -qn geda-gaf-%{version}
%patch0 -p0

%build
%configure2_5x --disable-update-xdg-database --disable-static
%make

%install
rm -fr %buildroot
%makeinstall_std

%find_lang lib%{name}%{libmajor}
%find_lang %{name}-gattrib
%find_lang %{name}-gschem

%clean
rm -fr %buildroot
