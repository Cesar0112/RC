import http.client
import argparse

def send_http_request(server_host, server_port, file_path):
    # Establecer la conexión con el servidor
    conn = http.client.HTTPConnection(server_host, server_port)

    # Enviar la solicitud HTTP GET
    conn.request("GET", file_path)

    # Obtener la respuesta del servidor
    response = conn.getresponse()

    # Imprimir la respuesta del servidor
    print(response.read().decode())

    # Cerrar la conexión
    conn.close()

def main():
    # Configurar los argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description='Cliente HTTP')
    parser.add_argument('servidor_host', help='Dirección IP del servidor o nombre del host')
    parser.add_argument('servidor_puerto', type=int, help='Puerto en el que el servidor está escuchando')
    parser.add_argument('nombre_archivo', help='Ruta en la que el objeto solicitado está almacenado en el servidor')

    # Analizar los argumentos de la línea de comandos
    args = parser.parse_args()

    # Enviar la solicitud HTTP al servidor
    send_http_request(args.servidor_host, args.servidor_puerto, args.nombre_archivo)

if __name__ == "__main__":
    main()
