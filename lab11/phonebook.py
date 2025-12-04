import psycopg2
import csv

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "phonebook",
    "user": "ihlasova75icloud.com",
    "password": "20022009"
}

def connect_to_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("[INFO] Connected to the database")
        return conn
    except psycopg2.Error as e:
        print("[ERROR] Connection failed:", e)
        return None

def create_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook(
            id SERIAL PRIMARY KEY,
            surname VARCHAR(50),
            name VARCHAR(50),
            number VARCHAR(11)
        );
    """)
    conn.commit()
    cur.close()
    print("[INFO] Table ready")

def insert_or_update_user(conn):
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    number = input("Enter phone (11 digits): ")
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s, %s);", (surname, name, number))
    conn.commit()
    cur.close()
    print("[INFO] User inserted/updated successfully")

def insert_many_users(conn, csv_path):
    users = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if len(row) == 3:
                users.append(row)
    if not users:
        print("[INFO] No valid data found in CSV")
        return

    cur = conn.cursor()
    cur.execute("CALL insert_many_users(%s);", (users,))
    conn.commit()
    cur.close()
    print("[INFO] CSV users inserted (incorrect data will be notified by DB)")

def query_users_by_pattern(conn):
    pattern = input("Enter search pattern (name, surname, or number): ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_phone_users(%s);", (pattern,))
    rows = cur.fetchall()
    if rows:
        print("\nResults:")
        for r in rows:
            print(r)
    else:
        print("[INFO] No results found")
    cur.close()

def query_users_with_pagination(conn):
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur = conn.cursor()
    cur.execute("SELECT * FROM query_by_pagination(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    if rows:
        print("\nResults:")
        for r in rows:
            print(r)
    else:
        print("[INFO] No results found")
    cur.close()

def delete_user(conn):
    key_type = input("Delete by 'name' or 'phone': ").strip().lower()
    value = input("Enter value: ").strip()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s, %s);", (key_type, value))
    conn.commit()
    cur.close()
    print("[INFO] User deleted if exists")

def main():
    conn = connect_to_db()
    if not conn:
        return
    create_table(conn)

    while True:
        print("\n=== 📒 PHONEBOOK MENU ===")
        print("1. Insert or update single user")
        print("2. Insert many users from CSV")
        print("3. Search users by pattern")
        print("4. Query users with pagination")
        print("5. Delete user")
        print("6. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            insert_or_update_user(conn)
        elif choice == "2":
            csv_path = input("Enter CSV file path: ")
            insert_many_users(conn, csv_path)
        elif choice == "3":
            query_users_by_pattern(conn)
        elif choice == "4":
            query_users_with_pagination(conn)
        elif choice == "5":
            delete_user(conn)
        elif choice == "6":
            print("[INFO] Exiting...")
            break
        else:
            print("[ERROR] Invalid option, try again")

    conn.close()
    print("[INFO] PostgreSQL connection closed")

if __name__ == "__main__":
    main()
