from flask import Flask, redirect, render_template, request, session

print(__name__)
app = Flask(__name__)
app.secret_key = 'key_name' 

@app.route('/')
def index():
    if 'totalcount' not in session:
        session['totalcount'] = 1
    else:
        session['totalcount'] += 1
    if 'times' not in session:
        session['times'] = 1
    else:
        session['times'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add2')
def add2():
    session['times'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('times')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
