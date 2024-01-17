# calculate_imc.py

def calculate_imc(weight, height):
    height_meters = height / 100.0
    imc = weight / (height_meters * height_meters)
    return imc
