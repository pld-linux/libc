Summary:	The compatibility libraries needed by old libc.so.5 applications
Summary(de):	Kompabilit�ts-Libraries f�r alte libc.so.5-Anwendungen
Summary(es):	Biblioteca compartida padr�n para programas
Summary(fr):	Librairies de compatibilit� pour les vieilles appl. libc.so.5
Summary(pl):	Biblioteki umo�liwiaj�ce uruchomienie aplikacji libc.so.5
Summary(pt_BR):	Biblioteca compartilhada padr�o para programas
Summary(tr):	Eski libc.so.5 uygulamalar� ile uyumlululu�u sa�layan kitapl�klar
Name:		libc
Version:	5.4.46
Release:	3
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
Requires(post):	grep
Requires(post,postun):	/sbin/ldconfig
Requires(postun):	fileutils
Requires:	/lib/ld-linux.so.1
Requires:	ld.so >= 1.9.9
Provides:	libc.so.5
Provides:	libm.so.5
Provides:	libstdc++.so.27
Provides:	libg++.so.27
Autoreqprov:	0
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

%description -l de
�ltere Linux-Systeme (einschlie�lich aller Red-Hat-Linux-Releases
zwischen 2.0 und 4.2 inkl.) basierten auf libc5. Dieses Paket schlie�t
diese Libraries und andere auf libc 5 basierende mit ein, so da�
�ltere Applikationen auf Systemen mit glibc (libc6) gefahren werden
k�nnen.

%description -l es
Contiene las bibliotecas padr�n que usan muchos programas en el
sistema.  Para guardar espacio en disco y memoria, y para facilitar
actualizaciones, c�digo com�n en el sistema se deja en un lugar
y se comparte entre los programas. Este paquete contiene los m�s
importantes conjuntos de bibliotecas compartidas, la biblioteca
padr�n C, y la biblioteca matem�tica padr�n. Sin este paquete un
sistema Linux no funcionar�.

%description -l fr
Les anciens syst�mes Linux (y compris les versions Red Hat de 2.0 �
4.2 comprise) �taient bas�s sur libc 5. Ce paquetage contient ces
biblioth�ques et celles qui sont bas�es sur la libc 5 pour permettre
aux anciennes applications de tourner sur les syst�mes bas�s sur glibc
(libc 6).

%description -l pl
Dawno, dawno temu aplikacje korzysta�y z wersji 5 biblioteki libc. Ten
pakiet zawiera t� i kilka innych, pomocniczych bibliotek, umo�liwiaj�c
tym samym uruchomienie starszych program�w. Przed zainstalowaniem,
sprawd� jednak, czy nie istniej� ich nowsze wersje, dzia�aj�ce z
bibliotek� libc 6.

%description -l pt_BR
Cont�m as bibliotecas-padr�o que s�o usadas por muitos programas
no sistema. Para salvar espa�o em disco e mem�ria, e para
facilitar atualiza��es, c�digo comum no sistema � deixado em
um lugar e compartilhado entre os programas. Este pacote cont�m
os mais importantes conjuntos de bibliotecas compartilhadas, a
biblioteca-padr�o C, e a biblioteca matem�tica-padr�o. Sem este
pacote um sistema Linux n�o ir� funcionar.

%description -l tr
Eski Linux sistemleri libc 5 �zerine kurulmu�tu. Bu paket, libc 5
kitapl�klar� ve eski uygulamalar�n glibc (libc 6) �zerine kurulu olan
sistemlerde �al��mas�n� sa�layan kitapl�klar� i�erir.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if ! grep -qs '^%{_libdir}/libc5$' /etc/ld.so.conf ; then
	echo "%{_libdir}/libc5" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun
umask 022
/sbin/ldconfig
if [ "$1" = '0' ]; then
	grep -v '^%{_libdir}/libc5$' /etc/ld.so.conf > /etc/ld.so.conf.new 2>/dev/null
	mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi

%files
%defattr(644,root,root,755)
%dir %{_libdir}/libc5
%attr(755,root,root) %{_libdir}/libc5/*
%attr(755,root,root) /lib/*
