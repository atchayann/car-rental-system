import cx_Oracle

def execute_query(cursor, query):
    try:
        cursor.execute(query)
        
        # Check if the query is a SELECT statement
        if query.strip().lower().startswith("select"):
            # Fetch all rows and column names
            rows = cursor.fetchall()
            column_names = [col[0] for col in cursor.description]
            
            # Display column names
            print(" | ".join(column_names))
            print("-" * (len(" | ".join(column_names)) + len(column_names) * 3))
            
            # Display each row
            for row in rows:
                print(" | ".join(str(value) for value in row))
        else:
            # Commit for non-SELECT queries (INSERT, UPDATE, DELETE)
            cursor.connection.commit()
            print("Query executed successfully.")
            
    except cx_Oracle.DatabaseError as e:
        print(f"Error executing query: {e}")
