%define upstream_name Gnome2-PanelApplet
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl module for the GNOME panel-applet library
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		https://gtk2-perl.sf.net/
Source0:	http://www.cpan.org/modules/by-module/Gnome2/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libpanelapplet-2.0)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Glib) >= 1.153
BuildRequires:	perl(Gnome2) >= 1.042
BuildRequires:	perl(Gnome2::GConf) >= 1.044
Buildrequires:	perl-devel

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
%makeinstall_std

%files
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.30.0-2
+ Revision: 773590
- drop redundant dependencies
- cleanout spec
- use pkgconfig() deps for buildrequires
- mass rebuild of perl extensions against perl 5.14.2

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 515364
- update to 0.03

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 504827
- rebuild using %%perl_convert_version

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 420193
- new perl version macro

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.02-5mdv2009.0
+ Revision: 257117
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2008.1
+ Revision: 152091
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 09 2007 Thierry Vignaud <tv@mandriva.org> 0.02-2mdv2008.0
+ Revision: 95783
- versionnate buildrequires
- buildrequires perl-Gnome2-GConf
- new release

* Mon Aug 13 2007 Thierry Vignaud <tv@mandriva.org> 0.01-1mdv2008.0
+ Revision: 62779
- fixx requires
- new release

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 0.0-7mdv2008.0
+ Revision: 43106
- rebuild


* Wed Nov 02 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.0-6mdk
- Fix Mistake

* Thu Sep 29 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.0-5mdk
- Rebuild

* Mon Jun 27 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0-4mdk
- build release

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0-3mdk
- rebuild for new perl

* Fri Aug 13 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0-2mdk
- rebuild for perl-5.8.5
- remove explicit require on libgtk+2
- use %%makeinstall_std

* Sun Mar 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0-1mdk
- initial release

