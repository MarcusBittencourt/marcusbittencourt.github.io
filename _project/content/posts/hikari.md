Title: Hikari connection with SQLite
Category: Data Engineering
Date: 22/05/2019 11:21
Tags: hikari, sqlite
Slug: hikari-connection-with-sqlite
Authors: Marcus Bittencourt
Summary: Setting up big data environment on Centos 7

(underconstruction)

Example code (references https://www.baeldung.com/hikaricp)

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