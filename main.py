import colorgram
from flask import Flask, render_template, request, flash
import os

UPLOAD_FOLDER = 'C:/Users/VBALAJI/PycharmProjects/Color Palette Picker Website/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "SOME_SECRET_KEY"


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def change_file(name):
    new = ""
    count = 0
    for i in name:
        if i == "\\" and count < 2:
            count += 1
            new += i
        else:
            new += i
            count = 0
    print(new)
    return new


def color(filename):
    colors = colorgram.extract(f=filename, number_of_colors=10)
    colors_dict = {

        "a": {
            "hex": rgb2hex(colors[0].rgb.r, colors[0].rgb.g, colors[0].rgb.b),
            "proportion": colors[0].proportion
        },
        "b": {
                "hex": rgb2hex(colors[1].rgb.r, colors[1].rgb.g, colors[1].rgb.b),
                "proportion": colors[1].proportion
            },
        "c": {
                "hex": rgb2hex(colors[2].rgb.r, colors[2].rgb.g, colors[2].rgb.b),
                "proportion": colors[2].proportion
            },
        "d": {
                "hex": rgb2hex(colors[3].rgb.r, colors[3].rgb.g, colors[3].rgb.b),
                "proportion": colors[3].proportion
            },
        "e": {
                "hex": rgb2hex(colors[4].rgb.r, colors[4].rgb.g, colors[4].rgb.b),
                "proportion": colors[4].proportion
            },
        "f": {
                "hex": rgb2hex(colors[5].rgb.r, colors[5].rgb.g, colors[5].rgb.b),
                "proportion": colors[5].proportion
            },
        "g": {
                "hex": rgb2hex(colors[6].rgb.r, colors[6].rgb.g, colors[6].rgb.b),
                "proportion": colors[6].proportion
            },
        "h": {
                "hex": rgb2hex(colors[7].rgb.r, colors[7].rgb.g, colors[7].rgb.b),
                "proportion": colors[7].proportion
            },
        "i": {
                "hex": rgb2hex(colors[8].rgb.r, colors[8].rgb.g, colors[8].rgb.b),
                "proportion": colors[8].proportion
            },
        "j": {
                "hex": rgb2hex(colors[9].rgb.r, colors[9].rgb.g, colors[9].rgb.b),
                "proportion": colors[9].proportion
            },
    }
    return colors_dict


@app.route('/')
def main():
    return render_template("index.html", filename="download.png", colors=color(filename="static/download.png"))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template("index.html", filename="download.png", colors=color(filename="static/download.png"))

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return render_template("index.html", filename="download.png", colors=color(filename="static/download.png"))

        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return render_template("index.html", filename=f"{change_file(file.filename)}",
                                   colors=color(filename=f"static/{change_file(file.filename)}"))
        else:
            return render_template("index.html", filename="download.png", colors=color(filename="static/download.png"))

    return render_template("index.html", filename="download.png", colors=color(filename="static/download.png"))


if __name__ == '__main__':
    app.run(debug=True)
