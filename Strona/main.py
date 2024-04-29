from flask import Flask, render_template, request
import mysql.connector

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
@app.route('/logowanie')
def render_logowanie():
    return render_template('logowanie.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Odbierz dane z formularza
    name = request.form['name']
    surname = request.form['surname']
    tel = request.form['tel']
    email = request.form['email']
    pas = request.form['pas']
    sign_for_newsletter = 1 if request.form.get('sign_for_newsletter') else 0

    cursor.execute("INSERT INTO users (name, surname, tel, email, password, newsletter) VALUES (%s, %s, %s, %s, %s)", (name, surname, tel, email, pas, sign_for_newsletter))
    conn.commit()

    return 'Dziękujemy za rejestrację!'

if __name__ == '__main__':
    app.run(debug=True)
