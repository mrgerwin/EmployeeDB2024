import sqlite3

class Database:
    def __init__(self, fn):
        self.db = sqlite3.connect(fn)
        self.conn = self.db.cursor()
        self.id = 1
        
    def createTable(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE(ID INT PRIMARY KEY NOT NULL, FIRSTNAME TEXT NOT NULL, LASTNAME TEXT NOT NULL, EMPLOYEENUM INT NOT NULL, SALARY REAL NOT NULL, JOB TEXT NOT NULL, YEARS INT NOT NULL);''')
        
    def addEmployee(self, fn, ln, en, sal, job, yrs):
        sql = 'INSERT INTO EMPLOYEE(ID, FIRSTNAME, LASTNAME, EMPLOYEENUM, SALARY, JOB, YEARS) VALUES (?,?,?,?,?,?,?);'
        self.conn.execute(sql, (self.id, fn, ln, en, sal, job, yrs))
        self.db.commit()
    
    def close(self):
        self.conn.close()
        
filename = "./employee.db"

db = Database(filename)

db.createTable()
db.addEmployee('test', 'testL', 1, 200000, 'testJob', 20)
db.close()