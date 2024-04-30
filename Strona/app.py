from flask import Flask, render_template, request
import mysql.connector
import bcrypt

app = Flask(__name__)

# Połączenie z bazą danych MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="23solutions"
)
cursor = conn.cursor()

@app.route('/')
def render_index():
    return render_template('index.html')

@app.route('/onas')
def render_onas():
    return render_template('onas.html')

@app.route('/szkolenia')
def render_szkolenia():
    return render_template('szkolenia.html')

@app.route('/kontakt')
def render_kontakt():
    return render_template('kontakt.html')

@app.route('/logowanie')
def render_logowanie():
    return render_template('logowanie.html')

@app.route('/szkolenie')
def render_szkolenie():
    return render_template('szkolenie.html')


@app.route('/rejestracja')
def render_rejestracja():
    return render_template('rejestracja.html')




@app.route('/register', methods=['GET', 'POST'])
def register():
    name = request.form['name']
    surname = request.form['surname']
    tel = request.form['tel']
    email = request.form['email']
    pas = request.form['password']
    sign_for_newsletter = 1 if request.form.get('sign_for_newsletter') else 0


    h_pas = bcrypt.hashpw(pas.encode('utf-8'), bcrypt.gensalt())

    cursor.execute("INSERT INTO users (name, surname, mail, phone, password, newsletter) VALUES (%s, %s, %s, %s, %s, %s)",
                   (name, surname,  email, tel, h_pas, sign_for_newsletter))
    conn.commit()

    return render_template('logowanie.html',login_label = "Konto zostało utworzone")

if __name__ == '__main__':
    app.run(debug=True)
