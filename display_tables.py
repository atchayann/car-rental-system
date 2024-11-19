import cx_Oracle

def display_tables(conn, cursor):
    try:
        # Branch table display
        cursor.execute("SELECT * FROM Branch")
        print("\nBranch Table:")
        branch_columns = ["BranchID", "City", "State"]
        branch_data = cursor.fetchall()
        max_lengths = [max(len(str(row[i])) for row in branch_data) for i in range(len(branch_columns))]
        
        # Print column headers with proper alignment
        print(f"{branch_columns[0]:<{max_lengths[0]}} | {branch_columns[1]:<{max_lengths[1]}} | {branch_columns[2]:<{max_lengths[2]}}")
        
        # Print data
        for row in branch_data:
            print(f"{row[0]:<{max_lengths[0]}} | {row[1]:<{max_lengths[1]}} | {row[2]:<{max_lengths[2]}}")
        
        # Car table display
        cursor.execute("SELECT * FROM Car")
        print("\nCar Table:")
        car_columns = ["CarID", "Make", "Model", "ManufactureYear", "ModelYear", "BranchID"]
        car_data = cursor.fetchall()
        max_lengths = [max(len(str(row[i])) for row in car_data) for i in range(len(car_columns))]
        
        # Print column headers with proper alignment
        print(f"{car_columns[0]:<{max_lengths[0]}} | {car_columns[1]:<{max_lengths[1]}} | {car_columns[2]:<{max_lengths[2]}} | {car_columns[3]:<{max_lengths[3]}} | {car_columns[4]:<{max_lengths[4]}} | {car_columns[5]:<{max_lengths[5]}}")
        
        # Print data
        for row in car_data:
            print(f"{row[0]:<{max_lengths[0]}} | {row[1]:<{max_lengths[1]}} | {row[2]:<{max_lengths[2]}} | {row[3]:<{max_lengths[3]}} | {row[4]:<{max_lengths[4]}} | {row[5]:<{max_lengths[5]}}")
        
        # CarColors table display
        cursor.execute("SELECT * FROM CarColors")
        print("\nCarColors Table:")
        carcolors_columns = ["CarID", "Color"]
        carcolors_data = cursor.fetchall()
        max_lengths = [max(len(str(row[i])) for row in carcolors_data) for i in range(len(carcolors_columns))]
        
        # Print column headers with proper alignment
        print(f"{carcolors_columns[0]:<{max_lengths[0]}} | {carcolors_columns[1]:<{max_lengths[1]}}")
        
        # Print data
        for row in carcolors_data:
            print(f"{row[0]:<{max_lengths[0]}} | {row[1]:<{max_lengths[1]}}")
        
        # Customer table display
        cursor.execute("SELECT * FROM Customer")
        print("\nCustomer Table:")
        customer_columns = ["CustomerID", "Name", "Street", "Area", "Phone"]
        customer_data = cursor.fetchall()
        max_lengths = [max(len(str(row[i])) for row in customer_data) for i in range(len(customer_columns))]
        
        # Print column headers with proper alignment
        print(f"{customer_columns[0]:<{max_lengths[0]}} | {customer_columns[1]:<{max_lengths[1]}} | {customer_columns[2]:<{max_lengths[2]}} | {customer_columns[3]:<{max_lengths[3]}} | {customer_columns[4]:<{max_lengths[4]}}")
        
        # Print data
        for row in customer_data:
            print(f"{row[0]:<{max_lengths[0]}} | {row[1]:<{max_lengths[1]}} | {row[2]:<{max_lengths[2]}} | {row[3]:<{max_lengths[3]}} | {row[4]:<{max_lengths[4]}}")
        
        # Employee table display
        cursor.execute("SELECT * FROM Employee")
        print("\nEmployee Table:")
        employee_columns = ["EmployeeID", "Name", "Position", "Salary", "BranchID"]
        employee_data = cursor.fetchall()
        max_lengths = [max(len(str(row[i])) for row in employee_data) for i in range(len(employee_columns))]
        
        # Print column headers with proper alignment
        print(f"{employee_columns[0]:<{max_lengths[0]}} | {employee_columns[1]:<{max_lengths[1]}} | {employee_columns[2]:<{max_lengths[2]}} | {employee_columns[3]:<{max_lengths[3]}} | {employee_columns[4]:<{max_lengths[4]}}")
        
        # Print data
        for row in employee_data:
            print(f"{row[0]:<{max_lengths[0]}} | {row[1]:<{max_lengths[1]}} | {row[2]:<{max_lengths[2]}} | {row[3]:<{max_lengths[3]}} | {row[4]:<{max_lengths[4]}}")
        
        # RentalAgreement table display
        cursor.execute("""
            SELECT RentalID, 
                TO_CHAR(RentalDate, 'YYYY-MM-DD') AS RentalDate,
                TO_CHAR(ReturnDate, 'YYYY-MM-DD') AS ReturnDate,
                CarID, CustomerID, BranchID
            FROM RentalAgreement
        """)
        print("\nRentalAgreement Table:")
        rentalagreement_columns = ["RentalID", "RentalDate", "ReturnDate", "CarID", "CustomerID", "BranchID"]
        rentalagreement_data = cursor.fetchall()
        max_lengths = [max(len(str(row[i])) for row in rentalagreement_data) for i in range(len(rentalagreement_columns))]

        # Print column headers with proper alignment
        print(f"{rentalagreement_columns[0]:<{max_lengths[0]}} | {rentalagreement_columns[1]:<{max_lengths[1]}} | {rentalagreement_columns[2]:<{max_lengths[2]}} | {rentalagreement_columns[3]:<{max_lengths[3]}} | {rentalagreement_columns[4]:<{max_lengths[4]}} | {rentalagreement_columns[5]:<{max_lengths[5]}}")

        # Print data
        for row in rentalagreement_data:
            print(f"{row[0]:<{max_lengths[0]}} | {row[1]:<{max_lengths[1]}} | {row[2]:<{max_lengths[2]}} | {row[3]:<{max_lengths[3]}} | {row[4]:<{max_lengths[4]}} | {row[5]:<{max_lengths[5]}}")

        # InsurancePolicy table display
        cursor.execute("SELECT * FROM InsurancePolicy")
        print("\nInsurancePolicy Table:")
        insurancepolicy_columns = ["PolicyID", "CoverageAmount", "RentalID"]
        insurancepolicy_data = cursor.fetchall()
        max_lengths = [max(len(str(row[i])) for row in insurancepolicy_data) for i in range(len(insurancepolicy_columns))]
        
        # Print column headers with proper alignment
        print(f"{insurancepolicy_columns[0]:<{max_lengths[0]}} | {insurancepolicy_columns[1]:<{max_lengths[1]}} | {insurancepolicy_columns[2]:<{max_lengths[2]}}")
        
        # Print data
        for row in insurancepolicy_data:
            print(f"{row[0]:<{max_lengths[0]}} | {row[1]:<{max_lengths[1]}} | {row[2]:<{max_lengths[2]}}")
    
    except cx_Oracle.DatabaseError as e:
        print(f"Error: {e}")

