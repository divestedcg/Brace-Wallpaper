Name: brace-background
Version: 20210128
Release: 4
Summary: A different default background.
License: Unsplash
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%define _binary_payload w3T.xzdio
%define _sourcedir %(echo $PWD)
%define _rpmdir %(echo $PWD/build)

%description
- GNOME/Cinnamon/MATE: change default background

%post
if [ -f /usr/bin/dconf ]; then dconf update; fi;

%postun
if [ -f /usr/bin/dconf ]; then dconf update; fi;

%install
install -Dm644 %{_sourcedir}/00-brace-background %{buildroot}/etc/dconf/db/local.d/00-brace-background
install -Dm644 %{_sourcedir}/brace-backgrounds.xml %{buildroot}/usr/share/gnome-background-properties/brace-backgrounds.xml
install -Dm644 %{_sourcedir}/brace-backgrounds.xml %{buildroot}/usr/share/mate-background-properties/brace-backgrounds.xml
install -Dm644 %{_sourcedir}/pawel-czerwinski-1538544-unsplash-1080p.jpg %{buildroot}/usr/share/backgrounds/brace/brace.jpg
install -Dm644 %{_sourcedir}/pawel-czerwinski-1538544-unsplash-2160p.jpg %{buildroot}/usr/share/backgrounds/brace/brace-2160p.jpg

%files
/etc/dconf/db/local.d/00-brace-background
/usr/share/gnome-background-properties/brace-backgrounds.xml
/usr/share/mate-background-properties/brace-backgrounds.xml
/usr/share/backgrounds/brace/brace.jpg
/usr/share/backgrounds/brace/brace-2160p.jpg
