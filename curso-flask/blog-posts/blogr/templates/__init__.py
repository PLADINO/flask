from flask import Flask

def create_app():

    #Crear la aplicación
    app = Flask(__name__)
    
    @app.route('/')
    def hola():
        return 'Hola blog-posts'

    return app
