from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Clave para las sesiones

# almacenamos datos de usuario y contraseña
users = {
    "carlos": "password123",
    "admin": "adminpass"
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificación de usuario
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            flash('Nombre de usuario o contraseña incorrectos')

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        return render_template('bienvenida.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
