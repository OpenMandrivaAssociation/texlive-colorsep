# revision 13293
# category Package
# catalog-ctan /graphics/colorsep/colorsep.pro
# catalog-date 2009-09-15 14:15:21 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-colorsep
Version:	20090915
Release:	1
Summary:	Color separation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/colorsep/colorsep.pro
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorsep.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips %{buildroot}%{_texmfdistdir}
