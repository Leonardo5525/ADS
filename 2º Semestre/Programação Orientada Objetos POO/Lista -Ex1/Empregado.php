<?php

class Empregado
{
    private $nome;
    private $sobrenome;
    private $setor;
    private $salarioMensal;

    // Usado quando se utiliza GET and SET quando se trata propriedade PRIVATE;


    // Método construtor
    public function __construct($valorNome, $valorSobrenome, $valorSetor, $valorSalarioMensal) {
        $this->setNome($valorNome);
        $this->setSobrenome($valorSobrenome);
        $this->setSetor($valorSetor);
        $this->setSalarioMensal($valorSalarioMensal);
    }

    public function setNome($valorNome)
    {
        $this->nome = $valorNome;
    }

    public function getNome()
    {
        return $this-> nome;
    }

    public function setSobrenome($valorSobrenome)
    {
        $this->sobrenome = $valorSobrenome;
    }
    

    public function getSobrenome()
    {
        return $this-> sobrenome;
    }

    public function setSetor($valorSetor)
    {
        return $this-> setor = $valorSetor;
    }

    public function getSetor()
    {
        return $this->setor;
    }

    public function setSalarioMensal($valorSalarioMensal)
    {
        if ($valorSalarioMensal < 0) {
            $this->salarioMensal = 0;
        } else {
            $this->salarioMensal = $valorSalarioMensal;
        }
    }

    public function getSalarioMensal()
    {
        return $this->salarioMensal;
    }

    public function salarioAnual(){
        return $this -> salarioMensal * 12;
    }

}

$newEmpregado1 = new Empregado('Leo', 'Nakamura', 'TI', 1000);
$newEmpregado2 = new Empregado('Vi', 'Fonseca', 'Médica', 20000);

echo "Nome: {$newEmpregado1 -> getNome()} <br>";
echo "Nome: {$newEmpregado1 -> getSobrenome()} <br>";
echo "Nome: {$newEmpregado1 -> getSetor()} <br>";
echo "Nome: {$newEmpregado1 -> salarioAnual()} <br>";

echo "Nome: {$newEmpregado2 -> getNome()} <br>";
echo "Nome: {$newEmpregado2 -> getSobrenome()} <br>";
echo "Nome: {$newEmpregado2 -> getSetor()} <br>";
echo "Nome: {$newEmpregado2 -> salarioAnual()} <br>";
