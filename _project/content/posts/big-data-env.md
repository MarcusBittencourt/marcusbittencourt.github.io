Title: Setting up big data environment on Centos 7
Category: Data Engineering
Date: 22/05/2019 09:22
Tags: hadoop, tez, hive
Slug: setting-up-big-data-env-centos
Authors: Marcus Bittencourt
Summary: Setting up big data environment on Centos 7

This environment setup is desined for supports scaled big data process in organizations with BI demand and needs data lake insfrastructure in single node.

(underconstruction)

# Building Tez 0.9.2 from source for Hadoop 3.1.2

### Utils

    :::bash
    $ yum install nano autoconf automake libtool unzip gcc-c++ git

### Java OpenJDK 1.8

	:::bash
	$ sudo yum install java-1.8.0-openjdk-devel
	$ export JAVA_HOME=/usr/lib/jvm
	$ export PATH=$PATH:$JAVA_HOME/bin
	$ source ~/.bashrc

### Maven 3.6.1

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

### Node 6.16.0

	:::bash
	$ yum install node
	$ node --version
	v6.16.0
	$ npm cache clean -f
	$ npm install -g n 
	$ n stable
	$ sudo ln -sf /usr/local/n/versions/node/10.15.3/bin/node /usr/bin/node
	$ node --version
	v10.15.3

### Npm 6.9.1 

	$ npm install -g npm@next
	$ npm --version
	6.9.1-next-0

Try logout of your bash if npm previous version persist

### Protobuf 2.5.0

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

### Tez 0.9.2

	:::bash
	$ mkdir /opt/tez-src
	$ wget http://mirror.nbtelecom.com.br/apache/tez/0.9.2/apache-tez-0.9.2-src.tar.gz
	$ tar zxvf apache-tez-0.9.2-src.tar.gz --directory=/opt/tez --strip 1
	$ mvn clean package -DskipTests=true -Dmaven.javadoc.skip=true -Phadoop28 -Dhadoop.version=3.1.2 -Dfrontend-maven-plugin.version=0.0.23 -X 
	[INFO] ------------------------------------------------------------------------
	[INFO] Reactor Summary for tez 0.9.2:
	[INFO]
	[INFO] tez ................................................ SUCCESS [  1.924 s]
	[INFO] hadoop-shim ........................................ SUCCESS [  4.789 s]
	[INFO] tez-api ............................................ SUCCESS [ 12.615 s]
	[INFO] tez-build-tools .................................... SUCCESS [  2.085 s]
	[INFO] tez-common ......................................... SUCCESS [  4.235 s]
	[INFO] tez-runtime-internals .............................. SUCCESS [  4.680 s]
	[INFO] tez-runtime-library ................................ SUCCESS [ 10.753 s]
	[INFO] tez-mapreduce ...................................... SUCCESS [  5.256 s]
	[INFO] tez-examples ....................................... SUCCESS [  3.046 s]
	[INFO] tez-dag ............................................ SUCCESS [ 14.565 s]
	[INFO] tez-tests .......................................... SUCCESS [  4.699 s]
	[INFO] tez-ext-service-tests .............................. SUCCESS [  4.466 s]
	[INFO] tez-plugins ........................................ SUCCESS [  0.538 s]
	[INFO] tez-protobuf-history-plugin ........................ SUCCESS [  3.780 s]
	[INFO] tez-yarn-timeline-history .......................... SUCCESS [  4.404 s]
	[INFO] tez-yarn-timeline-history-with-acls ................ SUCCESS [  2.517 s]
	[INFO] tez-history-parser ................................. SUCCESS [02:03 min]
	[INFO] tez-aux-services ................................... SUCCESS [ 45.909 s]
	[INFO] tez-yarn-timeline-cache-plugin ..................... SUCCESS [01:22 min]
	[INFO] tez-yarn-timeline-history-with-fs .................. SUCCESS [  2.244 s]
	[INFO] tez-tools .......................................... SUCCESS [  0.222 s]
	[INFO] tez-perf-analyzer .................................. SUCCESS [  0.247 s]
	[INFO] tez-job-analyzer ................................... SUCCESS [  2.940 s]
	[INFO] tez-javadoc-tools .................................. SUCCESS [  2.204 s]
	[INFO] hadoop-shim-impls .................................. SUCCESS [  0.188 s]
	[INFO] hadoop-shim-2.8 .................................... SUCCESS [  1.844 s]
	[INFO] tez-dist ........................................... SUCCESS [02:02 min]
	[INFO] Tez ................................................ SUCCESS [  0.194 s]
	[INFO] ------------------------------------------------------------------------
	[INFO] BUILD SUCCESS
	[INFO] ------------------------------------------------------------------------
	[INFO] Total time:  07:49 min
	[INFO] Finished at: 2019-05-22T14:44:06-03:00
	[INFO] ------------------------------------------------------------------------
	# before tez installation this directory can be deleted
	$ rm /opt/tez-src

### Yarn pkg 1.16.0

if tez build fails with mvn problem '[ERROR] error An unexpected error occurred: "https://registry.yarnpkg.com/ember-cli-app-version/-/ember-cli-app-version-1.0.0.tgz: self signed certificate in certificate chain".' then is need install yarn specific version manually    

	$ npm install --global yarn@0.21.3
	$ yarn --version
	v0.21.3

# Install big data environment with hadoop 3.1.2 and tez 0.9.2

