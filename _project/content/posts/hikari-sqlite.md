Title: Hikari connection with SQLite
Category: Development
Date: 22/05/2019 11:21
Tags: hikari, sqlite
Slug: hikari-connection-with-sqlite
Authors: Marcus Bittencourt
Summary: Setting up big data environment on Centos 7

(underconstruction)

### add hikaricp dependency to your pom.xml
    
    :::xml

    <dependency>
        <groupId>com.zaxxer</groupId>
        <artifactId>HikariCP</artifactId>
        <version>3.3.1</version>
    </dependency>


### example code (references https://www.baeldung.com/hikaricp)

    :::java

    public class DataSource {
 
        private static HikariConfig config = new HikariConfig();
        private static HikariDataSource ds;
    
        static {
            config.setJdbcUrl( "jdbc_url" );
            config.setUsername( "database_username" );
            config.setPassword( "database_password" );
            config.addDataSourceProperty( "cachePrepStmts" , "true" );
            config.addDataSourceProperty( "prepStmtCacheSize" , "250" );
            config.addDataSourceProperty( "prepStmtCacheSqlLimit" , "2048" );
            ds = new HikariDataSource( config );
        }
    
        private DataSource() {}
    
        public static Connection getConnection() throws SQLException {
            return ds.getConnection();
        }
    }