import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "123456",
  database= "music"
)

cursor = mydb.cursor()



def update (album_a_cambiar, year_a_cambiar, artist_a_cambiar, album_nuevo, year_nuevo, artist_nuevo):
    sql = "UPDATE albums SET name = %s WHERE name = %s"
    sql2 = "UPDATE albums SET year = %s WHERE year = %s"
    sql3 = "UPDATE albums SET artist = %s WHERE artist = %s"
    val = (album_nuevo, album_a_cambiar)
    val2 = (year_nuevo, year_a_cambiar)
    val3 = (artist_nuevo, artist_a_cambiar)

    queries = [sql, sql2, sql3]
    data = [val, val2, val3]
    cursor.execute(queries[0], data[0])
    mydb.commit()
    cursor.execute(queries[1], data[1])
    mydb.commit()
    cursor.execute(queries[2], data[2])
    mydb.commit()

def create (album, year, artist):

    sql = "INSERT INTO albums (name, year, artist) VALUES (%s, %s, %s)"
    val = (album, year, artist)
    cursor.execute(sql, val)

    mydb.commit()   
    print(cursor.rowcount, "record inserted.")


def delete (id):
    sql = f"DELETE FROM albums WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)

    mydb.commit()   
    print(cursor.rowcount, "record deleted.")
delete("5")
def read ():
    cursor.execute("SELECT * FROM albums")
    
    for x in cursor:
        print(x)