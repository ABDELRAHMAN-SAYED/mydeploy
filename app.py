#!/usr/bin/env python
# coding: utf-8

# In[8]:

# In[ ]:


from flask import Flask, render_template, url_for, request, redirect,flash,session
import warnings
warnings.filterwarnings("ignore")
# from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = { 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
app = Flask(__name__,template_folder='template')
app.config['SECRET_KEY'] = 'AJDJRJS24$($(#$$33--' #<--- SECRET_KEY must be set in 
@app.route('/')
def hello():
    session['secrrt']='sec'
    return render_template('index.html')



@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'pdf-file' in request.files:
            pdf_file = request.files['pdf-file']
            if pdf_file.filename == '':
                flash('No pdf file selected')
                return redirect(request.url)
            if pdf_file and allowed_file(pdf_file.filename):
        #         file = secure_filename(pdf_file.filename)
                pdf_file.save("static/"+pdf_file.filename)
                caption = extract_text_caption_image("static/"+pdf_file.filename)
                result_dic = {

                    'description' : caption
                }
            return render_template('index.html', results = result_dic)
        else:
            img_file = request.files['img-file']
            if img_file.filename == '':
                flash('No image file selected')
                return redirect(request.url)
            if img_file and allowed_file(img_file.filename):
                img_file.save("static/"+img_file.filename)
                caption = caption_this_image("static/"+img_file.filename)
            
                result_dic = {

                    'description' : caption
                }
            return render_template('index.html', results = result_dic)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug = True,use_debugger=False, use_reloader=False)


# In[ ]:




