import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        #image=cv2.imread('/var/www/html/prueba.jpg')
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
#        image=cv2.resize(image,(640,480))
        scale_percent=600
        width=int(image.shape[1]*scale_percent/100)
        height=int(image.shape[0]*scale_percent/100)
        dim=(width,height)
        image=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
