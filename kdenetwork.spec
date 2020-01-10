
Summary: KDE Network Applications
Name:    kdenetwork
Epoch:   7
Version: 4.10.5
Release: 8%{?dist}

License: GPLv2
URL:     http://www.kde.org
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz
Source1: krdc-icons.tar.bz2

# rhbz#540433 - KPPP is unable to add DNS entries to /etc/resolv.conf
Patch2: kdenetwork-4.3.3-resolv-conf-path.patch

# Fix build failure with g++4.7
Patch3: kdenetwork-4.7.97-fix-for-g++47.patch

# support USE_SYSTEM_IRIS build option
Patch4: kdenetwork-4.10.0-kopete_system_iris.patch

# disable skype protocol
Patch6: kdenetwork-4.10.5-disable-skype.patch

## upstreamable patches
Patch50: kdenetwork-4.9.5-libjingle_openssl.patch
Patch51: kdenetwork-4.10.4-krdc_icon.patch
Patch52: kdenetwork-4.10.5-kget-doc.patch
Patch53: kdenetwork-4.10.5-krdc-bz#1008890.patch

## upstream patches
Patch100: kdenetwork-4.10.5-freerdp.patch

## security patches
Patch1000: kdenetwork-4.10.5-CVE-2014-6055.patch

%if 0%{?fedora}
BuildRequires: openslp-devel
BuildRequires: pkgconfig(avahi-compat-libdns_sd)
BuildRequires: pkgconfig(libgadu) >= 1.8.0
BuildRequires: pkgconfig(libotr)
BuildRequires: libktorrent-devel
BuildRequires: pkgconfig(nxcl)
%global telepathy 1
BuildRequires: pkgconfig(TelepathyQt4)
BuildRequires: linphone-devel >= 2.3.0
%endif
BuildRequires: boost-devel
BuildRequires: expat-devel
BuildRequires: giflib-devel
BuildRequires: gmp-devel
# gnutls-devel is needed for rfbclient
BuildRequires: gnutls-devel
BuildRequires: gpgme-devel
# libkonq
BuildRequires: kde-baseapps-devel >= %{version}
BuildRequires: kde-workspace-devel >= %{version}
BuildRequires: kdepimlibs-devel >= %{version}
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(alsa) 
BuildRequires: pkgconfig(glib-2.0) 
BuildRequires: pkgconfig(jasper)
BuildRequires: pkgconfig(libidn) 
BuildRequires: pkgconfig(libmsn) 
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libstreamanalyzer) pkgconfig(libstreams)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(meanwhile)
BuildRequires: pkgconfig(ortp)
%if 0%{?use_system_iris:1}
BuildRequires: pkgconfig(iris) >= 2.0.0
%endif
BuildRequires: pkgconfig(qca2)
BuildRequires: pkgconfig(qimageblitz)
BuildRequires: pkgconfig(soprano)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libv4l2)
BuildRequires: libvncserver-devel
BuildRequires: openldap-devel
# freerdp support
BuildRequires: freerdp >= 1.0.2
#-----------------------------------------------------------------------------
#-- The following OPTIONAL packages could NOT be located on your system.
#-- Consider installing them to enable more features from this software.
#-----------------------------------------------------------------------------
#   * XMMS  <http://www.xmms.org>
#     X MultiMedia System development libraries
#     Used by the Kopete nowlistening plugin to support the XMMS player.

Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: %{name}-fileshare-samba = %{epoch}:%{version}-%{release}
Requires: %{name}-kdnssd = %{epoch}:%{version}-%{release}
Requires: %{name}-kget = %{epoch}:%{version}-%{release}
Requires: %{name}-kopete = %{epoch}:%{version}-%{release}
Requires: %{name}-krdc = %{epoch}:%{version}-%{release}
Requires: %{name}-krfb = %{epoch}:%{version}-%{release}

%description
Networking applications, including:
* kget: downloader manager
* kopete: chat client
* krdc: a client for Desktop Sharing and other VNC servers
* krfb: Desktop Sharing server, allow others to access your desktop via VNC

%package common 
Summary: Common files for %{name}
BuildArch: noarch
# when split occurred
Conflicts: kdenetwork < 7:4.6.95-10
Obsoletes: kdenetwork-libs < 7:4.6.95-10
%description common 
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: %{name}-kopete-devel = %{epoch}:%{version}-%{release}
Requires: %{name}-krdc-devel = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description devel
%{summary}.

