# https://github.com/jmank88/nuts
%global goipath         github.com/jmank88/nuts
%global commit          8b28145dffc87104e66d074f62ea8080edfad7c8

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        A collections of BoltDB utilities
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml



%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/boltdb/bolt)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q


%install
%goinstall glide.lock glide.yaml

%check
# constant 2147483648 overflows int
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git8b28145
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.2.20180315git8b28145
- Upload glide files

* Thu Mar 15 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git8b28145
- First package for Fedora
  resolves: #1556923
