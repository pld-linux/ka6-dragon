#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		dragon
Summary:	Dragon Player
Name:		ka6-%{kaname}
Version:	25.08.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Multimedia
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	6d978bc54341159fae6a5019eee337af
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
Requires(post,postun):	desktop-file-utils
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
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

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dragon
%dir %{_libdir}/qt6/qml/org/kde/dragon
%{_libdir}/qt6/qml/org/kde/dragon/AboutPage.qml
%{_libdir}/qt6/qml/org/kde/dragon/ControlsBar.qml
%{_libdir}/qt6/qml/org/kde/dragon/IconToolButton.qml
%{_libdir}/qt6/qml/org/kde/dragon/Main.qml
%{_libdir}/qt6/qml/org/kde/dragon/OverlayPopup.qml
%{_libdir}/qt6/qml/org/kde/dragon/PlayerPage.qml
%{_libdir}/qt6/qml/org/kde/dragon/VolumeButton.qml
%{_libdir}/qt6/qml/org/kde/dragon/WelcomeView.qml
%{_libdir}/qt6/qml/org/kde/dragon/dragonmodule.qmltypes
%{_libdir}/qt6/qml/org/kde/dragon/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/dragon/libdragonmodule.so
%{_libdir}/qt6/qml/org/kde/dragon/qmldir
%{_desktopdir}/org.kde.dragonplayer.desktop
%{_iconsdir}/hicolor/*x*/apps/dragonplayer.png
%{_iconsdir}/hicolor/scalable/apps/dragonplayer.svgz
%{_datadir}/metainfo/org.kde.dragonplayer.appdata.xml
