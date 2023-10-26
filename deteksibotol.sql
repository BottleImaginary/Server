CREATE DATABASE deteksibotol;

USE deteksibotol;

CREATE TABLE user (
	id_user INT AUTO_INCREMENT PRIMARY KEY,
	nama_user VARCHAR(20) NOT NULL
);
CREATE TABLE botol (
	id_botol INT AUTO_INCREMENT PRIMARY KEY,
	id_user INT NOT NULL,
	gambar_botol BLOB NOT NULL,
	waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (id_user) REFERENCES user(id_user)
);
CREATE TABLE catatan (
	id_catatan INT AUTO_INCREMENT PRIMARY KEY,
	id_botol INT NOT NULL,
	waktu_deteksi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	lokasi_deteksi VARCHAR(30),
	FOREIGN KEY (id_botol) REFERENCES botol(id_botol)
)