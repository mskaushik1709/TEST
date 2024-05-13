import webbrowser 

import pyshorteners

url = "https://www.geeksforgeeks.org"

try:
	webbrowser.get("chrome").open(url)
except:
	try:
		webbrowser.get("dev").open(url)
	except:
		try:
			webbrowser.get("firefox").open(url)
		except:
			print("browswer not found")
		



