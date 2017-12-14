
class PhotoInfo:
	def __init__(self,id,url):
		self._id=id
		self._url = url
		

	def getUrl(self):
		return self._url

	def __repr__(self):
		return "id:{idPhoto},url:{url}".format(idPhoto=self._id,url=self._url)



	


