import scrapy
import json
import base64
from scrapy_splash import SplashRequest
from PIL import Image
from io import BytesIO


class CriticReviewScreenshots(scrapy.Spider):
	"""
		This scrapy will screenshot  critic review links and saved it to your local machine
	"""
	name = 'thegamer'


	def start_requests(self):
		"""
			links = scraped thegamer.com critic review links
		"""
		links = ['the', 'gamer', 'links']
		for link in links:
			url = link[0]
			image_name = 'file-name'
			yield SplashRequest(
									url=url,
									callback=self.parse,
									dont_filter=True,
									args={
											"html": 1,
											"png": 1,
											'wait': 15,
											'url':url,
											'render_all': 1
										},
									endpoint='render.json',
									meta={'image_name': image_name}
								)


	def parse(self, response):
		url = response.url
		file_name = response.meta['image_name']
		imgdata = base64.b64decode(response.data['png'])#decoding response .png data
		file_name = "{}.webp".format(file_name)#set file name
		image = Image.open(BytesIO(imgdata))#open converted bytes image
		image.save('/file/path/' + file_name)#saving image

		print (file_name)
		print ('screenshot done...saved')