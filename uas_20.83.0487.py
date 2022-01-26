import requests
import json
import mysql.connector


url = requests.get('https://api.abcfdab.cfd/students')
hasil = url.text

with open('isi.json', 'w') as outfile:
    outfile.write(hasil)


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="db_akademik_20.83.0487"
	)

if mydb.is_connected():
	print("Connect")

def import_data():
	with open('isi.json', 'r') as get:
		isi = json.load(get)
		data = isi["data"]
		cursor = mydb.cursor()
		sql = '''INSERT INTO tbl_students_0487(id,nim,nama,jk,jurusan,alamat) VALUES (%s, %s, %s, %s, %s, %s )'''
		for i in data :
			val = (i['id'],i['nim'], i['nama'] ,i['jk'], i['jurusan'], i['alamat'])		
			cursor.execute(sql,val)
			mydb.commit()
	print("Data sudah dimasukkan ke database")

def tampil_data():
	cursor = mydb.cursor()
	cursor.execute("SELECT * FROM tbl_students_0487")
	result = cursor.fetchall()
	for x in result:
		print(x)

def tampil_limit():
	baris = input("\nBerapa limitnya yang di tampilkan : ")
	cursor = mydb.cursor()
	sql = ("SELECT * FROM tbl_students_0487 limit ")
	cursor.execute(sql + baris)
	result = cursor.fetchall()
	print(result)

def tampil_nim():
	nim = input('Masukan NIM :')
	cursor = mydb.cursor()
	sql = ("SELECT * FROM tbl_students_0487 WHERE nim=%s")
	val = (nim,)
	cursor.execute(sql, val)
	result = cursor.fetchone()
	print(result)

def menu():
    print("1. Tampilkan Semua Data")
    print("2. Tampilkan Data Berdasarkan Limit")
    print("3. Cari Data Berdasarkan NIM")
    print("4. Import Data")
    print("0. Keluar")


    option = input("Pilih menu> ")

    if option == "1":
        tampil_data()
    elif option == "2":
        tampil_limit()
    elif option == "3":
        tampil_nim()
    elif option == "4":
        import_data()
    elif option == "0":
        exit()
    else:
        print("Menu Salah!")


if __name__ == "__main__":
    while(True):
        menu()