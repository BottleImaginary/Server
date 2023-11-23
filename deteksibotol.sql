-- Active: 1700712435596@@127.0.0.1@3306@deteksibotol_db
CREATE DATABASE deteksibotol_db;

USE deteksibotol_db;

CREATE TABLE botol (
	id_botol INT AUTO_INCREMENT PRIMARY KEY,
	nama_botol VARCHAR(25) NOT NULL,
	gambar_botol BLOB,
	tgl_input DATETIME
);
CREATE TABLE lantai (
	id_lantai INT AUTO_INCREMENT PRIMARY KEY,
	nama_lantai VARCHAR(25) NOT NULL
);
CREATE TABLE deteksi (
	id_deteksi INT AUTO_INCREMENT PRIMARY KEY,
	id_botol INT,
	id_lantai INT,
	hasil_deteksi VARCHAR(25) NOT NULL,
	FOREIGN KEY (id_botol) REFERENCES botol(id_botol) ON DELETE CASCADE ,
	FOREIGN KEY (id_lantai) REFERENCES lantai(id_lantai) ON DELETE CASCADE
);