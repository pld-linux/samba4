Summary:	SMB client and server
Summary(pl):	Klient i serwer SMB
Summary(cs):	Klient a server SMB
Summary(da):	SMB klient og server
Summary(de):	SMB-Client und -Server
Summary(fi):	SMB-asiakasohjelma ja palvelin
Summary(fr):	Client et serveur SMB
Summary(it):	Client e server SMB
Summary(tr):	SMB istemci ve sunucusu
Name:		samba
Version:	2.0.6
Release:	2
License:	GPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://samba.anu.edu.au/pub/samba/%{name}-%{version}.tar.gz
Source1:	smb.init
Source2:	samba.pamd
Source3:	swat.inetd
Patch1:		samba-config.patch
Patch2:		samba-cap.patch
Patch3:		samba-DESTDIR.patch
Prereq:		/sbin/chkconfig
Requires:	pam >= 0.66
Requires:	logrotate
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	pam-devel > 0.66
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_sysconfdir	/etc/samba
%define		_libdir		%{_sysconfdir}
%define		_localstatedir	/var/log/samba

%description
Samba provides an SMB server which can be used to provide network services
to SMB (sometimes called "Lan Manager") clients, including various versions
of MS Windows, OS/2, and other Linux machines. Samba also provides some SMB
clients, which complement the built-in SMB filesystem in Linux. Samba uses
NetBIOS over TCP/IP (NetBT) protocols and does NOT need NetBEUI (Microsoft
Raw NetBIOS frame) protocol.

This release is known as the "Locking Update" and has full support for
Opportunistic File Locking. In addition this update includes native support
for Microsoft encrypted passwords, improved browse list and WINS database
management.

Please refer to the WHATSNEW.txt document for fixup information. This binary
release includes encrypted password support. Please read the smb.conf file
and ENCRYPTION.txt in the docs directory for implementation details.

