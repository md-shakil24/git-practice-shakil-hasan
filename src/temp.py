class Tempconvert:

    def menu(self):
        select_method=input("""Please select your convert path

1. Press c for Celcius
2. Press f for Farenhit
3. Press k for Kelvin
4. Press anything for exit
    Please Press :  """)
        
        if select_method=="c":
            #call temp_Celcius
            self.temp_Celcius()
        
        
        
        elif select_method=="f":
            #call temp_farenheit
            self.temp_Farenheit()
        
        
        elif select_method=="k":
            #call temp_kelvin
            self.temp_Kelvin()
        
        
        else:
            print ("thank you")

    def temp_Celcius(self):
        select=input("Press f for farenheit or k for kelvin  : ")
        C=int(input(" Input Celcius Tempareture : "))
        
        
        if select=="f":
            temp_farenheitc=9*C/5+32
            print(f" Your celcius tempareture is {C} and The farenheit tempareture is {temp_farenheitc}")
        
        
        elif select=="k":
            temp_kelvinc=C+273
            print(f"Your celcius tempareture is {C} and The kelvin tempareture is {temp_kelvinc}")
          

    def temp_Farenheit(self):
        select=input("Press c for celcius or k for kelvin  : ")
        f=int(input(" Input farenheit Tempareture : "))
        
        
        if select=="c":
            temp_celciusf=5/9*(f-32)
            print(f" Your farenheit tempareture is {f} and The celcius tempareture is {temp_celciusf}")
        
        
        elif select=="k":
            temp_kelvinf=5/9*(f-32)+273
            print(f"Your farenheit tempareture is {f} and The kelvin tempareture is {temp_kelvinf}")


    def temp_Kelvin(self):
        select=input("Press c for celcius or f for Farenheit  : ")
        k=int(input(" Input Kelvin Tempareture : "))
        
        
        if select=="c":
            temp_celciusk=k-273
            print(f" Your Kelvin tempareture is {k} and The celcius tempareture is {temp_celciusk}")
        
        
        elif select=="f":
            temp_farenheitk=9/5*(k-273)+32
            print(f"Your Kelvin tempareture is {k} and The farenheit tempareture is {temp_farenheitk}")


convert= Tempconvert()
convert.menu()