#
# Conditional build:
%bcond_without	ads		# without ActiveDirectory support
%bcond_without	cups		# without CUPS support
%bcond_without	kerberos5	# without Kerberos V support
%bcond_without	ldap		# without LDAP support
%bcond_without	avahi
%bcond_without	system_libs

# ADS requires kerberos5 and LDAP
%if %{without kerberos5} || %{without ldap}
%undefine	with_ads
%endif

%if %{with system_libs}
%define		talloc_ver	2.0.7
%define		tdb_ver		2:1.2.10
%define		ldb_ver		1.1.12
%define		tevent_ver	0.9.17
%endif

%define		virusfilter_version 0.1.3
Summary:	SMB server
Summary(cs.UTF-8):	Server SMB
Summary(da.UTF-8):	SMB server
Summary(de.UTF-8):	SMB-Server
Summary(es.UTF-8):	El servidor SMB
Summary(fi.UTF-8):	SMB-palvelin
Summary(fr.UTF-8):	Serveur SMB
Summary(it.UTF-8):	Server SMB
Summary(ja.UTF-8):	Samba SMB サーバー
Summary(ko.UTF-8):	삼바 SMB 서버
Summary(pl.UTF-8):	Serwer SMB
Summary(pt_BR.UTF-8):	Cliente e servidor SMB
Summary(ru.UTF-8):	SMB клиент и сервер
Summary(tr.UTF-8):	SMB sunucusu
Summary(uk.UTF-8):	SMB клієнт та сервер
Summary(zh_CN.UTF-8):	Samba 客户端和服务器
Name:		samba4
Version:	4.0.0
Release:	0.1
License:	GPL v3
Group:		Networking/Daemons
Source0:	http://www.samba.org/samba/ftp/stable/samba-%{version}.tar.gz
# Source0-md5:	93e9aad40893ba48d08e1b28e7efff72
Source1:	smb.init
Source2:	samba.pamd
Source3:	swat.inetd
Source4:	samba.sysconfig
Source5:	samba.logrotate
Source6:	smb.conf
Source7:	winbind.init
Source8:	winbind.sysconfig
Source10:	https://github.com/downloads/fumiyas/samba-virusfilter/samba-virusfilter-%{virusfilter_version}.tar.bz2
# Source10-md5:	a3a30d5fbf309d356e8c5833db680c17
Patch0:		system-heimdal.patch
Patch1:		samba-c++-nofail.patch
Patch3:		samba-nscd.patch
Patch4:		samba-lprng-no-dot-printers.patch
Patch5:		samba-passdb-smbpasswd.patch
URL:		http://www.samba.org/
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_avahi:BuildRequires:	avahi-devel}
BuildRequires:	ctdb-devel
%{?with_cups:BuildRequires:	cups-devel >= 1:1.2.0}
BuildRequires:	dmapi-devel
BuildRequires:	gamin-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
%{?with_kerberos5:BuildRequires:	heimdal-devel >= 1.5.3-1}
BuildRequires:	iconv
BuildRequires:	keyutils-devel
BuildRequires:	libcom_err-devel
BuildRequires:	libmagic-devel
BuildRequires:	libnscd-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	make >= 3.81
BuildRequires:	ncurses-devel >= 5.2
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel >= 0.99.8.1
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpmbuild(macros) >= 1.304
BuildRequires:	sed >= 4.0
%if %{with system_libs}
BuildRequires:	talloc-devel >= %{talloc_ver}
BuildRequires:	tdb-devel >= %{tdb_ver}
BuildRequires:	tevent-devel >= %{tevent_ver}
BuildRequires:	ldb-devel >= %{ldb_ver}
BuildRequires:	python-ldb-devel >= %{ldb_ver}
BuildRequires:	python-talloc-devel >= %{talloc_ver}
BuildRequires:	python-tevent >= %{tevent_ver}
%endif
BuildRequires:	xfsprogs-devel
BuildConflicts:	libbsd-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{version}-%{release}
Requires:	logrotate >= 3.7-4
Requires:	pam >= 0.99.8.1
Requires:	rc-scripts >= 0.4.0.12
Requires:	setup >= 2.4.6-7
# smbd links with libcups
%{?with_cups:Requires:	cups-lib >= 1:1.2.0}
Obsoletes:	samba-pdb-xml
Obsoletes:	samba-vfs-block
Obsoletes:	samba-doc-html
Obsoletes:	samba-doc-pdf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sambahome	/home/services/samba
%if %{with cups}
%define		cups_serverbin	%{_prefix}/lib/cups
%endif
%define		schemadir	/usr/share/openldap/schema

# CFLAGS modified (the second ./configure)
%undefine	configure_cache

%description
Samba provides an SMB server which can be used to provide network
services to SMB (sometimes called "Lan Manager") clients, including
various versions of MS Windows, OS/2, and other Linux machines. Samba
also provides some SMB clients, which complement the built-in SMB
filesystem in Linux. Samba uses NetBIOS over TCP/IP (NetBT) protocols
and does NOT need NetBEUI (Microsoft Raw NetBIOS frame) protocol.

This release is known as the "Locking Update" and has full support for
Opportunistic File Locking. In addition this update includes native
support for Microsoft encrypted passwords, improved browse list and
WINS database management.

Please refer to the WHATSNEW.txt document for fixup information. This
binary release includes encrypted password support. Please read the
smb.conf file for implementation details.

