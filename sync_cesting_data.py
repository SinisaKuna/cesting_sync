import pyodbc
import mysql.connector


def connect_cesting(data_base):
    # *** CESTING SERVER ***
    server = '213.202.107.109,1433'
    database = data_base
    username = 'sa'
    password = '@betaStudio2017'
    conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD=' + password)
    return conn    


def connect_mysql():
    # *** betastudio.hr ***
    conn = mysql.connector.connect(
        host="178.218.166.150",
        user="betastudio_sa",
        password="@korisnik",
        database="betastudio_dbbetasoft"
    )
    return conn


# kupci
myconn = connect_mysql()
mycursor = myconn.cursor()
myquery = "delete from kupci"
mycursor.execute(myquery)

conn = connect_cesting('cesting_2022')
cursor = conn.cursor()
query = "select sifra, naziv, duguje from web_rang_lista_1200 where dug != 0 order by dug desc"
cursor.execute(query)
result = cursor.fetchall()

polja = "sifra, naziv, duguje"
for redak in result:
    query = "insert into kupci (" + str(polja) + ") values " + str(redak)
    myconn.cursor().execute(query)
myconn.commit()

# dobavljači
myconn = connect_mysql()
mycursor = myconn.cursor()
myquery = "delete from dobavljaci"
mycursor.execute(myquery)

conn = connect_cesting('cesting_2022')
cursor = conn.cursor()
query = "select sifra, naziv, potrazuje from web_rang_lista_2200 where pot != 0 order by pot desc"
cursor.execute(query)
result = cursor.fetchall()

polja = "sifra, naziv, potrazuje"
for redak in result:
    query = "insert into dobavljaci (" + str(polja) + ") values " + str(redak)
    myconn.cursor().execute(query)
myconn.commit()

# prosjek_place
myconn = connect_mysql()
mycursor = myconn.cursor()
myquery = "delete from prosjek_place"
mycursor.execute(myquery)

conn = connect_cesting('placa_0000')
cursor = conn.cursor()
query = "select prezime_ime, obj, radno_mjesto, netto, brutto, brutto_II from web_analiza_prosjeka_primanja order by prezime_ime"
cursor.execute(query)
result = cursor.fetchall()

polja = "prezime_ime, obj, radno_mjesto, netto, brutto, brutto_II"
for redak in result:
    query = "insert into prosjek_place (" + str(polja) + ") values " + str(redak)
    myconn.cursor().execute(query)
myconn.commit()
