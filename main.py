from Postfix import *
from AFN import * 
from AFNtoAFD import AFNtoAFD
from PostifixToAFN import *
#ingreso de la expresion
r =  input("\nIngrese una expresion a convertir: ")
print("\nRegex: ", r)

#ε

#infix a postfix
conversion = convertExpression(len(r))
conversion.RegexToPostfix(r)
if conversion.verificar == True:
    
    # ///////////////////////   AFN ////////////////////////////////
    postfix = conversion.res
    print("\nPostfix: ", postfix)

    #Postfix a AFN
    # resultado=AFN(postfix)
    # resultado.conversion()
    #0?(1?)?0*
    afn = AFN(postfix)
    afn.conversion()
    afn.graph_afn()
    
    # //////////////////////// AFN a AFD /////////////////////////////////////
     # instancia de clase para convertir a AFN
    conversionAFN = PostifixToAFN(postfix)
    
    # llamada a metodo para convertir afn
    conversionAFN.conversion()
    
     # listas de estados, simbolos, estado inicial, estado final y transiciones del AFN
    estados = conversionAFN.estados
    transiciones = conversionAFN.transiciones_splited
    estado_inicial = conversionAFN.e0
    estado_final = conversionAFN.ef
    simbolos = conversionAFN.simbolos
    afn = conversionAFN.afn_final

    # instacia de clase para convertir AFN a AFD
    conversionAFD = AFNtoAFD(estados, transiciones,
                             estado_inicial, estado_final, simbolos, afn)
    
else:
    pass
