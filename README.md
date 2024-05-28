# leakfinder

# Install <img src="ico.jpg" alt="Image description" width="65" height="45">
pip install -r requirements.txt

# Usage  <img src="exe.jpg" alt="Image description" width="85" height="65">
python3 leakfinder.py -domain exemple.com -number 10 -api xxxxxx

<img src="capture.PNG" alt="Image description" width="470" height="290">

# Disclaimer <img src="OIP.jpg" alt="Image description" width="85" height="65">
Please make good use of this tool

# Poc Orgin
> curl -H 'accept: application/json' "https://leakix.net/api/subdomains/**domain.com**"


> curl -H 'accept: application/json' https://leakix.net/api/subdomains/domain.com

