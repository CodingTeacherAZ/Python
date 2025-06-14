''' Most commonly used data types in SQLite databases:
Type         Python Equivalent    Use
NULL         NoneType             Means 'know nothing about it'
INETEGER    int                     integers
REAL         float                   8-byte floating point number
TEXT         str                     Strings of characters
BLOB         bytes                  Binary data (Binary Language OBject):  image, MP3, etc
'''

import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

# Drop the table if it exists
cur.execute('DROP TABLE IF EXISTS PopByRegion')

## A column in a table that is used to uniquely identify the 
## row of data is called a KEY.
## PRIMARY KEY causes the database to enforce unique KEYS

# Create the table
cur.execute('''
            CREATE TABLE IF NOT EXISTS PopByRegion(
            Region TEXT NOT NULL,
            Population INTEGER,
            PRIMARY KEY (Region)
            )
            ''')

# Code to create the table entries: Estimated World Populations in 2300
cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330933)')
cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 10062)')
cur.execute('INSERT INTO PopByRegion VALUES (?, ?)', ("North America", 661157))
cur.execute('INSERT INTO PopByRegion VALUES (?, ?)', ("Northern Africa", 1037463))
cur.execute('INSERT INTO PopByRegion VALUES (?, ?)', ("Southern Asia", 2051941))
cur.execute('INSERT INTO PopByRegion VALUES (?, ?)', ("Asia Pacific", 785468))
cur.execute('INSERT INTO PopByRegion VALUES("Middle East", 687630)')
cur.execute('INSERT INTO PopByRegion VALUES(?, ?)', ("Eastern Asia", 1362955))
cur.execute('INSERT INTO PopByRegion VALUES(?, ?)', ('South America', 593121))
cur.execute('INSERT INTO PopByRegion VALUES("Eastern Europe", 223427)')
cur.execute('INSERT INTO PopByRegion VALUES(?, ?)', ("Western Europe", 387933))

# Commit changes to the database
con.commit()

# Execute a SELECT statement
cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Population DESC')
print(cur.fetchone())
print(cur.fetchall())
print(cur.fetchone())  #once it has been fetched, subsequent fetches are empty
print(cur.fetchall())

# Select by name
cur.execute('SELECT Region from PopByRegion')
print(cur.fetchall())

# use * to indicate that we want al columns
cur.execute('SELECT * from PopByRegion')
print(cur.fetchall())

# Query Conditions
# WHERE uses = (equal to), !=, >, <, >=, <=, AND, OR, NOT
# WHERE applied row by row so cannot be used to compare two rows
cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000')
print(cur.fetchall())

cur.execute('''SELECT Region FROM PopByRegion WHERE Population > 1000000 AND Region < "L" ''')
print(cur.fetchall())

# Updating and Deleting
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan" ')
print(cur.fetchone())
cur.execute('''UPDATE PopByRegion SET Population = 100600 WHERE Region ="Japan" ''')
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print(cur.fetchone())

# Using NULL for Missing Data
cur.execute('INSERT INTO PopByRegion VALUES ("Antartica", NULL)')


#### Relational Databases

# Drop the table if it exists
con.execute('DROP TABLE IF EXISTS PopByCountry')

## CONSTRAINT is used to specify that no two entries in the table
## being created will every have the same values for region and country

# Create the table with 2300 projec4ed populations by country
cur.execute('''
                CREATE TABLE PopByCountry(
                Region TEXT NOT NULL,
                Country TEXT NOT NULL,
                Population INTEGER,
                CONSTRAINT CountryKey PRIMARY KEY (Region, Country))''')
countries = [("Eastern Asia", "DPR Korea", 24056), ("Eastern Asia", "Hong Kong (China)", 8764),
            ("Eastern Asia", "Mongolia", 3407), ("Eastern Asia", "Republic of Korea", 41491),
            ("Eastern Asia", "Taiwan", 1433), ("North America", "Bahamas", 368),
            ("North America", "Canada", 40876), ("North America", "Greenland", 43),
            ("North America", "Mexico", 126875), ("North America", "United States", 493038)]


