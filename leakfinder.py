import requests
import json
import argparse
import urllib3
from rich.console import Console
import pyfiglet
from colorama import Fore, Style
import threading

def banner():

   text = "leakfinder"
   font = "slant"
   taille=10000
   banner = str(pyfiglet.figlet_format(text, font,width=taille))
   console=Console()
   ban='''   __               __   _______           __         
   / /   ___  ____ _/ /__/ ____(_)___  ____/ /__  _____
  / /   / _ \/ __ `/ //_/ /_  / / __ \/ __  / _ \/ ___/
 / /___/  __/ /_/ / ,< / __/ / / / / / /_/ /  __/ /    
/_____/\___/\__,_/_/|_/_/   /_/_/ /_/\__,_/\___/_/     
                                     Author:Jhonson   
'''                                     
   print(Fore.YELLOW+ Style.BRIGHT + ban+ Style.RESET_ALL)

banner()
def main(domain, number,api):
  
   try :
      url=f'https://leakix.net/api/subdomains/{domain}'

      headers = {'api-key': f'{api}',
               'accept': 'application/json'}

      r=requests.get(url,headers=headers)
      if r.status_code==200:
         dict = json.loads(r.text)

         for i in range(0,number):
            
             string=str(dict[i]['subdomain'])
             print(Fore.GREEN + Style.BRIGHT +f'http://{string}'+ Style.RESET_ALL+ Style.RESET_ALL)
 
   except requests.exceptions.ConnectionError :
             print(Fore.RED + Style.BRIGHT +'Pas de connexion Internet'+ Style.RESET_ALL)

   except urllib3.exceptions.MaxRetryError :
             print(Fore.RED+ Style.BRIGHT +'Pas de connexion Internet'+ Style.RESET_ALL)

   except :
            print(Fore.RED + Style.BRIGHT +'nombre trop grande'+ Style.RESET_ALL)

if __name__=='__main__':

         parser = argparse.ArgumentParser(description="Subdomain-finder")
         parser.add_argument("-domain", "--domain", dest="domain",
                  help="google.com", required=True)

         parser.add_argument("-number", "--number", dest="number",
                  help="10", required=True)
         
         parser.add_argument("-api", "--api", dest="api",
                  help="leakix-api", required=False)

         
         args = parser.parse_args()


         thread = threading.Thread(target=main, args=(args.domain,int(args.number), args.api))
         thread.start()
         thread.join(timeout=2)


         
     
