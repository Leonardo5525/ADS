
from bottle import route, run, template
from ex.metro import calculo
from ex.salario import calculos
from ex.fh import calc
from ex.imc import imc
from ex.pescador import exer
from ex.inss import final
from ex.unimar import acabou

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/ex1/<m:float>')
def ex1_route(m):
    cm = calculo(m)
    cm = f'{cm:.2f}'
    return template('<h1>{{r}}cm</h1>',r=cm)

@route('/ex2/<m:float>/<n:float>')
def ex2_route(m,n):
    salario = calculos(m,n)
    salario = f'{salario:.2f}'
    return template('<h1>{{r}}R$</h1>',r=salario)

@route('/ex3/<m:float>')
def ex3_route(m):
    c = calc(m)
    c = f'{c:.1f}'
    return template('<h1>{{r}}Cº</h1>',r=c)

@route('/ex4/<h:float>/<w:float>')
def ex4_route(h,w):
    ideal = imc(w,h)
    ideal = f'{ideal:.2f}'
    return template('<h1>{{r}}imc</h1>',r=ideal)

@route('/ex5/<m:float>')
def ex5_route(m):
    kilo = exer(m)
    kilo = f'{kilo:.2f}'
    return template('<h1>{{r}}Kg</h1>',r=kilo)

@route('/ex6/<x:float>/<y:float>')
def ex6_route(x,y):
    ins = final (x,y)
    return template('<h1>{{!r}}</h1>',r=ins)

@route('/ex7/<a:float>/<l:float>')
def ex7_route(a,l):
    call = acabou (a,l)
    call = f'{call:.2f}'
    return template('<h1>{{r}} R$</h1>',r=call)

run(host='localhost', port=8081, reloader=True)