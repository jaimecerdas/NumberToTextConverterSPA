# Convertidor

cedula = "3-101-339245"
index = 0
new = ""

while index < len(cedula):
    if cedula[index] == "-":
        new = new + ("- ")
    elif cedula[index] == "1":
        new = new + ("uno ")
    elif cedula[index] == "2":
        new = new + ("dos ")
    elif cedula[index] == "3":
        new = new + ("tres ")
    elif cedula[index] == "4":
        new = new + ("cuatro ")
    elif cedula[index] == "5":
        new = new + ("cinco ")
    elif cedula[index] == "6":
        new = new + ("seis ")
    elif cedula[index] == "7":
        new = new + ("siete ")
    elif cedula[index] == "8":
        new = new + ("ocho ")
    elif cedula[index] == "9":
        new = new + ("nueve ")
    elif cedula[index] == "0":
        new = new + ("cero ")
    index += 1
print(new)

