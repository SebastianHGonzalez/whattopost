from darkflow.net.build import TFNet
import cv2
#Agregado por Lautaro
import sqlManager
import getpass
import PhotoAdmin

server = input('Ingrese el server de base de datos ')
usr = input('Ingrese usuario ')
psw = getpass.getpass('Ingrese password ')
db = input('Ingrese una base de datos ')

amountPics = input('Cuantas fotos desea analizar? ')
amountPics = int(amountPics)

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.5, "gpu": 1.0}

tfnet = TFNet(options)

registro = sqlManager.SqlManager()
registro.configure(server, usr, psw, db)

f = PhotoAdmin.PhotoAdmin()
f.getPhotosFromFlickr(amountPics)
f.saveImages()
paths=f.getPaths()

for path in paths:
	print("analizando imagen: " + path)
	imgcv = cv2.imread(path)
	f.erasePhoto(path)
	results = tfnet.return_predict(imgcv)
	for result in results:

		registro.updateRecords(result['label'])
