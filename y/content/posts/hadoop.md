Title: Setting up big data environment on Centos 7
Category: Data Engineering
Date: 22/05/2019 09:22
Tags: hadoop, tez, hive
Slug: setting-up-big-data-env-centos
Authors: Marcus Bittencourt
Summary: Setting up big data environment on Centos 7

# Compiling Tez 0.9.2 for Hadoop 3.1.2

*Utils*
	:::bash
	$ yum install autoconf automake libtool unzip gcc-c++ git

*Node v6.16.0*
	:::bash
	$ yum install node
	$ node --version
	v6.16.0

*Java OpenJDK 1.8*
	:::bash
	$ sudo yum install java-1.8.0-openjdk-devel
	$ export JAVA_HOME=/usr/lib/jvm
	$ export PATH=$PATH:$JAVA_HOME/bin
	$ source ~/.bashrc

*Maven 3.6.1* 
	:::bash
	$ mkdir /opt/maven
	$ wget http://ftp.unicamp.br/pub/apache/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz
	$ tar zxvf apache-maven-3.6.1-bin.tar.gz --directory=/opt/maven --strip 1
	$ export M3_HOME=/opt/maven
	$ export PATH=$PATH:$M3_HOME/bin
	$ source ~/.bashrc
	$ mvn --version
	Apache Maven 3.6.1 (d66c9c0b3152b2e69ee9bac180bb8fcc8e6af555; 2019-04-04T16:00:29-03:00)
	Maven home: /opt/maven
	Java version: 1.8.0_212, vendor: Oracle Corporation, runtime: /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.212.b04-0.el7_6.x86_64/jre
	Default locale: en_US, platform encoding: UTF-8
	OS name: "linux", version: "3.10.0-957.10.1.el7.x86_64", arch: "amd64", family: "unix"

*Protobuf 2.5.0*
	:::bash
	$ mkdir /opt/protobuf
	$ wget https://github.com/google/protobuf/releases/download/v2.5.0/protobuf-2.5.0.tar.gz
	$ tar zxvf protobuf-2.5.0.tar.gz --directory=/opt/protobuf --strip 1
	$ cd /opt/protobuf/
	$ ./autogen.sh 
	$ ./configure
	$ make 
	$ make install
	$ protoc --version
	libprotoc 2.5.0

*Tez 0.9.2*
	:::bash
	$ mkdir /opt/tez
	$ wget http://mirror.nbtelecom.com.br/apache/tez/0.9.2/apache-tez-0.9.2-src.tar.gz
	$ tar zxvf apache-tez-0.9.2-src.tar.gz --directory=/opt/tez --strip 1
	# Alterar hadoop.version no pom.xml para a versão instalada do hadoop, nesse caso 3.1.2
	$ npm install yarn -g
	$ mvn clean package -DskipTests=true -Dmaven.javadoc.skip=true -Phadoop28 -Dhadoop.version=3.1.2

# Install big data environment with hadoop 3.1.2 and tez 0.9.2

*Hadoop 3.2.1*
	:::bash
	$ mkdir /opt/hadoop
	$ wget 
	$ 
	$

# Install and configure hive 3.1.1 on tez 0.9.2

*Mysql 5.7.26* 
	:::bash
	$ msyql --version
	$ msyql -u root -p 
	mysql> create database metastore; 

*Hive 3.1.1*
	:::bash
	$ mkdir /opt/hive
	$ wget https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
	$

Install and configure sqoop

*Sqoop 1.4.7*
	:::bash
	$ mkdir /opt/sqoop
	$ wget http://ftp.unicamp.br/pub/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
	$ tar zxvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz --directory=/opt/sqoop --strip 1
	$ 
	$ sqoop version
	Sqoop 1.4.7
	git commit id 2328971411f57f0cb683dfb79d19d4d19d185dd8
	Compiled by maugli on Thu Dec 21 15:59:58 STD 2017

*inspirated by https://hnlaomie.github.io/*