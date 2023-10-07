import cv2
from PIL import Image

imagePath = "cat.jpeg"

catFaceCascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
image = cv2.imread(imagePath)
catFace = catFaceCascade.detectMultiScale(image)
# print(catFace)
# for(x, y, w, h) in catFace:
#     cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 0), 3)

cat = Image.open(imagePath)
glasses = Image.open("glasses.png")

cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for(x, y, w, h) in catFace:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y + h/4)), glasses)
    cat.save("catWithGlasses.png")
    catWithGlassesImage = cv2.imread("catWithGlasses.png")
    cv2.imshow("catWithGlasses", catWithGlassesImage)

cv2.imshow("Cat", image)
cv2.waitKey()