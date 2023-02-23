from Postfix import *
from AFN import * 

#ingreso de la expresion
r =  input("\nIngrese una expresion a convertir: ")
print("\nRegex: ", r)

#ε

#infix a postfix
conversion = convertExpression(len(r))
conversion.RegexToPostfix(r)
if conversion.verificar == True:
    
    postfix = conversion.res
    print("\nPostfix: ", postfix)

    #Postfix a AFN
    # resultado=AFN(postfix)
    # resultado.conversion()

    afn = AFN(postfix)
    afn.conversion()
    afn.graph_afn()
else:
    pass
