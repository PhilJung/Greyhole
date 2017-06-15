Name:           greyhole
Version:        $VERSION
Release:        $BUILD_NUMBER
Summary:        Greyhole is a drive pooling technology for Samba
Group:          System Environment/Daemons
Source:         http://greyhole.googlecode.com/files/%{name}-%{version}.tar.gz
License:        GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       samba >= 3.4.3, php-cli >= 5, php-pdo, php-mysql, php-mbstring, php-intl, rsync, sysstat, lsof

%description
Greyhole allows you to create a storage pool, accessible from 
Samba shares, that offers data redundancy and JBOD concatenation.

%define debug_package %{nil}

%prep
%setup -q

%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/usr/share/greyhole/web-app/
mkdir -p $RPM_BUILD_ROOT/usr/share/greyhole/scripts-examples/
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1/
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man5/

install -m 0755 -D -p greyhole ${RPM_BUILD_ROOT}%{_bindir}
install -m 0755 -D -p greyhole-dfree ${RPM_BUILD_ROOT}%{_bindir}
install -m 0755 -D -p greyhole-php ${RPM_BUILD_ROOT}%{_bindir}
install -m 0755 -D -p greyhole-dfree.php ${RPM_BUILD_ROOT}/usr/share/greyhole/
install -m 0755 -D -p greyhole-custom-cp.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/

install -m 0644 -D -p schema-mysql.sql ${RPM_BUILD_ROOT}/usr/share/greyhole/
install -m 0644 -D -p greyhole.example.conf ${RPM_BUILD_ROOT}/usr/share/greyhole/

install -m 0644 -D -p greyhole.example.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/greyhole.conf
install -m 0755 -D -p initd_script.sh ${RPM_BUILD_ROOT}/etc/rc.d/init.d/greyhole
install -m 0644 -D -p logrotate.greyhole ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/greyhole
install -m 0644 -D -p greyhole.cron.d ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.d/greyhole
install -m 0755 -D -p greyhole.cron.weekly ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.weekly/greyhole
install -m 0755 -D -p greyhole.cron.daily ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/greyhole

install -m 0644 -D -p web-app/index.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/README ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/

install -m 0755 -D -p scripts-examples/greyhole_file_changed.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/scripts-examples/
install -m 0755 -D -p scripts-examples/greyhole_idle.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/scripts-examples/
install -m 0755 -D -p scripts-examples/greyhole_notify_error.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/scripts-examples/
install -m 0755 -D -p scripts-examples/greyhole_send_fsck_report.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/scripts-examples/

install -m 0644 -D -p USAGE ${RPM_BUILD_ROOT}/usr/share/greyhole/

install -m 0644 -D -p docs/greyhole.1.gz ${RPM_BUILD_ROOT}/usr/share/man/man1/
install -m 0644 -D -p docs/greyhole-dfree.1.gz ${RPM_BUILD_ROOT}/usr/share/man/man1/
install -m 0644 -D -p docs/greyhole.conf.5.gz ${RPM_BUILD_ROOT}/usr/share/man/man5/

%ifarch x86_64
	install -m 0644 -D -p samba-module/bin/3.4/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba34.so
	install -m 0644 -D -p samba-module/bin/3.5/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba35.so
	install -m 0644 -D -p samba-module/bin/3.6/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba36.so
	install -m 0644 -D -p samba-module/bin/4.0/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba40.so
    install -m 0644 -D -p samba-module/bin/4.1/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba41.so
    install -m 0644 -D -p samba-module/bin/4.2/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba42.so
    install -m 0644 -D -p samba-module/bin/4.3/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba43.so
    install -m 0644 -D -p samba-module/bin/4.4/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba44.so
    install -m 0644 -D -p samba-module/bin/4.5/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba45.so
    install -m 0644 -D -p samba-module/bin/4.6/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba46.so
