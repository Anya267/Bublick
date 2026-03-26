while True :
    a = input ("Enter combination of 8 bits(1 or 0)")
    if len(a) == 8 and a.count("0") + a.count("1") == 8:
        if a.count("1") %2 == 0:
            print("parity bit = 0")
        else :
            print("parity bit = 1")
    else :
        print("Error,plise enter combination of 8 bits 1 or 0")
    if len(a)==0 :
        break

