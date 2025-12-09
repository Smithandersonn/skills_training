
const modo = document.getElementById("modo"); 
const color_switch = document.getElementById("sw_color")
const custom_section = document.getElementById("custom_section")
let startstop = document.getElementById("start_stop")
let time_study = document.getElementById("estudo");
let time_rest = document.getElementById("pausa");
let operacao = document.getElementById('operacao');
let stop_bottom = document.getElementById("stop")

/*variaveis timer*/
let timerInterval = null;

let isRunning = false;
let isPausa = false;

let minutos = parseInt(time_study.value) || 25;
let segundos = 0;

let pausaMinutos = parseInt(time_rest.value)|| 5;
let pausaSegundos = 0;

const totalCiclos = 3;
let cicloAtual = 0;

/*Só uma condição para definir a quando o timer deve parar*/
if (cicloAtual == 3){pararTimer();resetCompleto();}

/*Função Responsavel Pelo Loop Do timer*/
function iniciarTimer(){

    if (isRunning){console.log("Timer Já está rodando!");return;}
        
    isRunning = true
  
    timerInterval = setInterval(function() {

        if (!isPausa) {
        segundos--;
        
        if (segundos < 0) {
            minutos--;
            segundos = 59;
        }
        if (minutos < 0) {
            cicloAtual++;
            console.log(`✅ Ciclo ${cicloAtual} de ${totalCiclos} completado!`);
                
            if (cicloAtual >= totalCiclos) {
                pararTimer();
                resetCompleto();
                alert("🎉 Todos os ciclos completos!");
                return;
                }
                iniciarPausa();
        }}
    else {
        pausaSegundos--;
        
        if (pausaSegundos < 0) {
            pausaMinutos--;
            pausaSegundos = 59;
        }
        if (pausaMinutos < 0) {
            console.log("Pausa finalizada! Hora de estudar!");
            pararTimer(); 
            voltarAoEstudo(); 
            iniciarTimer();
            return;
        }
    }
    atualizarDisplay();
    }, 1000);
};
/*Função Responsavel Pelo Loop Da Pausa*/
function iniciarPausa() {
    isPausa = true;
    console.log("🔄 Iniciando pausa de 5 minutos...");
    pausaMinutos = parseInt(time_rest.value)|| 5;
    pausaSegundos = 0;
    atualizarDisplay();
};
/*Função Responsavel Por Retornar ao Primeiro Loop*/
function voltarAoEstudo() {

    isPausa = false;
    minutos = parseInt(time_study.value)|| 25;
    segundos = 0;
    
    console.log(`🔄 Voltando ao estudo de ${minutos + 1} minutos...`);
    atualizarDisplay();
};
/*Função Responsavel Por parar o Loop Do timer*/
function pararTimer() {
    isRunning = false;
    if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
    }
};
/*Função Responsavel Por atualizar os valores do timer no modo custom*/
function atualizarValores() {
    if (operacao.textContent === "CUSTOM" && !isRunning) {
        if (time_study.value) {
            minutos = parseInt(time_study.value);
            segundos = 0;
        } else {
            minutos = 25;
        }
        }
        if (time_rest.value) {
            pausaMinutos = parseInt(time_rest.value);
            pausaSegundos = 0;
        } else {
            pausaMinutos = 5;
        }
    atualizarDisplay();
};
/*Função Responsavel Por resetar Tudo*/
function resetCompleto(){
    pararTimer();
    isPausa = false;
    isRunning = false;
    cicloAtual = 0;

    minutos = parseInt(time_study.value) || 25;
    segundos = 0;
    pausaMinutos = parseInt(time_rest.value) || 5;
    pausaSegundos = 0;
    
    modo.disabled = false;
    startstop.textContent = "START";
    startstop.style.backgroundImage = "url('./imagens/play.png')";
    startstop.style.backgroundPosition = "center";
    startstop.style.backgroundSize = "90px";
    startstop.style.backgroundRepeat = "no-repeat";
    startstop.style.opacity = "0.5"; 
    startstop.style.filter = "blur(0.2px)";
    time_rest.value = "";
    time_study.value = "";
    if (operacao.textContent == "CUSTOM") {
        time_study.disabled = false;
        time_rest.disabled = false;
    }

    clock.textContent = "25:00";
};
/* Funções do botão Padrão ou Custom*/
function change(){
    if (operacao.textContent == "PADRAO") {
        operacao.textContent = "CUSTOM";
        time_study.disabled = false;
        time_rest.disabled = false;
        time_rest.placeholder = "pausa";
        time_study.placeholder = "minutos";
        resetCompleto();
    } else {
        operacao.textContent = "PADRAO"; 
        time_study.disabled = true;
        time_rest.disabled = true;     
        time_rest.placeholder = "";
        time_study.placeholder = ""; 
        time_rest.value = "";
        time_study.value = "";
}
atualizarDisplay();};
/* Funções do botão Play e pause*/ 
function swstartstop(){
    if (startstop.textContent == "START" && !isRunning){
        iniciarTimer();
        startstop.textContent = "PAUSE";
        startstop.style.backgroundImage = "url(./imagens/pause.png)";
        startstop.style.backgroundPosition = "center";
        startstop.style.backgroundSize = "70px";
        startstop.style.backgroundRepeat = "no-repeat";
        startstop.style.opacity = "0.5"; 
        startstop.style.filter = "blur(0.2px)";
        modo.disabled = true;
        time_study.disabled = true;
        time_rest.disabled = true;
        
    }
    else{
        startstop.textContent = "START";
        pararTimer();
        startstop.style.backgroundImage = "url(./imagens/play.png)";
        startstop.style.backgroundPosition = "center";
        startstop.style.backgroundSize = "90px";
        startstop.style.backgroundRepeat = "no-repeat";
        startstop.style.opacity = "0.5"; 
        startstop.style.filter = "blur(0.2px)";
        modo.disabled = true;
    }

};
/*Atualizar Display*/
function atualizarDisplay() {
    let m, s;
    
    if (!isPausa) {
        m = minutos.toString().padStart(2, '0');
        s = segundos.toString().padStart(2, '0');
        document.getElementById('clock').textContent = `${m}:${s}`;
    } else {
        m = pausaMinutos.toString().padStart(2, '0');
        s = pausaSegundos.toString().padStart(2, '0');
        document.getElementById('clock').textContent = `${m}:${s} `;
    }
};
/* Função para alternar as cores do tema */
color_switch.addEventListener("click", function(){
    let currentColor = this.textContent;
    let nextColor;  

    document.body.classList.remove('color1', 'color2', 'color3', 'color4');
    
    if (currentColor === "color1") {
        nextColor = "color2";
    } else if (currentColor === "color2") {
        nextColor = "color3";
    } else if (currentColor === "color3") {
        nextColor = "color4";
    } else {
        nextColor = "color1";
    }
    document.body.classList.add(nextColor);
    this.textContent = nextColor;
});

/*Uma espécie de escuta para atualizar os valores do timer quando em modo custom*/
time_study.addEventListener('input', atualizarValores||25);
time_rest.addEventListener('input', atualizarValores);
console.log("Timer Pronto!");
atualizarDisplay();