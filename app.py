import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('password') == '1712008':
            session['unlocked'] = True
            return redirect(url_for('gift'))
        else:
            return render_template('index.html', error=True)
    return render_template('index.html', error=False)

@app.route('/gift')
def gift():
    if not session.get('unlocked'):
        return redirect(url_for('home'))
    return render_template('gift.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