#Populate the table
for country in countries:
    cur.execute('INSERT INTO PopByCountry VALUES (?, ?, ?)', (country[0], country[1], country[2]))
    con.commit()
                                                                                
#### INNER JOINS
#  1. All combinations or rows in the tables are combined
#  2. Selection criteria WHERE is applied and rows that don't match are removed
#  3. Selected columns are kept, others discarded

# inner-join the tables and select by region and population greater than 1billion people
cur.execute('''
            SELECT PopByRegion.Region, PopByCountry.Country
            FROM PopByRegion INNER JOIN PopByCountry
            WHERE (PopByRegion.Region = PopByCountry.Region)
            AND (PopByRegion.Population > 1000000)
            ''')
print(cur.fetchall())

# removing duplicates
cur.execute('''
            SELECT DISTINCT PopByRegion.Region
            FROM PopByRegion INNER JOIN PopByCountry
            WHERE (PopByRegion.Region = PopByCountry.Region)
            AND ((PopByCountry.Population * 1.0) / PopbyRegion.Population > 0.10)
            ''')
print(cur.fetchall())


## AGGREGATE FUNCTIONS
# AVG: average of the values
# MIN: minimum of the values
# MAX: maximum of the values
# COUNT: Number of all nonnull values
# SUM: sum of the values
# Calculate the total projected world population for 2300 by applying
#  SQL aggregate function SUM on the PopByRegion Population
cur.execute('SELECT SUM (Population) FROM PopByRegion')
print(cur.fetchone())
cur.execute('SELECT COUNT (Population) FROM PopByRegion')
print(cur.fetchone())
cur.execute("SELECT MIN (Population) From PopByRegion")
print(cur.fetchone())
cur.execute("SELECT MAX (Population) FROM PopByRegion")
print(cur.fetchone())
cur.execute("SELECT AVG (Population) FROM PopByRegion")
print(cur.fetchone())

## GROUPING
cur.execute('''SELECT Region, SUM (Population) FROM PopByCountry
                GROUP BY Region''')
print(cur.fetchall())

cur.execute('''SELECT SUM (Population) FROM PopByCountry
                WHERE Region = "North America" ''')
print(cur.fetchall())
cur.execute('''SELECT SUM (Population) FROM PopByCountry
                WHERE Region = "Eastern Asia" ''')
print(cur.fetchall())

###### SELF JOINS
# allows us to compare two lines in the same table or
# two lines in two different tables
cur.execute('''
SELECT A.Country, B.Country
FROM   PopByCountry A INNER JOIN PopByCountry B
WHERE  (ABS(A.Population - B.Population) <= 1000) 
AND     (A.Country < B.Country) ''')  #if you use !=, you will get duplicate pairs
print(cur.fetchall())


##### NESTED QUERIES
# since the result of every query is a table with a fixed number of
# columns and some number of rows, we can run a second SELECT
#  usually used when negation is involved (NOT IN)

# query PopByCountry to get regions that do NOT have a country
# with a populatio of 8,764, 000
cur.execute('''
    SELECT DISTINCT Region
    FROM PopByCountry
    WHERE (PopByCountry.Population = 8764) ''')
print(cur.fetchall())
cur.execute('''
    SELECT DISTINCT Region
    FROM PopByCountry
    WHERE Region NOT IN
        (SELECT DISTINCT Region
        FROM PopByCountry
        WHERE (PopByCountry.Population = 8764))
    ''')
print(cur.fetchall())



#### TRANSACTION
#  A transaction s a sequence of database operations that are
# independent.  No operation in a transaction can be committed
#  unles every sing one can be successfully commited in sequence
# for example:  paying an employee involves a withdraw fom the
# employer's account and a deposit to the employee's account

# If one operation fails, the transaction must be ROLLED BACK
# which causes all the operations in the transaction to be undone.





# Close the cursor and connection
cur.close()
con.close()
