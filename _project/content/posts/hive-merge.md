Title: Hive merge query for History strategy
Category: Data Engineering
Date: 22/05/2019 11:11
Tags: hive
Slug: hive-merge-history-strategy
Authors: Marcus Bittencourt
Summary: Hive merge query for History strategy

(underconstruction)

# Hive merge query for History strategy

Create an external table for intermadiate updates from extracted data and load jobs

    :::sql
    CREATE EXTERNAL TABLE staging.update_contributors (
        login string,
        email string,
        nome string,
        idcentrocusto string,
        nmcentrocusto string,
        idempresa string,
        nmempresa string,
        idunidade string,
        nmunidade string,
        nucargahoraria string,
        nmcargo string,
        nmperfil string,
        dtadmissao string,
        dtdemissao string
    ) 
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    STORED AS TEXTFILE;

    LOAD DATA INPATH '/user/pig/serp' OVERWRITE INTO TABLE staging.update_contributors;

Create destiny table for results after merge action

    :::sql
    CREATE TABLE IF NOT EXISTS staging.contributors
    ROW FORMAT DELIMITED 
        FIELDS TERMINATED BY ','
    STORED AS ORC
    tblproperties ('transactional' = 'true', 'orc.compression' = 'ZLIB')
    AS (SELECT update_contributors.*, current_timestamp as load_date, FALSE as archived FROM staging.update_contributors);

Create temporary table for manage actions and auxiliary decisions when upserts is necessary

    :::sql
    CREATE TEMPORARY TABLE staging.diff_contributors 
    STORED AS ORC
    TBLPROPERTIES ("auto.purge"="true")
    AS (
    SELECT 
            update_contributors.*,
            CASE 
                WHEN (update_contributors.login <> contributors.login 
                OR update_contributors.nome <> contributors.nome
                OR update_contributors.idcentrocusto <> contributors.idcentrocusto
                OR update_contributors.nmcentrocusto <> contributors.nmcentrocusto
                OR update_contributors.idempresa <> contributors.idempresa
                OR update_contributors.nmempresa <> contributors.nmempresa
                OR update_contributors.idunidade <> contributors.idunidade
                OR update_contributors.nmunidade <> contributors.nmunidade
                OR update_contributors.nucargahoraria <> contributors.nucargahoraria
                OR update_contributors.nmcargo <> contributors.nmcargo
                OR update_contributors.nmperfil <> contributors.nmperfil
                OR update_contributors.dtadmissao <> contributors.dtadmissao
                OR update_contributors.dtdemissao <> contributors.dtdemissao) THEN TRUE 
                ELSE FALSE 
            END AS changed
        FROM staging.contributors, staging.update_contributors
        WHERE contributors.login = update_contributors.login
        AND NOT contributors.archived
    );

Perform the merge between table of update data and the historical records (tez engine, is required because spark dont need support for merge clause)

    :::sql
    MERGE INTO staging.contributors c USING (
        SELECT *, FALSE AS to_filed FROM staging.diff_contributors
        UNION ALL
        SELECT *, TRUE AS to_filed FROM staging.diff_contributors WHERE changed
    )
    AS updates ON updates.login = c.login AND NOT c.archived
    WHEN matched AND updates.changed AND updates.to_filed
        THEN UPDATE SET archived = TRUE
    WHEN matched AND updates.changed AND NOT updates.to_filed THEN INSERT VALUES (
        updates.login, updates.email, updates.nome, updates.idcentrocusto, updates.nmcentrocusto, updates.idempresa, 
        updates.nmempresa, updates.idunidade, updates.nmunidade, updates.nucargahoraria, updates.nmcargo, updates.nmperfil, updates.dtadmissao, 
        updates.dtdemissao, current_timestamp, FALSE)
    WHEN NOT matched THEN INSERT VALUES (
        updates.login, updates.email, updates.nome, updates.idcentrocusto, updates.nmcentrocusto, updates.idempresa, 
        updates.nmempresa, updates.idunidade, updates.nmunidade, updates.nucargahoraria, updates.nmcargo, updates.nmperfil, updates.dtadmissao, 
        updates.dtdemissao, current_timestamp, FALSE);