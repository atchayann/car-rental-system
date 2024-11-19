# drop_project_tables.py
import cx_Oracle

def drop_project_tables(cursor):
    tables = [
        "InsurancePolicy",
        "RentalAgreement",
        "CarColors",
        "Car",
        "Employee",
        "Customer",
        "Branch"
    ]

    for table in tables:
        try:
            cursor.execute(f"DROP TABLE {table} CASCADE CONSTRAINTS")
            print(f"Table {table} dropped successfully.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error dropping table {table}: {e}")