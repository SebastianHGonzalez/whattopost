from darkflow.net.build import TFNet
import cv2
#Agregado por Lautaro
import sqlManager
import getpass
import PhotoAdmin

server = input('Ingrese el server de base de datos ')
#Se checkea q los inputs de conexion son validos
usr = input('Ingrese usuario ')
psw = getpass.getpass('Ingrese password ')
db = input('Ingrese una base de datos ')

amountPics = input('Cuantas fotos desea analizar? ')
amountPics = int(amountPics)

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.5, "gpu": 1.0}

tfnet = TFNet(options)

#Agregado por Lautaro
registro = sqlManager.SqlManager()
registro.configure(server, usr, psw, bd)

f = PhotoAdmin.PhotoAdmin()
f.getPhotosFromFlickr(amountPics)
f.saveImages()
paths=f.getPaths()

for path in paths:
	print("analizando imagen: " + path)
	# la convierto
	imgcv = cv2.imread(path)
	f.erasePhoto(path)
	# se la paso a YOLO
	results = tfnet.return_predict(imgcv)
	# guardo el resultado
	for result in results:

		#Actualizado por Lautaro
		registro.updateRecords(result['label'])
