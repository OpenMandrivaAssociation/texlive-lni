Name:		texlive-lni
Version:	71883
Release:	1
Summary:	Official class for the "Lecture Notes in Informatics"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lni
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lni.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lni.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lni.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the official version of the class "lni" for submissions
to the Lecture Notes in Informatics published by the
Gesellschaft fur Informatik. To use it, download the file
lni-author-template.tex and edit it in your favorite LaTeX
editor.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/lni
%{_texmfdistdir}/tex/latex/lni
%{_texmfdistdir}/bibtex/bst/lni
%doc %{_texmfdistdir}/doc/latex/lni

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
