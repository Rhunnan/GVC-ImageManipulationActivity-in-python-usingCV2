import cv2
import matplotlib.pyplot as plt
import numpy as np
#gabuhat kog choice para sa user mo pili og image 
img1 = "peacock.jpg"
img2 = "pheagle.jpg"
img3 = "lionAbstract.webp"
print("Select Image to be use permanently: ")
print("Input [1] for Peacock Image")
print("Input [2] for  PH Eagle IImage")
print("Input [3] for Lion Abstract Image")
selectedImage = int(input("Input here: "))

if selectedImage == 1:
    image1 = cv2.imread(img1, cv2.IMREAD_COLOR)
    grayScaledImage1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
elif selectedImage ==2:     
    image1 = cv2.imread(img2, cv2.IMREAD_COLOR)
    grayScaledImage1 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)
else:
    image1 = cv2.imread(img3, cv2.IMREAD_COLOR)
    grayScaledImage1 = cv2.imread(img3, cv2.IMREAD_GRAYSCALE)


while True:
        
    print("MENU: Select flag to display image:")
    print("input [1] to display Original Image")
    print("input [2] to display Grayscaled Image")
    print("input [3] to display the GrayScaled Image Histograms")
    print("input [4] to display the edges of the image in one figure ")
    print("input [0] to Exit")

    selected = input("Input Here: ")
    if selected == '0':
        break
    elif selected == "1":
        cv2.imshow('Peacock', image1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif selected == "2":
        cv2.imshow('grayscaledImage', grayScaledImage1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif selected == "3":
        histImage1 = cv2.calcHist([grayScaledImage1], [0], None, [256], [0,256])
        #image1
        plt.figure()
        plt.title("Historam of Image 1 in grayscaled")
        plt.plot(histImage1) 
    elif selected == "4":
        if selectedImage == 1:
            grayScaledImage2 = cv2.imread(img2, cv2.IMREAD_COLOR)
            grayScaledImage3 = cv2.imread(img3, cv2.IMREAD_COLOR)
        elif selectedImage == 2: 
            grayScaledImage2 = cv2.imread(img1, cv2.IMREAD_COLOR)
            grayScaledImage3 = cv2.imread(img3, cv2.IMREAD_COLOR)
        else:
            grayScaledImage2 = cv2.imread(img1, cv2.IMREAD_COLOR)
            grayScaledImage3 = cv2.imread(img2, cv2.IMREAD_COLOR)
            
        figure = plt.figure(figsize=(10, 7))
    else:
        print("The inputted Value is not in the Menu")
    
    


