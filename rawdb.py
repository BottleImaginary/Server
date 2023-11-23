import json
import sqlite3


class BottleDetectionBackend:
    def __init__(data):
        data.conn = sqlite3.connect("cobaServer.db")
        data.cursor = data.conn.cursor()
        data.create_tables()  # Panggil fungsi ini untuk membuat tabel jika belum ada

    def create_tables(data):
        with open(
            "deteksibotol.sql", "r"
        ) as sql_file:  # Pastikan nama file dan pathnya sesuai
            sql_script = sql_file.read()
        data.cursor.executescript(sql_script)
        data.conn.commit()  # Simpan perubahan ke database

    def simpan_botol(data, nama_botol, gambar_botol, tgl_input):
        try:
            data.cursor.execute(
                "INSERT INTO Sayur (nama_botol, gambar_botol,tgl_input) VALUES (?, ?, ?)",
                (nama_botol, gambar_botol, tgl_input),
            )
            data.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error:", str(e))
            return False

    def simpan_lantai(data, nama_lantai):
        try:
            data.cursor.execute(
                "INSERT INTO pasar (nama_lantai) VALUES (?)",
                (nama_lantai),
            )
            data.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error:", str(e))
            return False

    def simpan_deteksi(data, id_botol, id_lantai, hasil_deteksi):
        try:
            data.cursor.execute(
                "INSERT INTO deteksi (id_botol ,id_lantai , hasil_deteksi) VALUES (?, ?, ?)",
                (id_botol, id_lantai, hasil_deteksi),
            )
            data.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error saat menyimpan deteksi:", str(e))
            return False