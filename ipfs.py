import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
    #YOUR CODE HERE
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "pinata_api_key": "ac9537e620b538b6b2c0",
        "pinata_secret_api_key": "1210c27915e141456bf6e2161dc7de8f6beace5a43d2128ae46a76dd14ae359c",
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response.raise_for_status()
    cid = response.json()["IpfsHash"]

    return cid

def get_from_ipfs(cid,content_type="json"):
    assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
    #YOUR CODE HERE	
    url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    assert isinstance(data,dict), f"get_from_ipfs should return a dict"
    return data
