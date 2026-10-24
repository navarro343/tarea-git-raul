#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el
#vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
#ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
#base y comisiones.
sueldo = float(input("Dime cual es el sueldo: "))
ventas = float(input("Cuantas ventas realizo: "))

print(f'La comision seria {(10*sueldo)/100} su ganancia en el mes es de {sueldo +((10*sueldo/100)*ventas)}')