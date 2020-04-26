import cv2 , os
import numpy as np
from os import listdir
from os.path import isfile , join
import faceRecognition_1 as fr

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
li1 = os.listdir('D:/PYTHON/ImageClassifier/Faces')
li , i = [] , 0

def face_detector(img , size = 0.5):
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray , 1.1 , 10)
    if faces is():
        return img,[]
    for (x,y,w,h) in faces:
        cv2.rectangle(img , (x,y) , (x+w , y+h) , (0,255,0) , 2)
        roi = img[y:y+h , x:x+w]
        roi = cv2.resize(roi , (200 , 200))
    return img,roi

def rel(cap):
    cap.release()
    cv2.destroyAllWindows()

def mains():
    for nme in li:
        print('Training Model for ' + nme + '...')
        data_path = 'D:/PYTHON/ImageClassifier/Faces/' + nme + '/'

        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

        Training_Data, Labels = [], []

        for i, file in enumerate(onlyfiles):
            image_path = data_path + onlyfiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)

        Labels = np.asarray(Labels, dtype=np.int32)

        model = cv2.face.LBPHFaceRecognizer_create()

        model.train(np.asarray(Training_Data), np.asarray(Labels))

        print('Model Training Complete !!!')
        #######################################################
        cap = cv2.VideoCapture(0)
        while True:

            ret, frame = cap.read()
            image, face = face_detector(frame)
            try:
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                result = model.predict(face)
                if result[1] < 500:
                    confidence = int((1 - (result[1]) / 300) * 100)
                    # print(confidence)
                    #display_string = str(confidence) + '% Match'
                    #cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)

                if confidence >= 95:
                    # print(nme + "User Found ...")
                    cv2.putText(image, "Unlocked" , (20, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
                    cv2.imshow('Face Cropper', image)
                else:
                    cv2.putText(image, "Locked", (20, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
                    cv2.imshow('Face Cropper', image)
                    if nme == li[len(li) - 1]:
                        exit()
            except:
                cv2.putText(image, "USER NOT REGISTERED", (20, 100), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 255), 1)
                cv2.imshow('Face Cropper', image)

            if cv2.waitKey(1) == 13:
                rel(cap)
                break

opt = int(input('''1. MODEL TRAINING
2. FACE RECOGNITION
3. EXIT
    
OPTIONS : '''))
if opt == 1:
    fr.main()
elif opt == 2:
    name = input("Enter the User Name : ")
    if name not in li1:
        print("User Registeration Not Found. \n Register the user first please.")
    else:
        li.append(name)
        mains()
elif opt == 3:
    exit()
else:
    print("Invalid Input !!!")
    exit()