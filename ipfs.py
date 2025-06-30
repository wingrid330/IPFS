import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"
    # YOUR CODE HERE
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "pinata_api_key": "ac9537e620b538b6b2c0",
        "pinata_secret_api_key": "1210c27915e141456bf6e2161dc7de8f6beace5a43d2128ae46a76dd14ae359c",
        "Content-Type": "application/json"
    }

    payload = {
        "pinataMetadata": {"name": "eas583-test"},
        "pinataContent": data
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()
    cid = response.json()["IpfsHash"]

    return cid

# def get_from_ipfs(cid,content_type="json"):
#     assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
#     #YOUR CODE HERE	
#     url = f"https://gateway.pinata.cloud/ipfs/{cid}"
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()

#     assert isinstance(data,dict), f"get_from_ipfs should return a dict"
#     return data

# def get_from_ipfs(cid, content_type="json", gateway="https://gateway.pinata.cloud/ipfs/"):
#     assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"
#     #YOUR CODE HERE
#     url = f"{gateway}{cid}"
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()

#     assert isinstance(data, dict), f"get_from_ipfs should return a dict"
#     return data

def get_from_ipfs(cid, content_type="json", gateways=None):
    assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"
    #YOUR CODE HERE
    if gateways is None:
        gateways = [
            "https://gateway.pinata.cloud/ipfs/",
            "https://ipfs.io/ipfs/",
            "https://cloudflare-ipfs.com/ipfs/"
        ]

    for gateway in gateways:
        url = f"{gateway}{cid}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            assert isinstance(data, dict), "get_from_ipfs should return a dict"
            return data
        except Exception as e:
            print(f"Failed with {gateway}: {e}")

    raise Exception("All IPFS gateways failed.")


