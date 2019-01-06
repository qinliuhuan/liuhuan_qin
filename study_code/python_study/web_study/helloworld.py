from flask import Flask

app = Flask(__name__)

from flask import render_template
from flask import request
from flask import url_for, redirect

from WTForm_test import BulletinForm

# @app.route('/')
# def index():
#     return redirect('/check')
#
# @app.route('/check')
# def f_check():
#     abort(400)
#
# @app.errorhandler(400)
# def bad_request(error):
#     return render_template('bad_request.html'), 400
#
# def hello_flask():
#     return "hello world ,this is the frame of Flask"
#
# @app.route('/sayhello')
# def say_hello():
#     return "say hello router"
#
# @app.route('/hello/')
# def hello_none():
#     tmp = (Markup('<strong> Hi %s ! </strong>' % '<blink> David </blink>'))
#     print tmp
#     return tmp
#
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

# @app.route('/login/<username>')
# def show_welcome(username):
#     return 'Hi %s ' % username
#
# @app.route('/add/<int:number>')
# def add_one(number):
#     return '%d ' % (number + 10)
#
# @app.route('/SendMessage', methods=['GET', 'POST'])
# def Messing():
#     if request.method == "POST":
#         do_send()
#     else:
#         show_the_send_form()
#
# @app.route('/Message', methods=['POST'])
# def do_send():
#     print "do send()func"
#
# @app.route('/Message', methods=['GET'])
# def show_the_send_form():
#     print "shdow the send form func"

# @app.route('/redirect_url')
# def redirect_url():
#     next = request.args.get('next') or url_for('index')
#     return redirect(next)
#
#
# @app.route('/echo_url')
# def echo_url():
#     return request.base_url

import orm
import os
import datetime
from distutils import util as Util
import uuid


def do_view_bulletins(form):
    if request.method == 'POST' and form.validate():
        if form.id.data:
            bulltin = orm.Bulltin.query.get(int(form.id.data))
            bulltin.dt = form.dt.data
            bulltin.title = form.title.data
            bulltin.content = form.content.data
            bulltin.source = form.source.data
            bulltin.author = form.author.data
            orm.db.session.commit()
        else:
            bulletin = orm.Bulltin(form.dt.data, form.title.data, form.content.data,
                                   form.source.data, form.author.data)
            orm.db.session.add(bulletin)
            orm.db.session.commit()
            form.id.data = bulletin.id

        if request.form.has_key('upload'):
            file = request.files['image']
            if file:
                UPLOAD_PATH = ''
                file_server = str(uuid.uuid1()) + Util.file_extension(file.filename)
                pathfile_server = os.path.join(UPLOAD_PATH, file_server)
                file.save(pathfile_server)
                if os.stat(pathfile_server).st_size < 1 * 1024 * 1024:
                    bulletinimage = orm.Bulltinimage(bulletin.id, file_server)
                    orm.db.session.merge(bulletinimage)
                    orm.db.session.commit()
                else:
                    os.remove(pathfile_server)
            else:
                return redirect(url_for('view_bulletin'))
    else:
        form.dt.data = datetime.datetime.now()

    if form.id.data:
        bulletin = orm.Bulltin.query.get(int(form.id.data))
        form.bulletin = bulletin
        if form.bulletin:
            form.bulletinimages = form.bulletin.bulletinimages

    return render_template('view_bulletin.html', form=form)


@app('/bd/view_bulletins', method=['GET', 'POST'])
def view_bulletins():
    form = BulletinForm(request.form)
    do_view_bulletins(form)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5555')
