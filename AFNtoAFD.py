'''
CLASE DEDICADA A LA CONVERSION DE UN AFN A UN AFD
'''
import pandas as pd
import os.path
import time

class AFNtoAFD():
    def __init__(self, estados_afn, transiciones_afn, estado_inicial_afn, estado_final_afn, simbolos_afn, afn):
        # variables necesarias para poder pasar de un afn a un afd
        self.estados_afn = estados_afn
        self.transiciones_afn = transiciones_afn
        self.estado_inicial_afn = estado_inicial_afn
        self.estado_final_afn = estado_final_afn
        self.simbolos_afn = simbolos_afn
        self.afn = afn

        self.estados_afd = []
        self.estados_iniciales_afd = []
        self.estados_finales_afd = []
        self.afd = []

    def e_closure_past(self, estado, list_estados):
        list_estados.append(estado)
        for i in range(len(self.transiciones_afn)):
            if self.transiciones_afn[i][0] == estado and self.transiciones_afn[i][1] == "ε" and self.transiciones_afn[i][2] not in list_estados:
                list_estados = self.e_closure(self.transiciones_afn[i][2], list_estados)           
        return list_estados

    def e_closure(self, estados):
        stack = []
        res = []

        for estado in estados:
            if estado not in stack:
                stack.append(estado)
                res.append(estado)
        
        while len(stack) > 0:
            state = stack.pop()
            for i in self.transiciones_afn:
                if i[0] == state and i[1] == 'ε':
                    if i[2] not in res:
                        res.append(i[2])
                        stack.append(i[2])
        return res

    def move(self, estado, symbol):
        for i in range(len(self.transiciones_afn)):
            if self.transiciones_afn[i][0] == estado and self.transiciones_afn[i][1] == symbol:
                return self.transiciones_afn[i][2]

        return None


    def conversion(self):
        print("\nConvirtiendo de AFN a AFD...")
        t0 = time.perf_counter()
        #afn = self.afn
        numero_estados = len(self.estados_afn)
        numero_transiciones = len(self.transiciones_afn)

        #se asignan valores de nuevo al afn
        afn = {}                                 
        for estado in range(numero_estados):  
            afn[estado] = {} 
            reaching_state = []
            for j in range(len(self.simbolos_afn)):
                path = self.simbolos_afn[j]
                for j in range(numero_transiciones):               
                    reaching_state = [x[2] for x in self.transiciones_afn if x[0] == estado and x[1] == path]                 
                    afn[estado][path] = reaching_state   

        #print(self.transiciones_afn)
        afn_table = pd.DataFrame(afn)
        #print(afn_table.transpose())
        #print(afn_table)

        estado_inicial = self.estado_inicial_afn



        dfa_states = []

        dfa_states.append([estado_inicial])

        res_final = []

        res_final.append([estado_inicial])

        final_feliz = []

        while len(dfa_states) > 0:
        
            temp = dfa_states.pop()
            for symbol in self.simbolos_afn:
                letras = []
                temp_eclosure = []
                if temp == estado_inicial:
                    temp_eclosure = self.e_closure([temp])
                else:
                    temp_eclosure = self.e_closure(temp)

                for transicion in self.transiciones_afn:
                    for estado in temp_eclosure:
                        if transicion[0] == estado and transicion[1] == symbol:
                            if transicion[2] not in letras:
                                temp_eclosure.append(transicion[2])

                letras = self.e_closure(temp_eclosure)

                if len(letras) > 0:
                    if letras not in dfa_states and letras not in res_final:
                        dfa_states.append(letras)
                        res_final.append(letras)
                   
                    final_feliz.append(("Q"+str(res_final.index(temp)+1), symbol, "Q"+str(res_final.index(letras)+1)))

        


        tablita_feliz =  pd.DataFrame(final_feliz)

        estados_afd = []
        estados_finales = []
        estados_iniciales = []
        
        for i in res_final:
            estados_afd.append("Q"+str(res_final.index(i)+1))
            if self.estado_final_afn in i:
                estados_finales.append("Q"+str(res_final.index(i)+1))
        
        estados_iniciales.append("Q"+str(res_final.index([self.estado_inicial_afn])+1))     

        #print(tablita_feliz)    

        string_afd = tablita_feliz.to_string()  

        self.afd = final_feliz   

        self.estados_afd = estados_afd
        self.estados_iniciales_afd = estados_iniciales
        self.estados_finales_afd = estados_finales

        t1 = time.perf_counter()

        nombre_archivo = input('\nIngrese el nombre del archivo para guardar el AFD convertido del AFN -> ')

        nombre_archivo = nombre_archivo + '.txt'

        if os.path.exists(nombre_archivo):
            print("\nArchivo AFD existente")

        else:
            with open(nombre_archivo, 'a', encoding="utf-8") as f:
                f.write("AFD a partir de un AFN -->")
                f.write("\n")
                f.write("Símbolos: "+', '.join(self.simbolos_afn))
                f.write("\n")
                f.write("Estados:  " + str(estados_afd))
                f.write("\n")
                f.write("Estado inicial: " + str(estados_iniciales))
                f.write("\n")
                f.write("Estados de aceptación:" + str(estados_finales) )
                f.write("\n")
                f.write("Transiciones: " + str(final_feliz))

            print("\nArchivo de AFD escrito con éxito")

        print('\nEl tiempo para pasar de AFN a AFD es: ',t1-t0)