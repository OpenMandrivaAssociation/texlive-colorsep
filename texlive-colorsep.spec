%global tl_name colorsep
%global tl_revision 13293

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Color separation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/colorsep
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorsep.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for colour separation when using dvips.