%description -l cs
Samba poskytuje server SMB, kter� lze pou��t pro poskytov�n� s��ov�ch slu�eb
klient�m SMB (n�kdy naz�van�ch klienti "LAN mana�er") v�etn� klient� r�zn�ch
verz� MS Windows, OS/2 a dal��ch linuxov�ch stroj�. Samba t� poskytuje
n�kter� klienty SMB, kte�� komplementuj� vestav�n� souborov� syst�m SMB v
Linuxu. Samba pou��v� protokoly NetBIOS p�es TCP/IP (NetBT) a NEpot�ebuje
protokol NetBEUI (neform�tovan� r�mec NetBIOS od spole�nosti Microsoft.

%description -l da
Samba tilbyder en SMB server som kan bruges til at tilbyde netv�rk services
til SMB (ogs� kaldet "Lan Manager") klienter, incl. forskellige versioner af
MS Windows, OS/2, og andre Linux maskiner. Samba tilbyder ogs� SMB klienter,
som udbygger det indbyggede SMB filsystem i Linux. Samba benytter NetBIOS
over TCP/IP (NetBT) protocolen og kr�ver ikke NetBEUI (Microsoft Raw NetBIOS
frame) protokollen.

%description -l de
Samba stellt einen SMB-Server zum Anbieten von Netzwerkdiensten f�r
SMB-Clients (auch "Lan Manager" genannt) zur Verf�gung, darunter
verschiedenen Versionen von MS Windows-, OS/2- und anderen Linux-Rechnern.
Samba enth�lt au�erdem einige SMB-Clients, die das in Linux integrierte
SMB-Dateisystem erg�nzen. Samba benutzt NetBIOS-�ber-TCP/IP
(NetBT)-Protokolle und ben�tigt KEIN NetBEUI (Microsoft Raw NetBIOS
frame)-Protokoll.

%description -l fi
Samba on SMB-palvelin, jota voidaan k�ytt�� SMB-asiakasohjelmien
verkkopalvelujen tarjoajana. SMB-protokollaa kutsutaan joskus "Lan Manager"
protokollaksi ja asiakasohjelmat toimivat dosissa, Windowseissa, OS/2:ssa ja
toisissa Linux-koneissa. Samban mukana on my�s joitakin SMB-asiakasohjelmia,
jotka t�ydent�v�t Linuxin kerneliss� olevaa SMB-tiedostoj�rjestelm�n tukea.
Samba vaatii NetBIOS over TCP/IP (NetBT) protokollaa eik� tarvitse tai pysty
k�ytt�m��n NetBEUI-protokollaa.

%description -l it
Samba fornisce un server SMB che puo` essere usato per fornire servizi di
rete ai client SMB, incluse le versioni MS Windows, OS/2 e per altre
macchine Linux. Samba fornisce anche i client SMB. Samba usa NetBIOS sopra
TCP/IP e non ha bisogno del protocollo NetBEUI.

%description -l pl
Samba udost�pnia serwer SMB, kt�ry mo�e by� u�yty w celu dostarczenia us�ug
sieciowych (potocznie zwanych "Lan Manager"), dla klient�w takich jak MS
Windows, OS/2 a tak�e maszyn linuxowych.  W pakiecie znajduje si� r�wnie�
oprogramowanie klienckie. Samba u�ywa protoko�u NetBIOS po TCP/IP (NetBT) i
nie wymaga protoko�u NetBEUI. Ta wersja ma pe�ne wsparcie dla blokowania
plik�w, a tak�e wsparcie dla kodowania hase� w standardzie MS i zarzadzania
baz� WINS.

%package -n swat
Summary:	Samba Web Administration Tool
Summary(pl):	Narz�dzie administracyjne serwisu Samba
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracja
Requires:	%{name}
Requires:	rc-inetd
Requires:	inetdaemon

%description -n swat
swat allows a Samba administrator to configure the complex smb.conf file via
a Web browser. In addition, a swat configuration page has help links to all
the configurable options in the smb.conf file allowing an administrator to
easily look up the effects of any change.

swat is run from inet server.

%description -n swat -l pl
swat pozwala na kompleksow� konfiguracj� smb.conf przy pomocy przegl�darki
internetowej.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cd source
autoconf
LDFLAGS="-s" export LDFLAGS \
%configure \
	--with-privatedir=%{_sysconfdir} \
	--with-lockdir=/var/lock/samba \
	--with-swatdir=%{_datadir}/swat \
	--with-smbmount \
	--without-smbwrapper \
	--with-quotas \
	--with-syslog \
	--with-mmap \
	--with-pam \
	--with-automount
	
make all 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/codepages/src \
	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

( cd source; make install DESTDIR=$RPM_BUILD_ROOT)


install  source/codepages/codepage_def.* \
	$RPM_BUILD_ROOT%{_sysconfdir}/codepages/src

install  packaging/PLD/smb.conf		$RPM_BUILD_ROOT%{_sysconfdir}
install  packaging/PLD/smbusers		$RPM_BUILD_ROOT%{_sysconfdir}
install  packaging/PLD/smbprint		$RPM_BUILD_ROOT%{_bindir}
install  packaging/PLD/smbadduser	$RPM_BUILD_ROOT%{_bindir}
install  packaging/PLD/findsmb		$RPM_BUILD_ROOT%{_bindir}
install  packaging/PLD/smb.init		$RPM_BUILD_ROOT/etc/rc.d/init.d/smb
install  packaging/PLD/samba.log	$RPM_BUILD_ROOT/etc/logrotate.d/samba
install  %{SOURCE2}			$RPM_BUILD_ROOT/etc/pam.d/samba
install  %{SOURCE3}		$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/swat

strip $RPM_BUILD_ROOT/{%{_bindir},%{_sbindir}}/* || :

touch $RPM_BUILD_ROOT/var/lock/samba/{STATUS..LCK,wins.dat,browse.dat}

echo 127.0.0.1 localhost > $RPM_BUILD_ROOT%{_sysconfdir}/lmhosts

echo "NICELEVEL=+5" > $RPM_BUILD_ROOT/etc/sysconfig/samba

for i in 437 737 850 852 861 866 932 949 950 936; do
$RPM_BUILD_ROOT%{_bindir}/make_smbcodepage c $i \
$RPM_BUILD_ROOT%{_sysconfdir}/codepages/src/codepage_def.$i \
$RPM_BUILD_ROOT%{_sysconfdir}/codepages/codepage.$i; done

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man?/* \
	README Manifest WHATSNEW.txt Roadmap docs/*.reg swat/README \
	docs/textdocs/* docs/*.txt docs/{history,announce,THANKS}

rm -f docs/faq/*.{sgml,txt}

%post
/sbin/chkconfig --add smb
if test -r ; then
	/etc/rc.d/init.d/smb restart >&2
else
	echo "Run \"/etc/rc.d/init.d/smb start\" to start samba daemons."
fi

%preun
if [ "$1" = "0" ]; then
	/etc/rc.d/init.d/smb stop >&2
	/sbin/chkconfig --del smb
fi

%post -n swat
if [ -f /var/lock/subsys/rc-inetd ]; then
   /etc/rc.d/init.d/rc-inetd restart 1>&2
else
   echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun -n swat
if [ -f /var/lock/subsys/rc-inetd ]; then
   /etc/rc.d/init.d/rc-inetd stop
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz Manifest.gz WHATSNEW.txt.gz
%doc Roadmap.gz docs/faq docs/*.reg.gz
%doc docs/textdocs docs/*.txt.gz docs/{history,announce,THANKS}.gz

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/nmbd
%attr(755,root,root) %{_sbindir}/smbd

%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/smb.conf
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/smbusers
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lmhosts

%attr(750,root,root) /etc/rc.d/init.d/smb
%attr(640,root,root) %config %verify(not size mtime md5) /etc/sysconfig/samba
%attr(640,root,root) /etc/logrotate.d/samba
%attr(640,root,root) /etc/pam.d/samba

#%attr(755,root,root) /lib/security/*.so

%{_mandir}/man[157]/*
%{_mandir}/man8/nmbd.8*
%{_mandir}/man8/smbd.8*
%{_mandir}/man8/smbmnt.8*
%{_mandir}/man8/smbmount.8*
%{_mandir}/man8/smbpasswd.8*
%{_mandir}/man8/smbumount.8*

%dir /home/samba
%{_sysconfdir}/codepages

%dir /var/lock/samba
%ghost /var/lock/samba/*

%attr(0750,root,root) %dir /var/log/samba
%attr(1777,root,root) %dir /var/spool/samba

%files -n swat
%defattr(644,root,root,755)
%doc swat/README*
%attr(755,root,root) %{_sbindir}/swat
%{_datadir}/swat
%{_mandir}/man8/swat.8*

%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/swat