%description -l cs.UTF-8
Samba poskytuje server SMB, který lze použít pro poskytování síťových
služeb klientům SMB (někdy nazývaných klienti "LAN manažer") včetně
klientů různých verzí MS Windows, OS/2 a dalších linuxových strojů.
Samba též poskytuje některé klienty SMB, kteří komplementují vestavěný
souborový systém SMB v Linuxu. Samba používá protokoly NetBIOS přes
TCP/IP (NetBT) a NEpotřebuje protokol NetBEUI (neformátovaný rámec
NetBIOS od společnosti Microsoft.

%description -l da.UTF-8
Samba tilbyder en SMB server som kan bruges til at tilbyde netværk
services til SMB (også kaldet "Lan Manager") klienter, incl.
forskellige versioner af MS Windows, OS/2, og andre Linux maskiner.
Samba tilbyder også SMB klienter, som udbygger det indbyggede SMB
filsystem i Linux. Samba benytter NetBIOS over TCP/IP (NetBT)
protocolen og kræver ikke NetBEUI (Microsoft Raw NetBIOS frame)
protokollen.

%description -l de.UTF-8
Samba stellt einen SMB-Server zum Anbieten von Netzwerkdiensten für
SMB-Clients (auch "Lan Manager" genannt) zur Verfügung, darunter
verschiedenen Versionen von MS Windows-, OS/2- und anderen
Linux-Rechnern. Samba enthält außerdem einige SMB-Clients, die das in
Linux integrierte SMB-Dateisystem ergänzen. Samba benutzt
NetBIOS-über-TCP/IP (NetBT)-Protokolle und benötigt KEIN NetBEUI
(Microsoft Raw NetBIOS frame)-Protokoll.

%description -l es.UTF-8
Samba provee un servidor SMB que se puede usar para ofrecer servicios
de red a clientes SMB (algunas veces se le llama de "Lan Manager"),
incluyendo varias versiones de MS Windows, OS/2, y otras máquinas
Linux. Samba también ofrece algunos clientes SMB, que complementan el
sistema de archivos SMB de Linux. Samba usa el protocolo NetBIOS sobre
TCP/IP (NetBT) y no necesita del protocolo NetBEUI (Microsoft Raw
NetBIOS frame).

%description -l fi.UTF-8
Samba on SMB-palvelin, jota voidaan käyttää SMB-asiakasohjelmien
verkkopalvelujen tarjoajana. SMB-protokollaa kutsutaan joskus "Lan
Manager" protokollaksi ja asiakasohjelmat toimivat dosissa,
Windowseissa, OS/2:ssa ja toisissa Linux-koneissa. Samban mukana on
myös joitakin SMB-asiakasohjelmia, jotka täydentävät Linuxin
kernelissä olevaa SMB-tiedostojärjestelmän tukea. Samba vaatii NetBIOS
over TCP/IP (NetBT) protokollaa eikä tarvitse tai pysty käyttämään
NetBEUI-protokollaa.

%description -l it.UTF-8
Samba fornisce un server SMB che puo` essere usato per fornire servizi
di rete ai client SMB, incluse le versioni MS Windows, OS/2 e per
altre macchine Linux. Samba fornisce anche i client SMB. Samba usa
NetBIOS sopra TCP/IP e non ha bisogno del protocollo NetBEUI.

%description -l ja.UTF-8
Samba は MS Windows の様々なバージョン、OS/2 そして他の Linux マシン
を含む SMB (たまに "Lan Manager" と呼ばれる)
クライアントにネットワーク サービスを提供するために使用される SMB
サーバを提供します。Samba は NetBIOS over TCP/IP (NetBT)
プロトコルを使用し、 NetBEUI(Microsoft Raw NetBIOS frame)
プロトコルは必要ありません。

Samba ほとんど動作する NT ドメインコントロールの機能を特徴とし、
好きなブラウザを使って samba の smb.conf ファイルをリモート管理する
新しい SWAT (Samba Web Administration Tool) を含みます。
目下のところこれは inetd を通して TCP ポート 901 で有効になります。

%description -l ko.UTF-8
삼바는 MS Windows, OS/2, 혹은 다른 리눅스 머신을 포함하는 SMB(혹은
"Lan Manager"라고도 불림) 클라이언트를 네트워크 서비스 위해 사용할 수
있는 SMB 서버를 제공한다. 삼바는 TCP/IP 프로토콜을 통해 NetBIOS를
사용하고 NetBEUI (Microsoft Raw NetBIOS 프레임) 프로토콜은 필요하지
않다.

삼바-2.2 의 특징은 NT 도메인 컨트롤의 성능으로 작업을 하고, 새로운
SWAT(Samba Web Administration Tool)로 웹브라우저를 사용하여 원격지에서
삼바의 smb.conf 파일을 관리하도록 한다. 이러한 경우 inetd 데몬을 통해
TCP 901 포트를 사용하게 된다.

최근 정보로 WHATSNEW.txt 파일의 문서를 참고하도록 한다. 바이너리의
릴리즈는 암호화된 패스워드를 제공한다.

%description -l pl.UTF-8
Samba udostępnia serwer SMB, który może być użyty w celu dostarczenia
usług sieciowych (potocznie zwanych "Lan Manager"), dla klientów
takich jak MS Windows, OS/2 a także maszyn linuksowych. W pakiecie
znajduje się również oprogramowanie klienckie. Samba używa protokołu
NetBIOS po TCP/IP (NetBT) i nie wymaga protokołu NetBEUI. Ta wersja ma
pełne wsparcie dla blokowania plików, a także wsparcie dla kodowania
haseł w standardzie MS i zarządzania bazą WINS.

%description -l pt_BR.UTF-8
O Samba provê um servidor SMB que pode ser usado para oferecer
serviços de rede a clientes SMB (algumas vezes chamado de "Lan
Manager"), incluindo várias versões de MS Windows, OS/2, e outras
máquinas Linux. O Samba também fornece alguns clientes SMB, que
complementam o sistema de arquivos SMB do Linux. O Samba usa o
protocolo NetBIOS sobre TCP/IP (NetBT) e não necessita do protocolo
NetBEUI (Microsoft Raw NetBIOS frame).

O Samba inclui a maioria das características de um servidor de
Controle de Domínios NT e o SWAT (Samba Web Administration Tool), que
permite que o arquivo smb.conf seja gerenciado remotamente através de
um navegador. Atualmente isto está sendo habilitado na porta TCP 901
via inetd.

%description -l ru.UTF-8
Samba предоставляет SMB-сервер, который может быть использован для
предоставления сетевых сервисов SMB (иногда называемым "Lan Manager")
клиентам, включая разнообразные версии MS Windows, OS/2, и другие
Linux-машины. Samba также предоставляет SMB-клиентов, которые работают
со встроенной в Linux файловой системой SMB.

Samba использует протокол NetBIOS over TCP/IP (NetBT) и не нуждается в
протоколе NetBEUI (Microsoft Raw NetBIOS frame).

Samba содержит практически работающую реализацию NT Domain Control и
включает новый SWAT (Samba Web Administration Tool), который позволяет
удаленно управлять конфигурационным файлом smb.conf при помощи вашего
любимого WEB-броузера. Пока что он разрешен через inetd на TCP-порту
901.

%description -l uk.UTF-8
Samba надає SMB-сервер, що може бути використаний для надання
мережевих сервісів SMB (що їх іноді називають "Lan Manager") клієнтам,
включаючи різноманітні версії MS Windows, OS/2, та інші Linux-машини.
Samba також надає SMB-клієнтів, що працюють з вбудованою в Linux
файловою системою SMB.

Samba використовує протокол NetBIOS over TCP/IP (NetBT) та не потребує
протоколу NetBEUI (Microsoft Raw NetBIOS frame).

Samba містить майже працюючу реализацію NT Domain Control та новый
SWAT (Samba Web Administration Tool), котрий дозволяє віддалено
керувати конфігураційним файлом smb.conf за допомогою вашого
улюбленого WEB-броузера. Поки що він дозволений через inetd на
TCP-порту 901.

%package swat
Summary:	Samba Web Administration Tool
Summary(pl.UTF-8):	Narzędzie administracyjne serwisu Samba
Summary(pt_BR.UTF-8):	Samba SWAT e documentação Web
Summary(ru.UTF-8):	Программа конфигурации SMB-сервера Samba
Summary(uk.UTF-8):	Програма конфигурації SMB-сервера Samba
Group:		Networking/Admin
Requires:	%{name} = %{version}-%{release}
Requires:	inetdaemon
Requires:	rc-inetd >= 0.8.2
Obsoletes:	swat

%description swat
swat allows a Samba administrator to configure the complex smb.conf
file via a Web browser. In addition, a swat configuration page has
help links to all the configurable options in the smb.conf file
allowing an administrator to easily look up the effects of any change.

%description swat -l pl.UTF-8
swat pozwala na kompleksową konfigurację smb.conf przy pomocy
przeglądarki WWW.

%description swat -l pt_BR.UTF-8
SWAT - ferramentada Web de configuração do Samba.

%description swat -l ru.UTF-8
Пакет samba-swat включает новый SWAT (Samba Web Administration Tool),
для удаленного администрирования файла smb.conf при помощи вашего
любимого Web-браузера.

%description swat -l uk.UTF-8
Пакет samba-swat містить новий SWAT (Samba Web Administration Tool),
для дистанційного адміністрування файлу smb.conf за допомогою вашого
улюбленого Web-браузеру.

%package client
Summary:	Samba client programs
Summary(es.UTF-8):	Cliente SMB de Samba
Summary(ja.UTF-8):	Samba (SMB) クライアントプログラム
Summary(pl.UTF-8):	Klienci serwera Samba
Summary(pt_BR.UTF-8):	Cliente SMB do samba
Summary(ru.UTF-8):	Клиентские программы Samba (SMB)
Summary(uk.UTF-8):	Клієнтські програми Samba (SMB)
Group:		Applications/Networking
Requires:	%{name}-common = %{version}-%{release}
%{?with_kerberos5:Requires:	heimdal-libs >= 1.5.3-1}
Requires:	libsmbclient = %{version}-%{release}
Obsoletes:	smbfs
Suggests:	cifs-utils

%description client
Samba-client provides some SMB clients, which complement the build-in
SMB filesystem in Linux. These allow accessing of SMB shares and
printing to SMB printers.

%description client -l es.UTF-8
Cliente SMB de Samba.

%description client -l ja.UTF-8
Samba-client は Linux 上に含まれている SMB ファイルシステムを補う SMB
クライアントを提供します。これらは SMB 共有のアクセスと SMB
プリンタへの印刷を許可します。

%description client -l pl.UTF-8
Samba-client dostarcza programy uzupełniające obsługę systemu plików
SMB zawartą w jądrze. Pozwalają one na współdzielenie zasobów SMB i
drukowanie w sieci SMB.

%description client -l pt_BR.UTF-8
O pacote samba-clientes prove alguns clientes SMB, que complementam o
sistema de arquivos SMB do Linux. Eles permitem o acesso a shares SMB,
e também, à impressoras SMB.

%description client -l ru.UTF-8
Пакет samba-client предоставляет некоторые клиенты SMB для работы со
встроенной файловой системой SMB в Linux. Эти клиенты позволяют
получать доступ к разделяемым каталогам SMB и печать на SMB-принтеры.

%description client -l uk.UTF-8
Пакет samba-client надає деякі клієнти SMB для роботи зі вбудованою
файловою системою SMB в Linux. Ці клієнти дозволяють отримувати доступ
до каталогів спільного використання SMB та друк на SMB-прінтери.

%package common
Summary:	Files used by both Samba servers and clients
Summary(ja.UTF-8):	Samba サーバーとクライアントで使用されるプログラム
Summary(pl.UTF-8):	Pliki używane przez serwer i klientów Samba
Summary(pt_BR.UTF-8):	Arquivos em comum entre samba e samba-clients
Summary(ru.UTF-8):	Файлы, используемые как сервером, так и клиентом Samba
Summary(uk.UTF-8):	Файли, що використовуються як сервером, так і клієнтом Samba
Group:		Networking/Daemons
Requires:	talloc >= %{talloc_ver}
Requires:	tdb >= %{tdb_ver}

%description common
Samba-common provides files necessary for both the server and client
packages of Samba.

%description common -l ja.UTF-8
Samba-common は Samba のサーバとクライアントの両方のパッケージで
使用されるファイルを提供します。

%description common -l pl.UTF-8
Samba-common dostarcza pliki niezbędne zarówno dla serwera jak i
klientów Samba.

%description common -l pt_BR.UTF-8
Arquivos em comum entre os pacotes samba e samba-clients.

%description common -l ru.UTF-8
Samba-common содержит файлы, необходимые для работы как клиента, так и
сервера Samba.

%description common -l uk.UTF-8
Samba-common містить файли, необхідні для роботи як клієнта, так і
сервера Samba.

%package winbind
Summary:	Samba-winbind daemon, utilities and documentation
Summary(pl.UTF-8):	Demon samba-winbind, narzędzia i dokumentacja
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{version}-%{release}

%description winbind
Provides the winbind daemon and testing tools to allow authentication
and group/user enumeration from a Windows or Samba domain controller.

%description winbind -l pl.UTF-8
Pakiet zawiera demona winbind oraz narzędzia testowe. Umożliwia
uwierzytelnianie i wyliczanie grup/użytkowników z kontrolera domeny
Windows lub Samba.

%package -n nss_wins
Summary:	Name Service Switch service for WINS
Summary(pl.UTF-8):	Usługa Name Service Switch dla WINS
Group:		Base
Requires:	%{name}-common = %{version}-%{release}

%description -n nss_wins
Provides the libnss_wins shared library which resolves NetBIOS names
to IP addresses.

%description -n nss_wins -l pl.UTF-8
Biblioteka dzielona libnss_wins rozwiązująca nazwy NetBIOS na adresy
IP.

%package -n pam-pam_smbpass
Summary:	PAM Samba Password Module
Summary(pl.UTF-8):	Moduł PAM smbpass
Group:		Base
Obsoletes:	pam_smbpass

%description -n pam-pam_smbpass
PAM module which can be used on conforming systems to keep the
smbpasswd (Samba password) database in sync with the Unix password
file.

%description -n pam-pam_smbpass -l pl.UTF-8
Moduł PAM, który może być używany do trzymania pliku smbpasswd (hasła
Samby) zsynchronizowanego z hasłami uniksowymi.

%package -n libsmbclient
Summary:	libsmbclient - samba client library
Summary(pl.UTF-8):	libsmbclient - biblioteka klienta samby
Group:		Libraries

%description -n libsmbclient
libsmbclient - library that allows to use samba clients functions.

%description -n libsmbclient -l pl.UTF-8
libsmbclient - biblioteka pozwalająca korzystać z funcji klienta
samby.

%package -n libsmbclient-devel
Summary:	libsmbclient - samba client library
Summary(pl.UTF-8):	libsmbclient - biblioteka klienta samby
Summary(pt_BR.UTF-8):	Ferramentas de desenvolvimento para clientes samba
Group:		Development/Libraries
Requires:	libsmbclient = %{version}-%{release}
Obsoletes:	libsmbclient-static

%description -n libsmbclient-devel
Header files for libsmbclient.

%description -n libsmbclient-devel -l pl.UTF-8
Pliki nagłówkowe dla libsmbclient.

%description -n libsmbclient-devel -l pt_BR.UTF-8
Arquivos de inclusão, bibliotecas e documentação necessários para
desenvolver aplicativos clientes para o samba.

%package devel
Summary:	Header files for Samba
Summary(pl.UTF-8):	Pliki nagłówkowe Samby
Group:		Development/Libraries

%description devel
Header files for Samba.

%description devel -l pl.UTF-8
Pliki nagłówkowe Samby.

%package -n smbget
Summary:	A utility for retrieving files using the SMB protocol
Summary(pl.UTF-8):	Narzędzie do pobierania plików protokołem SMB
Group:		Applications/Networking

%description -n smbget
wget-like utility for download files over SMB.

%description -n smbget -l pl.UTF-8
Narzędzie podobne do wgeta do pobierania plików protokołem SMB
używanym w sieciach MS Windows.

%package -n cups-backend-smb
Summary:	CUPS backend for printing to SMB printers
Summary(pl.UTF-8):	Backend CUPS-a drukujący na drukarkach SMB
Group:		Applications/Printing
Requires:	%{name}-client = %{version}-%{release}
Requires:	cups >= 1:1.2.0

%description -n cups-backend-smb
CUPS backend for printing to SMB printers.

%description -n cups-backend-smb -l pl.UTF-8
Backend CUPS-a drukujący na drukarkach SMB.

%package vfs-audit
Summary:	VFS module to audit file access
Summary(pl.UTF-8):	Moduł VFS do monitorowania operacji na plikach
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-audit
A simple module to audit file access to the syslog facility. The
following operations are logged:
 - share connect/disconnect,
 - directory opens/create/remove,
 - file open/close/rename/unlink/chmod.

%description vfs-audit -l pl.UTF-8
Proste moduły do monitorowania dostępu do plików na serwerze samba do
do sysloga. Monitorowane są następujące operacje:
 - podłączenie do/odłączenie od zasobu,
 - otwarcie/utworzenie/zmiana nazwy katalogu,
 - otwarcie/zamknięcie/zmiana nazwy/skasowanie/zmiana praw plików.

Zawiera moduły audit, extd_audit i full_audit.

%package vfs-cap
Summary:	VFS module for CAP and samba compatibility
Summary(pl.UTF-8):	Moduł VFS zgodności z CAP (Columbia AppleTalk Program)
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-cap
Convert an incoming Shift-JIS character to the 3 byte hex
representation used by the Columbia AppleTalk Program (CAP), i.e. :AB.
This is used for compatibility between Samba and CAP.

%description vfs-cap -l pl.UTF-8
Zamienia znaki kodowane Shift-JIS do trzybajowej szestnastkowej
reprezentacji używanej przez program Columbia AppleTalk Program (CAP).

%package vfs-default_quota
Summary:	VFS module to store default quotas in a specified quota record
Summary(pl.UTF-8):	Moduł VFS do zapisywania domyślnych limitów w określonym rekordzie
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-default_quota
This VFS modules stores default quotas in a specified quota record.

%description vfs-default_quota -l pl.UTF-8
Ten moduł VFS zapisuje domyślne limity (quoty) w określonym rekordzie
limitów.

%package vfs-expand_msdfs
Summary:	VFS module for hosting a Microsoft Distributed File System Tree
Summary(pl.UTF-8):	Moduł VFS obsługi Microsoft Distributed File System
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-expand_msdfs
A VFS module for hosting a Microsoft Distributed File System Tree.

The Distributed File System (DFS) provides a means of separating the
logical view of files and directories that users see from the actual
physical locations of these resources on the network. It allows for
higher availability, smoother storage expansion, load balancing, and
so on.

%description vfs-expand_msdfs -l pl.UTF-8
Moduł VFS do udostępniania drzewa systemu plików Microsoft Distributed
File System.

Distributed File System (DFS) umożliwia rozdzielanie logicznego widoku
plików i katalogów widocznych przez użytkowników z fizycznego
umiejscowienia tych zasobów w sieci. Pozwala to na wyższą dostępność,
płynniejsze powiększanie przestrzeni, rozdzielanie obciążenia itp.

%package vfs-fake_perms
Summary:	VFS module to report read-only fires as writable
Summary(pl.UTF-8):	Moduł VFS udający, że pliki tylko do odczytu są zapisywalne
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-fake_perms
This module allow Roaming Profile files and directories to be set (on
the Samba server under UNIX) as read only. This module will, if
installed on the Profiles share, report to the client that the Profile
files and directories are writeable. This satisfies the client even
though the files will never be overwritten as the client logs out or
shuts down.

%description vfs-fake_perms -l pl.UTF-8
Ten moduł pozwala na ustawienie plików i katalogów z wędrujących
profili (Roaming Profiles) jako tylko do odczytu. Moduł ten w
przypadku zainstalowania na udziale z profilami będzie zgłaszał
klientom, że pliki i katalogi z profilu są zapisywane. To wystarczy
klientom pomimo, że pliki nie zostaną nigdy nadpisane przy logowaniu
lub wylogowywaniu klienta.

%package vfs-notify_fam
Summary:	VFS module to implement file change notifications
Summary(pl.UTF-8):	Moduł VFS implementujący informowanie o zmianach w plikach
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-notify_fam
The vfs_notify_fam module makes use of the system FAM (File Alteration
Monitor) daemon to implement file change notifications for Windows
clients.

%description vfs-notify_fam -l pl.UTF-8
Ten moduł używa demona FAM (File Alteration Monitor) do implementacji
informowania o zmianach w plikach dla klientów Windows.

%package vfs-netatalk
Summary:	VFS module for ease co-existence of samba and netatalk
Summary(pl.UTF-8):	Moduł VFS ułatwiający współpracę serwisów samba i netatalk
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-netatalk
Package contains a netatalk VFS module for ease co-existence of Samba
and netatalk file sharing services.

%description vfs-netatalk -l pl.UTF-8
Pakiet zawiera moduł VFS netatalk umożliwiający współpracę usług samba
i netatalk przy udostępnianiu zasobów.

%package vfs-recycle
Summary:	VFS module to add recycle bin facility to a samba share
Summary(pl.UTF-8):	Moduł VFS dodający możliwość kosza do zasobu samby
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-recycle
VFS module to add recycle bin facility to a samba share.

%description vfs-recycle -l pl.UTF-8
Moduł VFS dodający możliwość kosza do zasobu samby.

%package vfs-readahead
Summary:	VFS module for pre-loading the kernel buffer cache
Summary(pl.UTF-8):	Moduł VFS do wczesnego odczytu danych do bufora cache jądra
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-readahead
This VFS module detects read requests at multiples of a given offset
(hex 0x80000 by default) and then tells the kernel via either the
readahead system call (on Linux) or the posix_fadvise system call to
pre-fetch this data into the buffer cache.

This module is useful for Windows Vista clients reading data using the
Windows Explorer program, which asynchronously does multiple file read
requests at offset boundaries of 0x80000 bytes.

%description vfs-readahead -l pl.UTF-8
Ten moduł VFS wykrywa żądania odczytu spod wielokrotności podanych
pozycji (domyślnie 0x80000 szesnastkowo) i instruuje jądro poprzez
wywołanie systemowe readahead (pod Linuksem) lub posix_fadvise do
wczesnego odczytu tych danych do bufora cache.

Ten moduł jest przydatny dla klientów Windows Vista odczytujących dane
przy użyciu programu Windows Explorer, który asynchronicznie wykonuje
wiele żądań odczytu plików spod pozycji o wielokrotnościach 0x80000
bajtów.

%package vfs-readonly
Summary:	VFS module for read-only limitation for specified share
Summary(pl.UTF-8):	Moduł VFS do ograniczania określonego udziału tylko do odczytu
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-readonly
This module performs a read-only limitation for specified share (or
all of them if it is loaded in a [global] section) based on period
definition in smb.conf.

%description vfs-readonly -l pl.UTF-8
Ten moduł wprowadza ograniczenie tylko do odczytu dla określonego
udziału (lub wszystkich, jeśli jest wczytywany w sekcji [global]) w
oparciu o definicje okresów w smb.conf.

%package vfs-shadow_copy
Summary:	VFS module to make automatic copy of data in samba share
Summary(pl.UTF-8):	Moduł VFS do tworzenia automatycznych kopii danych w zasobach samby
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-shadow_copy
VFS module to make automatic copy of data in samba share.

%description vfs-shadow_copy -l pl.UTF-8
Moduł VFS do tworzenia automatycznych kopii danych w zasobach samby.

%package vfs-catia
Summary:	VFS module to fix Catia CAD filenames
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-catia
The Catia CAD package commonly creates filenames that use characters
that are illegal in CIFS filenames. The vfs_catia VFS module
implements a fixed character mapping so that these files can be shared
with CIFS clients.

%package vfs-scannedonly
Summary:	Anti-virus solution as VFS module
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description vfs-scannedonly
The vfs_scannedonly VFS module ensures that only files that have been
scanned for viruses are visible and accessible to the end user. If
non-scanned files are found an anti-virus scanning daemon is notified.

%package -n openldap-schema-samba
Summary:	Samba LDAP schema
Summary(pl.UTF-8):	Schemat LDAP dla samby
Group:		Networking/Daemons
Requires(post,postun):	sed >= 4.0
Requires:	openldap-servers

%description -n openldap-schema-samba
This package contains samba.schema for openldap.

%description -n openldap-schema-samba -l pl.UTF-8
Ten pakiet zawiera schemat samby dla openldap-a.

%package -n python-samba4
Summary:	Samba Module for Python
Group:		Development/Languages/Python
%pyrequires_eq 	python
Requires:	%{name}-common = %{version}-%{release}

%description -n python-samba4
Samba Module for Python.

%prep
%setup -q -n samba-%{version}
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1

%build
LDFLAGS="${LDFLAGS:-%rpmldflags}" \
CFLAGS="${CFLAGS:-%rpmcflags}" \
CXXFLAGS="${CXXFLAGS:-%rpmcxxflags}" \
FFLAGS="${FFLAGS:-%rpmcflags}" \
FCFLAGS="${FCFLAGS:-%rpmcflags}" \
CPPFLAGS="${CPPFLAGS:-%rpmcppflags}" \
%{?__cc:CC="%{__cc}"} \
%{?__cxx:CXX="%{__cxx}"} \
./configure \
	--enable-fhs \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--sharedstatedir=%{_sharedstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--with-privatelibdir=%{_libdir}/samba \
	--with-modulesdir=%{_libdir}/samba \
	--with-pammodulesdir=/%{_lib}/security \
	--with-lockdir=/var/lib/samba \
	--with-privatedir=%{_sysconfdir}/samba \
	--disable-gnutls \
	--disable-rpath-install \
	--builtin-libraries=ccan \
	--bundled-libraries=NONE,subunit,iniparser,%{!?with_system_libs:talloc,tdb,ldb,tevent,pytalloc,pytalloc-util,pytdb,pytevent,pyldb,pyldb-util} \
	--private-libraries=smbclient,smbsharemodes,wbclient \
	--with-shared-modules=idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2,pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4,auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4 \
	--with-acl-support \
	--with%{!?with_ads:out}-ads \
	--with-aio-support \
	--with-automount \
	--with-dmapi \
	--with-dnsupdate \
	--with-iconv \
	--with%{!?with_ldap:out}-ldap \
	--with-pam \
	--with-pam_smbpass \
	--with-quotas \
	--with-sendfile-support \
	--with-swat \
	--with-syslog \
	--with-utmp \
	--with-winbind \
	--%{?with_avahi:en}%{!?with_avahi:dis}able-avahi \
	--enable-cups \
	--enable-iprint

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,pam.d,security,sysconfig/rc-inetd} \
	$RPM_BUILD_ROOT{/var/{log/archive,spool}/samba,/var/lib/samba/printing} \
	$RPM_BUILD_ROOT/var/log/samba/cores/{smbd,nmbd} \
	$RPM_BUILD_ROOT{/sbin,/%{_lib}/security,%{_libdir},%{_libdir}/samba/vfs,%{_includedir},%{_sambahome},%{schemadir}} \
	$RPM_BUILD_ROOT{%{systemdtmpfilesdir},%{systemdunitdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CONFIGDIR=$RPM_BUILD_ROOT%{_sysconfdir}/samba

install -p source3/script/mksmbpasswd.sh $RPM_BUILD_ROOT%{_sbindir}

install packaging/systemd/samba.conf.tmp $RPM_BUILD_ROOT%{systemdtmpfilesdir}/samba.conf
install packaging/systemd/nmb.service $RPM_BUILD_ROOT%{systemdunitdir}
install packaging/systemd/samba.service $RPM_BUILD_ROOT%{systemdunitdir}
install packaging/systemd/smb.service $RPM_BUILD_ROOT%{systemdunitdir}
install packaging/systemd/winbind.service $RPM_BUILD_ROOT%{systemdunitdir}

install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/smb
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/samba
install -p %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/swat
cp -p %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/samba
cp -p %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/samba
cp -p %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/samba/smb.conf
install -p %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/winbind
cp -p %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/winbind

%{__mv} $RPM_BUILD_ROOT%{_libdir}/libnss_winbind.so* $RPM_BUILD_ROOT/%{_lib}
%{__mv} $RPM_BUILD_ROOT%{_libdir}/libnss_wins.so* $RPM_BUILD_ROOT/%{_lib}
install -p bin/vfstest $RPM_BUILD_ROOT%{_bindir}

# these are needed to build samba-pdbsql
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}/nsswitch
cp -a source3/include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -a nsswitch/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/nsswitch
%if %{without system_libtdb}
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}/tdb
cp -a lib/tdb/include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/tdb
%endif

touch $RPM_BUILD_ROOT/var/lib/samba/{wins.dat,browse.dat}

echo '127.0.0.1 localhost' > $RPM_BUILD_ROOT%{_sysconfdir}/samba/lmhosts

%if %{with cups}
install -d $RPM_BUILD_ROOT%{cups_serverbin}/backend
ln -s %{_bindir}/smbspool $RPM_BUILD_ROOT%{cups_serverbin}/backend/smb
%endif

> $RPM_BUILD_ROOT%{_sysconfdir}/samba/smbusers
> $RPM_BUILD_ROOT/etc/security/blacklist.samba

%if %{with ldap}
install examples/LDAP/samba.schema $RPM_BUILD_ROOT%{schemadir}
%endif

%if %{with system_libtdb}
# remove manuals of tdb if system lib used
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/tdbbackup.8*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/tdbdump.8*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/tdbtool.8*
%endif

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" -o -name "*.a" -o -name "*.la" | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add smb
if [ -f /var/lock/samba/connections.tdb -a ! -f /var/lib/samba/connections.tdb ]; then
	echo >&2 "Moving old /var/lock/samba contents to /var/lib/samba"
	/sbin/service smb stop >&2
	mv -f /var/lock/samba/*.tdb /var/lib/samba 2>/dev/null || :
	mv -f /var/lock/samba/*.dat /var/lib/samba 2>/dev/null || :
	if [ -d /var/lock/samba/printing ]; then
		mv -f /var/lock/samba/printing/*.tdb /var/lib/samba/printing 2>/dev/null || :
	fi
	/sbin/service smb start >&2
else
	%service smb restart "Samba daemons"
fi

%preun
if [ "$1" = "0" ]; then
	%service smb stop
	/sbin/chkconfig --del smb
fi

%post winbind
/sbin/chkconfig --add winbind
%service winbind restart "Winbind daemon"

%preun winbind
if [ "$1" = "0" ]; then
	%service winbind stop
	/sbin/chkconfig --del winbind
fi

%post swat
%service -q rc-inetd reload

%postun swat
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post -n openldap-schema-samba
# dependant schemas: cosine(uid) inetorgperson(displayName) nis(gidNumber)
%openldap_schema_register %{schemadir}/samba.schema -d cosine,inetorgperson,nis
%service -q ldap restart

%postun -n openldap-schema-samba
if [ "$1" = "0" ]; then
	%openldap_schema_unregister %{schemadir}/samba.schema
	%service -q ldap restart
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/nmbd
%attr(755,root,root) %{_sbindir}/smbd
%attr(755,root,root) %{_sbindir}/mksmbpasswd.sh
%attr(755,root,root) %{_bindir}/reg*
%attr(755,root,root) %{_bindir}/smbstatus
%attr(755,root,root) %{_bindir}/smbpasswd
%attr(755,root,root) %{_bindir}/smbta-util
%attr(755,root,root) %{_bindir}/smbcontrol

%dir %{_libdir}/samba/idmap
%attr(755,root,root)  %{_libdir}/samba/idmap/autorid.so
%{_mandir}/man8/idmap_autorid.8*
%dir %{_libdir}/samba/pdb
%dir %{_libdir}/samba/vfs
%attr(755,root,root) %{_libdir}/samba/vfs/acl_tdb.so
%attr(755,root,root) %{_libdir}/samba/vfs/acl_xattr.so
%attr(755,root,root) %{_libdir}/samba/vfs/aio_fork.so
%attr(755,root,root) %{_libdir}/samba/vfs/crossrename.so
%attr(755,root,root) %{_libdir}/samba/vfs/dirsort.so
%attr(755,root,root) %{_libdir}/samba/vfs/fileid.so
%attr(755,root,root) %{_libdir}/samba/vfs/linux_xfs_sgid.so
%attr(755,root,root) %{_libdir}/samba/vfs/preopen.so
%attr(755,root,root) %{_libdir}/samba/vfs/shadow_copy2.so
%attr(755,root,root) %{_libdir}/samba/vfs/smb_traffic_analyzer.so
%attr(755,root,root) %{_libdir}/samba/vfs/streams_depot.so
%attr(755,root,root) %{_libdir}/samba/vfs/streams_xattr.so
%attr(755,root,root) %{_libdir}/samba/vfs/syncops.so
%attr(755,root,root) %{_libdir}/samba/vfs/time_audit.so
%attr(755,root,root) %{_libdir}/samba/vfs/xattr_tdb.so
%{_datadir}/samba/setup
%{_mandir}/man8/vfs_acl_tdb.8*
%{_mandir}/man8/vfs_acl_xattr.8*
%{_mandir}/man8/vfs_crossrename.8*
%{_mandir}/man8/vfs_dirsort.8*
%{_mandir}/man8/vfs_fileid.8*
%{_mandir}/man8/vfs_preopen.8*
%{_mandir}/man8/vfs_shadow_copy2.8*
%{_mandir}/man8/vfs_smb_traffic_analyzer.8*
%{_mandir}/man8/vfs_streams_xattr.8*
%{_mandir}/man8/vfs_streams_depot.8*
%{_mandir}/man8/vfs_time_audit.8*
%{_mandir}/man8/vfs_xattr_tdb.8*


%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/samba/smbusers
%attr(754,root,root) /etc/rc.d/init.d/smb
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/samba
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/samba
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/samba
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.samba
%{_mandir}/man1/log2pcap.1*
%{_mandir}/man1/smbstatus.1*
%{_mandir}/man1/smbcontrol.1*
%{_mandir}/man5/smbpasswd.5*
%{_mandir}/man7/samba.7*
%{_mandir}/man8/nmbd.8*
%{_mandir}/man8/smbd.8*
%{_mandir}/man8/smbpasswd.8*

%dir %{_sambahome}
%dir /var/lib/samba
%ghost /var/lib/samba/*.dat
%dir /var/lib/samba/printing

%attr(750,root,root) %dir /var/log/samba
%attr(750,root,root) %dir /var/log/samba/cores
%attr(750,root,root) %dir /var/log/samba/cores/smbd
%attr(750,root,root) %dir /var/log/samba/cores/nmbd
%attr(750,root,root) %dir /var/log/archive/samba
%attr(1777,root,root) %dir /var/spool/samba
%if %{with ldap}
%doc examples/LDAP
%endif

%files winbind
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/winbindd
%attr(755,root,root) %{_bindir}/wbinfo
#%attr(755,root,root) %{_bindir}/wbinfo4
%attr(755,root,root) /%{_lib}/security/pam_winbind*
%attr(755,root,root) /%{_lib}/libnss_winbind*
%attr(754,root,root) /etc/rc.d/init.d/winbind
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/winbind
%{_mandir}/man1/wbinfo*.1*
%{_mandir}/man5/pam_winbind.conf.5*
%{_mandir}/man8/pam_winbind.8*
%{_mandir}/man8/winbindd*.8*

%files -n nss_wins
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_wins*

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nmblookup4
%attr(755,root,root) %{_bindir}/smbclient4
%attr(755,root,root) %{_bindir}/net
%attr(755,root,root) %{_bindir}/nmblookup
%attr(755,root,root) %{_bindir}/rpcclient
%attr(755,root,root) %{_bindir}/sharesec
%attr(755,root,root) %{_bindir}/smbcacls
%attr(755,root,root) %{_bindir}/smbclient
%attr(755,root,root) %{_bindir}/smbtree
%{_mandir}/man1/findsmb.1*
%{_mandir}/man1/nmblookup.1*
%{_mandir}/man1/rpcclient.1*
%{_mandir}/man1/sharesec.1*
%{_mandir}/man1/smbcacls.1*
%{_mandir}/man1/smbclient.1*
%{_mandir}/man1/smbtar.1*
%{_mandir}/man1/smbtree.1*
%{_mandir}/man8/net.8*

%files common
%defattr(644,root,root,755)
%doc README WHATSNEW.txt Roadmap
%dir %{_sysconfdir}/samba
%attr(664,root,fileshare) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/samba/smb.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/samba/lmhosts
%attr(755,root,root) %{_bindir}/eventlogadm
%attr(755,root,root) %{_bindir}/ntlm_auth
%attr(755,root,root) %{_bindir}/pdbedit
%attr(755,root,root) %{_bindir}/profiles
%attr(755,root,root) %{_bindir}/smbcquotas
%attr(755,root,root) %{_bindir}/testparm
%attr(755,root,root) %{_bindir}/vfstest
%dir %{_libdir}/samba
%dir %{_libdir}/samba/auth
%attr(755,root,root) %{_libdir}/samba/auth/script.so
%{_mandir}/man1/ntlm_auth.1*
%{_mandir}/man1/profiles.1*
%{_mandir}/man1/smbcquotas.1*
%{_mandir}/man1/testparm.1*
%{_mandir}/man1/vfstest.1*
#%{_mandir}/man1/log2pcap.1*
%{_mandir}/man5/lmhosts.5*
%{_mandir}/man5/smb.conf.5*
%{_mandir}/man8/pdbedit.8*
%{_mandir}/man8/eventlogadm.8*
%{_mandir}/man8/idmap_ad.8*
%{_mandir}/man8/idmap_hash.8*
%{_mandir}/man8/idmap_ldap.8*
%{_mandir}/man8/idmap_nss.8*
%{_mandir}/man8/idmap_rid.8*
%{_mandir}/man8/idmap_tdb.8*
%{_mandir}/man8/idmap_tdb2.8*

%if %{without system_libs}
%attr(755,root,root) %{_bindir}/tdbbackup
%attr(755,root,root) %{_bindir}/tdbdump
%attr(755,root,root) %{_bindir}/tdbtool
%attr(755,root,root) %{_libdir}/samba/libtalloc.so.*
%attr(755,root,root) %{_libdir}/samba/libtdb.so.*
%{_mandir}/man8/tdbbackup.8*
%{_mandir}/man8/tdbdump.8*
%{_mandir}/man8/tdbtool.8*
%endif


%files swat
%defattr(644,root,root,755)
#%doc swat/README* swat/help/*
%doc swat/help/*
%attr(755,root,root) %{_sbindir}/swat
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/swat
%dir %{_datadir}/samba/swat
%{_datadir}/samba/swat/help
%{_datadir}/samba/swat/images
%{_datadir}/samba/swat/include
%dir %{_datadir}/samba/swat/lang
%lang(ja) %{_datadir}/samba/swat/lang/ja
%lang(tr) %{_datadir}/samba/swat/lang/tr
%lang(de) %{_datadir}/samba/codepages/de.msg
%{_datadir}/samba/codepages/en.msg
%lang(fi) %{_datadir}/samba/codepages/fi.msg
%lang(fr) %{_datadir}/samba/codepages/fr.msg
%lang(it) %{_datadir}/samba/codepages/it.msg
%lang(ja) %{_datadir}/samba/codepages/ja.msg
%lang(nl) %{_datadir}/samba/codepages/nl.msg
%lang(pl) %{_datadir}/samba/codepages/pl.msg
%lang(ru) %{_datadir}/samba/codepages/ru.msg
%lang(tr) %{_datadir}/samba/codepages/tr.msg
%{_mandir}/man8/swat.8*

%files -n pam-pam_smbpass
%defattr(644,root,root,755)
%doc source3/pam_smbpass/{CHAN*,README,TODO} source3/pam_smbpass/samples
%attr(755,root,root) /%{_lib}/security/pam_smbpass.so

%files -n libsmbclient
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/libsmbclient.so.*
%attr(755,root,root) %{_libdir}/samba/libwbclient.so.*
%{_mandir}/man7/libsmbclient.7*

%files -n libsmbclient-devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/samba/libsmbclient.so
#%attr(755,root,root) %{_libdir}/samba/libwbclient.so
#%{_includedir}/libsmbclient.h
#%{_includedir}/wbclient.h

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_includedir}/samba-4.0

%files -n smbget
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smbget
%{_mandir}/man1/smbget.1*
%{_mandir}/man5/smbgetrc.5*

%if %{with cups}
%files -n cups-backend-smb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smbspool
%attr(755,root,root) %{cups_serverbin}/backend/smb
%{_mandir}/man8/smbspool.8*
%endif

%files vfs-audit
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/audit.so
%attr(755,root,root) %{_libdir}/samba/vfs/extd_audit.so
%attr(755,root,root) %{_libdir}/samba/vfs/full_audit.so
%{_mandir}/man8/vfs_audit.8*
%{_mandir}/man8/vfs_extd_audit.8*
%{_mandir}/man8/vfs_full_audit.8*

%files vfs-cap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/cap.so
%{_mandir}/man8/vfs_cap.8*

%files vfs-default_quota
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/default_quota.so
%{_mandir}/man8/vfs_default_quota.8*

%files vfs-expand_msdfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/expand_msdfs.so

%files vfs-fake_perms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/fake_perms.so
%{_mandir}/man8/vfs_fake_perms.8*

#%files vfs-notify_fam
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/samba/vfs/notify_fam.so
#%{_mandir}/man8/vfs_notify_fam.8*

%files vfs-netatalk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/netatalk.so
%{_mandir}/man8/vfs_netatalk.8*

%files vfs-readahead
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/readahead.so
%{_mandir}/man8/vfs_readahead.8*

%files vfs-readonly
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/readonly.so
%{_mandir}/man8/vfs_readonly.8*

%files vfs-recycle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/recycle.so
%{_mandir}/man8/vfs_recycle.8*

%files vfs-shadow_copy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/shadow_copy.so
%{_mandir}/man8/vfs_shadow_copy.8*

%files vfs-catia
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/catia.so
%{_mandir}/man8/vfs_catia.8*

%files vfs-scannedonly
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/samba/vfs/scannedonly.so
%{_mandir}/man8/vfs_scannedonly.8*

%if %{with ldap}
%files -n openldap-schema-samba
%defattr(644,root,root,755)
%{schemadir}/*.schema
%endif

%files -n python-samba4
%defattr(644,root,root,755)
%dir %{py_sitedir}/samba
%attr(755,root,root) %{py_sitedir}/samba/*.so
%{py_sitedir}/samba/*.py[co]
%dir %{py_sitedir}/samba/dcerpc
%{py_sitedir}/samba/dcerpc/*.py[co]
%attr(755,root,root) %{py_sitedir}/samba/dcerpc/*.so
%dir %{py_sitedir}/samba/external
%{py_sitedir}/samba/external/*.py[co]
%dir %{py_sitedir}/samba/external/subunit
%{py_sitedir}/samba/external/subunit/*.py[co]
%dir %{py_sitedir}/samba/external/subunit/tests
%{py_sitedir}/samba/external/subunit/tests/*.py[co]
%dir %{py_sitedir}/samba/external/testtools
%{py_sitedir}/samba/external/testtools/*.py[co]
%dir %{py_sitedir}/samba/external/testtools/testresult
%{py_sitedir}/samba/external/testtools/testresult/*.py[co]
%dir %{py_sitedir}/samba/external/testtools/tests
%{py_sitedir}/samba/external/testtools/tests/*.py[co]
%dir %{py_sitedir}/samba/netcmd
%{py_sitedir}/samba/netcmd/*.py[co]
%dir %{py_sitedir}/samba/provision
%{py_sitedir}/samba/provision/*.py[co]
%dir %{py_sitedir}/samba/samba3
%attr(755,root,root) %{py_sitedir}/samba/samba3/*.so
%{py_sitedir}/samba/samba3/*.py[co]
%dir %{py_sitedir}/samba/tests
%{py_sitedir}/samba/tests/*.py[co]
%dir %{py_sitedir}/samba/tests/blackbox
%{py_sitedir}/samba/tests/blackbox/*.py[co]
%dir %{py_sitedir}/samba/tests/samba_tool
%{py_sitedir}/samba/tests/samba_tool/*.py[co]
%dir %{py_sitedir}/samba/tests/dcerpc
%{py_sitedir}/samba/tests/dcerpc/*.py[co]
%dir %{py_sitedir}/samba/web_server
%{py_sitedir}/samba/web_server/*.py[co]
%if %{without system_libs}
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/tevent.py[co]
%endif
