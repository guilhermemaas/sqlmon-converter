import os
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:\\Users\\guilherme.maas\\Documents\\dev\\sqlmon-converter\\uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',
            #                        filename=filename))
    #try:
    #    return send_file(f'{UPLOAD_FOLDER}\{filename}', attachment_filename=f'{filename}')
    #except Exception as e:
    #    return str(e)
    return'''
    <!doctype html>
    <html lang="en">
    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>SQLMon>SQL</title>
    </head>
    <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">
            <img src=".\static\sqlmon.png">
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
            <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <a class="nav-link" href="https://github.com/guilhermemaas/sqlmon-converter">GitHub<span class="sr-only">(current)</span></a>
            </li>
            </ul>
            <span class="navbar-text">
                guilherme.maas@gmail.com
            </span>
        </div>
    </nav>

    <div class="jumbotron">
        <h1 class="display-4">SQLMon>SQL</h1>
        <p class="lead">Cria um arquivo de fácil visualização com base nos parâmetros de entrada e dados de saída dos comandos SQL.</p>
        <hr class="my-4">
        <p class="lead">
            <div>
                <form method=POST enctype=multipart/form-data>
                    <div class="form-group">
                        <label for="exampleFormControlFile1">Selecione o arquivo de entrada:</label>
                        <input type="file" class="form-control-file" id="exampleFormControlFile1" name="file">
                        <br>
                        <div class="col-xs-12 col-xs-offset-0 col-sm-6 col-sm-offset-3"></div>
                            <input type="submit" class="btn btn-secondary btn-lg" id="sendfile1" text="Gerar Arquivo" value=Enviar>
                        </div>
                    </div>
                </form>
            </div>
        </p>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    </body>
    </html>
    '''

