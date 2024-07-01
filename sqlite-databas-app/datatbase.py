import sqlite3

# def Create():
#     conn = sqlite3.connect('customer.db')
#     c = conn.cursor()

#     c.execute("CREATE TABLE customers (frist_name text, last_name text, email text)")
    
#     data = [
#         ('sidi', 'ahmed', 'sidiahmed@exemple.com'),
#         ('zeinab', 'ahmed', 'sidiahmed@exemple.com'),
#         ('med', 'ahmed', 'sidiahmed@exemple.com'),
#         ('sidi', 'lemine', 'sidiahmed@exemple.com'),
#         ('mariem', 'ahmed', 'sidiahmed@exemple.com'),
#         ('sidi', 'taleb', 'sidiahmed@exemple.com'),
#         ('sidi', 'abrahim', 'sidiahmed@exemple.com'),
#     ]
#     c.executemany("INSERT INTO customers VALUES (?,?,?)",data)

#     print("Done")
#      # Commit our command
#     conn.commit()
#     # Close our connection
#     conn.close()

#Query the DB and return all records
def show_all():
    #connect to database and create a cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    #Query The database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()    


#Add A new Record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    # Commit our command and Close our connection
    conn.commit()
    conn.close()  

#Add many Records to the table
def add_many(List):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (List))
    # Commit our command and Close our connection
    conn.commit()
    conn.close()  

  

#Delete Record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid =(?)", id)
    # Commit our cmd and Close connection
    conn.commit()
    conn.close()    


#look up with wehre 
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)
    
    # Commit our cmd and Close connection
    conn.commit()
    conn.close() 