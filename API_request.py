import requests

class geneacity_API_request():
    json:object=None
    url:str=None
    status:int=0
    error:str=None
    def __init__(self,url:str):
        self.url=url
        response=requests.get(url)
        if response.status_code == 200:
            self.json = response.json()
        else:
            self.error=response.status_code
        
        self.status=self.json['status']


consulta1=geneacity_API_request('https://geneacity.life/API/getHouses/?x=250&y=250')
consulta2=geneacity_API_request('https://geneacity.life/API/getHouses/?x=99999&y=99999')
consulta3=geneacity_API_request('https://geneacity.life/API/getHouses/?x=700&y=400')
print(consulta1.json)
print(consulta2.json)
print(consulta3.json)

