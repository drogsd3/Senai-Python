from math import pi
def AreaTriangulo(base,altura):
    area = base * altura /2
    return area

def AreaRetangulo(lado, altura):
    area = lado * altura
    return area

def AreaTrapezio(baseMaior,baseMenor, altura):
    area = ((baseMaior+baseMenor)*altura)/2
    return area

def AreaCirculo(raio):
    area = pi * raio**2
    return area 
