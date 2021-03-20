import cv2
import numpy

PATH_LOCAL = 'C:/Users/janes/Pool/PROJECT/SUT/API/FlaskAPI/FLASK_API/project/models/image/img1.jpg'


def getAllImage():
    image = cv2.imread(PATH_LOCAL)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def faceRecognitionProcess(img):
    print("--------------------- faceRecognitionProcess -----------------------")




def analyze(img):
    print("--------------------- processing -----------------------")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBase = getAllImage()

    h,w = gray.shape
    hBase,wBase = imgBase.shape

    score = 0;

    for i in range(0,h,1):
        for j in range(0,w,1):
            if gray[i][j] == imgBase[i][j]:
                score = score+1

    print("img input ==> ",h," X ",w," : ",(h*w))
    print("img base  ==> ",hBase," X ",wBase," : ",(hBase*wBase))
    print("score : ",score)

    size = h*w
    avg = 100/size
    avg = avg*score

    print("avg : ",avg)


    # cv2.imshow('gray image',gray)
    # cv2.waitKey(0)
    return "waiting processing ..."


