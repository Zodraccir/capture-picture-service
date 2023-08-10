from flask import (
    Flask,
    jsonify
)
from flask_cors import CORS
import os
import camera_capture as cc
import base64
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
IMAGE_DIR='images'

@app.route('/capture_image')
def capture_image():

    print(os.getcwd())
    dir_path=os.getcwd()+'/'+IMAGE_DIR
    # checking if the directory to store the images 
    # exist or not.
    if not os.path.exists(dir_path):
        # if the directory to store the images is not present 
        # then create it.
        os.makedirs(dir_path)

    filename_path=dir_path+'/last_shot.png'
    if cc.shot(filename_path):
        try:
            with open(filename_path, 'rb') as f: # open the file in read binary mode
                data = f.read() # read the bytes from the file to a variable
        
            img_base64 = base64.b64encode(data)
            
            return jsonify({'status': True, 'image': img_base64.decode()}), 200
        except Exception as e:
            return jsonify({'status':False, 'message': f'Error converting image {e}'}),400


    else:
        return jsonify({'status':False, 'message': 'Error taking picture'}),400
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8989, debug=True)
