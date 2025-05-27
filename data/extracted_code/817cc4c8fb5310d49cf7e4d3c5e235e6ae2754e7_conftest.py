def init_db():
    """Creates the database tables."""
    with open(SCHEMA, "r") as fp:
            schema = fp.read()
    with psycopg.connect(DATABASE) as con:
        with con.cursor() as cursor:
            for statement in schema.split(";"):
                if statement.strip():  # Avoid empty statements
                    cursor.execute(statement)
            con.commit()

def reset_db():
    """Empty the database and initialize the schema again"""
    with psycopg.connect(DATABASE) as con:
        with con.cursor() as cursor:
            cursor.execute("DROP SCHEMA public CASCADE;")
            cursor.execute("CREATE SCHEMA public;")  # Resets schema instead of dropping tables one by one
            con.commit()