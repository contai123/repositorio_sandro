import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",  
    user="users",       
    password="1234",       
    database="insta_python"  
)

cursor = conn.cursor()


cursor.execute("SELECT ID, Nickname, Seguidores, Seguindo, Postagens FROM users WHERE Postagens > 10 AND Seguidores > 200 ORDER BY Seguidores DESC, Postagens DESC  LIMIT 5")
resultados = cursor.fetchall()
for row in resultados:
    print(row)
    
    engine = create_engine("mysql+pymysql://users:1234@localhost:3306/insta_python")    
    query = "select * from users"  
    df = pd.read_sql(query, engine)
    df.to_excel('dados_instagram.xlsx', index=False)

cursor.close()
conn.close()
