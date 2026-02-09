Name:		python-poetry-core
Version:	2.3.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/poetry-core/poetry_core-%{version}.tar.gz
Summary:	Poetry PEP 517 Build Backend
URL:		https://pypi.org/project/poetry-core/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
Poetry PEP 517 Build Backend

%files
%{py_sitedir}/poetry
%{py_sitedir}/poetry_core-*.dist-info
