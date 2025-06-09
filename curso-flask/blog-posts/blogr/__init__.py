from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    #Crear la aplicación
    app = Flask(__name__)

    #PROBAR LA APLICACION CON UNA VISTA DE EJEMPLO
    # @app.route('/')
    # def hola():
    #     return 'Hola blog-posts'
    
    app.config.from_object('config.Config')
    db.init_app(app)

    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)
    
    import locale 
    locale.setlocale(locale.LC_ALL, 'es_ES')

    #Registrar las vistas
    from blogr import home
    app.register_blueprint(home.bp)
    
    from blogr import auth
    app.register_blueprint(auth.bp)

    from blogr import post
    app.register_blueprint(post.bp)

    from .models import User, Post

    with app.app_context():
        db.create_all()

    return app
