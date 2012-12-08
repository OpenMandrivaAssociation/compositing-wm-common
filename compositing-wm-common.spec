%define rname compositing-wm
%define imgname mandriva-top 
%define name %{rname}-common
%define version 2010.0
%define release %mkrel 2

Name: %name
Version: %version
Release: %release
Summary: Common tools for compositing window managers
Group: System/X11
URL: http://www.mandriva.com
Source0: %{rname}.xinit
Source1: %{rname}.sysconfig
Source2: %{rname}-start
Source3: %{imgname}.png
Source5: compiz-manager
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-root
Requires: glxinfo
Requires: xvinfo

%description
This package contains tools for compositing window managers, such as
Compiz. This includes X session scripts, configuration files and
images.

%prep
%setup -q -c -T

%install
rm -rf %{buildroot}
install -D -m 0755 %SOURCE0 %{buildroot}%{_sysconfdir}/X11/xinit.d/40%{rname}
install -D -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/sysconfig/%{rname}
install -D -m 0755 %SOURCE2 %{buildroot}%{_bindir}/%{rname}-start
install -D -m 0755 %SOURCE5 %{buildroot}%{_bindir}/compiz-manager
install -D -m 0644 %SOURCE3 %{buildroot}%{_datadir}/%{rname}/%{imgname}.png
perl -pi -e "s!__LIBDIR__!%{_libdir}!" %{buildroot}%{_bindir}/%{rname}-start



# Fix the paths in the compiz-manager script
sed -i "s|/usr/local|/usr|" %{buildroot}%{_bindir}/compiz-manager
sed -i "s|/usr/bin|%{_bindir}|" %{buildroot}%{_bindir}/compiz-manager
sed -i "s|/usr/lib|%{_libdir}|" %{buildroot}%{_bindir}/compiz-manager

# And a default config to override some defaults
mkdir -p %{buildroot}%{_sysconfdir}/xdg/compiz
cat >%{buildroot}%{_sysconfdir}/xdg/compiz/compiz-manager <<EOF
# We start the decorator via compiz' decoration plugin so set it to "no" here.
START_DECORATOR="no"
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/X11/xinit.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/%{rname}
%config(noreplace) %{_sysconfdir}/xdg/compiz/compiz-manager
%{_bindir}/%{rname}-start
%{_bindir}/compiz-manager
%dir %{_datadir}/%{rname}
%{_datadir}/%{rname}/%{imgname}.png



%changelog
* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-2mdv2011.0
+ Revision: 603849
- rebuild

