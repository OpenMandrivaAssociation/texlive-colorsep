Name:		texlive-colorsep
Version:	13293
Release:	2
Summary:	Color separation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/colorsep/colorsep.pro
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorsep.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Support for colour separation when using dvips.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/colorsep/colorsep.pro

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips %{buildroot}%{_texmfdistdir}
