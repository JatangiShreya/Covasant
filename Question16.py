# flask
# Question-16:
# Sharing of content 
# @app.route("/updatefortoday", methods=['GET','POST'])#http://localhost:5000/updatefortoday
# @app.route("/share", methods=['GET'])#http://localhost:5000/share
# @app.route("/clearnotepadtxt", methods=['GET'])#http://localhost:5000/clearnotepadtxt

from flask import Flask, request, render_template_string, redirect, url_for
import os

app = Flask(__name__)
NOTE_FILE = 'note.txt'

#
if not os.path.exists(NOTE_FILE):
    with open(NOTE_FILE, 'w') as f:
        f.write("")

@app.route("/updatefortoday", methods=['GET', 'POST'])  # http://localhost:5000/updatefortoday
def update_for_today():
    if request.method == 'POST':
        note_content = request.form.get('note')
        with open(NOTE_FILE, 'w') as f:
            f.write(note_content)
        return redirect(url_for('share')) 

    else:
     
        with open(NOTE_FILE, 'r') as f:
            current_note = f.read()

        return render_template_string("""
            <h1>Update Today's Note</h1>
            <form method="POST">
                <textarea name="note" rows="10" cols="50">{{ current_note }}</textarea><br>
                <input type="submit" value="Save">
            </form>
            <a href="{{ url_for('share') }}">View Shared Note</a>
        """, current_note=current_note)


@app.route("/share", methods=['GET'])  # http://localhost:5000/share
def share():
    with open(NOTE_FILE, 'r') as f:
        note = f.read()

    return render_template_string("""
        <h1>Shared Note for Today</h1>
        <pre>{{ note }}</pre>
        <a href="{{ url_for('update_for_today') }}">Edit</a> |
        <a href="{{ url_for('clear_notepad_txt') }}">Clear Note</a>
    """, note=note)


@app.route("/clearnotepadtxt", methods=['GET'])  # http://localhost:5000/clearnotepadtxt
def clear_notepad_txt():
    with open(NOTE_FILE, 'w') as f:
        f.write("")
    return render_template_string("""
        <h1>Note Cleared</h1>
        <a href="{{ url_for('update_for_today') }}">Back to Update</a>
    """)


if __name__ == "__main__":
    app.run(debug=True)
