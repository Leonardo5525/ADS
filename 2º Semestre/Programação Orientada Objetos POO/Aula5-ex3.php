<?php

class Carro
{
    private $marca;
    private $modelo;
    private $capacidadeTanque;
    private $kmL;

    // Usado quando se utiliza GET and SET quando se trata propriedade PRIVATE;


    // Método construtor
    public function __construct($valorMarca, $valorModelo, $valorCapacidadeTanque, $valorKmL) {
        $this->setMarca($valorMarca);
        $this->setModelo($valorModelo);
        $this->setCapacidadeTanque($valorCapacidadeTanque);
        $this->setValorKmL($valorKmL);
    }

    public function setMarca($valorMarca)
    {
        if (empty($valorMarca)) {
            $this-> marca = 'Marca';
        } else {
            $this-> marca = $valorMarca;
        }
    }


    public function getMarca()
    {
        return $this-> marca;
    }

    public function setModelo($valorModelo)
    {
        if (empty($valorModelo)) {
            $this-> modelo = 'Modelo';
        } else {
            $this-> modelo = $valorModelo;
        }
    }


    public function getModelo()
    {
        return $this-> modelo;
    }


    public function setCapacidadeTanque($valorCapacidadeTanque)
    {
        if ($valorCapacidadeTanque < 0) {
            $this-> capacidadeTanque = 0;
        } else {
            $this-> capacidadeTanque = $valorCapacidadeTanque;
        }
    }

    public function getCapacidadeTanque()
    {
        return $this-> capacidadeTanque;
    }

    public function setValorKmL($valorKmL)
    {
        if ($valorKmL < 0) {
            $this-> kmL = 0;
        } else {
            $this-> kmL = $valorKmL;
        }
    }

    public function getKmL()
    {
        return $this-> kmL;
    }

    public function abastecer($valorCombustivel){
        return $this -> capacidadeTanque * $valorCombustivel;
    }

    public function autonomia(){
        return $this -> capacidadeTanque / $this -> kmL;
    }
}

$newCar1 = new Carro('Honda', 'Fit', 60, 11);

echo "Nome do comprador: {$comprador1->getNomeProduto()} <br>";
echo "Valor a pagar: {$comprador1->totalCompra()} <br>";