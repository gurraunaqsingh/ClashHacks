import face_recognize as fr
import face_data as fd
import py_cloudinary as Cloud

name = fr.train_and_reco() #Train, and Start recognization

#Now upload this image and send to the Face data
pic_url = Cloud.upload_media(name)

#Send Image to get Data
data = fd.face_response(pic_url)

print(data)
