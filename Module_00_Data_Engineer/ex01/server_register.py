import requests

def register_server(server_name, host, port, username, password):
    base_url = 'http://localhost:5050'
    register_server_endpoint = '/api/servers'

    new_server_data = {
        'name': server_name,
        'host': host,
        'port': port,
        'username': username,
        'password': password
    }

    try:
        response = requests.post(base_url + register_server_endpoint, json=new_server_data)
        
        if response.status_code == 200:
            print("Servidor registrado correctamente en pgAdmin.")
        else:
            print("Error al registrar el servidor en pgAdmin. Código de estado:", response.status_code)
    
    except Exception as e:
        print("Error al registrar el servidor en pgAdmin:", e)

register_server(
    server_name='piscineds',
    host='localhost',
    port=5432,
    username='dgerwig',
    password='ueserpw'
)