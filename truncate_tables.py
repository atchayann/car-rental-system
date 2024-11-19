import cx_Oracle

# Function to truncate all tables
def truncate_all_tables(cursor):
    try:
        # Disable foreign key constraints
        cursor.execute("ALTER TABLE InsurancePolicy DISABLE CONSTRAINT FK_INSURANCEPOLICY_RENTALID")
        cursor.execute("ALTER TABLE RentalAgreement DISABLE CONSTRAINT FK_RENTALAGREEMENT_CARID")
        cursor.execute("ALTER TABLE RentalAgreement DISABLE CONSTRAINT FK_RENTALAGREEMENT_CUSTOMERID")
        cursor.execute("ALTER TABLE RentalAgreement DISABLE CONSTRAINT FK_RENTALAGREEMENT_BRANCHID")
        cursor.execute("ALTER TABLE Employee DISABLE CONSTRAINT FK_EMPLOYEE_BRANCHID")
        cursor.execute("ALTER TABLE Car DISABLE CONSTRAINT FK_CAR_BRANCHID")
        cursor.execute("ALTER TABLE CarColors DISABLE CONSTRAINT FK_CARCOLORS_CARID")

        # Truncate tables in the correct order
        cursor.execute("TRUNCATE TABLE InsurancePolicy")
        cursor.execute("TRUNCATE TABLE RentalAgreement")
        cursor.execute("TRUNCATE TABLE Employee")
        cursor.execute("TRUNCATE TABLE Customer")
        cursor.execute("TRUNCATE TABLE CarColors")
        cursor.execute("TRUNCATE TABLE Car")
        cursor.execute("TRUNCATE TABLE Branch")

        # Re-enable foreign key constraints
        cursor.execute("ALTER TABLE InsurancePolicy ENABLE CONSTRAINT FK_INSURANCEPOLICY_RENTALID")
        cursor.execute("ALTER TABLE RentalAgreement ENABLE CONSTRAINT FK_RENTALAGREEMENT_CARID")
        cursor.execute("ALTER TABLE RentalAgreement ENABLE CONSTRAINT FK_RENTALAGREEMENT_CUSTOMERID")
        cursor.execute("ALTER TABLE RentalAgreement ENABLE CONSTRAINT FK_RENTALAGREEMENT_BRANCHID")
        cursor.execute("ALTER TABLE Employee ENABLE CONSTRAINT FK_EMPLOYEE_BRANCHID")
        cursor.execute("ALTER TABLE Car ENABLE CONSTRAINT FK_CAR_BRANCHID")
        cursor.execute("ALTER TABLE CarColors ENABLE CONSTRAINT FK_CARCOLORS_CARID")

        print("All tables truncated successfully.")

    except cx_Oracle.DatabaseError as e:
        print(f"Error: {e}")