### Hadoop 3.1.2

	:::bash
	$ mkdir /data
	$ mkdir /opt/hadoop
	$ wget http://mirror.nbtelecom.com.br/apache/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
	$ tar zxvf hadoop-3.1.2.tar.gz --directory=/opt/hadoop --strip 1
	# Configure core-site.xml following the sample
	$ nano /opt/hadoop/etc/hadoop/core-site.xml
	# Configure hdfs-site.xml following the sample
	$ nano /opt/hadoop/etc/hadoop/hdfs-site.xml
	# Configure yarn-site.xml following the sample
	$ nano /opt/hadoop/etc/hadoop/yarn-site.xml
	# Configure mapred-site.xml following the sample
	$ nano /opt/hadoop/etc/hadoop/mapred-site.xml
	# Configure hadoop-env.sh following the sample
	$ nano /opt/hadoop/etc/hadoop/hadoop-env.sh
	$ $HADOOP_HOME/sbin/start-all.sh
	Starting namenodes on [localhost]
	Starting datanodes
	Starting secondary namenodes [flnsrvungp000129]
	Starting resourcemanager
	Starting nodemanagers

*core-site.xml*
	
	:::xml
	<configuration>
			<property>
					<name>fs.default.name</name>
					<value>hdfs://localhost:8020</value>
			</property>
			<property>
					<name>hadoop.proxyuser.hadoop.groups</name>
					<value>*</value>
			</property>
			<property>
					<name>hadoop.proxyuser.hadoop.hosts</name>
					<value>*</value>
			</property>
	</configuration>

*hdfs-site.xml*
	
	:::xml
	<configuration>
			<property>
					<name>dfs.datanode.data.dir</name>
					<value>/data/1/dn</value>
			</property>
			<property>
					<name>dfs.namenode.name.dir</name>
					<value>/data/1/nn</value>
			</property>
			<property>
					<name>dfs.namenode.http-address</name>
					<value>localhost:50070</value>
			</property>
			<property>
					<name>dfs.replication</name>
					<value>1</value>
			</property>
	</configuration>

*yarn-site.xml*
	
	:::xml
	<configuration>
        <property>
                <name>yarn.nodemanager.aux-services</name>
                <value>mapreduce_shuffle</value>
        </property>
        <property>
                <name>yarn.scheduler.minimum-allocation-mb</name>
                <value>2560</value>
        </property>
        <property>
                <name>yarn.scheduler.maximum-allocation-mb</name>
                <value>4096</value>
        </property>
        <property>
                <name>yarn.scheduler.maximum.resource.memory-mb</name>
                <value>7680</value>
        </property>
        <property>
                <name>yarn.scheduler.maximum.allocation-vcores</name>
                <value>3</value>
        </property>
        <property>
                <name>yarn.nodemanager.resource.cpu-vcores</name>
                <value>3</value>
        </property>
        <property>
                <name>yarn.resourcemanager.scheduler.class</name>
                <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler</value>
        </property>
	</configuration>


*mapred-site.xml*
	
	:::xml
	<configuration>
        <property>
                <name>mapreduce.framework.name</name>
                <value>yarn-tez</value>
        </property>
	</configuration>

*hadoop-env.sh*
	
	:::bash
	export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk


### Tez 0.9.2

	:::bash
	$ hadoop fs -mdkir /user/tez
	$ hadoop fs -put /opt/tez-src/tez-dist/target/tez-0.9.2.tar.gz /user/tez
	$ mkdir /opt/tez
	$ mkdir /opt/tez/conf
	$ tar zxvf /opt/tez-src/tez-dist/target/tez-0.9.2-minimal.tar.gz --directory=/opt/tez --strip 1
	# configure tez-site.xml following the sample
	$ nano /opt/tez/conf/tez-site.xml
	$ 
	$ 

*tez-site*

	:::xml
	<configuration>	
		<property>
			<name>tez.uri.libs</name>
			<value>http://localhost:8020/user/tez/tez-0.9.2.tar.gz</value>
		</property>
	</configuration>

Test tez install using one of the functions of tez-test-<>.jar, example:
	
	:::bash
	hadoop jar tez-test.0.9.2.jar orderedwordcount file.txt out.log

# Install and configure hive 3.1.1 on tez 0.9.2

### Mysql 5.7.26 

	:::bash
	$ msyql --version
	$ msyql -u root -p 
	mysql> create database metastore; 

### Hive 3.1.1

	:::bash
	$ mkdir /opt/hive
	$ wget https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
	$

Install and configure sqoop

### Sqoop 1.4.7

	:::bash
	$ mkdir /opt/sqoop
	$ wget http://ftp.unicamp.br/pub/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
	$ tar zxvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz --directory=/opt/sqoop --strip 1
	$ 
	$ sqoop version
	Sqoop 1.4.7
	git commit id 2328971411f57f0cb683dfb79d19d4d19d185dd8
	Compiled by maugli on Thu Dec 21 15:59:58 STD 2017


*Knowledge problems:*

1. mvn fails during tez compilation with yarn install error, check your nodejs version, this must be fixed updatating.
2. mvn fails during tez compilation with yarn install error, dont set the YARN_HOME variable in your path.
3. mvn fails during tez compilation with protoc not found, check yout version of protobufer, is required 2.5.0 for hadoop 3.1.2
4. mvn fails during tez compilation with execute goal com.github.eirslett:frontend-maven-plugin, add the paramenter -Dfrontend-maven-plugin.version=0.0.23


*References*

1. https://tecadmin.net/upgrade-nodejs-via-npm/
2. https://github.com/apache/tez/blob/master/BUILDING.txt
