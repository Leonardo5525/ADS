<?php

class Terreno
{
    private $frente;
    private $lateral;
    private $precoMetro;

    // Usado quando se utiliza GET and SET quando se trata propriedade PRIVATE;


    // Método construtor
    public function __construct($valorFrente, $valorLateral, $valorPrecoMetro) {
        $this->setFrente($valorFrente);
        $this->setLateral($valorLateral);
        $this->setPrecoMetro($valorPrecoMetro);
    }

    // Altera o valor do metro quadrado
    public function setPrecoMetro($valorPrecoMetro)
    {
        if ($valorPrecoMetro < 0) {
            $this->precoMetro = 0;
        } else {
            $this->precoMetro = $valorPrecoMetro;
        }
    }

    // Retorna o valor da propriedade
    public function getPrecoMetroFrente()
    {
        return $this->precoMetro;
    }


    public function area()
    {
        return $this->frente * $this->lateral;
    }
    
    // Altera o valor da propriedade
    public function setFrente($valorFrente)
    {
        if ($valorFrente < 0) {
            $this->frente = 0;
        } else {
            $this->frente = $valorFrente;
        }
    }

    // Retorna o valor da propriedade
    public function getFrente()
    {
        return $this->frente;
    }

    // Altera o valor da propriedade
    public function setLateral($valorLateral)
    {
        if ($valorLateral < 0) {
            $this->lateral = 0;
        } else {
            $this->lateral = $valorLateral;
        }
    }

    // Retorna o valor da propriedade
    public function getLateral()
    {
        return $this->lateral;
    }

    // Calcular o perimetro
    public function perimetro(){
        return $this -> lateral*2 + $this -> frente*2;
    }

    public function precoVenda(){
        return $this -> area() * $this -> precoMetro;
    }
}

$terreno1 = new Terreno(5, 30, 10);

echo "Área do terreno: {$terreno1->area()} <br>";
echo "Frente do terreno {$terreno1->getFrente()} <br>";
echo "Perimetro {$terreno1->perimetro()} <br>";
echo "Valor do Metro quadrado {$terreno1->precoVenda()}";
