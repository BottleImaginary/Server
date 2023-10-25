from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="",
    database="bda"
)

cursor = db.cursor()


@app.route('/users', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM user")
        result = cursor.fetchall()
        data = []
        for row in result:
            data.append({
                'id_user': row[0],
                'nama_user': row[1],
            })
        return jsonify(data)

    elif request.method == 'POST':
        if request.headers['Content-Type'] != 'application/json':
            return jsonify({'error': 'Unsupported Media Type'}), 415

        new_data = request.json
        query = "INSERT INTO user1 (nama_user) VALUES ( %s )"
        values = ( new_data['nama_user'],)
        cursor.execute(query, values)
        db.commit()
        return jsonify({'message': 'Data berhasil ditambahkan'})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3931)