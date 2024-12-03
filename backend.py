from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/<folder_name>', methods=['GET'])
def get_images(folder_name):
    # Utiliser le paramètre folder_name pour définir le chemin du dossier
    IMAGE_FOLDER = os.path.join(os.getcwd(), folder_name)
    
    # Vérifier si le dossier existe
    if not os.path.exists(IMAGE_FOLDER):
        return jsonify({"error": "Folder not found"}), 404
    
    # Récupérer la liste des fichiers d'images dans le dossier
    images = []
    for filename in os.listdir(IMAGE_FOLDER):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            images.append(request.host_url + f'images/{folder_name}/{filename}')
    
    return jsonify(images)

@app.route('/images/<folder_name>/<path:filename>', methods=['GET'])
def serve_image(folder_name, filename):
    IMAGE_FOLDER = os.path.join(os.getcwd(), folder_name)
    
    # Vérifier si le fichier demandé existe dans le dossier
    if not os.path.exists(os.path.join(IMAGE_FOLDER, filename)):
        return jsonify({"error": "File not found"}), 404
    
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