%package fileshare-samba
Summary: Share files via samba 
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: samba
%description fileshare-samba 
%{summary}.

%package strigi-analyzers
Summary: meta information plugin for BitTorrent files
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description strigi-analyzers
%{summary}.

%package kdnssd
Summary: Kdnssd
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description kdnssd
%{summary}.

%package kget
Summary: A downloader manager 
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: %{name}-kget-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description kget
%{summary}.

%package kget-libs
Summary: Runtime libraries for %{name}
Requires: %{name}-kget = %{epoch}:%{version}-%{release}
%description kget-libs
%{summary}.

%package kopete
Summary: A chat client 
Requires: %{name}-kopete-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: kate-part >= %{version}
Requires: mozilla-filesystem
# jabber
Requires: qca-ossl%{?_isa}
%description kopete
%{summary}.

%package kopete-libs
Summary: Runtime libraries for %{name}
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: %{name}-kopete = %{epoch}:%{version}-%{release}
%description kopete-libs
%{summary}.

%package kopete-devel
Summary: Development files for Kopete
Requires: %{name}-kopete-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: kdelibs4-devel
%description kopete-devel
%{summary}.

%package krdc
Summary: A client for Desktop Sharing and other VNC servers
Requires: %{name}-krdc-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: freerdp
%description krdc
%{summary}.

%package krdc-libs
Summary: Runtime libraries for %{name} 
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: %{name}-krdc = %{epoch}:%{version}-%{release}
%description krdc-libs
%{summary}.

%package krdc-devel
Summary: Developer files for %{name} 
Requires: %{name}-krdc-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: kdelibs4-devel
%description krdc-devel
%{summary}.

%package krfb
Summary: Desktop Sharing server, allow others to access your desktop via VNC 
Requires: %{name}-krfb-libs%{?_isa} = %{epoch}:%{version}-%{release}
# https://bugzilla.redhat.com/655844
Provides: bundled(libvncserver)
%description krfb
%{summary}.

%package krfb-libs
Summary: Runtime libraries for %{name}
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: %{name}-krfb = %{epoch}:%{version}-%{release}
%description krfb-libs
%{summary}.



%prep
%setup -q -n kdenetwork-%{version} -a1
%patch2 -p1 -b .resolv-conf-path
%patch3 -p1 -b .fix-for-g++47
%patch4 -p1 -b .kopete_system_iris
%patch6 -p1 -b .disable-skype

%patch50 -p1 -b .libjingle_openssl
%patch51 -p1 -b .krdc_icon
%patch52 -p1 -b .doc
%patch53 -p1 -b .krdc-bz#1008890
%patch100 -p1 -b .freerdp
%patch1000 -p1 -b .2014-6055

%if 0%{?use_system_iris:1}
mv kopete/protocols/jabber/libiris \
   kopete/protocols/jabber/libiris.BAK
%endif

%if 0%{?rhel}
sed -i 's|macro_optional_add_subdirectory( kdenetwork-strigi-analyzers )|#macro_optional_add_subdirectory( kdenetwork-strigi-analyzers )|g' CMakeLists.txt
sed -i 's|macro_optional_add_subdirectory( kppp )|#macro_optional_add_subdirectory( kppp )|g' CMakeLists.txt
%endif

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  -DWITH_JINGLE=TRUE \
  -DMOZPLUGIN_INSTALL_DIR=%{_libdir}/mozilla/plugins \
  %{?use_system_iris:-DUSE_SYSTEM_IRIS:BOOL=ON} \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# fix documentation multilib conflict in index.cache
for f in kget kopete krdc krfb; do
   if [ -f %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache.bz2 ] ; then
     bunzip2 %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache.bz2
     sed -i -e 's!name="id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
     sed -i -e 's!#id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
     bzip2 -9 %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
   fi
done

%find_lang kget --with-kde --without-mo
%find_lang kopete --with-kde --without-mo
%find_lang krdc --with-kde --without-mo
%find_lang krfb --with-kde --without-mo

# unpackaged files
rm -f %{buildroot}%{_kde4_libdir}/libkgetcore.so


