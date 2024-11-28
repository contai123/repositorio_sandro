import os
import requests
import http.client
import json
import pandas as pd

def buscar_perfis_rapidapi(palavra_chave):
    
    conn = http.client.HTTPSConnection("instagram-scraper-api2.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "bcfad742aemsh7e2de12c9c28586p18af25jsnca1fbf81bc06",
        'x-rapidapi-host': "instagram-scraper-api2.p.rapidapi.com"
    }

    # params = {"query": palavra_chave}

    try:
        # conn.request("GET", "/v1/followers?username_or_id_or_url=mrbeast", headers=headers)
        conn.request("GET", f"/v1/followers?username_or_id_or_url={palavra_chave}", headers=headers)
        response = conn.getresponse()
        
        if response.status == 200:
            try:
                data = response.read().decode("utf-8")
                data_json = json.loads(data)

                with open("resultado.json.txt", "w", encoding="utf-8") as file:
                    json.dump(data_json, file, indent=4, ensure_ascii=False)
                    
                usernames = [
                    item["username"] 
                    for item in data_json.get("data", {}).get("items", [])
                ]
                
                return usernames

            except ValueError:
                print("A resposta não está no formato JSON.")
                return []
        else:
            print(f"Erro na resposta: {response.status}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return []

if __name__ == "__main__":
    palavra_chave = "programming"
    usernames = buscar_perfis_rapidapi(palavra_chave)
    print("Usernames coletados:", usernames)