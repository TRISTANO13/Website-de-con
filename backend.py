from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/images/<folder_name>', methods=['GET'])
def get_images(folder_name):
    IMAGE_FOLDER = os.path.join(os.getcwd(), folder_name)
    
    # Récupérer la liste des fichiers d'images dans le dossier
    images = []
    if os.path.exists(IMAGE_FOLDER):
        for filename in os.listdir(IMAGE_FOLDER):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                images.append(request.host_url + 'images/' + filename)
    
    return jsonify(images)

@app.route('/images/<path:filename>', methods=['GET'])
def serve_image(filename):
    # Servir une image directement depuis le dossier des images
    IMAGE_FOLDER = os.path.dirname(os.path.abspath(filename))
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
