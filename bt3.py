from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="HoangMinhTri_bt3",
        user="postgres",
        password="130104",
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "users";')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])  
def add_user():
    username = request.form.get('username')  
    email = request.form.get('email')  

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, email) VALUES (%s, %s);', (username, email))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)