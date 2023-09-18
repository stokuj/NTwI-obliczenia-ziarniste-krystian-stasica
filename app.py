import sys
import numpy as np
import matplotlib.pyplot as plt
from RozmytyZbior import RozmytyZbior

### Przypadek wyświetlania liczby
if len(sys.argv) == 4:
    try:
        lp = float(sys.argv[1])
        śr = float(sys.argv[2])
        pp = float(sys.argv[3])
        
        ###   Sprawdzenie czy mamy poprawny trójkąt
        ###
        if not (lp<=śr<=pp):
            raise ValueError
        if lp==śr:
            lp=lp-0.01
        if pp==śr:
            pp=pp+0.01
        
        A = RozmytyZbior(lp,śr,pp,np.arange(lp-0.2, pp+0.2, 0.01))
        
        ### Wyświetlanie liczb 
        ###
        plt.figure(figsize=(12, 4))
        A.wyswietl(111)
        print("A:{:<7} {:<7} {:<7}".format(round(A.x1, 2), round(A.m, 2), round(A.x2, 2)))
        plt.title('A')
        plt.xlabel('Wartość')
        plt.ylabel('Stopień przynależności')
        plt.tight_layout()
        plt.show()
        
    except ValueError:
        print("Niepoprawne argumenty. ")
 
### Przypadek mnożenia lub potęgowania        
elif len(sys.argv) == 6:
    operator = sys.argv[4]
    if operator in ("*", "^"):
        try:
            lp = float(sys.argv[1])
            śr = float(sys.argv[2])
            pp = float(sys.argv[3])
            liczba = float(sys.argv[5])
            
            ###   Sprawdzenie czy mamy poprawny trójkąt
            ###
            if not (lp<=śr<=pp):
                raise ValueError
            if lp==śr:
                lp=lp-0.01
            if pp==śr:
                pp=pp+0.01
                
                
            A = RozmytyZbior(lp,śr,pp,np.arange(lp-0.2, pp+0.2, 0.01))
            
            ###  Mnożeymy czy potęgujemy
            ###
            if operator == "*":
                B = A.pomnóż(liczba)
            else:
                B = A.potęgowanie(liczba)
                
            ### Wyświetlanie liczb 
            ###
            plt.figure(figsize=(12, 4))
            A.wyswietl(311)
            plt.title('A')
            B.wyswietl(312)
            plt.title('A*{}'.format(liczba))
            A.wyswietl(313)
            B.wyswietl(313)
            # plt.title('A and A*{}'.format(d))
            
            print("A:{:<7} {:<7} {:<7} B:{:<7} {:<7} {:<7}".format(A.x1, A.m, A.x2, round(B.x1, 2), round(B.m, 2), round(B.x2, 2)))
            plt.xlabel('Wartość')
            plt.ylabel('Stopień przynależności')
            plt.tight_layout()
            plt.show()
        except ValueError:
            print("Niepoprawne argumenty. ")
    else:
        print("Niepoprawne użycie. Użyj: python main.py 2 3 4 * 2 lub 2 3 4 ^ 2")    

### Przypadek dodawania lub odejnowania       
elif len(sys.argv) >= 8 and (len(sys.argv) - 8) % 4 == 0:#len(sys.argv) == 8:
    C = None
    
    # Gdy dodajemy więcej niż 2 liczby, wynik z poprzedniego działania jest przekazywany jako A,
    # Po czym program wykonuje w pętli A + B = C, A = C
    for i in range(0, len(sys.argv)-4, 4):
        operator = sys.argv[i+4]
        if operator in ("+", "-","*"):
            try:
                lp = float(sys.argv[1])
                śr = float(sys.argv[2])
                pp = float(sys.argv[3])
                lp2 = float(sys.argv[i+5])
                śr2 = float(sys.argv[i+6])
                pp2 = float(sys.argv[i+7])
                
                ###   Sprawdzenie czy mamy poprawny trójkąt
                ###
                if not ((lp<=śr<=pp) and (lp2<=śr2<=pp2)):
                    raise ValueError
                if lp==śr:
                    lp=lp-0.01
                if pp==śr:
                    pp=pp+0.01
                if lp2==śr2:
                    lp2=lp2-0.01
                if pp2==śr2:
                    pp2=pp2+0.01
                
                ### Sprawdzenie która iteracja
                ###   
                if(i>=4):   #   dla 8 lub więcej argumentów 
                    A = C   #   wynik ostatniego działania jest przekazywany jako pierwsza liczba
                else:       #   pierwsza iteracja
                    A = RozmytyZbior(lp,śr,pp,np.arange(lp-0.2, pp+0.2, 0.01))
                B = RozmytyZbior(lp2,śr2,pp2,np.arange(lp2-0.2, pp2+0.2, 0.01))
                
                ### Dodajemy czy odejmujemy
                ###
                if operator == "+":
                    C = A.dodaj(B)
                elif operator == "*":
                    C = A.pomnoz_przez_zbior(B)
                else:
                    C = A.odejmij(B)
                    
                    
                ### Wyświetlanie liczb 
                ###
                plt.figure(figsize=(12, 4))
                A.wyswietl(311)
                B.wyswietl(311)
                plt.title('A i B')
                C.wyswietl(312)
                plt.title('A {} B'.format(operator))
                A.wyswietl(313)
                B.wyswietl(313)
                C.wyswietl(313)
                plt.title('A,B i A {} B'.format(operator))
                
                print("A:{:<7} {:<7} {:<7} B:{:<7} {:<7} {:<7} C:{:<7} {:<7} {:<7}".format(A.x1, A.m, A.x2, B.x1, B.m, B.x2, round(C.x1, 2), round(C.m, 2), round(C.x2, 2)))
                plt.xlabel('Wartość')
                plt.ylabel('Stopień przynależności')
                plt.tight_layout()
                plt.show()

            
            except ValueError:
                print("Niepoprawne argumenty. ")
        else:
            print("Niepoprawne użycie. Użyj: python main.py 2 3 4 + 5 6 7 lub 2 3 4 - 5 6 7")

else:
    print('Niepoprawne użycie. Zła liczba argumentów. Przykłady użycia:\n'+
          'python main.py 2 3 4\n'+
          'python main.py 2 3 4 * 2\n'+
          'python main.py 2 3 4 + 5 6 7\n')