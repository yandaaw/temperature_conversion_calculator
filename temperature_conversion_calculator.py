# 1. Coba buat function untuk merubah suhu dari Celcius ke Reamur atau sebaliknya

# Input: 1 string
# Output: 1 string

# Contoh
# Input: '35C'
# Output: '..R'

# Input: '32R'
# Output: '..C'

def mainMenu():
    print("==========================================")
    print("     Temperature Conversion Calculator    ")
    print("==========================================")
    print("1. Convert temperature from Reamur: ")
    print("2. Convert temperature from Kelvin: ")
    print("3. Convert temperature from Celcius: ")
    print("4. Convert temperature from Farenheit: ")
    print("5. Quit")
    print("==========================================")
    
    selection=int(input("Enter choice: "))
    if selection==1:
        reamur()
        
    elif selection==2:
        kelvin()

    elif selection==3:
        celcius()

    elif selection==4:
        farenheit()

    elif selection==5:
        exit
        
    else:
        print("")
        print("<<<<< invalid choice. Enter 1-5 >>>>>")
        print("")
        
        mainMenu()
            
# konversi suhu dari reamur
def reamur():
    reamur = float(input("Masukan Suhu (°R): "))
    celcius_a = 5/4*reamur
    farenheit_a = (9/4*reamur)+32
    kelvin_a = 273+(5/4*reamur)
    
    print("")
    print("Hasil konversi: ")
    print("Celcius= ", celcius_a, "°C")
    print("Reamur= ", reamur, "°R")
    print("Farenheit= ", farenheit_a, "°F")
    print("Kelvin= ", kelvin_a, "°K")
    print("")
    
    mainMenu()
    
    return reamur


# konversi suhu dari kelvin
def kelvin():
    kelvin = float(input("Masukan Suhu (°K): "))
    celcius_b = kelvin-273
    farenheit_b = 9/5*(kelvin-273)+32
    reamur_b = (kelvin-273)*4/5
    
    print("")
    print("Hasil konversi: ")
    print("Celcius= ", celcius_b, "°C")
    print("Reamur= ", reamur_b, "°R")
    print("Farenheit= ", farenheit_b, "°F")
    print("Kelvin= ", kelvin, "°K")
    print("")
    
    mainMenu()
    
    return kelvin


# konversi suhu dari celcius
def celcius():
    celcius = float(input("Masukan Suhu (°C): "))
    reamur_c = 4/5*celcius
    farenheit_c = (9/5*celcius)+32
    kelvin_c = 273+celcius
    
    print("")
    print("Hasil konversi: ")
    print("Celcius= ", celcius, "°C")
    print("Reamur= ", reamur_c, "°R")
    print("Farenheit= ", farenheit_c, "°F")
    print("Kelvin= ", kelvin_c, "°K")
    print("")
    
    mainMenu()
    
    return celcius 


# konversi suhu dari farenheit
def farenheit():
    farenheit = float(input("Masukan Suhu (°F): "))
    reamur_d = 4/9*(farenheit-32)
    celcius_d = 5/9*(farenheit-32)
    kelvin_d = 5/9*(farenheit-32)+273
    
    print("")
    print("Hasil konversi: ")
    print("Celcius= ", celcius_d, "°C")
    print("Reamur= ", reamur_d, "°R")
    print("Farenheit= ", farenheit, "°F")
    print("Kelvin= ", kelvin_d, "°K")
    print("")
    
    mainMenu() 
    
    return farenheit
    
# menjalankan Temperature Conversion Calculator
mainMenu()