from flask import Flask, url_for, render_template, request, session, redirect, flash
from flask_login import LoginManager, login_required, logout_user, login_user
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from form import ContactForm
from user import User

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'vidm'
app.config['MYSQL_PASSWORD'] = 'Kernel80_'
app.config['MYSQL_DB'] = 'contacts'
app.config['SECRET_KEY'] = 'klasdjfklj232ijr_'

mysql = MySQL(app)

Bootstrap(app)
login_manager = LoginManager(app)

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

@app.route('/update_contact/<id>', methods=['POST'])
def update_contact(id):

    form = ContactForm()
    contact = {}
    if form.validate_on_submit():
        name = form.name.data
        lName = form.lname.data
        phone = form.phone.data

        cur = mysql.connection.cursor()
        print("{} {} {} {}".format(name, lName, phone, id))
        query = "UPDATE contactos SET nombre=%s, apellido=%s, numero=%s WHERE id_contact=%s"
        cur.execute(query, (name, lName, phone,id))
        mysql.connection.commit()
        cur.close()

        flash("Actualización Exitosa")   
        return redirect(url_for('all_contacts'))

@app.route("/edit/<post_id>")
def edit(post_id):
    form = ContactForm()
    cur = mysql.connect.cursor()
    # query = "SELECT * FROM contactos WHERE id_contact=%s"
    print(post_id)
    cur.execute(""" SELECT * FROM contactos WHERE id_contact=%s """,(post_id))
    contact = cur.fetchall()
    print(contact)
    return render_template('edit.html',form=form, contacts=contact[0])

@app.route("/all_contacts")
def all_contacts():
    """Estamo obteniendo los datos que están en la tabla contactos"""
    #TODO: Filtrar cuando por usuario que inicie sesión
    cur = mysql.connect.cursor()
    query = "SELECT * FROM contactos;"
    cur.execute(query)
    contacts = cur.fetchall()
    cur.close()
    return render_template('allcontacts.html', contacts=contacts)

#login manager
@login_manager.user_loader
def load_user(user_id):
    pass

