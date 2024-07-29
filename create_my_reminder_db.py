import sqlite3
conn = sqlite3.connect('reminders.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE reminder (id INTEGER PRIMARY KEY, reminder char(100) NOT NULL)")
conn.execute("INSERT INTO reminder (reminder) VALUES ('This is where you can save reminders')")
conn.commit()