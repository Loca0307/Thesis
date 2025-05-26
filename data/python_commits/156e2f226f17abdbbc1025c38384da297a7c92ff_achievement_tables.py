def create_table(name, columns, metadata, schema):
    return Table(
        name,
        metadata,
        *columns,
        mysql_engine=MYSQL_ENGINE,
        mysql_charset=MYSQL_CHARSET,
        mysql_collate=MYSQL_COLLATE,
        schema=schema,
    )

achievements_list_columns = [