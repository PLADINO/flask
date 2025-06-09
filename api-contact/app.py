from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

#Crear modelo de la base de datos

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)

    #Método en tipo diccionario paa facilitar pasarlo a tipo JSON
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'phone':self.phone
            }

#Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# --- Ejecutar la aplicación en modo debug ---
# flask  --app app --debug run


#Crear una función para rutas
@app.route('/contacts', methods = ['GET'])
def get_contacts():
    contacts = Contact.query.all()
    #list_contact = []
    #for contact in contacts:
    #    list_contact.append(contact.serialize())
    return jsonify({'contacts': [contact.serialize() for contact in contacts]}) #Aqui se hace en una sola línea

@app.route('/contacts', methods = ['POST'])
def create_contact():
    data = request.get_json()
    contact = Contact(name = data['name'], email = data['email'], phone = data['phone'])
    db.session.add(contact)
    db.session.commit()
    return jsonify({'message':'Contacto creado con éxito', 'contact': contact.serialize()}), 201 


#Crear una función para obtener un contacto específico
@app.route('/contacts/<int:id>', methods = ['GET'])
def get_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({'message':'No se encontró el contacto buscado'}), 404
    return jsonify(contact.serialize())

#Crear una función para editar un contacto específico
@app.route('/contacts/<int:id>', methods = ['PUT', 'PATCH'])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)
    
    data = request.get_json()

    if 'name' in data:
        contact.name = data['name']
    if 'email' in data:
        contact.email = data['email']
    if 'phone' in data:
        contact.phone = data['phone']
    
    #Guardar los cambios en la base de datos
    db.session.commit()

    return jsonify({'message':'Contacto actualizado con éxito', 'contact': contact.serialize()})
    
#Crear una función para eliminar un contacto específico
@app.route('/contacts/<int:id>', methods = ['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({'message':'No se encontró el contacto buscado'}), 404
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message':'Contacto eliminado con éxito'})
    