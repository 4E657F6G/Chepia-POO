def hallarPalabraMayor(lista: list):
    palabra = ""
    msg = " "
    tot = len(lista)
    try:
        for y in lista:
            if y.isdigit():
                tot = tot - 1
        if tot == 0:       
            return msg
        else: 
            for x in lista:
                if len(x) == len(palabra):
                    if x.islower() == True:
                        palabra = x
                    else:
                        palabra = palabra
                    return msg            
                elif len(x) > len(palabra):
                    palabra = x
        return palabra
    except Exception:
        return msg    
        

lista = ["cafeteleria", "hola", "asdasdasdfasdfasdfasdfasdfawefqwex"]
print(hallarPalabraMayor(lista))

def hallarPares(lista2: list):
    contador = 0
    try:
        for z in lista2:
            if z % 2 == 0:
                contador = contador + 1
        return contador        
    except Exception:
        return 0

lista2 = [2,2,3,4,5,6,7,8,8,9]
print(hallarPares(lista2))    

def generarArmonicos(n: int):
    armonico = "1"
    try:
        if n <= 0:
            raise ValueError("ValueError: Sólo se permiten números mayores o iguales a 1.")
        elif n == 1:
            return armonico
        else: 
            i = 1
            while i<=n:
                armonico = armonico + " + 1/" + str(i) 
                i = i + 1
            return armonico        
    except Exception as e:
        return e
    
n = 30
print(generarArmonicos(n))

def obtenerEdad(cedula: str):
    try:       
        spl = cedula.split("-")
        if len(spl) == 3:  
            año = int(spl[1])
            edad = 2018 - año
            return edad
        else:
            raise TypeError
    except Exception as e:
        return e

cedula = "0501-1996-08438"
print(obtenerEdad(cedula))

def obtenerDigitoMasSignificativo(n: int):
    try:
        m = list(str(n))
        return m[0]
    except Exception as e:
        return e    

n = 1232452342323562456345634562345234523452345
print(obtenerDigitoMasSignificativo(n))

def conteoPalabras(cadena: str):
    try:
        cad2 = cadena.split(" ")
        resp = ""
        for x in cad2:
            resp = resp + x + " = " + str(cad2.count(x)) + ", "
            if cad2.count(x) > 1:
                i = 1
                while i < cad2.count(x):
                    cad2.remove(x)
                    i = i + 1
        return resp
    except Exception as e:
        return e


cadena = "hola hace que hace hace"
print(conteoPalabras(cadena))












'''
def modificarTupla(t: tuple, indice: int, valor: object):
    list(t)

t = ('my', 'name', 'is', 'mr', 'tuple')
indice = 3
valor =
'''