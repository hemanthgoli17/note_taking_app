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
            notes.append(note_text)
            save_notes(notes)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

@app.route('/delete_note/<note_text>', methods = ["POST"])
def delete_note(note_text):
    if request.method == "POST":
        with open('notes.json', "r+") as f:
            data = json.load(f)
            for note_index,note_content in enumerate(data):
                if note_content == note_text:
                    del data[note_index]
                    save_notes(data)
                    break
            f.seek(0)
        return redirect(url_for('index'))

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def save_notes(data):
    with open('notes.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)