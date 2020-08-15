from flask import Flask, url_for, render_template, request, session
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
    if form.validate_on_submit():
        name = form.name.data
        lName = form.lname.data
        phone = form.phone.data
        
        cur = mysql.connection.cursor()
        query = "INSERT INTO contactos(nombre, apellido, numero) VALUES (%s,%s,%s)"
        cur.execute(query, (name, lName, phone))
        mysql.connection.commit()
        cur.close()
        return render_template('success.html')
    return render_template('insert.html', form=form)


@app.route("/all_contacts")
def all_contacts():
    """Estamo obteniendo los datos que están en la tabla contactos"""
    #TODO: Filtrar cuando por usuario que inicie sesión
    cur = mysql.connect.cursor()
    query = "SELECT * FROM contactos;"
    cur.executer(query)
    contacts=cur.fetchall()
    cur.close()
    return render_template('allcontacts.html', contacts=contacts)