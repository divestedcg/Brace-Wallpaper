Name: brace-background
Version: 20201206
Release: 1
Summary: A different default background.
License: Unsplash
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%define _binary_payload w3T.xzdio

%description
- GNOME/Cinnamon/MATE: change default background

%post
if [ -f /usr/bin/dconf ]; then dconf update; fi;

%postun
if [ -f /usr/bin/dconf ]; then dconf update; fi;

%install
install -Dm644 00-brace-background %{buildroot}/etc/dconf/db/local.d/00-brace-background
install -Dm644 brace-backgrounds.xml %{buildroot}/usr/share/gnome-background-properties/brace-backgrounds.xml
install -Dm644 brace-backgrounds.xml %{buildroot}/usr/share/mate-background-properties/brace-backgrounds.xml
install -Dm644 pawel-czerwinski-1538544-unsplash.jpg %{buildroot}/usr/share/backgrounds/brace/brace.jpg

%files
/etc/dconf/db/local.d/00-brace-background
/usr/share/gnome-background-properties/brace-backgrounds.xml
/usr/share/backgrounds/brace/brace.jpg
