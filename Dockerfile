# Utiliser l'image officielle Ubuntu comme image de base
FROM ubuntu:latest

# Mettre à jour les listes de paquets et installer les paquets nécessaires
RUN apt-get update && \
    apt-get install -y nano iproute2 iputils-ping && \
    rm -rf /var/lib/apt/lists/* # Nettoyer le cache

# Commande par défaut pour garder le conteneur en vie
CMD ["tail", "-f", "/dev/null"]
