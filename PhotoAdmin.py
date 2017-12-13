from photoInfo import *
from flickrapi import FlickrAPI
from pprint import pprint
import urllib.request
import os

class PhotoAdmin:
	def __init__(self):
		self._photosInfo = []
		self._photoPaths = []
		self._photoNumber= 0

	#Saves all images.
	def saveImages(self):

		for photo in self._photosInfo:

			path = "./imgs/img{n}.jpg".format(n=self._photoNumber)

			urllib.request.urlretrieve(photo.getUrl(), path)

			self._photoNumber += 1

			self._photoPaths.append(path)

	#Erase file in given path.
	def erasePhoto(self,path):
		os.remove(path)


	def getPhotosFromFlickr(self, amount):
		#Setting keys
		FLICKR_PUBLIC = '066a9fcaede67bc720f66f75ed20a970'
		FLICKR_SECRET = 'e95c436ea4863f6c'

		#Connecting to flickrAPI
		flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
		extras='url_c'

		#Searching random photos.
		randomPhotos = flickr.photos.getRecent(per_page=amount,extras=extras)
		photos = randomPhotos['photos']
		photos= photos['photo'] 

		#Handling data.
		for photo in photos:

			id = photo[u'id']
			url = photo[u'url_c']

			favs = flickr.photos.getFavorites(photo_id=id)	#?
			data = favs['photo']							#?
			numFavs = data[u'total']						#?

			photoInfo = PhotoInfo(id,url,numFavs)

			self._photosInfo.append(photoInfo)

	def getPhotosInfo(self):
		return self._photosInfo

	def getPaths(self):
		return self._photoPaths

'''
#----------------

pa = PhotoAdimin()
pa.getPhotosFromFlickr()
pprint(pa.getPhotosInfo())

#----

pa.saveImages()


#pa.erasePhoto('/home/camila/Desktop/Imagenes/img0.jpg')

#handlear resultado del yolo. 

'''
