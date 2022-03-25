#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	objgraph
Summary:	Draws Python object reference graphs with graphviz
Summary(pl.UTF-8):	Rysowanie referencji między obiektami przy uzyciu graphviza
Name:		python-objgraph
Version:	3.4.1
Release:	6
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/objgraph/
Source0:	https://files.pythonhosted.org/packages/source/o/objgraph/%{module}-%{version}.tar.gz
# Source0-md5:	4f416da377b3c7799799c357c6f0c2ed
Patch0:		%{name}-mock.patch
URL:		http://mg.pov.lt/objgraph/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-graphviz
BuildRequires:	python-mock
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-graphviz
%endif
%endif
%if %{with tests}
BuildRequires:	graphviz
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional dependency
%define		_noautoreq_pyegg	graphviz
%define		_noautoreq_py3egg	graphviz

%description
Module that lets you visually explore Python object graphs and debug
memory leaks.

%description -l pl.UTF-8
Moduł do wizualizacji grafów pythonowych obiektów i diagnozowania
wycieków pamięci.

%package -n python3-%{module}
Summary:	Draws Python object reference graphs with graphviz
Summary(pl.UTF-8):	Rysowanie referencji między obiektami przy uzyciu graphviza
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
Module that lets you visually explore Python object graphs and debug
memory leaks.

%description -n python3-%{module} -l pl.UTF-8
Moduł do wizualizacji grafów pythonowych obiektów i diagnozowania
wycieków pamięci.

%package apidocs
Summary:	API documentation for Python objgraph module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona objgraph
Group:		Documentation

%description apidocs
API documentation for Python objgraph module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona objgraph.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} tests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} tests.py
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/%{module}.py*
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.*
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_static,*.html,*.js}
%endif
