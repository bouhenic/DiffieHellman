import socket
import random

def diffie_hellman():
    # Choix des paramètres communs
    p = 23  # Nombre premier partagé
    g = 5   # Générateur partagé

    # Génération du nombre secret
    b = random.randint(1, p-1)  # Nombre secret du serveur
    # Calcul de la valeur publique
    B = pow(g, b, p)

    return p, g, b, B


def main():
    # Connexion au serveur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connexion établie avec le serveur...")
    
    # Échange des clés
    p, g, b, B = diffie_hellman()
    
    # Envoi de la valeur publique au serveur
    client_socket.sendall(str(B).encode())
    print("Valeur publique envoyée au serveur:", B)
    
    # Réception de la valeur publique du serveur
    A_received = int(client_socket.recv(1024).decode())
    print("Valeur publique reçue du serveur:", A_received)
    
    # Calcul de la clé secrète du client
    secret_key_client = pow(A_received, b, p)
    print("Clé secrète calculée par le client:", secret_key_client)
    
    # Fermeture de la connexion
    client_socket.close()

if __name__ == "__main__":
    main()
