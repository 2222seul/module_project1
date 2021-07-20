import json
import urllib.request

def Get_Request_GoUrl(url):
    pass

def GetGoVSearchResult(baseurl, pageValue, perPageValue):   
    paraData = "page=" + str(pageValue)
    paraData += "&perPage=" + str(perPageValue)
    keyValue = "&serviceKey=%2BptXuibm2mCBLhAZqH%2F88WSuHtU%2BmhKVJUWGVelVYJKc1NENMurzQaKEMPN%2Bd99LWr97LDZcj1XoIkcr6UlUjg%3D%3D"

    url = baseurl + paraData + keyValue

    resultData = Get_Request_GoUrl(url)

    if(resultData == None):
        return None
    else:
        return json.loads(resultData)
