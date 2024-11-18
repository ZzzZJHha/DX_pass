from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/custom")
def custom():
    return render_template("custom.html")


@app.route("/qr")
def qr():
    return render_template("qr.html")


@app.route("/DX_Pass")
def DX_Pass():
    return render_template("DX_Pass.html")


@app.route("/DX_Pass_custom")
def DX_Pass_custom():
    return render_template("DX_Pass_custom.html")


@app.route("/setting")
def setting():
    return render_template("setting.html")


@app.route("/cookie")
def cookie():
    return render_template("cookie.html")


@app.route("/cookie_error")
def cookie_error():
    return render_template("cookie_error.html")


@app.route("/test")
def test():
    return render_template("test.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        "static", "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )


# if __name__ == "__main__":
#    app.run(debug=True, host="0.0.0.0", port=2233)  # 设置端口为 2233


if __name__ == "__main__":

    from gevent import pywsgi

    server = pywsgi.WSGIServer(("0.0.0.0", 2233), app)
    server.serve_forever()
