import socket
import random

def diffie_hellman():
    # Choix des paramètres communs
    p = 23  # Nombre premier partagé
    g = 5   # Générateur partagé
    
    # Génération du nombre secret
    a = random.randint(1, p-1)  # Nombre secret du serveur
  
    # Calcul de la valeur publique
    A = pow(g, a, p)
    
    return p, g, a, A

def main():
    # Création de la socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Serveur en attente de connexion...")
    
    # Échange des clés
    conn, addr = server_socket.accept()
    print('Connexion établie avec', addr)
    
    # Serveur génère son nombre secret et sa valeur publique
    p, g, a, A = diffie_hellman()
    
    # Envoi de la valeur publique au client
    conn.sendall(str(A).encode())
    print("Attente de la valeur publique du client...")
    print("Valeur publique envoyée au client:", A)
    
    # Réception de la valeur publique du client
    B_received = int(conn.recv(1024).decode())
    print("Valeur publique reçue du client:", B_received)
    
    # Calcul de la clé secrète du serveur
    secret_key_server = pow(B_received, a, p)
    print("Clé secrète calculée par le serveur:", secret_key_server)
    
    # Fermeture de la connexion
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
