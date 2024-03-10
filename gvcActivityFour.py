import cv2
import matplotlib.pyplot as plt
import numpy as np
#gabuhat kog choice para sa user mo pili og image 
img1 = "peacock.jpg"

image1 = cv2.imread(img1, cv2.IMREAD_COLOR)
grayScaledImage1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)


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
        plt.show()
    elif selected == "4":    
        #getting the edges of the image 
        cannyEdges1 = cv2.Canny(grayScaledImage1, 100, 200)

        laplacianEdge = cv2.Laplacian(grayScaledImage1, cv2.CV_64F)

        sobelx = cv2.Sobel(grayScaledImage1, cv2.CV_64F, 1,0)
        sobely = cv2.Sobel(grayScaledImage1, cv2.CV_64F, 0,1)
        sobelEdges = cv2.bitwise_or(sobelx, sobely)

        scharrx = cv2.Scharr(grayScaledImage1, cv2.CV_64F, 1, 0)
        scharry = cv2.Scharr(grayScaledImage1, cv2.CV_64F, 0, 1)
        scharrEdges = cv2.bitwise_or(scharrx, scharry)

        #makinga a figure
        figure = plt.figure(figsize=(10, 7))
        #adding subplot in the figure
        figure1 = figure.add_subplot(1,4,1)
        figure1.imshow(cannyEdges1, cmap = 'gray')
        figure1.axis('off')
        figure1.set_title('1st Image')
        #adding subplot in the figure
        figure2 = figure.add_subplot(1,4,2)
        figure2.imshow(laplacianEdge, cmap = 'gray')
        figure2.axis('off')
        figure2.set_title('2nd Image')
        #adding subplot in the figure
        figure3 = figure.add_subplot(1,4,3)
        figure3.imshow(sobelEdges, cmap = 'gray')
        figure3.axis('off')
        figure3.set_title('Third Image')        
        #adding another subplot
        figure4 = figure.add_subplot(1,4,4)
        figure4.imshow(scharrEdges, cmap = 'gray')
        figure4.axis('off')
        figure4.set_title('Fourth Image') 
        plt.show()
    else:
        print("The inputted Value is not in the Menu")
    
    


