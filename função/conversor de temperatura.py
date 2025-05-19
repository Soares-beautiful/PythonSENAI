#conversos de temperatura

temperatura = float(input("digite sua temperatura"))

def calcular_fairi():
    return temperatura * 1.8 + 32

def calcular_kelvin():
    return  temperatura + 273
print("a conversão de fairi é", calcular_fairi())
print("a conversão do kelvin é", calcular_kelvin())