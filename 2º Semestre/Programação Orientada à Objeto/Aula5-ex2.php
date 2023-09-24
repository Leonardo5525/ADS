<?php

class Comprador
{
    private $nomeProduto;
    private $preco;
    private $quantidade;

    // Usado quando se utiliza GET and SET quando se trata propriedade PRIVATE;


    // Método construtor
    public function __construct($valorNomeProduto, $valorPreco, $valorQuantidade) {
        $this->setNomeProduto($valorNomeProduto);
        $this->setPreco($valorPreco);
        $this->setQuantidade($valorQuantidade);
    }

    public function setPreco($valorPreco)
    {
        if ($valorPreco < 0) {
            $this-> preco = 0;
        } else {
            $this-> preco = $valorPreco;
        }
    }


    public function getPreco()
    {
        return $this-> preco;
    }


    public function setQuantidade($valorQuantidade)
    {
        if ($valorQuantidade < 0) {
            $this->quantidade = 0;
        } else {
            $this->quantidade = $valorQuantidade;
        }
    }

    public function getQuantidade()
    {
        return $this->quantidade;
    }

    public function setNomeProduto($valorNomeProduto){
        if (empty($valorNomeProduto)){
            $this -> nomeProduto = 'Nome do Produto';
        }   else{
            $this -> nomeProduto = $valorNomeProduto;
        }
    }

    public function getNomeProduto()
    {
        return $this->nomeProduto;
    }

    public function totalCompra(){
        return $this -> quantidade * $this -> preco;
    }
}

$comprador1 = new Comprador('', 5.10, 5);

echo "Nome do comprador: {$comprador1->getNomeProduto()} <br>";
echo "Valor a pagar: {$comprador1->totalCompra()} <br>";