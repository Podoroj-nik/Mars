import json
import random

from flask import Flask, url_for, render_template, request
import os

addr_data = os.path.join('static', 'data')

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = addr_data

sp = ["Человечество вырастает из детства.", "Человечеству мала одна планета.", "Мы сделаем обитаемыми безжизненные "
      "пока планеты.", "И начнем с Марса!", "Присоединяйся!"]


@app.route('/')
def start():
    return f"Миссия Колонизация Марса"


@app.route('/index')
def index():
    return f"И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '</br>'.join(sp)


@app.route('/image_mars')
def mars_img():
    return f'''<!DOCTYPE html>
                 <html lang="en-US">
                   <head>
                     <meta charset="utf-8">
                     <meta name="viewport" content="width=device-width">
                     <title>Жди нас, Марс!</title>
                   </head>
                   <body>
                    <h1>Жди нас, Марс!</h1>
                    <figure>
                        <img src="{url_for('static', filename='img/Mars.jpg')}" 
                        alt="здесь должна была быть картинка, но не нашлась"
                        width=500px>
                        <figcaption>Вот она какая, красная планета.</figcaption>
                    </figure>
                   </body>
                 </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Загрузка фотографии</title>
                          </head>
                          <body>
                            <div class="card">
                                <h1>Загрузка фотографии</h1>
                                <h2>Для участия в миссии</h2>
                                <form method="post" enctype="multipart/form-data">
                                    <figure>
                                        <img src="{url_for('static', filename='data/im.png')}"
                                        alt="здесь должно быть выше фото))"
                                        width=500px>
                                    </figure>
                                    <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/data/im.png', "wb") as file:
            file.write(f.read())
        return "Форма отправлена"


@app.route('/carusel')
def carusel():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                         <link rel="stylesheet"
                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                         crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Пейзажи марса</title>
                      </head>
                      <body>
                        <div class="card">
                            <h1>Пейзажи марса</h1>
                            <div id="carouselExample" class="carousel slide">
                              <div class="carousel-indicators">
                                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                              </div>
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img src="static/img/Mars.jpg" class="d-block w-100" alt="Mars 1">
                                </div>
                                <div class="carousel-item">
                                  <img src="static/img/Mars2.jpg" class="d-block w-100" alt="Mars 2">
                                </div>
                                <div class="carousel-item">
                                  <img src="static/img/Mars3.jpg" class="d-block w-100" alt="Mars 3">
                                </div>
                              </div>
                              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                              </button>
                              <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                              </button>
                            </div>
                        </div>
                      </body>
                    </html>'''



@app.route('/galery', methods=['POST', 'GET'])
def galery():
    sp_img = []
    sp_im = os.listdir(addr_data)
    for i in range(len(sp_im)):
        im = os.path.join(app.config['UPLOAD_FOLDER'], sp_im[i])
        sp_img.append(im)
    if request.method == 'GET':
        return render_template('galery.html', user_images=sp_img)
    elif request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        f_name = f'static/data/' + f.filename
        with open(f_name, "wb") as file:
            file.write(f.read())
        return "Форма отправлена"


@app.route('/member')
def member():
    with open("./templates/members.json", "rt", encoding="utf8") as f:
        members_list = json.loads(f.read())
    k = members_list['members']
    member = random.randint(0, len(k) - 1)
    mem = k[member]
    im = os.path.join(app.config['UPLOAD_FOLDER'], mem['photo'])
    return render_template('members.html', member=mem, user_images=im)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
