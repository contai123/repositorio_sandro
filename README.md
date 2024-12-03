# PyPerfil

Este repositório contém o código do projeto **PyPerfil**, que utiliza a **Instagram Scraper API** hospedada na RapidAPI para coletar informações sobre os seguidores de um perfil do Instagram. O objetivo do projeto é buscar seguidores de um perfil (usando um nome de usuário ou hashtag), armazenar as informações em um arquivo JSON e extrair os nomes de usuário desses seguidores.

## Funcionalidades

- **Buscar Perfis no Instagram**: Coleta seguidores de um perfil do Instagram utilizando a API RapidAPI.
- **Armazenar Dados em JSON**: Os dados coletados, incluindo os nomes de usuário dos seguidores, são armazenados em um arquivo JSON.
- **Extração de Usernames**: Extrai os nomes de usuário dos seguidores coletados pela API.

## Requisitos

Este projeto utiliza as bibliotecas do Python para fazer requisições HTTP e manipular dados JSON:

- **requests**: Para fazer requisições à API do Instagram Scraper.
- **json**: Para manipulação e armazenamento dos dados no formato JSON.

Você pode instalar a biblioteca `requests` usando o comando:

```bash
pip install requests
