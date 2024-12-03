import asyncio
import websockets

# Função para conectar ao servidor WebSocket e receber o arquivo
async def get_perfil_excel():
    uri = "ws://localhost:8765"  # Endereço do servidor WebSocket
    try:
        # Tenta se conectar ao servidor WebSocket
        async with websockets.connect(uri) as websocket:
            # Receber os dados (arquivo binário) do servidor
            file_data = await websocket.recv()
            
            # Verificar se o servidor enviou uma resposta de erro ou o arquivo
            if file_data == b"Arquivo nao encontrado!":
                print("Arquivo não encontrado no servidor.")
            else:
                # Salvar o arquivo Excel recebido
                with open("detalhes_usuarios_recebido.xlsx", 'wb') as file:
                    file.write(file_data)  # Salva os dados binários recebidos no arquivo
                print("Arquivo Excel recebido e salvo como 'detalhes_usuarios_recebido.xlsx'")
    except Exception as e:
        print(f"Erro na conexão: {e}")

# Iniciar o cliente
if __name__ == "__main__":
    asyncio.run(get_perfil_excel())  # Utiliza asyncio.run() para rodar a função assíncrona