%else
	%ifarch %{arm}
		install -m 0644 -D -p samba-module/bin/3.4/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba34.so
		install -m 0644 -D -p samba-module/bin/3.5/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba35.so
		#install -m 0644 -D -p samba-module/bin/3.6/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba36.so # Not available yet
		#install -m 0644 -D -p samba-module/bin/4.0/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba40.so # Not available yet
		#install -m 0644 -D -p samba-module/bin/4.1/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba41.so # Not available yet
		#install -m 0644 -D -p samba-module/bin/4.2/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba42.so # Not available yet
		#install -m 0644 -D -p samba-module/bin/4.3/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba43.so # Not available yet
		#install -m 0644 -D -p samba-module/bin/4.4/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba44.so # Not available yet
		#install -m 0644 -D -p samba-module/bin/4.5/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba45.so # Not available yet
		#install -m 0644 -D -p samba-module/bin/4.6/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba46.so # Not available yet
	%else
		install -m 0644 -D -p samba-module/bin/3.4/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba34.so
		install -m 0644 -D -p samba-module/bin/3.5/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba35.so
		install -m 0644 -D -p samba-module/bin/3.6/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba36.so
		install -m 0644 -D -p samba-module/bin/4.0/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba40.so
        install -m 0644 -D -p samba-module/bin/4.1/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba41.so
        install -m 0644 -D -p samba-module/bin/4.2/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba42.so
        install -m 0644 -D -p samba-module/bin/4.3/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba43.so
        install -m 0644 -D -p samba-module/bin/4.4/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba44.so
        install -m 0644 -D -p samba-module/bin/4.5/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba45.so
        install -m 0644 -D -p samba-module/bin/4.6/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba46.so
	%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post
echo "Executing post-install script..."
mkdir -p /var/spool/greyhole
chmod 777 /var/spool/greyhole
/usr/bin/greyhole --create-mem-spool >/dev/null
mkdir -p /var/cache/greyhole-dfree
chmod 777 /var/cache/greyhole-dfree

if [ -d /usr/lib/x86_64-linux-gnu ]; then 
    SOURCE_LIBDIR="/usr/lib64"
    TARGET_LIBDIR="/usr/lib/x86_64-linux-gnu"
elif [ "`uname -m`" = "x86_64" ]; then
    SOURCE_LIBDIR="/usr/lib64"
    TARGET_LIBDIR="/usr/lib64"
else
    SOURCE_LIBDIR="/usr/lib"
    TARGET_LIBDIR="/usr/lib"
fi

TARGET_SYMLINK="${TARGET_LIBDIR}/samba/vfs/greyhole.so"

SMB_VERSION="`smbd --version | awk '{print $2}' | awk -F'-' '{print $1}' | awk -F'.' '{print $1,$2}'`"
if [ "${SMB_VERSION}" = "3 4" ]; then
    LIB_FILE="greyhole-samba34.so"
elif [ "${SMB_VERSION}" = "3 5" ]; then
    LIB_FILE="greyhole-samba35.so"
elif [ "${SMB_VERSION}" = "3 6" ]; then
    LIB_FILE="greyhole-samba36.so"
elif [ "${SMB_VERSION}" = "4 0" ]; then
    LIB_FILE="greyhole-samba40.so"
elif [ "${SMB_VERSION}" = "4 1" ]; then
    LIB_FILE="greyhole-samba41.so"
elif [ "${SMB_VERSION}" = "4 2" ]; then
    LIB_FILE="greyhole-samba42.so"
elif [ "${SMB_VERSION}" = "4 3" ]; then
    LIB_FILE="greyhole-samba43.so"
elif [ "${SMB_VERSION}" = "4 4" ]; then
    LIB_FILE="greyhole-samba44.so"
elif [ "${SMB_VERSION}" = "4 5" ]; then
    LIB_FILE="greyhole-samba45.so"
elif [ "${SMB_VERSION}" = "4 6" ]; then
    LIB_FILE="greyhole-samba46.so"
