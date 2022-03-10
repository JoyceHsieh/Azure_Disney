from PIL import Image
import cv2


def image_present(Characters):
    C=['Aladdin','Alice','Anna','Ariel','Aurora','Beast','Belle',
            'Cinderella','Elsa','Eric','Flynn Rider','Hercules','Jasmine',
            'Kristoff','Li Shang','Merida','Moana','Mulan','Perter Pan',
            'Prince Charming','Pocahontas','Rapunzel','Raya','Snow White','Tiana' ]
    
    im = C[Characters]

    
    return im



    
# im.rotate(45).show() 