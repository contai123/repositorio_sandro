import http.client
import json
import pandas as pd
import instaloader
import time
import openpyxl

# Função para buscar perfis com RapidAPI
def buscar_perfis_rapidapi(palavra_chave):
    conn = http.client.HTTPSConnection("instagram-scraper-api2.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "bcfad742aemsh7e2de12c9c28586p18af25jsnca1fbf81bc06",
        'x-rapidapi-host': "instagram-scraper-api2.p.rapidapi.com"
    }

    try:
        conn.request("GET", f"/v1/followers?username_or_id_or_url={palavra_chave}", headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            data = response.read().decode("utf-8")
            data_json = json.loads(data)

            # Salva a resposta no arquivo
            with open("resultado.json", "w", encoding="utf-8") as file:
                json.dump(data_json, file, indent=4, ensure_ascii=False)

            # Extrai o ID dos usuários
            users_data = data_json.get("data", {}).get("items", []) or data_json.get("items", [])
            lista_username = [item["username"] for item in users_data if "username" in item]
            '''lista_id = [
                item["id"]
                for item in data_json.get("data", {}).get("users", [])
            ]'''
            return lista_username
        else:
            print(f"Erro na resposta da API: {response.status}")
            return []
    except Exception as e:
        print(f"Erro ao acessar a API: {e}")
        return []

# Função para buscar detalhes dos usuários com Instaloader
def buscar_detalhes(lista_username):
    loader = instaloader.Instaloader()
    dados_usuarios = []

    # Autenticação do Instaloader (se necessário)
    #loader.context.log("Logging in...")
    #loader.load_session_from_file("seu_usuario")  # Se você já tiver sessão salva
    #if not loader.context.is_logged_in:
    #loader.context.log("Login failed! Realizando login...")
    loader.login("bizu_java", "knn1056c")
    print('Você está logado')

    for username in lista_username:
        try:
            # Aqui, você pode passar diretamente o nome de usuário para o `Profile.from_username`
            # Se você tem o ID, precisará converter para nome de usuário de alguma forma
            perfil = instaloader.Profile.from_username(loader.context, username)

            # Coleta dados apenas de perfis públicos
            if not perfil.is_private:
                dados_usuarios.append({
                    "ID": perfil.userid,
                    "Nickname": perfil.username,
                    "Seguidores": perfil.followers,
                    "Seguindo": perfil.followees,
                    "Postagens": perfil.mediacount
                })
            else:
                print(f"Perfil {username} é privado. Ignorado.")

        except instaloader.exceptions.ProfileNotExistsException:
            print(f"Perfil {username} não encontrado.")
        except instaloader.exceptions.InstaloaderException as e:
            print(f"Erro ao buscar {username}: {e}")
        finally:
            # Adiciona um pequeno delay para evitar bloqueios
            time.sleep(1)

    # Retorna DataFrame com dados dos perfis públicos
    return pd.DataFrame(dados_usuarios)

# Função principal
if __name__ == "__main__":
    palavra_chave = "funny"  # Palavra-chave para busca
    print(f"Buscando perfis relacionados a: {palavra_chave}...")

    # Busca de perfis usando a API
    lista_username = buscar_perfis_rapidapi(palavra_chave)
    
    if lista_username:
        print(f"Perfis coletados: {len(lista_username)} perfis encontrados.")
        
        # Busca detalhes dos perfis usando instaloader
        detalhes = buscar_detalhes(lista_username)
        
        if not detalhes.empty:
            # Salvar os dados em formato Excel
            detalhes.to_excel("detalhes_usuarios.xlsx", index=False, engine="openpyxl")
            print("Dados salvos no arquivo 'detalhes_usuarios.xlsx'.")
        else:
            print("Nenhum perfil público encontrado para salvar.")
    else:
        print("Nenhum perfil encontrado.")


#buscar_perfis_rapidapi("java")
