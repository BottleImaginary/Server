from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Konfigurasi database
db_config = {
    'host': 'mariadb',
    'user': 'root',
    'password': 'password',
    'database': 'ngukurbotol'
}

# Membuat koneksi ke database
def create_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Endpoint dengan metode GET
@app.route('/data', methods=['GET'])
def get_data():
    # Membuat koneksi ke database
    connection = create_db_connection()

    # Membuat kursor untuk menjalankan query
    cursor = connection.cursor()

    # Menjalankan query SELECT untuk mengambil data dari database
    query = "SELECT * FROM botol"
    cursor.execute(query)
    
    # Mengambil hasil query
    result = cursor.fetchall()

    # Menutup koneksi ke database
    cursor.close()
    connection.close()

    # Mengembalikan respons JSON dengan data yang diperoleh
    return jsonify(result)


# Endpoint dengan metode POST
@app.route('/data', methods=['POST'])
def add_data():
    # Mengambil data dari permintaan POST
    data = request.json

    # Membuat koneksi ke database
    connection = create_db_connection()

    # Membuat kursor untuk menjalankan query
    cursor = connection.cursor()

    # Menjalankan query INSERT untuk menyimpan data ke database
    query = "INSERT INTO botol (id_botol, id_user, gambar_botol) VALUES (%s, %s, %s)"
    values = (data['id_botol'], data['id_user'], data['gambar_ban'])
    cursor.execute(query, values)
    connection.commit()

    # Menutup koneksi ke database
    cursor.close()
    connection.close()

    # Mengembalikan respons JSON dengan pesan sukses
    return jsonify({'message': 'Data berhasil ditambahkan'})


if __name__ == '__main__':
    app.run(debug=True)