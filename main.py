from flask import Flask, url_for, render_template, request, session, redirect, flash
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from form import ContactForm, LoginForm
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
login_manager.login_view = "login"

@app.route('/insert', methods=['GET','POST'])
@login_required
def add_contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        lName = form.lname.data
        phone = form.phone.data
        cur = mysql.connection.cursor()
        query = "INSERT INTO contactos(nombre, apellido, numero, id_usuario) VALUES (%s,%s,%s,%s)"
        cur.execute(query, (name, lName, phone, current_user.id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('all_contacts'))
    return render_template('insert.html', form=form)

@app.route('/update_contact/<id>', methods=['POST'])
@login_required
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
@login_required
def edit(post_id):
    form = ContactForm()
    cur = mysql.connect.cursor()
    cur.execute(""" SELECT * FROM contactos WHERE id_contact=%s """,[post_id])
    contact = cur.fetchall()
    print(contact)
    return render_template('edit.html',form=form, contacts=contact[0])

#Delete contacts
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cur = mysql.connection.cursor()
    query = "DELETE FROM contactos WHERE id_contact={}".format(id)
    cur.execute(query)
    mysql.connection.commit()
    flash("Se elimino el contacto satisfactoriamente")
    return redirect(url_for('all_contacts'))


@app.route("/")
@app.route("/all_contacts")
@login_required
def all_contacts():
    """Estamo obteniendo los datos que están en la tabla contactos"""
    #TODO: Filtrar cuando por usuario que inicie sesión
    cur = mysql.connect.cursor()
    query = """SELECT contactos.id_contact, contactos.nombre, contactos.apellido, numero FROM contactos 
               LEFT JOIN usuarios ON usuarios.id_usuario = %s;"""
    cur.execute(query,[current_user.id])
    contacts = cur.fetchall()
    cur.close()
    return render_template('allcontacts.html', contacts=contacts)

@app.route("/login",methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('all_contacts'))

    form = LoginForm()
    if form.validate_on_submit():
        username=form.user.data
        password=form.password.data
        cur = mysql.connect.cursor()
        query = "SELECT id_usuario, nom_usuario, password FROM usuarios WHERE nom_usuario IN(%s)"
        cur.execute(query,[username])
        user = cur.fetchall()
        cur.close()

        if user[0][2] == password and user[0][1] == username:
            user = User(user[0][0], username)
            User.user.append(user)
            login_user(user)
            flash("Se inicio sesión exitosamente")
            return redirect(url_for('all_contacts'))

        print("user:{} password:{}".format(username,password))
    return render_template('login.html', form=form)

#login manager
@login_manager.user_loader
def load_user(user_id):
    users = User.user
    for user in users:
        if user.id == int(user_id):
            return user

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
