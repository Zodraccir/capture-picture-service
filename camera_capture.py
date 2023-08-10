# program to capture single image from webcam in python
# importing OpenCV library
import cv2 as cv  

# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 0

def shot(filename : str):
    cam = cv.VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()
    
    # If image will detected without any error, 
    # show result
    cam.release()
    if result:
    
        # showing result, it take frame name and image 
        # output
        #imshow("GeeksForGeeks", image)
    
        # saving image in local storage
        cv.imwrite(filename, image)
        return True
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")
        return False