#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.02.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		dragon
Summary:	Dragon Player
Name:		ka6-%{kaname}
Version:	24.02.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Multimedia
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2ecb7104b95c7044c9156c3e687f3422
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	kf6-solid-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	phonon-qt6-devel >= 4.6.60
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dragon Player is a very simple Phonon-based media player. It was
originally developed by Max Howell and called Codeine. I ported it to
KDE 4.0 and on Max's suggestion renamed it to Video Player (probably,
I might still rename it.)

%description -l pl.UTF-8
Dragon to bardzo prosty odtwarzacz multimediów bazujący na Phononie.
Pierwsza wersja została napisana przez Maxa Howella i była nazwana
Codeine. Potem została przeportowana do KDE 4.0, a za sugestią Maxa
została przemianowana na Video Player (prawdopobnie jeszcze kiedyś
zmienię jej nazwę.)

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/dragonplayerrc
%attr(755,root,root) %{_bindir}/dragon
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/dragonpart.so
%{_desktopdir}/org.kde.dragonplayer.desktop
%{_iconsdir}/hicolor/*x*/apps/dragonplayer.png
%{_iconsdir}/hicolor/scalable/apps/dragonplayer.svgz
%{_iconsdir}/oxygen/*x*/actions/player-volume-muted.png
%{_iconsdir}/oxygen/scalable/actions/player-volume-muted.svgz
%{_datadir}/kio/servicemenus/dragonplayer_play_dvd.desktop
%{_mandir}/man1/dragon.1*
%{_mandir}/ca/man1/dragon.1*
%{_mandir}/de/man1/dragon.1*
%{_mandir}/es/man1/dragon.1*
%{_mandir}/et/man1/dragon.1*
%{_mandir}/fr/man1/dragon.1*
%{_mandir}/it/man1/dragon.1*
%{_mandir}/nl/man1/dragon.1*
%{_mandir}/pt/man1/dragon.1*
%{_mandir}/pt_BR/man1/dragon.1*
%{_mandir}/sr/man1/dragon.1*
%{_mandir}/sr@latin/man1/dragon.1*
%{_mandir}/sv/man1/dragon.1*
%{_mandir}/tr/man1/dragon.1*
%{_mandir}/uk/man1/dragon.1*
%{_datadir}/metainfo/org.kde.dragonplayer.appdata.xml
%{_datadir}/solid/actions/dragonplayer-openaudiocd.desktop
%{_datadir}/solid/actions/dragonplayer-opendvd.desktop
