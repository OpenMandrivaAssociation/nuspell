%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Free and open source C++ spell checking library 
Name:		nuspell
Version:	3.0.0
Release:	1
License:	GPLv2+
Group:		System/Internationalization
Url:		http://nuspell.github.io/
Source0:	https://github.com/nuspell/nuspell/archive/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(icu-uc)

%description
Nuspell is a free and open source spell checker library and command-line program
designed for languages with rich morphology and complex word compounding.
Nuspell is a pure C++ re-implementation of Hunspell.
Main features of Nuspell spell checker:

* Full unicode support backed by ICU
* Backward compatibility with Hunspell dictionary file format
* Twofold affix stripping (for agglutinative languages, like Azeri, Basque,
    Estonian, Finnish, Hungarian, Turkish, etc.)
* Support complex compounds (for example, Hungarian, German and Dutch)
* Support language specific features (for example, special casing of Azeri and
    Turkish dotted i, or German sharp s)
* Handle conditional affixes, circumfixes, fogemorphemes, forbidden words,
    pseudoroots and homonyms.
* Free software. Licensed under GNU LGPL v3 or later.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
Main library for %{name}.

%package -n %{develname}
Summary:	Development and header files for %{name}
Group:		Development/C++
Requires:	%{libname} >= %{EVRD}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_TESTING=OFF \
	-G Ninja

%ninja_build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
