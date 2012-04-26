Name:          qyoto
Summary:       C# Mono Qt 4 bindings
Version: 4.8.2
Release: 3
Epoch:         1
Group:         Development/KDE and Qt
License:       GPL
URL:           https://projects.kde.org/projects/kde/kdebindings/csharp/qyoto
Source:        ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%version
BuildRequires: smokegen-devel >= 1:%version
BuildRequires: smokeqt-devel >= 1:%version
BuildRequires: pkgconfig(mono)
BuildRequires: pkgconfig(phonon)
BuildRequires: pkgconfig(qimageblitz)
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: qscintilla-qt4-devel

Provides: mono-qt4 = %epoch:%version-%release

%description
.NET/Mono bindings for the Qt libraries.

%files
%_prefix/lib/mono/qyoto/qt-dotnet.dll
%_prefix/lib/mono/qyoto/qscintilla.dll
%_prefix/lib/mono/qyoto/qtscript.dll
%_prefix/lib/mono/qyoto/qtuitools.dll
%_prefix/lib/mono/qyoto/qtwebkit.dll
%_prefix/lib/mono/qyoto/qttest.dll
%_prefix/lib/mono/qyoto/phonon.dll
%_prefix/lib/mono/gac/qttest
%_prefix/lib/mono/gac/qt-dotnet
%_prefix/lib/mono/gac/qscintilla
%_prefix/lib/mono/gac/qtscript
%_prefix/lib/mono/gac/qtwebkit
%_prefix/lib/mono/gac/qtuitools
%_prefix/lib/mono/gac/phonon
%_kde_libdir/libqscintilla-sharp.so
%_kde_libdir/libqtscript-sharp.so
%_kde_libdir/libqtuitools-sharp.so
%_kde_libdir/libqtwebkit-sharp.so
%_kde_libdir/libqttest-sharp.so
%_kde_libdir/libphonon-sharp.so

#------------------------------------------------------------

%define libqyoto_major 2
%define libqyoto %mklibname qyoto %{libqyoto_major}

%package -n %{libqyoto}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{libqyoto}
Qt generic bindings library.

%files -n %{libqyoto}
%_kde_libdir/libqyoto.so.%{libqyoto_major}*

#------------------------------------------------------------

%package -n qyoto-devel
Summary: Header files for qyoto
Group: Development/KDE and Qt
Provides: mono-qt4-devel = %epoch:%version-%release
Requires: qyoto = %epoch:%version-%release
Requires: %{libqyoto} = %epoch:%version-%release
Conflicts: qyoto < 1:4.4.95

%description -n qyoto-devel
qyoto devel files.

%files -n qyoto-devel
%_kde_bindir/csrcc
%_kde_bindir/uics
%_kde_includedir/qyoto
%_kde_libdir/libqyoto.so
%_kde_libdir/pkgconfig/qyoto.pc
%_kde_libdir/pkgconfig/qtscript-sharp.pc
%_kde_libdir/pkgconfig/qttest-sharp.pc
%_kde_libdir/pkgconfig/qtuitools-sharp.pc
%_kde_libdir/pkgconfig/qtwebkit-sharp.pc
%_kde_datadir/qyoto/cmake/*
%_kde_datadir/qyoto/key.snk

#------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

