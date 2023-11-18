from flask import Flask, request, redirect, url_for, render_template,send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__,static_folder='/static',template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    file_list = os.listdir(app.config['UPLOAD_FOLDER'])
    # 渲染模板并传递文件列表作为参数
    return render_template('files.html', files=file_list)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    directory = app.config['UPLOAD_FOLDER']
    return send_from_directory(directory, filename)

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = os.getcwd()+'/static/uploads/'
    app.run()
