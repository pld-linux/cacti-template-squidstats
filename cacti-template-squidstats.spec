%define		template	squidstats
Summary:	Squid Statistics template for Cacti
Name:		cacti-template-%{template}
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	SquidStats-%{version}.zip
# Source0-md5:	a37de602c6e5495049a368d0d2c87549
URL:		http://forums.cacti.net/about3158.html
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	cacti >= 0.8.6j
Requires:	cacti-add_template
Obsoletes:	cacti-plugin-squidstats
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts
%define		snmpqueriesdir	%{resourcedir}/snmp_queries

%description
Query and plot various metrics presented by Squid over SNMP.

%prep
%setup -q -c

%{__sed} -i -e 's,\r$,,' *.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{snmpqueriesdir},%{scriptsdir}}
cp -a webcache_squid_core.xml webcache_squid_median.xml $RPM_BUILD_ROOT%{snmpqueriesdir}
cp -a cacti_host_template_webcache_squid_server_snmp.xml $RPM_BUILD_ROOT%{resourcedir}

%post
%{_sbindir}/cacti-add_template %{resourcedir}/cacti_host_template_webcache_squid_server_snmp.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{snmpqueriesdir}/webcache_squid_core.xml
%{snmpqueriesdir}/webcache_squid_median.xml
%{resourcedir}/cacti_host_template_webcache_squid_server_snmp.xml
