import sqlite3

conn = sqlite3.connect("orgdb_assignment.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

fname = "mbox.txt"
try:
    fh = open(fname)
except:
    print("Unable to open the file", fname, "Quitting")
    quit()

for line in fh:
    if not line.startswith("From: "):
        continue
    try:
        org = line.split()[1].split("@")[1]
    except:
        continue

    cur.execute("SELECT count FROM Counts WHERE org = ? ", (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute(
            "INSERT INTO Counts (org, count) VALUES (?, 1)",
            (org,),
        )
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org,))

conn.commit()

# https://www.sqlite.org/lang_select.html
# sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"
# sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC"
#
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

cur.close()
