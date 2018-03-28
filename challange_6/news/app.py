#!/usr/bin/env python3
import os
import json
from flask import Flask, render_template, redirect, url_for, abort

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] =True

class Files(object):
    '''Get file title, content'''
    directory = os.path.join(os.path.abspath(os.path.dirname(__name__)),'..','files')
    
    def __init__(self):
       self._files = self._read_all_files()

    def _read_all_files(self):
        index_file_list = {}
        all_files = os.listdir(self.directory)
        for i in all_files:
            if os.path.splitext(i)[1] == '.json':
                filename = os.path.splitext(i)[0]
                file_path = os.path.join(self.directory,i)
                with open(file_path) as f:
                    content = json.loads(f.read())
                    index_file_list[filename] = content
        return index_file_list

    def show_title_list(self):
        return [item['title'] for item in self._files.values()]

    def show_essay_content(self, filename):
        return self._files.get(filename)

files = Files()

@app.route('/')
def index():
    return render_template('index.html',content=files.show_title_list())

@app.route('/files/<filename>')
def essays(filename):
    file_content = files.show_essay_content(filename)
    #if not file_content:
        #redirect(url_for('not_found'))
    # alternative way - 
    if not file_content:abort(404)
    return render_template('file.html',file_content=file_content)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
