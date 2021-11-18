...
        var listadehistorico = [qualquer = []]

        function CriaUlLI(array) 
            {

                var listhistoricoul = document.createElement('ul')

                var item = document.createElement('li')

                for(var i = 0; i < array.length; i++) 
                    {
                        item.appendChild(document.createTextNode(array[i]));
                        listhistoricoul.appendChild(item);
                    }

                // Retorne a lista construída:
                return listhistoricoul;
            }
        
        function somar() {

                var numerodigitado = parseFloat(document.getElementById("caixanumerodigitado").value)

                var resultado = parseFloat(document.querySelector("#resultado").innerText)
                
                var valoranterior = resultado

                resultado = resultado + numerodigitado

                document.querySelector("#resultado").innerText = resultado

                document.getElementById("caixanumerodigitado").value = ""

                qualquer.splice(0, qualquer.length);

                qualquer.push(valoranterior, " + ", numerodigitado , ' = ', resultado)

                document.getElementById('listahistorico').appendChild(CriaUlLI(listadehistorico[0]))

        }
        
        function diminuir() {

                var numerodigitado = parseFloat(document.getElementById("caixanumerodigitado").value)
                
                var resultado = parseFloat(document.querySelector("#resultado").innerText)

                var valoranterior = resultado
    
                resultado = resultado - numerodigitado
               
                document.querySelector("#resultado").innerText = resultado
    
                document.getElementById("caixanumerodigitado").value = ""

                qualquer.splice(0, qualquer.length);

                qualquer.push(valoranterior, " - ", numerodigitado , ' = ', resultado)

                document.getElementById('listahistorico').appendChild(CriaUlLI(listadehistorico[0]))

        }

        function multiplicar() {

                var numerodigitado = parseFloat(document.getElementById("caixanumerodigitado").value)
                
                var resultado = parseFloat(document.querySelector("#resultado").innerText)

                var valoranterior = resultado
    
                resultado = resultado * numerodigitado
               
                document.querySelector("#resultado").innerText = resultado
    
                document.getElementById("caixanumerodigitado").value = ""

                qualquer.splice(0, qualquer.length);

                qualquer.push(valoranterior, " x ", numerodigitado , ' = ', resultado)

                document.getElementById('listahistorico').appendChild(CriaUlLI(listadehistorico[0]))

        }

        function dividir() {

                var numerodigitado = parseFloat(document.getElementById("caixanumerodigitado").value)
                
                var resultado = parseFloat(document.querySelector("#resultado").innerText)

                var valoranterior = resultado
    
                resultado = resultado / numerodigitado
               
                document.querySelector("#resultado").innerText = resultado
    
                document.getElementById("caixanumerodigitado").value = ""

                qualquer.splice(0, qualquer.length);

                qualquer.push(valoranterior, " / ", numerodigitado , ' = ', resultado)

                document.getElementById('listahistorico').appendChild(CriaUlLI(listadehistorico[0]))

        }

        function zerarresultado() {

            document.querySelector("#resultado").innerText = 0
            
            document.getElementById("caixanumerodigitado").value = 0

        }

...