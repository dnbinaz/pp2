#/Users/ihlasova75icloud.com/Desktop/pp2/lab10/data.csv
import psycopg2
import csv

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            database='phonebook',            
            user='ihlasova75icloud.com',    
            password='20022009'         
        )
        print("Connected to the database")
        return conn
    except psycopg2.Error as e:
        print("Error connecting to DB:", e)
        return None

def create_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Phonebook(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            phone_number VARCHAR(11) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    print("Phonebook table ready")

def insert_data_from_csv(conn, csv_path):
    try:
        cur = conn.cursor()
        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for first_name, last_name, phone_number in reader:
                try:
                    cur.execute("""
                        INSERT INTO Phonebook (first_name, last_name, phone_number)
                        VALUES (%s, %s, %s);
                    """, (first_name, last_name, phone_number))
                except psycopg2.Error as e:
                    print("Skipped:", e)
        conn.commit()
        print("CSV import completed")
        cur.close()
    except Exception as e:
        print("CSV file error:", e)

def insert_data_from_console(conn):
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone (11 digits max): ")

    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Phonebook (first_name, last_name, phone_number)
            VALUES (%s, %s, %s);
        """, (first_name, last_name or None, phone_number))
        conn.commit()
        print("Contact added")
        cur.close()
    except psycopg2.Error as e:
        print("Insert error:", e)

def update_contact(conn):
    key = input("Enter first name or phone to update: ")
    print("Update:")
    print("1. First name")
    print("2. Last name")
    print("3. Phone number")
    choice = input("Choose option: ")
    new_value = input("New value: ")

    try:
        cur = conn.cursor()
        if choice == "1":
            cur.execute("UPDATE Phonebook SET first_name=%s WHERE first_name=%s OR phone_number=%s;", (new_value, key, key))
        elif choice == "2":
            cur.execute("UPDATE Phonebook SET last_name=%s WHERE first_name=%s OR phone_number=%s;", (new_value, key, key))
        elif choice == "3":
            cur.execute("UPDATE Phonebook SET phone_number=%s WHERE first_name=%s OR phone_number=%s;", (new_value, key, key))
        else:
            print("Invalid option")
            return
        conn.commit()
        print("Update successful")
        cur.close()
    except psycopg2.Error as e:
        print("Update error:", e)

def query_contacts(conn):
    print("\nFilters:")
    print("1. All contacts")
    print("2. By first name")
    print("3. By last name")
    print("4. Phone starts with")
    print("5. Phone contains")
    option = input("Choose filter: ")

    try:
        cur = conn.cursor()
        if option == "1":
            cur.execute("SELECT id, first_name, last_name, phone_number FROM Phonebook ORDER BY id;")
        elif option == "2":
            name = input("Enter first name: ")
            cur.execute("SELECT * FROM Phonebook WHERE first_name=%s;", (name,))
        elif option == "3":
            last = input("Enter last name: ")
            cur.execute("SELECT * FROM Phonebook WHERE last_name=%s;", (last,))
        elif option == "4":
            prefix = input("Phone starts with: ")
            cur.execute("SELECT * FROM Phonebook WHERE phone_number LIKE %s;", (prefix + "%",))
        elif option == "5":
            part = input("Phone contains: ")
            cur.execute("SELECT * FROM Phonebook WHERE phone_number LIKE %s;", ("%" + part + "%",))
        else:
            print("Invalid filter")
            return

        rows = cur.fetchall()
        print("\n Results:")
        for r in rows:
            print(r)
        cur.close()
    except psycopg2.Error as e:
        print("Query error:", e)


def delete_contact_by_key(conn):
    key = input("Enter first name or phone to delete: ")
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM Phonebook WHERE first_name=%s OR phone_number=%s;", (key, key))
        conn.commit()
        print("Deleted")
        cur.close()
    except psycopg2.Error as e:
        print("Delete error:", e)

def main():
    conn = connect_to_db()
    if not conn:
        return
    create_table(conn)

    while True:
        print("\n=== 📒 PHONEBOOK ===")
        print("1. Import from CSV")
        print("2. Add from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Exit")
        choice = input("Select: ")

        if choice == "1":
            insert_data_from_csv(conn, input("CSV path: "))
        elif choice == "2":
            insert_data_from_console(conn)
        elif choice == "3":
            update_contact(conn)
        elif choice == "4":
            query_contacts(conn)
        elif choice == "5":
            delete_contact_by_key(conn)
        elif choice == "6":
            print("All done!")
            break
        else:
            print("Invalid choice")

    conn.close()

if __name__ == "__main__":
    main()