* Wed Apr 07 2010 Frederic Crozat <fcrozat@mandriva.com> 2010.0-1mdv2010.1
+ Revision: 532604
- Ensure compositing-wm is not started with GNOME-Shell (GNOME3Preview) (Mdv bug #57573)
- Drop test on Xgl, no longer present in current distribution

* Wed Feb 03 2010 Thierry Vignaud <tv@mandriva.org> 2009.0-8mdv2010.1
+ Revision: 499979
- requires glxinfo instead of mesa-demos

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.0-7mdv2010.0
+ Revision: 423680
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2009.0-6mdv2010.0
+ Revision: 413266
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2009.0-5mdv2009.1
+ Revision: 350736
- rebuild

* Wed Nov 19 2008 Olivier Blin <oblin@mandriva.com> 2009.0-4mdv2009.1
+ Revision: 304647
- move kstylerc hack in compiz-decorator-kde

  + Frederic Crozat <fcrozat@mandriva.com>
    - Fix KDE4 to not break metisse startup

* Wed Sep 03 2008 Helio Chissini de Castro <helio@mandriva.com> 2009.0-3mdv2009.0
+ Revision: 279932
- Make kde3 use proper composite manager
- Make kde use proper composite manager

* Tue Aug 05 2008 Olivier Blin <oblin@mandriva.com> 2009.0-2mdv2009.0
+ Revision: 263906
- fix path to mesa libraries on i586

* Thu May 22 2008 Colin Guthrie <cguthrie@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 210118
- Switch the release to 2009.0
- Add support for starting under KDE4

* Tue Mar 04 2008 Colin Guthrie <cguthrie@mandriva.org> 2008.1-4mdv2008.1
+ Revision: 178348
- Fix paths in the script rather than overriding them in the config (will fix an XGL + x86_64 based error I missed before)

* Tue Mar 04 2008 Colin Guthrie <cguthrie@mandriva.org> 2008.1-3mdv2008.1
+ Revision: 178326
- Require xvinfo
- Put a prefix on log message to make them stand out in ~/.xsession-errors

* Sat Mar 01 2008 Colin Guthrie <cguthrie@mandriva.org> 2008.1-2mdv2008.1
+ Revision: 177013
- Add a (slightly modified) compiz-manager script which will be used to start
  compiz with suitible arguments and environment variables.

* Fri Feb 29 2008 Olivier Blin <oblin@mandriva.com> 2008.1-1mdv2008.1
+ Revision: 176923
- update cube image (from Helene)
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2007-15mdv2008.1
+ Revision: 123340
- kill re-definition of %%buildroot on Pixel's request

* Fri Oct 05 2007 Colin Guthrie <cguthrie@mandriva.org> 2007-15mdv2008.0
+ Revision: 95562
- Move the decorator start into xinit.d to help with gnome session restoration with vanilla compiz.
- Allow the starting of a decorator afterall even if it is not used on compiz fusion and does not play nice with gnome session saving.

* Wed Oct 03 2007 Colin Guthrie <cguthrie@mandriva.org> 2007-13mdv2008.0
+ Revision: 95026
- Do not start the decorator - compiz does this by itself now.

* Fri Sep 14 2007 Adam Williamson <awilliamson@mandriva.org> 2007-12mdv2008.0
+ Revision: 85775
- rebuild for 2008
- don't mention Beryl any more
- Fedora license policy


* Fri Mar 23 2007 Olivier Blin <oblin@mandriva.com> 2007-11mdv2007.1
+ Revision: 148463
- disable QT drop shadows at session start when compositing is enabled (can be disabled by touching ~/.mdv_no_auto_shadow)
- export COMPOSITING_WM_START variable
- allow per-user compositing configuration (based on work from Adam Pigg, #29001)

* Fri Dec 15 2006 Olivier Blin <oblin@mandriva.com> 2007-10mdv2007.1
+ Revision: 97390
- use SESSION variable instead of DESKTOP in xinit script (#25429)

* Thu Dec 14 2006 Olivier Blin <oblin@mandriva.com> 2007-9mdv2007.1
+ Revision: 97095
- update again comments in sysconfig file

* Thu Dec 14 2006 Olivier Blin <oblin@mandriva.com> 2007-8mdv2007.1
+ Revision: 96753
- rename COMPOSITING_SERVER_LATE_INIT as COMPOSITING_SERVER_SPAWNS_WINDOW (and add some doc)
- revert minor sysconfig comment

* Wed Dec 13 2006 Olivier Blin <oblin@mandriva.com> 2007-7mdv2007.1
+ Revision: 96575
- update sysconfig comments

* Wed Dec 13 2006 Olivier Blin <oblin@mandriva.com> 2007-6mdv2007.1
+ Revision: 96557
- use original X display if COMPOSITING_SERVER_LATE_INIT is "yes" (this is not for 3D desktops)
- do not run window decorator if not specified
- factorize xinit level and name in spec

* Wed Nov 15 2006 Olivier Blin <oblin@mandriva.com> 2007-5mdv2007.1
+ Revision: 84225
- bump release
- read window manager defaults if present

* Sat Nov 04 2006 Olivier Blin <oblin@mandriva.com> 2007-4mdv2007.1
+ Revision: 76586
- don't use default wm arguments

* Mon Oct 16 2006 Olivier Blin <oblin@mandriva.com> 2007-3mdv2007.1
+ Revision: 65402
- remove the noarch buildarch, some scripts are arch-dependent

* Sun Oct 15 2006 Olivier Blin <oblin@mandriva.com> 2007-2mdv2006.0
+ Revision: 65115
- default to gtk-window-decorator

* Sat Sep 30 2006 Colin Guthrie <cguthrie@mandriva.org> 2007-1mdv2006.0
+ Revision: 62774
- Fix typo in default config

  + Olivier Blin <oblin@mandriva.com>
    - move common compositing wm scripts/images in compositing-wm-common (configuration file is not backward compatible)
    - Created package structure for compositing-wm-common.

