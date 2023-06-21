let pesoHTML = document.querySelector("#peso")
let alturaHTML = document.querySelector("#altura")
let peso = 0
let altura = 0
pesoHTML.addEventListener("change", function(){
    peso = parseInt(this.value)
})
alturaHTML.addEventListener("change", function(){
    altura = parseInt(this.value)/100
})

function calcular(){
    let resultHTML = document.querySelector("#result")
    if (peso > 0 && altura > 0){
        let imc = parseInt((peso/(altura*altura)))
        resultHTML.textContent = "Su IMC es de: " + imc.toString() + " (" + suPeso(imc) + ")"
    } 
    else {
        resultHTML.textContent = "Ingrese datos validos"
    }
}

function suPeso(imc){
    let resultado = ""
    if(imc < 20){
        resultado = "Delgadez"
    }
    else if(imc <= 25){
        resultado = "Normal"
    }
    else if (imc <= 30){
        resultado = "Sobrepeso"
    }
    else{
        resultado = "Obesidad"
    }
    return resultado
}