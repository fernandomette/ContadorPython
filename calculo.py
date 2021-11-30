
qualquer = []
listadehistorico = [qualquer]


def CriaUlLI(array):
    listhistoricoul = document.createElement('ul')
    item = document.createElement('li')
    for i in array:
        item.appendChild(document.createTextNode(array[i]))
        listhistoricoul.appendChild(item)
    return listhistoricoul


def somar():
    numerodigitado = parseFloat(
        document.getElementById("caixanumerodigitado").value)
    resultado = parseFloat(document.querySelector("#resultado").innerText)
    valoranterior = resultado
    resultado = resultado + numerodigitado
    document.querySelector("#resultado").innerText = resultado
    document.getElementById("caixanumerodigitado").value = ""
    qualquer.splice(0, qualquer.length)
    qualquer.push(valoranterior, " + ", numerodigitado, ' = ', resultado)
    document.getElementById('listahistorico').appendChild(
        CriaUlLI(listadehistorico[0]))


def diminuir():
    numerodigitado = parseFloat(
        document.getElementById("caixanumerodigitado").value)
    resultado = parseFloat(document.querySelector("#resultado").innerText)
    valoranterior = resultado
    resultado = resultado - numerodigitado
    document.querySelector("#resultado").innerText = resultado
    document.getElementById("caixanumerodigitado").value = ""
    qualquer.splice(0, qualquer.length)
    qualquer.push(valoranterior, " - ", numerodigitado, ' = ', resultado)
    document.getElementById('listahistorico').appendChild(
        CriaUlLI(listadehistorico[0]))


def multiplicar():
    numerodigitado = parseFloat(
        document.getElementById("caixanumerodigitado").value)
    resultado = parseFloat(document.querySelector("#resultado").innerText)
    valoranterior = resultado
    resultado = resultado * numerodigitado
    document.querySelector("#resultado").innerText = resultado
    document.getElementById("caixanumerodigitado").value = ""
    qualquer.splice(0, qualquer.length)
    qualquer.push(valoranterior, " x ", numerodigitado, ' = ', resultado)
    document.getElementById('listahistorico').appendChild(
        CriaUlLI(listadehistorico[0]))


def dividir():
    numerodigitado = parseFloat(
        document.getElementById("caixanumerodigitado").value)
    resultado = parseFloat(document.querySelector("#resultado").innerText)
    valoranterior = resultado
    resultado = resultado / numerodigitado
    document.querySelector("#resultado").innerText = resultado
    document.getElementById("caixanumerodigitado").value = ""
    qualquer.splice(0, qualquer.length)
    qualquer.push(valoranterior, " / ", numerodigitado, ' = ', resultado)
    document.getElementById('listahistorico').appendChild(
        CriaUlLI(listadehistorico[0]))


def zerarresultado():
    document.querySelector("#resultado").innerText = 0
    document.getElementById("caixanumerodigitado").value = 0
