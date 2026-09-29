from flask import Flask, request, render_template
from csv import *

file = open('Booklist_price.txt')
file = file.readlines()
dictionary = {}
for item in file:
    if item == file[-1]:
        colon = item.find(',')
        dictionary[item[:colon]] = item[colon+1:]
        break
    colon = item.find(',')
    dictionary[item[:colon]] = item[colon+1:-1]

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('bookshop.html', books_and_price = dictionary)

@app.route('/confirm', methods=['POST'])
def confirm():
    choice = []
    choice += request.form.getlist('book_chosen')
    global name, email
    name = request.form.get('name')
    email = request.form.get('email')
    global chosen
    chosen = {}
    out_chose = 'No'
    for i in choice:
        if len(chosen) == 3:
            out_chose = 'Yes'
            break
        chosen[i] = dictionary[i]
    return render_template('confirm.html', choice = chosen, name=name, email=email, out_chose=out_chose)

@app.route('/receipt', methods=["GET","POST"])
def calculate():
    if request.method == "GET":
        return 'Choose your book first XD'
    if request.method =="POST":
        total = 0
        for i in chosen:
            total += float(dictionary[i])
        return render_template('calculate.html', choice = chosen, total = total, name=name, email=email)

app.run(debug=True, port=5000)


