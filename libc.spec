Summary:	The compatibility libraries needed by old libc.so.5 applications.
Summary(de):	Kompabilitäts-Libraries für alte libc.so.5-Anwendungen
Summary(fr):	Librairies de compatibilité pour les vieilles appl. libc.so.5
Summary(pl):	Biblioteki umo¿liwiaj±ce uruchomienie aplikacji libc.so.5
Summary(tr):	Eski libc.so.5 uygulamalarý ile uyumlululuðu saðlayan kitaplýklar
Name:		libc
Version:	5.4.46
Release:	2
Exclusivearch:	%{ix86}
Exclusiveos:	Linux
Copyright:	distributable
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
#######		From Slackware libc.so.5 & libm.so.5
#######		Other libraries from RH-5.2 updates
Source0:	libc-5.4.46.tar.bz2
Prereq:		/sbin/ldconfig grep fileutils
Requires:	/lib/ld-linux.so.1
Requires:	ld.so >= 1.9.9
Provides:	libc.so.5
Provides:	libm.so.5
Provides:	libstdc++.so.27
Provides:	libg++.so.27
Autoreqprov:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Older Linux systems (including all Red Hat Linux releases between 2.0
and 4.2, inclusive) were based on libc version 5. The libc package
includes the libc5 libraries and other libraries based on libc5. With
these libraries installed, old applications which need them will be
able to run on your glibc (libc version 6) based system. The libc
package should be installed so that you can run older applications
which need libc version 5.

%description -l de
Ältere Linux-Systeme (einschließlich aller Red-Hat-Linux-Releases
zwischen 2.0 und 4.2 inkl.) basierten auf libc5. Dieses Paket schließt
diese Libraries und andere auf libc 5 basierende mit ein, so daß
ältere Applikationen auf Systemen mit glibc (libc6) gefahren werden
können.

%description -l fr
Les anciens systèmes Linux (y compris les versions Red Hat de 2.0 à
4.2 comprise) étaient basés sur libc 5. Ce paquetage contient ces
bibliothèques et celles qui sont basées sur la libc 5 pour permettre
aux anciennes applications de tourner sur les systèmes basés sur glibc
(libc 6).

%description -l pl
Dawno, dawno temu aplikacje korzysta³y z wersji 5 biblioteki libc. Ten
pakiet zawiera tê i kilka innych, pomocniczych bibliotek, umo¿liwiaj±c
tym samym uruchomienie starszych programów. Przed zainstalowaniem,
sprawd¼ jednak, czy nie istniej± ich nowsze wersje, dzia³aj±ce z
bibliotekê libc 6.

%description -l tr
Eski Linux sistemleri libc 5 üzerine kurulmuþtu. Bu paket, libc 5
kitaplýklarý ve eski uygulamalarýn glibc (libc 6) üzerine kurulu olan
sistemlerde çalýþmasýný saðlayan kitaplýklarý içerir.

%prep
%setup -q -n %{name}5

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_libdir}/libc5}
for n in *; do
	install $n $RPM_BUILD_ROOT%{_libdir}/libc5/
done

(cd $RPM_BUILD_ROOT/lib ;\
ln -s ..%{_libdir}/libc5/libc.so.5.4.46 libc.so.5 ;\
ln -s ..%{_libdir}/libc5/libm.so.5.0.9 libm.so.5 )

%post
if ! grep '^%{_libdir}/libc5$' /etc/ld.so.conf > /dev/null 2>/dev/null; then
	echo "%{_libdir}/libc5" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun
/sbin/ldconfig
if [ "$1" = '0' ]; then
	grep -v '^%{_libdir}/libc5$' /etc/ld.so.conf > /etc/ld.so.conf.new 2>/dev/null
	mv /etc/ld.so.conf.new /etc/ld.so.conf
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/libc5
%attr(755,root,root) %{_libdir}/libc5/*
%attr(755,root,root) /lib/*
