Name:		texlive-colordoc
Version:	20100606
Release:	1
Summary:	Coloured syntax highlights in documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colordoc
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colordoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colordoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colordoc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package is used in documentation files (that use the doc
package); with it the code listings will highlight (for
example) pairs of curly braces with matching colors. Other
delimiters like \if ... \fi, are highlighted, as are the names
of new commands. All this makes code a little more readable,
and helps during process of writing. Three options are
provided, including a non-color option designed for printing
(which numbers delimiters and underlines new commands).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/colordoc/colordoc.sty
%doc %{_texmfdistdir}/doc/latex/colordoc/README
%doc %{_texmfdistdir}/doc/latex/colordoc/colordoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/colordoc/colordoc.dtx
%doc %{_texmfdistdir}/source/latex/colordoc/colordoc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
