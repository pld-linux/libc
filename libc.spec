Summary: The compatibility libraries needed by old libc.so.5 applications.
Name: libc
Version: 5.3.12
Release: 31
Exclusivearch: i386
Exclusiveos: Linux
Copyright: distributable
Group: System Environment/Libraries
Source0: libc-5.3.12-bins.tar.gz
Source1: libc-5.3.12-18.4.src.rpm
Prereq: /sbin/ldconfig grep fileutils 
Requires: /lib/ld-linux.so.1
Autoreqprov: 0
Provides: libc.so.5 libstdc++.so.27 libg++.so.27 libm.so.5
Buildroot: /var/tmp/libc5-root/

%description
Older Linux systems (including all Red Hat Linux releases between 2.0
and 4.2, inclusive) were based on libc version 5. The libc package
includes the libc5 libraries and other libraries based on libc5.  With
these libraries installed, old applications which need them will be able
to run on your glibc (libc version 6) based system.

The libc package should be installed so that you can run older applications
which need libc version 5.

%prep
%setup -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/i486-linux-libc5/lib
for n in *; do
    install -m 755 $n $RPM_BUILD_ROOT/usr/i486-linux-libc5/lib
done

%post
if ! grep '^/usr/i486-linux-libc5/lib$' /etc/ld.so.conf > /dev/null 2>/dev/null; then
    echo "/usr/i486-linux-libc5/lib" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun
if [ "$1" = '0' ]; then
    grep -v '^/usr/i486-linux-libc5/lib$' /etc/ld.so.conf > /etc/ld.so.conf.new 2>/dev/null
    mv /etc/ld.so.conf.new /etc/ld.so.conf
fi
/sbin/ldconfig

%files
/usr/i486-linux-libc5/lib

%clean
rm -rf $RPM_BUILD_ROOT
