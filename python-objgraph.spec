#
# Conditional build:
%bcond_with	tests	# do perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	objgraph
Summary:	Draws Python object reference graphs with graphviz
Summary(pl.UTF-8):	Rysuje referencje pomiedzy obiektamiy przy uzyciu graphviz
Name:		python-objgraph
Version:	3.4.0
Release:	3
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	cbe527c7dc095a41458d86cab2059591
URL:		http://mg.pov.lt/objgraph/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
%if %{with tests}
BuildRequires:	graphviz
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional dependency
%define _noautoreq pythonegg.graphviz python3egg.graphviz

%description
Module that lets you visually explore Python object graphs and debug
memory leaks.

%description -l pl.UTF-8
Moduł do wizualizacji grafów pythonowych obiektów i debugowania
wycieków pamięci.

%package -n python3-%{module}
Summary:	Draws Python object reference graphs with graphviz
Summary(pl.UTF-8):	Rysuje referencje pomiedzy obiektamiy przy uzyciu graphviz
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-%{module}
Module that lets you visually explore Python object graphs and debug
memory leaks.

%description -n python3-%{module} -l pl.UTF-8
Moduł do wizualizacji grafów pythonowych obiektów i debugowania
wycieków pamięci.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst docs
%{py_sitescriptdir}/%{module}.py*
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst docs
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.*
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

%clean
rm -rf $RPM_BUILD_ROOT
