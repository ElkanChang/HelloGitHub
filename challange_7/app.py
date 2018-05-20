#!/usr/bin/python3
import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/challange7'
db = SQLAlchemy(app)

class Category(db.Model):
    id_category = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(128))

    def __init__(self,category_name):
        self.category_name = category_name
    
    def __repr__(self):
        return '<Category(name=%s)>' % self.category_name

class File(db.Model):
    article_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id_category'))
    category = db.relationship('Category',backref=db.backref('articles',lazy='dynamic'))
    
    def __init__(self, title, content, category, created_time=None):
        self.title = title
        self.content = content
        self.category = category
        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time
    
    def __repr__(self):
        return '<File(name=%s)>' % self.title

@app.route('/')
def index():
    index_content = File.query.all()
    return render_template('index.html', index_content=index_content)

@app.route('/files/<int:file_id>')
def files(file_id):
    file_page_content = File.query.get_or_404(file_id)
    return render_template('files.html', file_page_content=file_page_content)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
