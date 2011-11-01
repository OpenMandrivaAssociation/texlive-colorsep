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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Support for colour separation when using dvips.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
