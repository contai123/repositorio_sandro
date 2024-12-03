import mysql.connector
import pandas as pd
conn = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="",       
    database="insta_python"  
)

cursor = conn.cursor()

caminhodoarquivo = "C:/Users/ALUNO/Desktop/repositorio_sandro/detalhes_usuarios.xlsx"

def lerInserirArquivo(caminhodoarquivo):
    
    df = pd.read_excel(caminhodoarquivo)
    print(df.columns)
    df.columns = df.columns.str.strip()

    for index, row in df.iterrows():
        try:
            idPerfil = row['ID']
            nome = row['Nickname']
            numSeg = row['Seguidores']
            numSeguindo = row['Seguindo']
            numPost = row['Postagens']
            if int(numPost) > 10 and int(numSeg) > 200:
                cursor.execute("INSERT INTO users (ID, Nickname, Seguidores, Seguindo, Postagens) "
                               "VALUES (%s, %s, %s, %s, %s)", 
                               (idPerfil, nome, numSeg, numPost, numSeguindo))
                conn.commit()
                print(f"Dados inseridos para o id: {idPerfil}")
            else:
                print("Perfil não atende aos requisitos, que bad hein")
        except KeyError as e:
            print(f"Erro ao acessar a coluna: {e}") 
try:
   
    lerInserirArquivo(caminhodoarquivo)

    cursor.execute("SELECT * FROM users")
    resultados = cursor.fetchall()
    for row in resultados:
        print(row)

finally:
    cursor.close()
    conn.close()
