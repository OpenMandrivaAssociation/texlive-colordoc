%global tl_name colordoc
%global tl_revision 18270

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Coloured syntax highlights in documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/colordoc
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colordoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colordoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colordoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is used in documentation files (that use the doc package);
with it the code listings will highlight (for example) pairs of curly
braces with matching colors. Other delimiters like \if ... \fi, are
highlighted, as are the names of new commands. All this makes code a
little more readable, and helps during process of writing. Three options
are provided, including a non-color option designed for printing (which
numbers delimiters and underlines new commands).

