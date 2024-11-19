import cx_Oracle
import getpass
from create_tables import create_tables
from insert_sample_data import insert_sample_data
from display_tables import *
from truncate_tables import truncate_all_tables
from drop_project_tables import drop_project_tables
from sql_executor import execute_query

# Database connection function
def connect_db():
    try:
        username = input("Enter Oracle DB username: ")
        password = getpass.getpass("Enter Oracle DB password: ")
        conn = cx_Oracle.connect(username, password, "localhost:1521/XE")  
        cursor = conn.cursor()
        print("Connection successful.")
        return conn, cursor
    except cx_Oracle.DatabaseError as e:
        print(f"Error: {e}")
        return None, None

def main_menu(conn, cursor):
    print("\nWelcome to Rent-A-Ride!")
    while True:
        print("\n---------------------------------------------------------------------")
        print("Choose an option:")
        print("1. Create tables")
        print("2. Insert sample data")
        print("3. Display tables")
        print("4. Truncate all tables")
        print("5. Drop all tables")
        print("6. Execute custom SQL query")
        print("7. Exit")
        print("---------------------------------------------------------------------")


        choice = input("Enter choice (1-7): ")

        # Check and reconnect if necessary
        if not conn or not cursor:
            conn, cursor = connect_db()
            if not conn or not cursor:
                print("Connection could not be established.")
                return

        if choice == "1":
            create_tables(conn, cursor)
            conn.commit()  # Ensure all creations are finalized
        elif choice == "2":
            insert_sample_data(conn, cursor)
            conn.commit()  # Commit after inserts
        elif choice == "3":
            display_tables(conn, cursor)
        elif choice == "4":
            truncate_all_tables(cursor)
            conn.commit()  # Commit truncations
        elif choice == "5":
            drop_project_tables(cursor)
            conn.commit()  # Commit after dropping tables
        elif choice == "6":
            query = input("Enter your SQL query: ")
            execute_query(cursor, query)
            conn.commit()  # Commit if there are changes
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Main entry point
if __name__ == "__main__":
    print("Welcome to Rent-A-Ride!")
    connect_prompt = input("Do you want to connect to the server? (y/n): ")
    if connect_prompt.lower() == 'y':
        conn, cursor = connect_db()
        
        if conn and cursor:
            print("Connected to the server successfully!")
            main_menu(conn, cursor)
            # Close the connection after all operations
            cursor.close()
            conn.close()
        else:
            print("Failed to connect to the database.")
    else:
        print("Exiting without connecting to the server.")
