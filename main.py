from Postfix import *

#ingreso de la expresion
r =  input("\nIngrese una expresion a convertir: ")
print("\nRegex: ", r)

#infix a postfix
conversion = convertir(len(r))
conversion.RegexToPostfix(r)
postfix = conversion.res
print("\nPostfix: ", postfix)