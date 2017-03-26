
import cloudinary
import json
import cloudinary.uploader

cloudinary.config(
  cloud_name = 'dwrado6nn',  
  api_key = '672197888834674',  
  api_secret = 'o4z2gXYb6tOCh-pVDwlnNl8o5a0'  
)

def upload_media(filename):
    res = cloudinary.uploader.upload("savedImages/" + filename + ".png", resource_type = "image")
    public_id = res["public_id"]
    url = res["url"]
    return(url)   
