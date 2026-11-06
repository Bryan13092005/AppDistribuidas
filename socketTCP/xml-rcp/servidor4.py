from xmlrpc.server import SimpleXMLRPCServer
#Fahrenheit a Kelvin es: K = (°F − 32) × 5/9 + 273.15.
#K = °C + 273.15
#°F = (°C × 1,8) + 32.
def celFar(celcius):
    far=(celcius*1.8)+32
    return (round(far,2))

def farCel(fahrenheit):
    cel=(fahrenheit-32)/(1.8)
    return (round(cel,2))

def celKel(celcius):
    return (round((celcius+273.15),2))

def kelCel(kelvin):
    return (round((kelvin-273.15),2))

def kelFar(kelvin):
    fahrenheit=((kelvin-273.15)*1.8)+32
    return round(fahrenheit,2)

def farKel(fahrenheit):
    kelvin=((fahrenheit-32)*(5/9))+273.15
    return round(kelvin,2)

servidor=SimpleXMLRPCServer(('0.0.0.0',8000))
servidor.register_function(celFar,'celFar')
servidor.register_function(farCel,'farCel')
servidor.register_function(celKel,'celKel')
servidor.register_function(kelCel,'kelCel')
servidor.register_function(kelFar,'kelFar')
servidor.register_function(farKel,'farKel')

servidor.serve_forever()