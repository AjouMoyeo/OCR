from flask import Flask
from werkzeug.utils import secure_filename
import subprocess
from flask import Flask, render_template, request, redirect, url_for
import json
from flask_cors import CORS


app= Flask(__name__)
CORS(app)

@app.route('/card', methods = ['POST'])
def file_upload():
    if request.method == 'POST':
        """
        print("hi")
        f = request.files['image']
        f.save('image/' + secure_filename(f.filename))

        subprocess.call("OCR.py", shell=True)
        sleep(10)
        with open ('info.json', 'r') as f:
            json_data = json.load(f)
            """
        return "hi"    
        
    
    
@app.route('/filtering',methods=['POST'])
def filtering():
    # 게시글 제목(title), 내용(text) 받아서 필터링
    subprocess.call("../../text_filtering/src/filtering.py --text ''", shell=True) #입력값이 있음
    
if __name__ =='__main__':
    app.run(port="7000",debug=True)
