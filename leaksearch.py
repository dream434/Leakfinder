import requests
import argparse

def main (url,number,header):
    
    for i in range(1,int(number)):
  
       parameter = {
            "page": i,
            "q": args.search,
            "scope": f"leak"} 

       r = requests.get(url, params=parameter, headers=header) 
       jsonfile=r.json()
       count=len(jsonfile)
       for xfile in range(count):
          result=jsonfile[xfile]
          print('\033[92m'+'http://'+result['host']+':'+str(result['port']+f'/{args.search}'))

if __name__ == '__main__':

         parser = argparse.ArgumentParser(description="Subdomain-finder")
         parser.add_argument("-search", "--search", dest="search",
                  help="", default=".DS_Store", required=True)

         parser.add_argument("-number", "--number", dest="number",
                  help="10", required=True)
         
         parser.add_argument("-api", "--api", dest="api",
                  help="leakix-api", required=False)

         args = parser.parse_args()


         headers = {
            "api-key": args.api,
            "Accept": "application/json"}

       

  
         main('https://leakix.net/search',args.number,headers)
                                                               
