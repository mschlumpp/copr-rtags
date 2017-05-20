Name:		rtags
Version:	2.9
Release:	3%{?dist}
Summary:	Generic library for just-in-time compiler functionality.

#Group:		
License:	GPLv3+
URL:		https://github.com/Andersbakken/rtags
Source0:	https://github.com/Andersbakken/rtags/archive/v%{version}.zip#/rtags-%{version}.zip
%global shortcommit1 2fb0698c1a44dd287dfaebbfa964b5d21bfe8300
Source1:	https://github.com/Andersbakken/rct/archive/2fb0698c1a44dd287dfaebbfa964b5d21bfe8300.zip#/rct-%{shortcommit1}.zip

BuildRequires:	clang-devel
BuildRequires:	llvm-devel
BuildRequires:	cmake
BuildRequires:	bash-completion
Requires:	clang
Requires:	llvm

%description
A C/C++ client/server indexer for C/C++/Objc[++] with integration for Emacs based on clang.

%prep
%autosetup
%autosetup -T -D -n %{name}-%{version} -a 1
rmdir src/rct
mv -f rct-%{shortcommit1} src/rct

%build
%cmake -DRTAGS_NO_ELISP_FILES=1 -FORCE_BASH_COMPLETION_INSTALLATION=ON .
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/rdm
%{_bindir}/rc
%{_bindir}/rp
%{_bindir}/gcc-rtags-wrapper.sh
%{_datadir}/bash-completion/completions/rc
%{_datadir}/bash-completion/completions/rdm
%{_datadir}/bash-completion/completions/rtags
%{_datadir}/man/man7/rc.7.gz
%{_datadir}/man/man7/rdm.7.gz
%doc



%changelog
* Sat May 20 2017 Marco Schlumpp <marco.schlumpp@gmail.com> 2.9-3
- Remove emacs files.

* Sat May 20 2017 Marco Schlumpp <marco.schlumpp@gmail.com>
- Remove emacs files.

* Sat May 20 2017 Marco Schlumpp <marco.schlumpp@gmail.com> 2.9-2
- Fixed spec file.


