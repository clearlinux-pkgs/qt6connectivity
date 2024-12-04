#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
Name     : qt6connectivity
Version  : 6.8.0
Release  : 22
URL      : https://download.qt.io/official_releases/qt/6.8/6.8.0/submodules/qtconnectivity-everywhere-src-6.8.0.zip
Source0  : https://download.qt.io/official_releases/qt/6.8/6.8.0/submodules/qtconnectivity-everywhere-src-6.8.0.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6connectivity-lib = %{version}-%{release}
Requires: qt6connectivity-libexec = %{version}-%{release}
Requires: qt6connectivity-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(libpcsclite)
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# HeartRateGame #
Demonstrates how to check a Bluetooth-connection, discover LE-devices, connect
to devices, discover services and finally connect to a heartrate-service.
The purpose of the game is increase the heartrate so much as possible in 60s.
Relax before starting the game. Don't be too nervous, it increases the heartrate!

%package dev
Summary: dev components for the qt6connectivity package.
Group: Development
Requires: qt6connectivity-lib = %{version}-%{release}
Provides: qt6connectivity-devel = %{version}-%{release}
Requires: qt6connectivity = %{version}-%{release}

%description dev
dev components for the qt6connectivity package.


%package lib
Summary: lib components for the qt6connectivity package.
Group: Libraries
Requires: qt6connectivity-libexec = %{version}-%{release}
Requires: qt6connectivity-license = %{version}-%{release}

%description lib
lib components for the qt6connectivity package.


%package libexec
Summary: libexec components for the qt6connectivity package.
Group: Default
Requires: qt6connectivity-license = %{version}-%{release}

%description libexec
libexec components for the qt6connectivity package.


%package license
Summary: license components for the qt6connectivity package.
Group: Default

%description license
license components for the qt6connectivity package.


