from flask import Flask, Response, render_template, send_file, json
import requests
import base64

# def takePicture():
#     stream = BytesIO()
#     camera.capture(stream, format='jpeg')
#     stream.seek(0)
#     im = Image.open(stream)
#     im_buffer = im.load()
#     return im, im_buffer

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/take')
def take_picture():
    image = '/justin_smells.jpeg'
    img_str = None
    with open(image, "rb") as imageFile:
        img_str = base64.b64encode(imageFile.read())
    response = Response(
        response = json.dumps({
            'data': 'data:image/png;base64,' + img_str
        }),
        status = 200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
