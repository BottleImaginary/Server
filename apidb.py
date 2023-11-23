from flask import Flask, request, jsonify
import mysql.connector
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Konfigurasi database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    port=3306,
    password="",
    database="deteksibotol_db"
)

cursor = db.cursor()


# Fungsi untuk memeriksa ekstensi gambar yang diunggah
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        # Implement your GET logic here to retrieve data from the database
        # Use request.args to access query parameters

        return jsonify({'message': 'This is a GET request'})

    elif request.method == 'POST':
        try:
            nama_botol = request.form.get('nama_botol')
            nama_lantai = request.form.get('nama_lantai')

            # Look up the 'id_botol' and 'id_lantai' based on provided names
            cursor.execute("SELECT id_botol FROM botol WHERE nama_botol = %s", (nama_botol,))
            result_botol = cursor.fetchone()

            cursor.execute("SELECT id_lantai FROM lantai WHERE nama_lantai = %s", (nama_lantai,))
            result_lantai = cursor.fetchone()

            if result_botol is None:
                return jsonify({'error': 'Nama botol not found'}), 404

            if result_lantai is None:
                return jsonify({'error': 'Nama lantai not found'}), 404

            id_botol = result_botol[0]
            id_lantai = result_lantai[0]

            gambar_botol = request.files['gambar_botol']
            if gambar_botol and allowed_file(gambar_botol.filename):
                filename = secure_filename(gambar_botol.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                gambar_botol.save(filepath)
            else:
                return jsonify({'error': 'Invalid image file'}), 400

            hasil_deteksi = request.form.get('hasil_deteksi')

            tgl_input = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            query = "INSERT INTO deteksi (id_botol, id_lantai, gambar_botol, tgl_input, hasil_deteksi) VALUES (%s, %s, %s, %s, %s)"
            values = (id_botol, id_lantai, filepath, tgl_input, hasil_deteksi)

            cursor.execute(query, values)
            db.commit()
            return jsonify({'message': 'Data deteksi berhasil ditambahkan'}), 200
        except Exception as e:
            return jsonify({'error': 'Internal Server Error', 'details': str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)