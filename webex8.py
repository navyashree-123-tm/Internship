from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import magic
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///video_metadata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class VideoMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    video_name = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)

def is_video(file_path):
    mime = magic.Magic()
    mime_type = mime.from_file(file_path)
    return mime_type.startswith('video/')

@app.route('/upload_video', methods=['POST'])
def upload_video():
    data = request.form
    user_id = data['user_id']
    video_name = data['video_name']

    # Assuming 'video_file' is the key for the file in the request
    video_file = request.files['video_file']

    # Save the video file
    file_path = f'uploads/{user_id}_{video_name}.mp4'
    video_file.save(file_path)

    # Check if the uploaded file is a video
    if not is_video(file_path):
        return jsonify({'error': 'Invalid file type. Please upload a video file'}), 400

    # Call the previous microservice to store the file
    store_data = {'user_id': user_id, 'item_name': video_name, 'quantity': 1}
    response = requests.post('http://localhost:5000/add_to_cart', json=store_data)

    # Save video metadata to the database
    video_metadata = VideoMetadata(user_id=user_id, video_name=video_name, file_path=file_path)
    db.session.add(video_metadata)
    db.session.commit()

    return jsonify({'message': 'Video uploaded successfully'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