else
	echo "Warning: Greyhole doesn't include a VFS module for your version of Samba (${SMB_VERSION})."
	echo "We will try to use the VFS for Samba 4.6, but that might not work."
    LIB_FILE="greyhole-samba46.so"
fi

SOURCE_LIB="${SOURCE_LIBDIR}/greyhole/${LIB_FILE}"

rm -f ${TARGET_SYMLINK}
ln -s ${SOURCE_LIB} ${TARGET_SYMLINK}

if [ -f /proc/fs/cifs/OplockEnabled ]; then
	# cifs client workaround
	# Ref: http://blog.dhampir.no/content/cifs-vfs-no-response-for-cmd-n-mid
	modprobe cifs
	echo 0 > /proc/fs/cifs/OplockEnabled
fi
if [ -f /sys/module/cifs/parameters/enable_oplocks ]; then
	# cifs client workaround
	# Ref: http://blog.dhampir.no/content/cifs-vfs-no-response-for-cmd-n-mid
	modprobe cifs enable_oplocks=0
	echo 0 > /sys/module/cifs/parameters/enable_oplocks
fi

running=0
# (SYSV) Service install & start
if [ -f /sbin/chkconfig ]; then
	/sbin/chkconfig --add greyhole
	/sbin/chkconfig greyhole on
else
	/usr/sbin/update-rc.d greyhole defaults
fi
if [ -f /etc/rc.d/init.d/greyhole ]; then
	if [ "`service greyhole stat 2> /dev/null | grep 'is running' | wc -l`" = "1" ]; then
		service greyhole restart
		running=1
	fi
fi

if [ $running -eq 0 ]; then
	echo "==========================================================================="
	echo "See /usr/share/greyhole/USAGE to learn how to configure and start Greyhole."
	echo "==========================================================================="
fi

man logrotate > /dev/null 2>&1 || echo "Warning! logrotate is not installed. You should install logrotate to make sure the Greyhole logs don't fill your root partition.
  Greyhole already installed the necessary conf file for logrotate; simply installing the logrotate package is enough."

%preun

# Delete VFS module symlinks, if any
rm -f /usr/lib/x86_64-linux-gnu/samba/vfs/greyhole.so
rm -f /usr/lib64/samba/vfs/greyhole.so
rm -f /usr/lib/samba/vfs/greyhole.so

# Delete cache folder
rm -rf /var/cache/greyhole-dfree

if [ "$1" != 0 ]; then
	/sbin/service greyhole condrestart 2>&1 > /dev/null
else
	# not an update, a complete uninstall
	
	# Service removal
	/sbin/service greyhole stop 2>&1 > /dev/null
	/sbin/chkconfig --del greyhole

	# Remove Greyhole from /etc/samba/smb.conf
	grep -v "dfree.*greyhole" /etc/samba/smb.conf > /etc/samba/smb.conf.new
	sed --in-place -e 's@\(vfs objects.*\) greyhole@\1@' /etc/samba/smb.conf.new
	sed --in-place -e 's@^[ \t]*vfs objects =$@@' /etc/samba/smb.conf.new
	mv -f /etc/samba/smb.conf.new /etc/samba/smb.conf
	/sbin/service smb reload 2>&1 > /dev/null
fi

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/greyhole.conf
/etc/rc.d/init.d/greyhole
/etc/*/greyhole*
/usr/bin/greyhole*
%{_libdir}/greyhole/
/usr/share/greyhole/
/usr/share/man/*/greyhole*

%changelog
* Sun Jan 13 2013 Guillaume Boudreau
- Including gh-du web UI
* Sun Jan 02 2011 Guillaume Boudreau
- Fedora 14 (Samba 3.5) compatibility fixes
* Mon Mar 29 2010 Carlos Puchol
- add sqlite schema file, rename mysql one
- use /usr/share/greyhole instead of local 
* Mon Feb 22 2010 Guillaume Boudreau
- major update in all sections; more automated installation
* Wed Jan 22 2010 Carlos Puchol
- initial version of Greyhole spec
