#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	SSH public key parser
Summary(pl.UTF-8):	Parser kluczy publicznych SSH
Name:		python-sshpubkeys
# keep 3.1.x here for python2 support
Version:	3.1.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sshpubkeys/
Source0:	https://files.pythonhosted.org/packages/source/s/sshpubkeys/sshpubkeys-%{version}.tar.gz
# Source0-md5:	4cbb967b208b7f5752501a570a76a255
URL:		https://pypi.org/project/sshpubkeys/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-cryptography >= 2.1.4
BuildRequires:	python-ecdsa >= 0.13
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography >= 2.1.4
BuildRequires:	python3-ecdsa >= 0.13
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Native implementation for validating OpenSSH public keys.

Currently ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST
curves are supported.

%description -l pl.UTF-8
Natywna implementacja do sprawdzania poprawności kluczy publicznych
OpenSSH.

Obecnie obsługiwane są ssh-rsa, ssh-dss (DSA), ssh-ed25519 oraz klucze
ecdsa z krzywymi NIST.

%package -n python3-sshpubkeys
Summary:	SSH public key parser
Summary(pl.UTF-8):	Parser kluczy publicznych SSH
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sshpubkeys
Native implementation for validating OpenSSH public keys.

Currently ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST
curves are supported.

%description -n python3-sshpubkeys -l pl.UTF-8
Natywna implementacja do sprawdzania poprawności kluczy publicznych
OpenSSH.

Obecnie obsługiwane są ssh-rsa, ssh-dss (DSA), ssh-ed25519 oraz klucze
ecdsa z krzywymi NIST.

%prep
%setup -q -n sshpubkeys-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc README.rst
%{py_sitescriptdir}/sshpubkeys
%{py_sitescriptdir}/sshpubkeys-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sshpubkeys
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/sshpubkeys
%{py3_sitescriptdir}/sshpubkeys-%{version}-py*.egg-info
%endif
