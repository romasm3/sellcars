import psycopg2
from psycopg2 import sql

# PostgreSQL connection settings
DB_NAME = "sellcars_db"
DB_USER = "postgres"
DB_PASSWORD = input("Enter PostgreSQL password for 'postgres' user: ")
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    # Connect to PostgreSQL server (default 'postgres' database)
    print("Connecting to PostgreSQL server...")
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Check if database already exists
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
    exists = cursor.fetchone()

    if exists:
        print(f"Database '{DB_NAME}' already exists!")
        drop = input("Do you want to drop and recreate it? (yes/no): ").lower()
        if drop == "yes":
            print(f"Dropping database '{DB_NAME}'...")
            cursor.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(DB_NAME)))
            print(f"Creating database '{DB_NAME}'...")
            cursor.execute(
                sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME))
            )
            print(f"✅ Database '{DB_NAME}' recreated successfully!")
        else:
            print("Keeping existing database.")
    else:
        # Create the database
        print(f"Creating database '{DB_NAME}'...")
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
        print(f"✅ Database '{DB_NAME}' created successfully!")

    cursor.close()
    conn.close()

    print("\n" + "=" * 60)
    print("Database Configuration:")
    print("=" * 60)
    print(f"Database Name: {DB_NAME}")
    print(f"User: {DB_USER}")
    print(f"Host: {DB_HOST}")
    print(f"Port: {DB_PORT}")
    print("=" * 60)

except psycopg2.Error as e:
    print(f"❌ Error: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
