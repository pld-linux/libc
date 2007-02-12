Summary:	The compatibility libraries needed by old libc.so.5 applications
Summary(de.UTF-8):   Kompabilitäts-Libraries für alte libc.so.5-Anwendungen
Summary(es.UTF-8):   Biblioteca compartida padrón para programas
Summary(fr.UTF-8):   Librairies de compatibilité pour les vieilles appl. libc.so.5
Summary(pl.UTF-8):   Biblioteki umożliwiające uruchomienie aplikacji libc.so.5
Summary(pt_BR.UTF-8):   Biblioteca compartilhada padrão para programas
Summary(tr.UTF-8):   Eski libc.so.5 uygulamaları ile uyumlululuğu sağlayan kitaplıklar
Name:		libc
Version:	5.4.46
Release:	5
License:	distributable
Group:		Libraries
#######		From Slackware libc.so.5 & libm.so.5
#######		Other libraries from RH-5.2 updates
Source0:	%{name}-%{version}-compatibility_libs.tar.bz2
# Source0-md5:	a693059b39a925c9a93cb2fdf4f44963
# latest sources
# Source1:	ftp://ftp.kernel.org/pub/linux/libs/libc5/%{name}5.cvs.tar.bz2
Source1:	ftp://ftp.kernel.org/pub/linux/libs/libc5/old/%{name}-%{version}.tar.bz2
# Source1-md5:	3814ea25047461fee1130713d34869cc
Requires(post,postun):	/sbin/ldconfig
Requires(triggerpostun):	sed >= 4.0
Requires:	/lib/ld-linux.so.1
Requires:	glibc >= 6:2.3.5-7.6
Requires:	ld.so >= 1.9.9
Provides:	libc.so.5
Provides:	libm.so.5
Provides:	libstdc++.so.27
Provides:	libg++.so.27
AutoReqProv:	no
ExclusiveArch:	%{ix86}
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Older Linux systems (including all Red Hat Linux releases between 2.0
and 4.2, inclusive) were based on libc version 5. The libc package
includes the libc5 libraries and other libraries based on libc5. With
these libraries installed, old applications which need them will be
able to run on your glibc (libc version 6) based system. The libc
package should be installed so that you can run older applications
which need libc version 5.

%description -l de.UTF-8
Ältere Linux-Systeme (einschließlich aller Red-Hat-Linux-Releases
zwischen 2.0 und 4.2 inkl.) basierten auf libc5. Dieses Paket schließt
diese Libraries und andere auf libc 5 basierende mit ein, so daß
ältere Applikationen auf Systemen mit glibc (libc6) gefahren werden
können.

%description -l es.UTF-8
Contiene las bibliotecas padrón que usan muchos programas en el
sistema.  Para guardar espacio en disco y memoria, y para facilitar
actualizaciones, código común en el sistema se deja en un lugar
y se comparte entre los programas. Este paquete contiene los más
importantes conjuntos de bibliotecas compartidas, la biblioteca
padrón C, y la biblioteca matemática padrón. Sin este paquete un
sistema Linux no funcionará.

%description -l fr.UTF-8
Les anciens systèmes Linux (y compris les versions Red Hat de 2.0 à
4.2 comprise) étaient basés sur libc 5. Ce paquetage contient ces
bibliothèques et celles qui sont basées sur la libc 5 pour permettre
aux anciennes applications de tourner sur les systèmes basés sur glibc
(libc 6).

%description -l pl.UTF-8
Dawno, dawno temu aplikacje korzystały z wersji 5 biblioteki libc. Ten
pakiet zawiera tę i kilka innych, pomocniczych bibliotek, umożliwiając
tym samym uruchomienie starszych programów. Przed zainstalowaniem,
sprawdź jednak, czy nie istnieją ich nowsze wersje, działające z
biblioteką libc 6.

%description -l pt_BR.UTF-8
Contém as bibliotecas-padrão que são usadas por muitos programas
no sistema. Para salvar espaço em disco e memória, e para
facilitar atualizações, código comum no sistema é deixado em
um lugar e compartilhado entre os programas. Este pacote contém
os mais importantes conjuntos de bibliotecas compartilhadas, a
biblioteca-padrão C, e a biblioteca matemática-padrão. Sem este
pacote um sistema Linux não irá funcionar.

%description -l tr.UTF-8
Eski Linux sistemleri libc 5 üzerine kurulmuştu. Bu paket, libc 5
kitaplıkları ve eski uygulamaların glibc (libc 6) üzerine kurulu olan
sistemlerde çalışmasını sağlayan kitaplıkları içerir.

%prep
%setup -q -n %{name}5

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_libdir}/libc5}
for n in *; do
	install $n $RPM_BUILD_ROOT%{_libdir}/libc5/
done

(cd $RPM_BUILD_ROOT/lib ;\
ln -sf ..%{_libdir}/libc5/libc.so.5.4.46 libc.so.5 ;\
ln -sf ..%{_libdir}/libc5/libm.so.5.0.9 libm.so.5 )

install -d $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo '%{_libdir}/libc5' > $RPM_BUILD_ROOT/etc/ld.so.conf.d/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post -p	/sbin/ldconfig
%postun -p	/sbin/ldconfig

%triggerpostun -- libc < 5.4.46-4.1
sed -i -e "/^%(echo %{_libdir}/libc5 | sed -e 's,/,\\/,g')$/d" /etc/ld.so.conf

%files
%defattr(644,root,root,755)
/etc/ld.so.conf.d/*.conf
%dir %{_libdir}/libc5
%attr(755,root,root) %{_libdir}/libc5/*
%attr(755,root,root) /lib/*
