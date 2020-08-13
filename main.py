from flask import Flask, url_for, render_template, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from form import ContactForm

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'vidm'
app.config['MYSQL_PASSWORD'] = 'Kernel80_'
app.config['MYSQL_DB'] = 'contacts'
app.config['SECRET_KEY'] = 'klasdjfklj232ijr_'

mysql = MySQL(app)

Bootstrap(app)

@app.route('/insert', methods=['GET','POST'])
def add_contact():
    form = ContactForm()
    # if request.method == "POST":
    #     name = request.form['fName']
    #     lName = request.form['fLastName']
    #     phone = request.form['fPhone']

    #     cur = mysql.connection.cursor()
    #     query = "INSERT INTO contactos(nombre, apellido, numero) VALUES (%s,%s,%s)"
    #     cur.execute(query, (name, lName, phone))
    #     mysql.connection.commit()
    #     cur.close()
    #     return render_template('success.html')
    return render_template('insert.html', form=form)