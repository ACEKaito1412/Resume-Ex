from cs50 import SQL

db = SQL('sqlite:///resource.db')

rows = db.execute("SELECT COUNT(*) as n FROM data")

for row in rows:
    print(row['n'])