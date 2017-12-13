
class PhotoInfo:
	def __init__(self,id,url,numFavs):
		self._id=id
		self._url = url
		self._favs = numFavs

	def getUrl(self):
		return self._url

	def __repr__(self):
		return "id:{idPhoto},url:{url},favorites:{favs}".format(idPhoto=self._id,url=self._url,favs=self._favs)



	


