import mysql.connector
conn = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="",       
    database="db_python"  
)

cursor = conn.cursor()

# cursor.execute("SELECT * FROM perfis")

id = input("diga o id")
idPerfil = input("diga o idPerfil")
nome= input("diga o nome")
numSeg = input("diga o numseg")
numPost = input("diga o numposts")
numSeguindo= input("diga o numseguindo")



cursor.execute("INSERT INTO perfis (id, idPerfil, nomePerfil, numSeguidores, numPosts, numSeguindo) "
    "VALUES (%s, %s, %s, %s, %s, %s)", 
    (id, idPerfil, nome, numSeg, numPost, numSeguindo))


conn.commit()

cursor.execute("SELECT * FROM perfis")
resultados = cursor.fetchall()
for row in resultados:
    print(row)


cursor.close()
conn.close()
