import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()
#create table
cur.execute("CREATE TABLE movie(title, year, score)")

#insert data into movie table 

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")


#insert many data into table 
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)


#looping on each row of the movie table 
for row in cur.execute("SELECT * FROM movie ORDER BY year"):
    print(row)



#return all resulting rows:
res = cur.execute("SELECT * FROM movie")
print(res.fetchall())

print("Done")
con.commit()