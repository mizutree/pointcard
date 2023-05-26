from flask import Flask, render_template, request

app = Flask(__name__)

point = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
}


@app.route("/")
def hello():
    return render_template("index.html", message="Hello, Flask!")


@app.route("/get/")
def get_all():
    return render_template("table.html", point=point)


@app.route("/get/<int:id>")
def get(id):
    return render_template("table.html", id=id)


@app.route("/form", methods=["POST"])
def horm():
    # idを取得
    id = request.form.get("id")
    add_point = request.form.get("point")
    # idがない場合はエラー
    if id is None or point is None:
        return "error"
    # pointを加算
    print(id, add_point)
    point[int(id)] += int(add_point)
    return render_template("result.html", point=add_point)


if __name__ == "__main__":
    app.run()
