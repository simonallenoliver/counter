from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    session['visits'] = session.get('visits', 0) + 1
    return render_template('index.html', visits = session['visits'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True) 