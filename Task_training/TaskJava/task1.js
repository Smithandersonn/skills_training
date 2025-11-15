/*Criando programação orientada a objeto ENCAPSULAMENTO*/


class Caracter{
/* O # na frente de cada propridade deixa ela privada, evitando modificar seu vaslor externamente*/
nome
#vida
#forca
#nivel
#velocidade

    constructor (nome,vida,forca,nivel,velocidade){
    this.nome = nome

    this.#vida = this.#validarValor(vida, 0, 250);
    this.#forca = this.#validarValor(forca, 5, 150);
    this.#nivel = this.#validarValor(nivel, 1, 100);
    this.#velocidade = this.#validarValor(velocidade, 1, 50);
    }
    #validarValor(valor, min, max) {
        if (valor < min || valor > max) {
            throw new Error(`Valor deve estar entre ${min} e ${max}`);
        }
        return valor;
    }

   getVida() {
        return this.#vida;
    }

    getForca() {
        return this.#forca;
    }

    getVelocidade() {
        return this.#velocidade;
    }

    getNivel() {
        return this.#nivel;
    }

    info(){
        return `${this.nome} Sua vida é de: ${this.#vida}, Sua força esta em: ${this.#forca} e Seu nivel é: ${this.#nivel}!`;
    }
    apresentar(){
        return `Òla ${this.nome} ...Seja muito Bem vindo a Legion Space`
    }
}

const guerreiro = new Caracter("Aragorn", 100, 85,1, 30);

console.log(guerreiro.apresentar());
console.log(guerreiro.info());
console.log("✅ Programa executado com sucesso!");