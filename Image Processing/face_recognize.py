import cv2, sys, numpy, os

def train_and_reco():
    size = 4
    haar_file = 'haarcascade_frontalface_default.xml'
    datasets = 'datasets/'

    print('Training...')

    (images, labels, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(datasets):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(datasets, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                label = id
                images.append(cv2.imread(path, 0))
                labels.append(int(label))
            id += 1
    (width, height) = (130, 100)

    (images, labels) = [numpy.array(lis) for lis in [images, labels]]

    model = cv2.face.createFisherFaceRecognizer()
    model.train(images, labels)

    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(1)

    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))

            #Try to recognize the face
            prediction = model.predict(face_resize)
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

            if prediction<500:
                print(str(names[prediction]))
            else:
                cv2.putText(im,'not recognized',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))

        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == ord('q'):
            break
        if key == ord('t'):
            take_image(webcam, (str(names[prediction])))
            return(str(names[prediction]))
            break


def test():
    print("GGWP")

def take_image(webcam, name):

    def get_image():
        retval, im = webcam.read()
        return im

    print("Taking image...")

    camera_capture = get_image()
    file = "savedImages/" + name + ".png"
    cv2.imwrite(file, camera_capture)

    print("File saved to : " + str(file))

    del(webcam)

    


