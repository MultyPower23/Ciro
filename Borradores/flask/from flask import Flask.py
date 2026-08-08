from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Esta es la página principal'

@app.route('/hola')
def hola():
    return 'Hola!'

@app.route('/adios')
def adios():
    return 'Hasta luego!'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return 'El usuario es: ' + nombre

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return 'Hola ' + nombre
    return '''
        <form method="POST">
            <input type="text" name="nombre" placeholder="Tu nombre">
            <button type="submit">Enviar</button>
        </form>
    '''

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return render_template('saludo.html', nombre=nombre)


if __name__ == '__main__':
    app.run(debug=True)
