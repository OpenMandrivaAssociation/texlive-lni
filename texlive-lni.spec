%global tl_name lni
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Official class for the Lecture Notes in Informatics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lni
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lni.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lni.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lni.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the official version of the class "lni" for submissions to the
Lecture Notes in Informatics published by the Gesellschaft fur
Informatik. To use it, download the file lni-author-template.tex and
edit it in your favorite LaTeX editor.

