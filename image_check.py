import numpy as np
# from matplotlib import pyplot as plt
from cv2 import cv2
# import seaborn as sns


characters=["Upload","Elsa", "Mulan", "Anna", "Moana", "Ariel", "Jasmine", "Cinderella", "Aurora"]
characters_face_index={"Elsa":1, "Mulan":2, "Anna":3, "Moana":4, "Ariel":5, "Jasmine":6, "Cinderella":7, "Aurora":8}



def opencv_open_into_rgb( image_file_name ):
    """ open image_file_name and convert to rgb """
    image_raw = cv2.imread(image_file_name, cv2.IMREAD_COLOR)  # reads into BGR
    image_rgb = cv2.cvtColor(image_raw, cv2.COLOR_BGR2RGB)     # convert from BGR to RGB
    return image_rgb



def save_rgb_image( image_rgb, new_file_name ):
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)     # convert from BGR to RGB
    result = cv2.imwrite(new_file_name,image_bgr)
    if result == True:
        print(f"image_rgb was saved to {new_file_name}")
    else:
        print(f"there was a problem saving image_rgb to {new_file_name}")




def image_check(file_name):

    Upload=opencv_open_into_rgb(f"static/{file_name}") 
    Elsa=opencv_open_into_rgb("static/F_image/Elsa_face.png") 
    Mulan=opencv_open_into_rgb("static/F_image/Mulan_face.png") 
    Anna=opencv_open_into_rgb("static/F_image/Anna_face.png") 
    Moana=opencv_open_into_rgb("static/F_image/Moana_face.png") 
    Ariel=opencv_open_into_rgb("static/F_image/Ariel_face.png")
    Jasmine=opencv_open_into_rgb("static/F_image/Jasmine_face.png") 
    Cinderella=opencv_open_into_rgb("static/F_image/Cinderella_face.png") 
    Aurora=opencv_open_into_rgb("static/F_image/Aurora_face.png") 


    Face=[Upload,Elsa,Mulan,Anna,Moana,Ariel,Jasmine,Cinderella,Aurora]

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    image_faces_gray = cv2.cvtColor(Upload, cv2.COLOR_RGB2GRAY)

    faces =faceCascade.detectMultiScale(
    image_faces_gray,
    scaleFactor=1.05,
    minNeighbors=1,
    minSize=(10,10),
    flags = cv2.CASCADE_SCALE_IMAGE,
    )

    image_faces_drawn_rgb = Upload.copy()
    for (x, y, w, h) in faces:
        # note that this draws on the color image!
        cv2.rectangle(image_faces_drawn_rgb, (x, y), (x+w, y+h), (0, 255, 0), 2) 

    LoFi = []

    for (x, y, w, h) in faces:
        # note that this draws on the color image!
        face= Upload[y:y+h,x:x+h,:]  #, (x, y), (x+w, y+h), (0, 255, 0), 2)  
        LoFi.append( face )

    Face[0]=LoFi[0]
    LoFace = [ cv2.resize(LoFiIm,dsize=(20,20)) for LoFiIm in Face ]


    A = np.zeros( (9,9) )
    for r in range(1):
        for c in range(9):
            res = cv2.matchTemplate(LoFace[r],LoFace[c],cv2.TM_SQDIFF_NORMED)
            # res is a 2d image, so... we extract the value
            A[r,c] = res[0,0]
    

    A[0,0]=42    
    location=np.argmin(A[0])
    return characters[location]