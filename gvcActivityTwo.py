import cv2
import numpy as np
#activity 2

def getPixelValue(x, y, image):
    #getting the pixel value using the [x, y ] method, ang pixel nga gekuha nako ani kay coordinate x og y na value
    pixelVal = image[x,y]

    return pixelVal

lionImg = "lionAbstract.webp"

#grayscaled imgae para gamiton sa thresholding
img2 = cv2.imread(lionImg, cv2.IMREAD_GRAYSCALE)
# ako gekuha ang dimension sa image ron makuha nako ang size or ang height og width sa image 
dimensions = img2.shape
print("shape of the image load ", img2.shape)
#converting image to black and white by thresholding the img2 which is already in grayscaled
ret, blackWhiteImg = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)

#finding laplacian edges using laplacian method in cv2
laplacianEdges = cv2.Laplacian(img2,cv2.CV_64F)

#finding Sobel edges of the image
sobelx = cv2.Sobel(img2, cv2.CV_64F, 1,0)
sobely = cv2.Sobel(img2, cv2.CV_64F, 0,1)
sobelEdges = cv2.bitwise_or(sobelx, sobely)

#finding scharr edges of the image 
scharrx = cv2.Scharr(img2, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(img2, cv2.CV_64F, 0, 1)
scharrEdges = cv2.bitwise_or(scharrx, scharry)

#finding Canny Edges of the image
cannyEdges = cv2.Canny(img2, 100, 200)

while True:
        
    print("MENU: Select flag to display image:")
    print("input [1] to get the size of an Image")
    print("input [2] to get BGR pixel of an image")
    print("input [3] to display laplacian Edges of the image")
    print("input [4] to display sobel Edges of the image")
    print("input [5] to display scharr Edges of the image")
    print("input [6] to display Canny Edges of the image")

    print("input [0] to Exit")

    selected = input("Input Here: ")
    if selected == '0':
        break
    elif selected == "1":
        print(f"Image heigt: {dimensions[0]} Image width: {dimensions[1]}")
    elif selected == "2":
        x = int(input("Input Coordinate X: "))
        y = int(input("Input Coordinate y: "))
        
        pixelVal = getPixelValue(x,y, blackWhiteImg)
        # since ang image na ge kwaan nakog value is black and white then it would have only one value dli same sa colored na naar BGR values
        print(f"Pixel Value at {x}, {y} = {pixelVal}")
    elif selected == "3":
        cv2.imshow('laplacianEdge', laplacianEdges)
    elif selected == "4":
        cv2.imshow('sobelEdges', sobelEdges)
    elif selected == "5":
        cv2.imshow('scharrEdge', scharrEdges)
    elif selected == "6":
        cv2.imshow('cannyEdge', cannyEdges) 
    else:
        print("The inputted Value is not in the Menu")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

