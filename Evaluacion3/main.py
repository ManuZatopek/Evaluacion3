from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        n3 = float(request.form['n3'])
        asistencia = int(request.form['asistencia'])
        promedio = 0
        promedio = (n1 + n2 + n3) /3
        if promedio >= 40 and asistencia >= 75:
            resultado = 'Aprobado'
            ruta = "/static/img/aprobado.jpg"
        else:
            resultado = 'Reprobado'
            ruta = "/static/img/reprobado.jpg"
        return render_template('ejercicio1.html', promedio=promedio, resultado=resultado, ruta=ruta)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nom1 = request.form['nom1']
        nom2 = request.form['nom2']
        nom3 = request.form['nom3']

        if len(nom1) > len(nom2) and len(nom1) > len(nom3):
            mayor = nom1
            cantidad = len(nom1)

        elif len(nom2) > len(nom1) and len(nom2) > len(nom3):
            mayor = nom2
            cantidad = len(nom2)
        else:
            mayor = nom3
            cantidad = len(nom3)
        return render_template('ejercicio2.html', mayor=mayor, cantidad=cantidad)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
