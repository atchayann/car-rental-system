import cx_Oracle

def insert_sample_data(conn, cursor):
    try:
        # Insert sample data into Branch table
        branches = [
            (1, 'Chennai', 'Tamil Nadu'),
            (2, 'Mumbai', 'Maharashtra'),
            (3, 'Bangalore', 'Karnataka'),
            (4, 'Delhi', 'Delhi'),
            (5, 'Hyderabad', 'Telangana')
        ]
        cursor.executemany("INSERT INTO Branch (BranchID, City, State) VALUES (:1, :2, :3)", branches)
        conn.commit()

        # Insert sample data into Car table (requires Branch to exist)
        cars = [
            (1, 'Toyota', 'Camry', 2018, 2019, 1),
            (2, 'Honda', 'Civic', 2019, 2020, 2),
            (3, 'Ford', 'Mustang', 2020, 2021, 3),
            (4, 'Chevrolet', 'Impala', 2015, 2016, 4),
            (5, 'BMW', 'X5', 2021, 2022, 5)
        ]
        cursor.executemany("INSERT INTO Car (CarID, Make, Model, ManufactureYear, ModelYear, BranchID) VALUES (:1, :2, :3, :4, :5, :6)", cars)
        conn.commit()

        # Insert sample data into CarColors table (requires Car to exist)
        car_colors = [
            (1, 'White'), (2, 'Black'), (3, 'Blue'),
            (4, 'Red'), (5, 'Silver')
        ]
        cursor.executemany("INSERT INTO CarColors (CarID, Color) VALUES (:1, :2)", car_colors)
        conn.commit()

        # Insert sample data into Customer table (no dependencies)
        customers = [
            (1, 'Alice Johnson', '15 Maple St', 'Downtown', '555-1234'),
            (2, 'Bob Smith', '22 Oak Ave', 'Uptown', '555-5678'),
            (3, 'Charlie Brown', '37 Pine Rd', 'Midtown', '555-9101'),
            (4, 'David Lee', '49 Elm St', 'Old Town', '555-1235'),
            (5, 'Emily Clark', '12 Cedar Dr', 'East Side', '555-5679'),
            (6, 'Frank Moore', '65 Birch Ln', 'West End', '555-9102')
        ]
        cursor.executemany("INSERT INTO Customer (CustomerID, Name, Street, Area, Phone) VALUES (:1, :2, :3, :4, :5)", customers)
        conn.commit()

        # Insert sample data into Employee table (requires Branch to exist, each branch gets 1 employee)
        employees = [
            (1, 'Daniel Roberts', 'Manager', 70000, 1),
            (2, 'Eva White', 'Sales', 50000, 2),
            (3, 'Frank Green', 'Technician', 55000, 3),
            (4, 'George Martin', 'Manager', 72000, 4),
            (5, 'Helen Brown', 'Sales', 51000, 5)
        ]
        cursor.executemany("INSERT INTO Employee (EmployeeID, Name, Position, Salary, BranchID) VALUES (:1, :2, :3, :4, :5)", employees)
        conn.commit()

        # Insert sample data into RentalAgreement table (requires Car, Customer, Branch to exist)
        rental_agreements = [
            (1, '2024-11-01', '2024-11-05', 1, 1, 1),
            (2, '2024-11-02', '2024-11-10', 2, 2, 2),
            (3, '2024-11-03', '2024-11-12', 3, 3, 3),
            (4, '2024-11-04', '2024-11-09', 4, 4, 4),
            (5, '2024-11-05', '2024-11-15', 5, 5, 5),
            (6, '2024-11-06', '2024-11-08', 1, 6, 1),
            (7, '2024-11-07', '2024-11-14', 2, 3, 2),
            (8, '2024-11-08', '2024-11-18', 3, 4, 3),
            (9, '2024-11-09', '2024-11-13', 4, 5, 4),
            (10, '2024-11-10', '2024-11-17', 5, 6, 5)
        ]
        cursor.executemany("INSERT INTO RentalAgreement (RentalID, RentalDate, ReturnDate, CarID, CustomerID, BranchID) VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6)", rental_agreements)
        conn.commit()

        # Insert sample data into InsurancePolicy table (requires RentalAgreement to exist)
        insurance_policies = [
            (1, 100000, 1), (2, 150000, 2), (3, 200000, 3),
            (4, 120000, 4), (5, 160000, 5), (6, 220000, 6),
            (7, 130000, 7), (8, 180000, 8), (9, 250000, 9),
            (10, 140000, 10)
        ]
        cursor.executemany("INSERT INTO InsurancePolicy (PolicyID, CoverageAmount, RentalID) VALUES (:1, :2, :3)", insurance_policies)
        conn.commit()

        print("Sample records inserted successfully.")

    except cx_Oracle.DatabaseError as e:
        print(f"Error: {e}")
