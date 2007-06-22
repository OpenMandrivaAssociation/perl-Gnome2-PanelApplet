%define module Gnome2-PanelApplet

Summary: Perl module for the GNOME panel-applet library
Name:    perl-%module
Version: 0.0
Release: %mkrel 7
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gnome2 >= 0.30
BuildRequires: perl-Glib > 1.00
BuildRequires: libpanel-applet-devel
BuildRequires: perl-ExtUtils-PkgConfig
Buildrequires: perl-devel

Requires: gtk+2

%description
This module provides perl access to the libpanel-applet library,
the Gnome Applet library.

%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 
perl Makefile.PL INSTALLDIRS=vendor

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/*


