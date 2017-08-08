Name:           fuse3
Version:        3.1.1
Release:        7%{?dist}
Summary:        File System in Userspace (FUSE) utilities
 
Group:          System Environment/Base
License:        GPL+
URL:            http://github.com/libfuse/libfuse
Source0:        https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz
#Source1:    %{name}.conf
 
#Patch1:        fuse-0001-More-parentheses.patch
#Patch2:        fuse-aarch64.patch
Requires:       which
Conflicts:      filesystem < 3
BuildRequires:  libselinux-devel
 
Requires(preun): chkconfig
 
%description
With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains the FUSE userspace tools to
mount a FUSE filesystem.
 
%package libs
Summary:        File System in Userspace (FUSE) libraries
Group:          System Environment/Libraries
License:        LGPLv2+
Conflicts:      filesystem < 3
 
%description libs
Devel With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains the FUSE libraries.
 
 
%package devel
Summary:        File System in Userspace (FUSE) devel files
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig
License:        LGPLv2+
Conflicts:      filesystem < 3
 
%description devel
With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains development files (headers,
pgk-config) to develop FUSE based applications/filesystems.
 
 
%prep
%setup -q -n fuse-%{version}
#disable device creation during build/install
#sed -i 's|mknod|echo Disabled: mknod |g' util/Makefile.in
#%patch1 -p1 -b .add_parentheses
#%patch2 -p1 -b .aarch64
 
%build
export MOUNT_FUSE_PATH="%{_sbindir}"
CFLAGS="%{optflags}" %configure
make %{?_smp_mflags}
 
%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
# change from 4755 to 0755 to allow stripping -- fixed later in files
chmod 0755 %{buildroot}/%{_bindir}/fusermount3
 
# No need to create init-script
rm -f %{buildroot}%{_sysconfdir}/init.d/fuse
 
# Install config-file
#install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}
 
# Delete pointless udev rules, which do not belong in /etc (brc#748204)
# /usr/lib64/udev/rules.d/99-fuse3.rules
rm -f %{buildroot}%{_libdir}/udev/rules.d/99-fuse3.rules
 
%post libs -p /sbin/ldconfig
 
%postun libs -p /sbin/ldconfig
 
%files
%doc AUTHORS ChangeLog.rst COPYING README.md doc/README.NFS
%{_sbindir}/mount.fuse3
%attr(4755,root,root) %{_bindir}/fusermount3

 
%files libs
%doc COPYING.LIB
%{_libdir}/libfuse3.so
%{_libdir}/libfuse3.so.*
%{_sysconfdir}/init.d/fuse3
 
%files devel
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/fuse3
%config(noreplace) %{_mandir}/man1/*
%config(noreplace) %{_mandir}/man8/*
