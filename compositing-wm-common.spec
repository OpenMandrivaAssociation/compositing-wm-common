%define rname compositing-wm
%define imgname mandriva-top 
%define name %{rname}-common
%define version 2009.0
%define release %mkrel 1

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
Source5: compiz-manager
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-root
# For glxinfo
Requires: mesa-demos
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
install -D -m 0755 %SOURCE4 %{buildroot}%{_sysconfdir}/X11/xinit.d/41kstylerc
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

