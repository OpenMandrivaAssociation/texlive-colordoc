# revision 18270
# category Package
# catalog-ctan /macros/latex/contrib/colordoc
# catalog-date 2010-06-06 13:50:32 +0200
# catalog-license lppl1
# catalog-version undef
Name:		texlive-colordoc
Version:	20190228
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is used in documentation files (that use the doc
package); with it the code listings will highlight (for
example) pairs of curly braces with matching colors. Other
delimiters like \if ... \fi, are highlighted, as are the names
of new commands. All this makes code a little more readable,
and helps during process of writing. Three options are
provided, including a non-color option designed for printing
(which numbers delimiters and underlines new commands).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100606-2
+ Revision: 750371
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100606-1
+ Revision: 718096
- texlive-colordoc
- texlive-colordoc
- texlive-colordoc
- texlive-colordoc
- texlive-colordoc