%prep
%setup -q -n qtconnectivity-everywhere-src-6.8.0
cd %{_builddir}/qtconnectivity-everywhere-src-6.8.0
pushd ..
cp -a qtconnectivity-everywhere-src-6.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732612804
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1732612804
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6connectivity
cp %{_builddir}/qtconnectivity-everywhere-src-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/qt6connectivity/1c619b057a9bf7a8234b3105fcfb5b375e749db1 || :
cp %{_builddir}/qtconnectivity-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6connectivity/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qtconnectivity-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6connectivity/dc8f2e570bf431427dbc3bab9d4d551b53a60208 || :
cp %{_builddir}/qtconnectivity-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6connectivity/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
cp %{_builddir}/qtconnectivity-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6connectivity/c70af14df11e3908dfc10397b1ba4b1f346661f3 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/adapter1_bluez5_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/battery1_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/bluetoothmanagement_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/bluez5_helper_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/bluez_data_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/bluezperipheralapplication_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/bluezperipheralconnectionmanager_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/bluezperipheralobjects_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/device1_bluez5_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/gattchar1_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/gattcharacteristic1adaptor_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/gattdesc1_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/gattdescriptor1adaptor_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/gattmanager1_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/gattservice1_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/gattservice1adaptor_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/hcimanager_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/leadvertisement1_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/leadvertisingmanager1_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/lecmaccalculator_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/objectmanager_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/objectmanageradaptor_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/profile1_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/profile1context_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/profilemanager1_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/properties_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/propertiesadaptor_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothdevicediscoveryagent_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothdeviceinfo_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothhostinfo_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothlocaldevice_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothserver_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothservicediscoveryagent_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothserviceinfo_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothsocket_bluez_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothsocket_bluezdbus_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qbluetoothsocketbase_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qleadvertiser_bluez_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qleadvertiser_bluezdbus_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qlowenergycontroller_bluez_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qlowenergycontroller_bluezdbus_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qlowenergycontrollerbase_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qlowenergyserviceprivate_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qprivatelinearbuffer_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qtbluetooth-config_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/qtbluetoothglobal_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/remotedevicemanager_p.h
/usr/include/QtBluetooth/6.8.0/QtBluetooth/private/servicemap_p.h
/usr/include/QtBluetooth/QBluetoothAddress
/usr/include/QtBluetooth/QBluetoothDeviceDiscoveryAgent
/usr/include/QtBluetooth/QBluetoothDeviceInfo
/usr/include/QtBluetooth/QBluetoothHostInfo
/usr/include/QtBluetooth/QBluetoothLocalDevice
/usr/include/QtBluetooth/QBluetoothServer
/usr/include/QtBluetooth/QBluetoothServiceDiscoveryAgent
/usr/include/QtBluetooth/QBluetoothServiceInfo
/usr/include/QtBluetooth/QBluetoothSocket
/usr/include/QtBluetooth/QBluetoothUuid
/usr/include/QtBluetooth/QLowEnergyAdvertisingData
/usr/include/QtBluetooth/QLowEnergyAdvertisingParameters
/usr/include/QtBluetooth/QLowEnergyCharacteristic
/usr/include/QtBluetooth/QLowEnergyCharacteristicData
/usr/include/QtBluetooth/QLowEnergyConnectionParameters
/usr/include/QtBluetooth/QLowEnergyController
/usr/include/QtBluetooth/QLowEnergyDescriptor
/usr/include/QtBluetooth/QLowEnergyDescriptorData
/usr/include/QtBluetooth/QLowEnergyHandle
/usr/include/QtBluetooth/QLowEnergyService
/usr/include/QtBluetooth/QLowEnergyServiceData
/usr/include/QtBluetooth/QtBluetooth
/usr/include/QtBluetooth/QtBluetoothDepends
/usr/include/QtBluetooth/QtBluetoothVersion
/usr/include/QtBluetooth/qbluetooth.h
/usr/include/QtBluetooth/qbluetoothaddress.h
/usr/include/QtBluetooth/qbluetoothdevicediscoveryagent.h
/usr/include/QtBluetooth/qbluetoothdeviceinfo.h
/usr/include/QtBluetooth/qbluetoothhostinfo.h
/usr/include/QtBluetooth/qbluetoothlocaldevice.h
/usr/include/QtBluetooth/qbluetoothserver.h
/usr/include/QtBluetooth/qbluetoothservicediscoveryagent.h
/usr/include/QtBluetooth/qbluetoothserviceinfo.h
/usr/include/QtBluetooth/qbluetoothsocket.h
/usr/include/QtBluetooth/qbluetoothuuid.h
/usr/include/QtBluetooth/qlowenergyadvertisingdata.h
/usr/include/QtBluetooth/qlowenergyadvertisingparameters.h
/usr/include/QtBluetooth/qlowenergycharacteristic.h
/usr/include/QtBluetooth/qlowenergycharacteristicdata.h
/usr/include/QtBluetooth/qlowenergyconnectionparameters.h
/usr/include/QtBluetooth/qlowenergycontroller.h
/usr/include/QtBluetooth/qlowenergydescriptor.h
/usr/include/QtBluetooth/qlowenergydescriptordata.h
/usr/include/QtBluetooth/qlowenergyservice.h
/usr/include/QtBluetooth/qlowenergyservicedata.h
/usr/include/QtBluetooth/qtbluetooth-config.h
/usr/include/QtBluetooth/qtbluetoothexports.h
/usr/include/QtBluetooth/qtbluetoothglobal.h
/usr/include/QtBluetooth/qtbluetoothversion.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qapduutils_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qndefaccessfsm_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qndefnfcsmartposterrecord_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qndefrecord_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qnearfieldmanager_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qnearfieldmanager_pcsc_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qnearfieldtarget_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qnearfieldtarget_pcsc_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qnfctagtype4ndeffsm_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qpcsc_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qpcsccard_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qpcscmanager_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qpcscslot_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qtnfc-config_p.h
/usr/include/QtNfc/6.8.0/QtNfc/private/qtnfcglobal_p.h
/usr/include/QtNfc/QNdefFilter
/usr/include/QtNfc/QNdefMessage
/usr/include/QtNfc/QNdefNfcIconRecord
/usr/include/QtNfc/QNdefNfcSmartPosterRecord
/usr/include/QtNfc/QNdefNfcTextRecord
/usr/include/QtNfc/QNdefNfcUriRecord
/usr/include/QtNfc/QNdefRecord
/usr/include/QtNfc/QNearFieldManager
/usr/include/QtNfc/QNearFieldTarget
/usr/include/QtNfc/QtNfc
/usr/include/QtNfc/QtNfcDepends
/usr/include/QtNfc/QtNfcVersion
/usr/include/QtNfc/qndeffilter.h
/usr/include/QtNfc/qndefmessage.h
/usr/include/QtNfc/qndefnfcsmartposterrecord.h
/usr/include/QtNfc/qndefnfctextrecord.h
/usr/include/QtNfc/qndefnfcurirecord.h
/usr/include/QtNfc/qndefrecord.h
/usr/include/QtNfc/qnearfieldmanager.h
/usr/include/QtNfc/qnearfieldtarget.h
/usr/include/QtNfc/qtnfc-config.h
/usr/include/QtNfc/qtnfcexports.h
/usr/include/QtNfc/qtnfcglobal.h
/usr/include/QtNfc/qtnfcversion.h
/usr/lib64/cmake/Qt6/FindBlueZ.cmake
/usr/lib64/cmake/Qt6/FindPCSCLITE.cmake
/usr/lib64/cmake/Qt6Bluetooth/Qt6BluetoothAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Bluetooth/Qt6BluetoothConfig.cmake
/usr/lib64/cmake/Qt6Bluetooth/Qt6BluetoothConfigVersion.cmake
/usr/lib64/cmake/Qt6Bluetooth/Qt6BluetoothConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Bluetooth/Qt6BluetoothDependencies.cmake
/usr/lib64/cmake/Qt6Bluetooth/Qt6BluetoothTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Bluetooth/Qt6BluetoothTargets.cmake
/usr/lib64/cmake/Qt6Bluetooth/Qt6BluetoothVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6Bluetooth/Qt6BluetoothVersionlessTargets.cmake
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtConnectivityTestsConfig.cmake
/usr/lib64/cmake/Qt6Nfc/Qt6NfcAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Nfc/Qt6NfcConfig.cmake
/usr/lib64/cmake/Qt6Nfc/Qt6NfcConfigVersion.cmake
/usr/lib64/cmake/Qt6Nfc/Qt6NfcConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Nfc/Qt6NfcDependencies.cmake
/usr/lib64/cmake/Qt6Nfc/Qt6NfcTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Nfc/Qt6NfcTargets.cmake
/usr/lib64/cmake/Qt6Nfc/Qt6NfcVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6Nfc/Qt6NfcVersionlessTargets.cmake
/usr/lib64/libQt6Bluetooth.prl
/usr/lib64/libQt6Bluetooth.so
/usr/lib64/libQt6Nfc.prl
/usr/lib64/libQt6Nfc.so
/usr/lib64/pkgconfig/Qt6Bluetooth.pc
/usr/lib64/pkgconfig/Qt6Nfc.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_bluetooth.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_bluetooth_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_nfc.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_nfc_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6Bluetooth.so.6.8.0
/V3/usr/lib64/libQt6Nfc.so.6.8.0
/usr/lib64/libQt6Bluetooth.so.6
/usr/lib64/libQt6Bluetooth.so.6.8.0
/usr/lib64/libQt6Nfc.so.6
/usr/lib64/libQt6Nfc.so.6.8.0
/usr/lib64/qt6/metatypes/qt6bluetooth_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6nfc_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/Bluetooth.json
/usr/lib64/qt6/modules/Nfc.json

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/sdpscanner
/usr/libexec/sdpscanner

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6connectivity/1c619b057a9bf7a8234b3105fcfb5b375e749db1
/usr/share/package-licenses/qt6connectivity/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6connectivity/79453f55fa8ee32d7b95581473edcbfd043e088f
/usr/share/package-licenses/qt6connectivity/c70af14df11e3908dfc10397b1ba4b1f346661f3
/usr/share/package-licenses/qt6connectivity/dc8f2e570bf431427dbc3bab9d4d551b53a60208
