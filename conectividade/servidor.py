import asyncio
import websockets
import os

# Função que será executada quando um cliente se conectar
async def handler(websocket): #, path):
    try:
        # Enviar o arquivo Excel para o cliente
        print(f"Conexão estabelecida com {websocket.remote_address}")
        
        # Caminho do arquivo Excel gerado
        excel_file_path = "detalhes_usuarios.xlsx"
        
        # Verificar se o arquivo existe
        if os.path.exists(excel_file_path):
            # Abrir o arquivo em modo binário
            with open(excel_file_path, 'rb') as file:
                file_data = file.read()  # Lê todo o conteúdo binário do arquivo
            
            # Enviar o conteúdo binário para o cliente
            await websocket.send(file_data)
            print(f"Arquivo '{excel_file_path}' enviado para {websocket.remote_address}")
        else:
            print(f"Arquivo '{excel_file_path}' não encontrado!")
            await websocket.send("Arquivo não encontrado!")
    except Exception as e:
        print(f"Erro ao enviar o arquivo para o cliente: {e}")

# Função principal para iniciar o servidor
async def main():
    try:
        # Iniciar o servidor WebSocket
        server = await websockets.serve(handler, "localhost", 8765)
        print("Servidor WebSocket iniciado na porta 8765...")
        
        # Manter o servidor rodando
        await server.wait_closed()
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")

# Rodar o servidor WebSocket
if __name__ == "__main__":
    asyncio.run(main())  # Utiliza asyncio.run() para rodar o servidor WebSocket
