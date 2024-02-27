from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

notes = []

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        load_notes()
        return render_template("home.html", notes = notes)
    
    if request.method == "POST":
        note_text = request.form.get("note")
        if note_text:
            notes.append({'text' : note_text})
            save_notes()
            return redirect(url_for('index'))

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)