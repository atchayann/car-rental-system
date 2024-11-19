import cx_Oracle

# Function to create tables
def create_tables(conn, cursor):
    try:
        # Create Branch table first as others depend on it
        cursor.execute('''CREATE TABLE Branch (
            BranchID NUMBER PRIMARY KEY,
            City VARCHAR2(50),
            State VARCHAR2(50)
        )''')
        print("Table Branch created successfully.")

        # Create Car table (depends on Branch table)
        cursor.execute('''CREATE TABLE Car (
            CarID NUMBER PRIMARY KEY,
            Make VARCHAR2(50) NOT NULL,
            Model VARCHAR2(50) NOT NULL,
            ManufactureYear NUMBER(4) NOT NULL,
            ModelYear NUMBER(4) NOT NULL,
            BranchID NUMBER,
            CONSTRAINT FK_CAR_BRANCHID FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)
        )''')
        print("Table Car created successfully.")

        # Create CarColors table (depends on Car table)
        cursor.execute('''CREATE TABLE CarColors (
            CarID NUMBER,
            Color VARCHAR2(30),
            PRIMARY KEY (CarID, Color),
            CONSTRAINT FK_CARCOLORS_CARID FOREIGN KEY (CarID) REFERENCES Car(CarID)
        )''')
        print("Table CarColors created successfully.")

        # Create Customer table (no dependencies)
        cursor.execute('''CREATE TABLE Customer (
            CustomerID NUMBER PRIMARY KEY,
            Name VARCHAR2(100) NOT NULL,
            Street VARCHAR2(100),
            Area VARCHAR2(100),
            Phone VARCHAR2(15)
        )''')
        print("Table Customer created successfully.")

        # Create Employee table (depends on Branch table)
        cursor.execute('''CREATE TABLE Employee (
            EmployeeID NUMBER PRIMARY KEY,
            Name VARCHAR2(100),
            Position VARCHAR2(50),
            Salary NUMBER,
            BranchID NUMBER,
            CONSTRAINT FK_EMPLOYEE_BRANCHID FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)
        )''')
        print("Table Employee created successfully.")

        # Create RentalAgreement table (depends on Car, Customer, and Branch tables)
        cursor.execute('''CREATE TABLE RentalAgreement (
            RentalID NUMBER PRIMARY KEY,
            RentalDate DATE,
            ReturnDate DATE,
            CarID NUMBER,
            CustomerID NUMBER,
            BranchID NUMBER,
            CONSTRAINT FK_RENTALAGREEMENT_CARID FOREIGN KEY (CarID) REFERENCES Car(CarID),
            CONSTRAINT FK_RENTALAGREEMENT_CUSTOMERID FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
            CONSTRAINT FK_RENTALAGREEMENT_BRANCHID FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)
        )''')
        print("Table RentalAgreement created successfully.")

        # Create InsurancePolicy table (depends on RentalAgreement table)
        cursor.execute('''CREATE TABLE InsurancePolicy (
            PolicyID NUMBER PRIMARY KEY,
            CoverageAmount NUMBER,
            RentalID NUMBER UNIQUE,
            CONSTRAINT FK_INSURANCEPOLICY_RENTALID FOREIGN KEY (RentalID) REFERENCES RentalAgreement(RentalID)
        )''')
        print("Table InsurancePolicy created successfully.")

    except cx_Oracle.DatabaseError as e:
        print(f"Error: {e}")
