Summary: A project manager
Name: geda
Epoch: 1
Version: 1.4.2
Release: %{mkrel 1}
License: GPLv2
Group: Office
Url: http://www.geda.seul.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: geda-gattrib
Requires: geda-gschem
Requires: geda-gnetlist
Requires: geda-gsymcheck
Requires: geda-symbols
Requires: geda-utils
Suggests: geda-docs
Suggests: geda-examples

%description
The gEDA project is working on producing a full GPL'd
suite of Electronic Design Automation tools.

gEDA Suite Project Manager is a start point for everything what 
you may want to do. It is used to organize your files and easy 
running tools. It simplifies your job.

%files 
%defattr(-,root,root)
