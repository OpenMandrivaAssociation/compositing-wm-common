%define rname compositing-wm
%define imgname mandriva-top 
%define name %{rname}-common
%define version 2007
%define release %mkrel 14

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
Source4: kstylerc.xinit
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-root
Requires: mesa-demos

%description
This package contains tools for compositing window managers, such as
Compiz. This includes X session scripts, configuration files and
images.

%prep
%setup -q -c -T

%install
rm -rf %{buildroot}
install -D -m 0755 %SOURCE0 %{buildroot}%{_sysconfdir}/X11/xinit.d/40%{rname}
install -D -m 0755 %SOURCE4 %{buildroot}%{_sysconfdir}/X11/xinit.d/41kstylerc
install -D -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/sysconfig/%{rname}
install -D -m 0755 %SOURCE2 %{buildroot}%{_bindir}/%{rname}-start
install -D -m 0644 %SOURCE3 %{buildroot}%{_datadir}/%{rname}/%{imgname}.png
perl -pi -e "s!__LIBDIR__!%{_libdir}!" %{buildroot}%{_bindir}/%{rname}-start

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/X11/xinit.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/%{rname}
%{_bindir}/%{rname}-start
%dir %{_datadir}/%{rname}
%{_datadir}/%{rname}/%{imgname}.png

