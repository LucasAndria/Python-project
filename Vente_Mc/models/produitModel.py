import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LUCAS\SQLEXPRESS04;'
                      'Database=Vente;'
                      'Trusted_Connection=yes;')

def listProduit():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Vente.dbo.Prod')
    return cursor

def addProduit():
    pass

def updateProduitById():
    pass