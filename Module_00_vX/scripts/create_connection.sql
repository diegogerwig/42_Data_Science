INSERT INTO pgadmin_private.pg_server (
    servergroup_id, 
    srvowner, 
    srvhost, 
    srvport, 
    srvmaintenance_db, 
    srvname, 
    srvusername, 
    srvpassword, 
    srvsslmode,
    srvsslcompression,
    srvtimeout,
    can_create_role,
    can_create_db
)
VALUES (
    1,  -- servergroup_id (usually 1 for the default server group)
    10, -- srvowner (ID of the user owning the connection, 10 is the default ID for admin in PgAdmin)
    'postgres',  -- srvhost (the hostname or IP address of the PostgreSQL server)
    5432,  -- srvport (the port PostgreSQL is listening on, 5432 is the default)
    'piscineds',  -- srvmaintenance_db (the name of the maintenance database)
    'data_science',  -- srvname (a descriptive name for the connection)
    'dgerwig',  -- srvusername (username for the connection)
    'userpw',  -- srvpassword (user's password)
    'prefer',  -- srvsslmode (SSL mode, prefer is a common option)
    False,  -- srvsslcompression (SSL compression)
    10,  -- srvtimeout (timeout in seconds)
    False,  -- can_create_role (permission to create roles)
    False   -- can_create_db (permission to create databases)
);
