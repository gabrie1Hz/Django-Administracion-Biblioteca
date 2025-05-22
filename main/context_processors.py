'''import requests



def qoutes(request):
	  

	url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
	querystring = {"cat":"famous","count":"1"}
	
	headers = {
	"X-RapidAPI-Host": "andruxnet-random-famous-quotes.p.rapidapi.com",
	"X-RapidAPI-Key": "ab350e22f1msh39a60467ebfe5d6p144a63jsn2ea18f647e08"
	}
	response = requests.request("POST", url, headers=headers, params=querystring)

	#r  = requests.get(url.format(response)).json()
		
	res = response.json()
	

	return {
		'q':res[0]['qoute'],
		}
'''