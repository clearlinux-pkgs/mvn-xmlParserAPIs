#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-xmlParserAPIs
Version  : 2.6.2
Release  : 1
URL      : https://repo1.maven.org/maven2/xerces/xmlParserAPIs/2.6.2/xmlParserAPIs-2.6.2.jar
Source0  : https://repo1.maven.org/maven2/xerces/xmlParserAPIs/2.6.2/xmlParserAPIs-2.6.2.jar
Source1  : https://repo1.maven.org/maven2/xerces/xmlParserAPIs/2.6.2/xmlParserAPIs-2.6.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : W3C
Requires: mvn-xmlParserAPIs-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-xmlParserAPIs package.
Group: Data

%description data
data components for the mvn-xmlParserAPIs package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/xerces/xmlParserAPIs/2.6.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/xerces/xmlParserAPIs/2.6.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/xerces/xmlParserAPIs/2.6.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/xerces/xmlParserAPIs/2.6.2


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/xerces/xmlParserAPIs/2.6.2/xmlParserAPIs-2.6.2.jar
/usr/share/java/.m2/repository/xerces/xmlParserAPIs/2.6.2/xmlParserAPIs-2.6.2.pom
