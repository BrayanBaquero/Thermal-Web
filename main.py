#!/usr/bin/env python
#instalar 
#sudo pip3 install opencv-contrib-python
#sudo pip3 install psutil
#sudo pip3 install h5py
#sudo pip3 install Flask
#sudo pip3 install Flask-RESTful

 # ~ git clone https://github.com/groupgets/libuvc
  # ~ sudo apt-get install cmake -y
  # ~ sudo apt-get install libusb-1.0-0-dev -y
  # ~ sudo apt-get install libjpeg-dev -y
  # ~ cd libuvc
  # ~ mkdir build
  # ~ cd build
  # ~ cmake ..
  # ~ make && sudo make install
  # ~ sudo ldconfig -v
  # ~ cd ../..

                                     
from flask import Flask, render_template, Response,stream_with_context, redirect, jsonify,request
from camera import VideoCamera
from urllib.request import urlopen
from flask_restful import Resource, Api




app = Flask(__name__)
api=Api(app)


class data(Resource):
	def get(self,temp):
		mint,maxt=temps(VideoCamera())
		return {"Tmin":mint,"Tmax":maxt}

api.add_resource(data,'/data/<temp>')


@app.route('/color/<color>')
def color(color):
	VideoCamera.col(color);
	return render_template('index.html')

def temps(camerat):
    maxt,mint=camerat.temperaturas()
    return mint,maxt

@app.route('/')
def index():
    return render_template('index.html')
        #~ return Response('index.html',**templateData)

def gen(camerat):
   
    while True:
        frame = camerat.get_frame()
        
  
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
       


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# ~ @app.route('/raimbow', methods=['GET','POST'])
# ~ def raimbow(x=None,y=None):
	# ~ print("pruebaaaaaa")
	# ~ pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False,threaded=True,port=8088)
