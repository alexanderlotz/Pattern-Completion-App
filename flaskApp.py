from flask import Flask, render_template, url_for, request, redirect, session
# mainfile = __import__("main.py")
# generate = mainfile.generate

globalRows = 10
globalCols = 3

def generate(seq, subsetRow, subsetCol, dir, n):
    return [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]
    print("hi")

app = Flask(__name__)

# @app.route('/generate', methods=['POST'])
# def gen():
#     if valid_input(request.form['rows'], request.form['cols'], request.form['seq']):
#         session['row'] = 5
#         # determine_direction() ???
#         out = generate(request.form['seq'],request.form['rows'], request.form['cols'], 'u', 0)
#         return render_template("index.html", output=out)

def resize_matrix(rows, cols):
    globalRows = rows
    globalCols = cols
    print(globalRows)
    print(globalCols)


def valid_input(rows, cols, seq):
    return (rows.isnumeric()
        and cols.isnumeric()
        and rows > 0 
        and cols > 0
        and cols*rows > len(seq))


@app.route('/')
def index():
    return render_template("index.html", 
    rows=globalRows, 
    cols=globalCols, 
    output=None, 
    resizeFn=resize_matrix,
    generateFn=generate)

if __name__ == "__main__":
    app.run(debug=True)