%check
for f in %{buildroot}%{_kde4_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate $f
done


%files
# blank

%files devel
# blank

%files common
#doc README COPYING*

%files fileshare-samba
%{_kde4_libdir}/kde4/sambausershareplugin.so
%{_kde4_datadir}/kde4/services/sambausershareplugin.desktop

%if 0%{?fedora}
%files strigi-analyzers
%{_kde4_libdir}/strigi/strigita_torrent_analyzer.so
%endif

%files kdnssd
%{_kde4_datadir}/kde4/services/zeroconf.protocol
%{_kde4_datadir}/kde4/services/kded/dnssdwatcher.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml
%dir %{_kde4_appsdir}/remoteview/
%{_kde4_appsdir}/remoteview/zeroconf.desktop
%{_kde4_libdir}/kde4/kded_dnssdwatcher.so
%{_kde4_libdir}/kde4/kio_zeroconf.so

%post kget
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:

%posttrans kget
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:
update-desktop-database -q &> /dev/null ||:

%postun kget
if [ $1 -eq 0 ] ; then
  touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:
  gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:
  update-desktop-database -q &> /dev/null ||:
fi

%files kget -f kget.lang
%{_kde4_bindir}/kget
%{_kde4_appsdir}/dolphinpart/kpartplugins/kget_plug_in.*
%{_kde4_appsdir}/kget/
%{_kde4_appsdir}/kconf_update/kget*
%{_kde4_appsdir}/khtml/kpartplugins/kget_plug_in.*
%{_kde4_appsdir}/kwebkitpart/kpartplugins/kget_plug_in.*
%{_kde4_iconsdir}/hicolor/*/apps/kget.*
%{_datadir}/dbus-1/services/org.kde.kget.service
%{_kde4_datadir}/applications/kde4/kget.desktop
%{_kde4_datadir}/kde4/services/kget*.desktop
%{_kde4_datadir}/kde4/services/plasma-engine-kget.desktop
%{_kde4_datadir}/kde4/services/plasma-runner-kget.desktop
%{_kde4_datadir}/kde4/servicetypes/kget*.desktop
%{_kde4_datadir}/config.kcfg/kget*.kcfg
%{_kde4_datadir}/ontology/kde/kget*
%{_kde4_libdir}/kde4/kget_*.so
%{_kde4_datadir}/kde4/services/ServiceMenus/kget_download.desktop
%{_kde4_libdir}/kde4/kcm_kget_*.so
%{_kde4_libdir}/kde4/krunner_kget.so
%{_kde4_libdir}/kde4/plasma_engine_kget.so
%{_kde4_libdir}/kde4/plasma_kget_barapplet.so
%{_kde4_libdir}/kde4/plasma_kget_piechart.so

%post kget-libs -p /sbin/ldconfig
%postun kget-libs -p /sbin/ldconfig

%files kget-libs
%{_kde4_libdir}/libkgetcore.so.4*

%post kopete 
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null ||:

%posttrans kopete 
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null ||:
update-desktop-database -q &> /dev/null ||:

%postun kopete
if [ $1 -eq 0 ] ; then
  touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:
  touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null ||:
  gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:
  gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null ||:
  update-desktop-database -q &> /dev/null ||:
fi

%files kopete -f kopete.lang
%if 0%{?fedora}
%{_kde4_bindir}/googletalk-call
%endif
%{_kde4_bindir}/kopete
%{_kde4_bindir}/winpopup*
%{_kde4_appsdir}/kopete*
%{_kde4_appsdir}/kconf_update/kopete*
%{_kde4_configdir}/kopeterc
%{_datadir}/dbus-1/interfaces/org.kde.Kopete.xml
%{_datadir}/dbus-1/interfaces/org.kde.kopete.*.xml
%{_kde4_datadir}/applications/kde4/kopete.desktop
%{_kde4_datadir}/config.kcfg/kopete*
%{_kde4_datadir}/sounds/Kopete_*
%{_kde4_datadir}/sounds/KDE-Im-Phone-Ring.wav
%{_kde4_datadir}/kde4/services/aim.protocol
%{_kde4_datadir}/kde4/services/chatwindow.desktop
%{_kde4_datadir}/kde4/services/emailwindow.desktop
%{_kde4_datadir}/kde4/services/kopete_*.desktop
%{_kde4_datadir}/kde4/services/kconfiguredialog/
%{_kde4_datadir}/kde4/services/xmpp.protocol
%{_kde4_datadir}/kde4/servicetypes/kopete*.desktop
%{_kde4_iconsdir}/hicolor/*/apps/kopete*.*
%{_kde4_iconsdir}/oxygen/*/actions/*
%if 0%{?fedora}
%{_kde4_iconsdir}/oxygen/*/status/object-locked*.*
%endif
%{_kde4_libdir}/kde4/kopete_*.so
%{_kde4_libdir}/kde4/kcm_kopete_*.so
%{_kde4_libdir}/libqgroupwise.so
%{_kde4_bindir}/kopete_latexconvert.sh
%{_kde4_libdir}/kde4/libchattexteditpart.so
%{_kde4_datadir}/config.kcfg/historyconfig.kcfg
%{_kde4_datadir}/config.kcfg/latexconfig.kcfg
%{_kde4_datadir}/config.kcfg/nowlisteningconfig.kcfg
%{_kde4_datadir}/config.kcfg/translatorconfig.kcfg
%{_kde4_datadir}/config.kcfg/urlpicpreview.kcfg
%{_kde4_datadir}/config.kcfg/webpresenceconfig.kcfg

%post kopete-libs -p /sbin/ldconfig
%postun kopete-libs -p /sbin/ldconfig

%files kopete-libs
%{_kde4_libdir}/kde4/plugins/accessible/
%{_kde4_libdir}/libkopete*.so.*
%{_kde4_libdir}/libkyahoo.so*
%{_kde4_libdir}/liboscar.so*

%files kopete-devel
%{_kde4_includedir}/kopete/
%{_kde4_libdir}/libkopete*.so

%post krdc
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:

%posttrans krdc
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:

%postun krdc
if [ $1 -eq 0 ] ; then
  touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:
  gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:
fi

%files krdc -f krdc.lang
%{_kde4_bindir}/krdc
%{_kde4_appsdir}/krdc/
%{_kde4_datadir}/applications/kde4/krdc.desktop
%{_kde4_datadir}/kde4/services/krdc_*.desktop
%{_kde4_datadir}/kde4/services/rdp.protocol
%{_kde4_datadir}/kde4/services/vnc.protocol
%{_kde4_datadir}/kde4/servicetypes/krdc*.desktop
%{_kde4_iconsdir}/hicolor/*/apps/krdc.*
%{_kde4_libdir}/kde4/kcm_krdc*.so
%{_kde4_datadir}/kde4/services/ServiceMenus/smb2rdc.desktop
%{_kde4_datadir}/config.kcfg/krdc.kcfg
%{_kde4_libdir}/kde4/krdc_*.so
%if 0%{?telepathy:1}
%{_kde4_bindir}/krdc_rfb_approver
%{_kde4_appsdir}/krdc_rfb_approver/
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.krdc_rfb_approver.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.krdc_rfb_handler.service
%{_datadir}/telepathy/clients/krdc_rfb_approver.client
%{_datadir}/telepathy/clients/krdc_rfb_handler.client
%endif

%post krdc-libs -p /sbin/ldconfig
%postun krdc-libs -p /sbin/ldconfig

%files krdc-libs
%{_kde4_libdir}/libkrdccore.so.4*

%files krdc-devel
%{_kde4_includedir}/krdc/
%{_kde4_libdir}/libkrdccore.so

%files krfb -f krfb.lang
%{_kde4_bindir}/krfb
%{_kde4_appsdir}/krfb/
%{_kde4_datadir}/applications/kde4/krfb.desktop
%{_kde4_datadir}/kde4/services/krfb_*.desktop
%{_kde4_datadir}/kde4/servicetypes/krfb*.desktop
%{_kde4_libdir}/kde4/krfb_*.so
%if 0%{?telepathy:1}
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.krfb_rfb_handler.service
%{_datadir}/telepathy/clients/krfb_rfb_handler.client
%endif

%post krfb-libs -p /sbin/ldconfig
%postun krfb-libs -p /sbin/ldconfig

%files krfb-libs
%{_kde4_libdir}/libkrfbprivate.so.4*


%changelog
* Fri Oct 31 2014 Than Ngo <than@redhat.com> - 7:4.10.5-8
- Resolves: CVE-2014-6055

* Tue Jan 28 2014 Daniel Mach <dmach@redhat.com> - 7:4.10.5-7
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 7:4.10.5-6
- Mass rebuild 2013-12-27

* Tue Oct 29 2013 Jan Grulich <jgrulich@redhat.com> - 7:4.10.5-5
- Do not crash if closing one of two vnc connection to the same server
- Resolves #1008890

* Fri Aug 30 2013 Than Ngo <than@redhat.com> - 7:4.10.5-4
- fix dep issue

* Thu Jul 18 2013 Than Ngo <than@redhat.com> - 7:4.10.5-3
- disable skype protocol

* Wed Jul 10 2013 Than Ngo <than@redhat.com> - 7:4.10.5-2
- drop kppp

* Thu Jul 04 2013 Than Ngo <than@redhat.com> - 7:4.10.5-1
- 4.10.5

* Thu Jun 27 2013 Than Ngo <than@redhat.com> - 7:4.10.4-2
- backport freerdp support 

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 7:4.10.4-1
- 4.10.4
- kopete-4.10.3-1 does not connect to Google Talk (#963310)

* Mon May 06 2013 Than Ngo <than@redhat.com> - 7: 4.10.3-1
- 4.10.3
- enable use_system_iris for all Fedora releases
- BR pkgconfig(iris) >= 2.0.0

* Thu May 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 7:4.10.2-6
- try use_system_iris again (#737305)

* Wed May 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 7:4.10.2-5
- revert use_system_iris, needs more work

* Wed May 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 7:4.10.2-4
- use system iris (#737305, f20+ only for now)
- .spec cleanup

* Mon Apr 29 2013 Than Ngo <than@redhat.com> - 7:4.10.2-3
- build kppp with -fno-strict-aliasing
- fix multilib issue

* Fri Apr 05 2013 Than Ngo <than@redhat.com> - 7:4.10.2-2
- fix rhel condition

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 7:4.10.2-1
- 4.10.2
- kopete FTBFS against recent kernels, uses deprecated v4l interfaces (#946924)

* Thu Mar 07 2013 Rex Dieter <rdieter@fedoraproject.org> 7:4.10.1-2
- KGet 4.10 deletes home (kde#316086)

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 7:4.10.1-1
- 4.10.1

* Mon Feb 11 2013 Rex Dieter <rdieter@fedoraproject.org> 7:4.10.0-3
- support USE_SYSTEM_IRIS build option (not used, yet...)

* Mon Feb 04 2013 Rex Dieter <rdieter@fedoraproject.org> 7:4.10.0-2
- Unowned directory /usr/share/kde4/apps/krdc_rfb_approver/ (#907664)

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 7:4.10.0-1
- 4.10.0

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 7:4.9.98-1
- 4.9.98

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 7:4.9.97-2
- rebuild due to "jpeg8-ABI" feature drop

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 7:4.9.97-1
- 4.9.97

* Sat Dec 29 2012 Rex Dieter <rdieter@fedoraproject.org> 7:4.9.95-2
- BR: linphone-devel

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 7:4.9.95-1
- 4.9.95

* Wed Dec 05 2012 Rex Dieter <rdieter@fedoraproject.org> - 7:4.9.90-2
- BR: strigi-devel
- BR: telepathy-qt4-devel

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 7:4.9.90-1
- 4.9.90

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 7:4.9.3-1
- 4.9.3

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> - 7:4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 7:4.9.1-1
- 4.9.1

* Tue Aug 21 2012 Than Ngo <than@redhat.com> - 7:4.9.0-3
- add rhel/fedora condition

* Wed Aug 15 2012 Alexey Kurov <nucleo@fedoraproject.org> 7:4.9.0-2
- rebuild for libktorrent-1.3rc1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 7:4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7:4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 7:4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 7:4.8.95-1
- 4.8.95

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 7:4.8.90-1
- 4.8.90

* Sun Jun 03 2012 Jaroslav Reznik <jreznik@redhat.com> - 7:4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 7:4.8.3-1
- 4.8.3

* Thu Apr 19 2012 Than Ngo <than@redhat.com> - 4.8.2-2
- add BR gnutls-devel, it's needed for rfbclient

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.2-1
- 4.8.2

* Thu Mar 08 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-1.1
- rebuild (libktorrent)

* Mon Mar 05 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-1
- 4.8.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7:4.8.0-2
- Rebuilt for c++ ABI breakage

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 7:4.8.0-1
- 4.8.0

* Sat Jan  7 2012 Alexey Kurov <nucleo@fedoraproject.org> 7:4.7.97-3
- rebuild for libktorrent-1.2rc1

* Thu Jan 05 2012 Radek Novacek <rnovacek@redhat.com> 7:4.7.97-2
- Fix the patch for g++ 4.7

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 7:4.7.97-1
- 4.7.97
- Fix build failure with g++ 4.7

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 7:4.7.95-1
- 4.7.95

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> - 7:4.7.90-1
- 4.7.90

* Fri Dec 02 2011 Than Ngo <than@redhat.com> - 7:4.7.80-3
- fix rhel/fedora condition

* Mon Nov 28 2011 Jaroslav Reznik <jreznik@redhat.com> 7:4.7.80-2
- move a11y kopete plugin to -libs

* Mon Nov 28 2011 Jaroslav Reznik <jreznik@redhat.com> 7:4.7.80-1
- 4.7.80 (beta 1)

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.7.3-1
- 4.7.3
- pkgconfig-style deps

* Sat Oct 08 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.7.2-2
- -kopete: build unconditionally, Requires: kate-part

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.7.2-1
- 4.7.2

* Wed Sep 07 2011 Than Ngo <than@redhat.com> - 7:4.7.1-1
- 4.7.1

* Thu Aug 11 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.7.0-4
- -krfb-libs: Requires: -krfb (not main pkg)

* Fri Aug 05 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.7.0-3
- kdenetwork(kopete) FTBFS against qt-4.8.0-beta1 (#724846)

* Fri Aug 05 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.7.0-2
- -common: Obsoletes: kdenetwork-libs

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> 7:4.7.0-1
- 4.7.0
- omit FTBFS kopete for now (#724846)

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.6.95-10
- kdenetwork split packaging (#724053)

* Mon Jul 11 2011 Jaroslav Reznik <jreznik@redhat.com> 7:4.6.95-1
- 4.6.95 (rc2)

* Mon Jun 27 2011 Radek Novacek <rnovacek@redhat.com> 7:4.6.90-1
- Update to 4.6.90

* Mon Jun 27 2011 Radek Novacek <rnovacek@redhat.com> 7:4.6.80-1
- Update to 4.6.80

* Fri Apr 29 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.6.3-1
- 4.6.3

* Wed Apr 20 2011 Than Ngo <than@redhat.com> - 7:4.6.2-2
- security fix for CVE-2010-1000

* Wed Apr 06 2011 Than Ngo <than@redhat.com> - 7:4.6.2-1
- 4.6.2

* Wed Mar 16 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.6.1-3
- make qca-ossl dep arch'd
- drop some ancient Obsoletes/Provides

* Thu Mar 03 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.6.1-2
- respin tarball

* Mon Feb 28 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.6.1-1
- 4.6.1

* Thu Feb 10 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 7:4.6.0-3
- drop v4l1 support from Kopete, keep v4l2 (F15+, fixes FTBFS, patch by nucleo)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7:4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Jaroslav Reznik <jreznik@redhat.com> - 7:4.6.0-1
- 4.6.0

* Sun Jan 09 2011 Rex Dieter <rdieter@fedoraproject.org> 7:4.5.95-2
- BR: expat-devel kdebase-devel kdebase-workspace-devel libvncserver-devel nxcl-devel

* Thu Jan 06 2011 Jaroslav Reznik <jreznik@redhat.com> 7:4.5.95-1
- 4.5.95 (4.6rc2)

* Fri Dec 31 2010 Alexey Kurov <nucleo@fedoraproject.org> 7:4.5.90-3
- patch for building against both libktorrent 1.1 and 1.0.x

* Thu Dec 30 2010 Alexey Kurov <nucleo@fedoraproject.org> 7:4.5.90-2
- rebuild for libktorrent-1.1beta1
- drop libktorrent_stable patch

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 7:4.5.90-1
- 4.5.90 (4.6rc1)

* Wed Dec 08 2010 Thomas Janssen <thomasj@fedoraproject.org> 7:4.5.85-2
- respun upstream tarball

* Sat Dec 04 2010 Thomas Janssen <thomasj@fedoraproject.org> 7:4.5.85-1
- 4.5.85 (4.6beta2)

* Mon Nov 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 7:4.5.80-2
- reenable KGet libktorrent support and make it build

* Sun Nov 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 7:4.5.80-1
- 4.5.80 (4.6beta)

* Fri Nov 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 7:4.5.3-3
- Kopete ICQ Plugin complains about wrong password (kde#257008)

* Fri Nov 05 2010 Thomas Janssen <thomasj@fedoraproject.org> - 7:4.5.3-2
- rebuild for new libxml2

* Sun Oct 31 2010 Than Ngo <than@redhat.com> - 7:4.5.3-1
- 4.5.3

* Sat Oct 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 7:4.5.2-1
- 4.5.2

* Fri Aug 27 2010 Jaroslav Reznik <jreznik@redhat.com> - 7:4.5.1-1
- 4.5.1

* Tue Aug 03 2010 Than Ngo <than@redhat.com> - 7:4.5.0-1
- 4.5.0
