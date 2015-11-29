#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	objgraph
Summary:	Draws Python object reference graphs with graphviz
Summary(pl.UTF-8):	Rysuje referencje pomiedzy obiektamiy przy uzyciu graphviz
Name:		python-objgraph
Version:	1.7.1
Release:	2
License:	MIT
Group:		Development/Languages/Python
# http://pypi.python.org/packages/source/o/objgraph/objgraph-1.7.1.tar.gz#md5=f6c501b68239e3063b05ca01041652d0
Source0:	http://pypi.python.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	f6c501b68239e3063b05ca01041652d0
URL:		http://mg.pov.lt/objgraph/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# remove BR: python-devel for 'noarch' packages.
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
#Requires:		python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module that lets you visually explore Python object graphs.


%description -l pl.UTF-8
Moduł do wizualizacji grafów pythonowych obiektów.

%prep
%setup -q -n %{module}-%{version}

# fix #!%{_bindir}/env python -> #!%{__python}:
# %{__sed} -i -e '1s,^#!.*python,#!%{__python},' %{name}.py

%build
# CC/CFLAGS is only for arch packages - remove on noarch packages
# CC="%{__cc}" \
# %py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

# install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
# cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
# %{py_sitedir}/*.py[co]
%{py_sitescriptdir}/*.py[co]

# %attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
# %{_examplesdir}/%{name}-%{version}
