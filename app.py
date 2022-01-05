from flask import *
import cv2
app=Flask(__name__)
filename=None
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/success",methods=["POST"])
def success():
    global filename
    file=request.files["file"]
    height=int(request.form["height"])
    width=int(request.form["width"])
    if height>0 and width>0:
        filename=file.filename
        file.save(filename)
        try:
            img=cv2.imread(filename)
            img=cv2.resize(img,(width,height))
            cv2.imwrite(filename,img)
        except:
            return render_template("error.html")
        return render_template("success.html")
    else:
        return render_template("value_error.html")
@app.route("/download",methods=["POST"])
def download():
    return send_file(filename,as_attachment=True)
if __name__ == "__main__":
    app.run(debug=True)