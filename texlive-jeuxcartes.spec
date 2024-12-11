Name:		texlive-jeuxcartes
Version:	73069
Release:	1
Summary:	Macros to insert playing cards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jeuxcartes
License:	lppl1.3c lgpl2.1 pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jeuxcartes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jeuxcartes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros to insert playing cards, single,
or hand, or random-hand, Poker or French Tarot or Uno, from png
files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jeuxcartes
%doc %{_texmfdistdir}/doc/latex/jeuxcartes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
