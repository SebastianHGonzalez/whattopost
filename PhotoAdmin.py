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

	#Erases file in given path.
	def erasePhoto(self,path):
		os.remove(path)


	#Connects with Flickr API,gets n number of random photos and saves id and url from each photo.
	# 0 < n =< 500
	def getPhotosFromFlickr(self, amount):
		#Setting keys
		FLICKR_PUBLIC = '066a9fcaede67bc720f66f75ed20a970'
		FLICKR_SECRET = 'e95c436ea4863f6c'

		#Connecting to flickrAPI
		flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
		extras='url_c, url_sq, url_t, url_s, url_q, url_n, url_z, url_l'

		#Searching random photos.
		randomPhotos = flickr.photos.getRecent(per_page=amount,extras=extras)
		photos = randomPhotos['photos']
		photos= photos['photo'] 

		#Handling data and saving data.
		for photo in photos:

			id = photo[u'id']
			url= self.getUrlFromPhoto(photo)

			
			photoInfo = PhotoInfo(id,url)

			self._photosInfo.append(photoInfo)

	#Gets url from photo and returns it. 
	def getUrlFromPhoto(self,photo):

		extras = ['url_c', 'url_sq', 'url_t', 'url_s', 'url_q', 'url_n', 'url_z', 'url_l']

		for i in extras:
			if(i in photo):
				print(i)
				url=photo[i]
				break

		return(url)

	def getPhotosInfo(self):
		return self._photosInfo

	def getPaths(self):
		return self._photoPaths

