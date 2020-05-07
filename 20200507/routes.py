from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 
# 읽어들인 파일을 보호해주기 위한 함수

app = Flask(__name__)

@app.route('/upload')
def load_file():
    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename)) # 보호해준다.
        return 'file uploaded successfully'
		
if __name__ == '__main__':
    app.run(debug = True)