%global packname doMC
%global rlibdir %{_libdir}/R/library

Name: R-%{packname}
Version: 1.3.0
Release: 1
Summary: Foreach parallel adaptor for the multicore package
Group: Sciences/Mathematics
License: GPLv2
URL: https://cran.r-project.org/web/packages/%{packname}/index.html
Source0: http://cran.r-project.org/src/contrib/%{packname}_1.3.0.tar.gz
BuildArch: noarch
Requires: R-core R-foreach R-iterators R-utils
BuildRequires: R-devel R-foreach R-iterators R-utils texlive-collection-latex

%description
Provides a parallel backend for the dopar function using
the multicore functionality of the parallel package.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/unitTests
