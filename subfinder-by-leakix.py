import requests
import json
import argparse
import urllib3
from rich.console import Console

console=Console()
def leakix_find(domain, number,api):
   try :
      url=f'https://leakix.net/api/subdomains/{domain}'

      headers = {'api-key': f'{api}',
               'accept': 'application/json'}

      r=requests.get(url,headers=headers)
      if r.status_code==200:
         dict = json.loads(r.text)
         console.print(f'Les sous domaines de cet url https://{domain} sont :\n ', style='white')

         for i in range(0,number):
            
             string=str(dict[i]['subdomain'])
             console.print(f'http://{string}')
 
   except requests.exceptions.ConnectionError :
             console.print('Pas de connexion Internet', style='red')

   except urllib3.exceptions.MaxRetryError :
             console.print('Pas de connexion Internet', style='red')

   except :
            console.print('nombre trop grande', style='yellow')

if __name__=='__main__':

         parser = argparse.ArgumentParser(description="Subdomain-finder")
         parser.add_argument("-domain", "--domain", dest="domain",
                  help="google.com", required=True)

         parser.add_argument("-number", "--number", dest="number",
                  help="10", required=True)
         
         parser.add_argument("-api", "--api", dest="api",
                  help="leakix-api", required=True)

         
         args = parser.parse_args()

         leakix_find(args.domain,int(args.number),args.api)
