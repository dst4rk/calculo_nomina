import time
import contextlib

def cnom():
    #Declaracion de las variables
    su_name = input("Digite Su Nombre: ")
    su_cargo = input("Digite Su Cargo: ")
    sueldo_bruto = int(input("Digite Su Sueldo Bruto: "))
    time.sleep(1)
    print("\n")

    #Identifiacion del cargo
    if su_cargo == 'Gerente' or su_cargo == 'gerente':
        gasto_pres =  5000
    elif su_cargo == 'Secretaria' or su_cargo == 'secretaria' or su_cargo == 'Secretario' or su_cargo == 'secretario':
        gasto_pres =  2000
    else:
        gasto_pres = 0

    #Calculo del ISR
    if sueldo_bruto > 37000:
        excedente = sueldo_bruto - 37000 
    else:
        excedente = 0
    isr = int (excedente * 0.10)    
    #Calculo del SS
    ss = int (sueldo_bruto * 0.15)
    #Calcuo AFP
    afp =  int (sueldo_bruto * 0.4)
    #Total de Descuento
    total_descuento = isr + ss + afp
    #Sueldo Neto
    sueldo_neto = sueldo_bruto + gasto_pres - total_descuento

    #Salida de Valores
    print ("[~] Realizando los calculos.......")
    print ("[~] Imprimiendo los resultados.......")
    print("\n")
    time.sleep(1)
    print  ("[+] Su Sueldo Bruto es: " + str(sueldo_bruto))
    print  ("[+] Gasto de Presentacion: " + str(gasto_pres))
    print  ("[+] Sueldo mas gasto de presentacion: " + str (sueldo_bruto + gasto_pres))
    print  ("[+] Impuesto sobre la Renta: " + str(isr))
    print  ("[+] Seguro Social: " + str(ss))
    print  ("[+] AFP: " + str(afp))
    print  ("[+] Total de retenciones: " + str(total_descuento))
    print  ("[+] Sueldo Neto: " + str(sueldo_neto))
    
    #Guardar en un Archivo la Salida de Valores
    file_path = su_name + '.txt'
    with open(file_path, "w") as o:
        with contextlib.redirect_stdout(o):
            print ("Calculo de Nomina para el Empleado: " + su_name)
            print ("\n")
            print ("[+] Su Sueldo Bruto es: " + str(sueldo_bruto))
            print ("[+] Gasto de Presentacion: " + str(gasto_pres))
            print ("[+] Sueldo mas gasto de presentacion: " + str (sueldo_bruto + gasto_pres))
            print ("[+] Impuesto sobre la Renta: " + str(isr))
            print ("[+] Seguro Social: " + str(ss))
            print ("[+] AFP: " + str(afp))
            print ("[+] Total de retenciones: " + str(total_descuento))
            print ("[+] Sueldo Neto: " + str(sueldo_neto))


if __name__ ==  '__main__':
    cnom()

time.sleep(10)


#By Maicker Miguel Ravelo Flores (dstark)