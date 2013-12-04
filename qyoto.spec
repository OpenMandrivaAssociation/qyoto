Name:		qyoto
Summary:	C# Mono Qt 4 bindings
Version:	4.11.4
Release:	1
Epoch:		1
Group:		Development/KDE and Qt
License:	GPL
URL:		https://projects.kde.org/projects/kde/kdebindings/csharp/qyoto
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel >= 2:%{version}
BuildRequires:	smokegen-devel >= 1:%{version}
BuildRequires:	smokeqt-devel >= 1:%{version}
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	kde4-macros
BuildRequires:	cmake
BuildRequires:	qscintilla-qt4-devel
Provides:	mono-qt4 = %{EVRD}

%description
.NET/Mono bindings for the Qt libraries.

%files
%{_prefix}/lib/mono/qyoto/qt-dotnet.dll
%{_prefix}/lib/mono/qyoto/qscintilla.dll
%{_prefix}/lib/mono/qyoto/qtscript.dll
%{_prefix}/lib/mono/qyoto/qtuitools.dll
%{_prefix}/lib/mono/qyoto/qtwebkit.dll
%{_prefix}/lib/mono/qyoto/qttest.dll
%{_prefix}/lib/mono/qyoto/phonon.dll
%{_prefix}/lib/mono/gac/qttest
%{_prefix}/lib/mono/gac/qt-dotnet
%{_prefix}/lib/mono/gac/qscintilla
%{_prefix}/lib/mono/gac/qtscript
%{_prefix}/lib/mono/gac/qtwebkit
%{_prefix}/lib/mono/gac/qtuitools
%{_prefix}/lib/mono/gac/phonon
%{_kde_libdir}/libqscintilla-sharp.so
%{_kde_libdir}/libqtscript-sharp.so
%{_kde_libdir}/libqtuitools-sharp.so
%{_kde_libdir}/libqtwebkit-sharp.so
%{_kde_libdir}/libqttest-sharp.so
%{_kde_libdir}/libphonon-sharp.so

#------------------------------------------------------------

%define libqyoto_major 2
%define libqyoto %mklibname qyoto %{libqyoto_major}

%package -n %{libqyoto}
Summary:	Qt generic bindings library
Group:		Development/KDE and Qt

%description -n %{libqyoto}
Qt generic bindings library.

%files -n %{libqyoto}
%{_kde_libdir}/libqyoto.so.%{libqyoto_major}*

#------------------------------------------------------------

%package -n qyoto-devel
Summary:	Header files for qyoto
Group:		Development/KDE and Qt
Provides:	mono-qt4-devel = %{EVRD}
Requires:	qyoto = %{EVRD}
Requires:	%{libqyoto} = %{EVRD}
Conflicts:	qyoto < 1:4.4.95

%description -n qyoto-devel
qyoto devel files.

%files -n qyoto-devel
%{_kde_bindir}/csrcc
%{_kde_bindir}/uics
%{_kde_includedir}/qyoto
%{_kde_libdir}/libqyoto.so
%{_kde_libdir}/pkgconfig/qyoto.pc
%{_kde_libdir}/pkgconfig/qtscript-sharp.pc
%{_kde_libdir}/pkgconfig/qttest-sharp.pc
%{_kde_libdir}/pkgconfig/qtuitools-sharp.pc
%{_kde_libdir}/pkgconfig/qtwebkit-sharp.pc
%{_kde_datadir}/qyoto/cmake/*
%{_kde_datadir}/qyoto/key.snk

#------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Mon Jul 09 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.1mib2010.2
+ Revision: 758088
- Backport to 2010.2 for MIB users
- Update to 4.8.0
- MIB (Mandriva International Backports)

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758088
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 744567
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 744325
- Remove merged patch
- New upstream tarball $NEW_VERSION
- Import qyoto
- Create folder

