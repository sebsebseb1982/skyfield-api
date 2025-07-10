# Utiliser une image officielle de Python comme image de base
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances (si tu as un requirements.txt)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source dans le conteneur
COPY src/ ./src/

# Exposer le port utilisé par l'application
EXPOSE 8000

# Lancer l'application avec uvicorn
CMD ["uvicorn", "src.api.api:app", "--host", "0.0.0.0", "--port", "8000"]