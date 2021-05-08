%define	_fname	6050
%define	_module	6050
Summary:	Microcode image for Intel Centrino Wireless-N + WiMAX 6150, Advanced-N + WiMAX 6250
Summary(pl.UTF-8):	Obraz mikrokodu dla układów Intel Centrino Wireless-N + WiMAX 6150, Advanced-N + WiMAX 6250
Name:		iwlwifi-%{_module}-ucode
Version:	41.28.5.1
Release:	1
License:	distributable
Group:		Base/Kernel
# Source0:	http://wireless.kernel.org/en/users/Drivers/iwlwifi?action=AttachFile&do=get&target=iwlwifi-6050-ucode-%{version}.tgz
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/iwl6050-firmware/iwlwifi-6050-ucode-%{version}.tgz/cb484a65b9139666d4ddebf60598a87b/iwlwifi-6050-ucode-41.28.5.1.tgz
# Source0-md5:	cb484a65b9139666d4ddebf60598a87b
# Source1:	http://wireless.kernel.org/en/users/Drivers/iwlwifi?action=AttachFile&do=get&target=iwlwifi-6050-ucode-9.201.4.1.tgz
Source1:	http://pkgs.fedoraproject.org/repo/pkgs/iwl6050-firmware/iwlwifi-6050-ucode-9.201.4.1.tgz/12a663e415e76b6c46fcfecaa9f8e40b/iwlwifi-6050-ucode-9.201.4.1.tgz
# Source1-md5:	12a663e415e76b6c46fcfecaa9f8e40b
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The file provided in this package must be present on your system in
order for the Intel Centrino Wireless-N + WiMAX 6150 and Advanced-N +
WiMAX 6250 driver for Linux (iwlwifi-%{_module}) to operate on your
system.

On adapter initialization, and at varying times during the uptime of
the adapter, the microcode is loaded into the RAM on the network
adapter. The microcode provides the low level MAC features including
radio control and high precision timing events (backoff, transmit,
etc.) while also providing varying levels of packet filtering which
can be used to keep the host from having to handle packets that are
not of interest given the current operating mode of the device.

%description -l pl.UTF-8
Plik dostarczany przez ten pakiet jest wymagany w systemie do
działania linuksowego sterownika dla układów bezprzewodowych Intel
Centrino Wireless-N + WiMAX 6150 and Advanced-N + WiMAX 6250
(iwlwifi-%{_module}).

Przy inicjalizacji układu i w różnych chwilach w trakcie jego
działania mikrokod jest wczytywany do pamięci RAM układu. Mikrokod
udostępnia funkcje niskopoziomowe MAC, w tym sterowanie częścią
radiową i zdarzeniami wymagającymi dużej dokładności czasowej
(oczekiwania, transmisja itp.), a także różne poziomy filtrowania
pakietów, zapobiegające docieraniu do komputera pakietów
niepotrzebnych w danym trybie pracy urządzenia.

%prep
%setup -q -n iwlwifi-%{_fname}-ucode-%{version} -a1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install iwlwifi-%{_fname}-*.ucode iwlwifi-*/iwlwifi-%{_fname}-*.ucode $RPM_BUILD_ROOT/lib/firmware
install LICENSE.* $RPM_BUILD_ROOT/lib/firmware/%{name}-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.*
/lib/firmware/%{name}-LICENSE
/lib/firmware/iwlwifi-6050-*.ucode
