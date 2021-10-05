

class Calculator(object): #hesap makinesi objemi oluşturdum
    def __init__(self,a,b): #dışarıdan 2 parametre alcam bu parametreler benim attributelarım
        self.a = a
        self.b = b
    
    def addition(self): #toplama behaviorım, classın kendi içindeki parametreleri kullanarak çalışan bir method
        return self.a + self.b
    
    def multiplication(self): #çarpma behaviorım, classın kendi içindeki parametreleri kullanrak çalışan bir method
        return self.a * self.b
    
    def division(self): #bölme behaviorım, classın kendi içindeki parametreleri kullanrak çalışan bir method
        return self.a / self.b
    
    
#bilgilendirme ekranı
print("""Welcome to calculator!
      [1] Addition
      [2] Multiplication
      [3] Division
      [Q] Quit
      
      """) 
    
    
selection = input("Make a selection: ") #bilgilendirme ekranı sonrası seçim alma


if selection == "1": #toplama işlemi seçimi koşulu
    a = int(input("Please type value 1: ")) #değer1 alımı
    b = int(input("Please type value 2: ")) #değer2 alımı
    calculator1 = Calculator(a,b) #calculator1 isminde bir hes. mak. oluşturmak istediğim için classıma eşitledim
    print("Result:",calculator1.addition()) #class için methodum sonucu return ediyordu doğrudan ekrana bastırdım
  
elif selection == "2":
    a = int(input("Please type value 1: "))
    b = int(input("Please type value 2: "))
    calculator1 = Calculator(a,b) 
    print("Result:",calculator1.multiplication())
    
elif selection == "3":
    a = int(input("Please type value 1: "))
    b = int(input("Please type value 2: "))
    calculator1 = Calculator(a,b) 
    print("Result:",int(calculator1.division()))
    
elif selection == "q" or selection == "Q":
    print("Quitted.")
    quit()
    
else:
    print("Wrong selection!")
    
    