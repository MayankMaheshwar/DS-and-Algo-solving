import urllib.request
import json


class Solution:

	def run(self, character):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		character = character.replace(" ", "+")
		with urllib.request.urlopen('https://challenges.hackajob.co/swapi/api/people/?search='+character) as response:
			html = response.read()


""" json.dumps() convert python object to a json string """
second = "".join(chr(x) for x in bytearray(
    html))  # convert byte literal api data to string
sd = json.loads(second)  # convert valid JSON string to python dictionary
			numberOfFilms = (len(sd["results"][0]['films']))





		return numberOfFilms
