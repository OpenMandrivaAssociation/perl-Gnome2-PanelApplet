%define upstream_name       Gnome2-PanelApplet
%define upstream_version    0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    Perl module for the GNOME panel-applet library
License:    GPL or Artistic
Group:      Development/GNOME and GTK+
URL:        http://gtk2-perl.sf.net/
Source:     %{upstream_name}-%{upstream_version}.tar.bz2
BuildRequires: gtk+2-devel 
BuildRequires: gnomeui2-devel
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gnome2 >= 1.042
BuildRequires: perl-Gnome2-GConf >= 1.044
BuildRequires: perl-Glib >= 1.153
BuildRequires: libpanel-applet-devel
BuildRequires: perl-ExtUtils-PkgConfig
Buildrequires: perl-devel
Requires: perl-Glib >= 1.153
Requires: gtk+2
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This module provides perl access to the libpanel-applet library,
the Gnome Applet library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="%{optflags}"
#%make test || :

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/*


