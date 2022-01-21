import sqlite3
connection = sqlite3.connect("projects.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE projects
    (Manufacturer TEXT, Category TEXT, Product TEXT, UID INTEGER, Status TEXT)
""")
cursor.execute("""INSERT INTO projects VALUES 
    ('MIFARE', 'Classic', 'Staff Pass', 1900, '1/1/2022 12:00:00 PM'),
    ('EPCglobal', 'Class 1', 'Computer', 3000, '2/1/2022 3:00:00 PM'),
    ('ISO', '18000-6C', 'Sensor', 120000, '2/1/2022 5:00:00 PM')
""")
connection.commit()
