#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-shinythemes
Version  : 1.2.0
Release  : 37
URL      : https://cran.r-project.org/src/contrib/shinythemes_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/shinythemes_1.2.0.tar.gz
Summary  : Themes for Shiny
Group    : Development/Tools
License  : GPL-3.0
Requires: R-shiny
BuildRequires : R-shiny
BuildRequires : buildreq-R

%description
shinythemes
===========
> NOTE: This package has been superseded by the [`{bslib}` package](https://rstudio.github.io/bslib/), which provides Bootswatch (and as well as custom) themes for both Bootstrap 3 and 4.

%prep
%setup -q -c -n shinythemes
cd %{_builddir}/shinythemes

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611676774

%install
export SOURCE_DATE_EPOCH=1611676774
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinythemes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinythemes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinythemes
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc shinythemes || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/shinythemes/DESCRIPTION
/usr/lib64/R/library/shinythemes/INDEX
/usr/lib64/R/library/shinythemes/LICENSE
/usr/lib64/R/library/shinythemes/Meta/Rd.rds
/usr/lib64/R/library/shinythemes/Meta/features.rds
/usr/lib64/R/library/shinythemes/Meta/hsearch.rds
/usr/lib64/R/library/shinythemes/Meta/links.rds
/usr/lib64/R/library/shinythemes/Meta/nsInfo.rds
/usr/lib64/R/library/shinythemes/Meta/package.rds
/usr/lib64/R/library/shinythemes/NAMESPACE
/usr/lib64/R/library/shinythemes/NEWS.md
/usr/lib64/R/library/shinythemes/R/shinythemes
/usr/lib64/R/library/shinythemes/R/shinythemes.rdb
/usr/lib64/R/library/shinythemes/R/shinythemes.rdx
/usr/lib64/R/library/shinythemes/help/AnIndex
/usr/lib64/R/library/shinythemes/help/aliases.rds
/usr/lib64/R/library/shinythemes/help/paths.rds
/usr/lib64/R/library/shinythemes/help/shinythemes.rdb
/usr/lib64/R/library/shinythemes/help/shinythemes.rdx
/usr/lib64/R/library/shinythemes/html/00Index.html
/usr/lib64/R/library/shinythemes/html/R.css
/usr/lib64/R/library/shinythemes/shinythemes/css/cerulean.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/cosmo.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/cyborg.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/darkly.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/flatly.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/journal.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/lumen.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/paper.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/readable.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/sandstone.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/simplex.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/slate.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/spacelab.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/superhero.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/united.min.css
/usr/lib64/R/library/shinythemes/shinythemes/css/yeti.min.css
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Lato_300.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Lato_400.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Lato_400italic.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Lato_700.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/News_Cycle_400.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/News_Cycle_700.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Open_Sans_300.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Open_Sans_300italic.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Open_Sans_400.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Open_Sans_400italic.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Open_Sans_700.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Open_Sans_700italic.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/README.md
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Raleway_400.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Raleway_700.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Roboto_300.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Roboto_400.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Roboto_500.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Roboto_700.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Source_Sans_Pro_300.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Source_Sans_Pro_400.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Source_Sans_Pro_400italic.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Source_Sans_Pro_700.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/Ubuntu_400.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/glyphicons-halflings-regular.eot
/usr/lib64/R/library/shinythemes/shinythemes/fonts/glyphicons-halflings-regular.svg
/usr/lib64/R/library/shinythemes/shinythemes/fonts/glyphicons-halflings-regular.ttf
/usr/lib64/R/library/shinythemes/shinythemes/fonts/glyphicons-halflings-regular.woff
/usr/lib64/R/library/shinythemes/shinythemes/fonts/glyphicons-halflings-regular.woff2
