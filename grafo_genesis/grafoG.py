import time
from graphviz import Digraph

def crear_red_petri():
    """Crea la red de Petri con la estructura exacta requerida"""
    dot = Digraph()
    
    # Lugares principales
    lugares = ['Inicio', 'Filtrar', 'Letra', 'A', 'P', 'R', 'O', 'B', 'D', 'Fin', 'Error']
    for lugar in lugares:
        dot.node(lugar, shape='circle', width='0.7')
    
    # Transiciones
    transiciones = {
        'T_filtrar': 'Filtrar entrada',
        'T_es_numero': '¿Es número?',
        'T_es_letra': '¿Es letra válida?',
        'T_A': 'Aceptar A',
        'T_P': 'Aceptar P',
        'T_R': 'Aceptar R',
        'T_O': 'Aceptar O',
        'T_B': 'Aceptar B',
        'T_D': 'Aceptar D',
        'T_error': 'Rechazar',
        'T_fin': 'Finalizar'
    }
    
    for trans, label in transiciones.items():
        dot.node(trans, label=label, shape='rectangle', width='1.2', height='0.4')
    
    # Conexiones
    conexiones = [
        # Flujo principal
        ('Inicio', 'T_filtrar'),
        ('T_filtrar', 'Filtrar'),
        ('Filtrar', 'T_es_numero'),
        ('Filtrar', 'T_es_letra'),
        
        # Manejo de números
        ('T_es_numero', 'Error'),
        
        # Manejo de letras
        ('T_es_letra', 'Letra'),
        ('Letra', 'T_A'), ('Letra', 'T_P'), ('Letra', 'T_R'),
        ('Letra', 'T_O'), ('Letra', 'T_B'), ('Letra', 'T_D'),
        ('Letra', 'T_error'),
        
        # Letras válidas
        ('T_A', 'A'), ('T_P', 'P'), ('T_R', 'R'),
        ('T_O', 'O'), ('T_B', 'B'), ('T_D', 'D'),
        
        # Finalización
        ('A', 'T_fin'), ('P', 'T_fin'), ('R', 'T_fin'),
        ('O', 'T_fin'), ('B', 'T_fin'), ('D', 'T_fin'),
        ('T_fin', 'Fin'),
        
        # Manejo de errores
        ('T_error', 'Error')
    ]
    
    for origen, destino in conexiones:
        dot.edge(origen, destino)
    
    return dot

def simular_procesamiento(input_string):
    """Simula el procesamiento completo"""
    secuencia_esperada = ['a', 'p', 'r', 'o', 'b', 'a', 'd', 'o']
    estados = []
    estado_actual = {
        'Inicio': 1,
        'Filtrar': 0,
        'Letra': 0,
        'A': 0, 'P': 0, 'R': 0, 'O': 0, 'B': 0, 'D': 0,
        'Fin': 0,
        'Error': 0
    }
    estados.append(estado_actual.copy())
    
    idx_esperado = 0
    continuar_procesamiento = True
    
    for caracter in input_string.lower():
        if not continuar_procesamiento:
            break
            
        # Reiniciar lugares (excepto Error/Fin)
        for lugar in estado_actual:
            if lugar not in ['Error', 'Fin']:
                estado_actual[lugar] = 0
        
        # Paso 1: Filtrado inicial
        estado_actual['Inicio'] = 0
        estado_actual['Filtrar'] = 1
        estados.append(estado_actual.copy())
        
        # Paso 2: Determinar si es número o letra
        if caracter.isdigit():
            # Es número - ir a Error
            estado_actual['Filtrar'] = 0
            estado_actual['Error'] = 1
            estados.append(estado_actual.copy())
            continuar_procesamiento = False
            break
        else:
            # Es letra - evaluar
            estado_actual['Filtrar'] = 0
            estado_actual['Letra'] = 1
            estados.append(estado_actual.copy())
            
            # Paso 3: Verificar letra esperada
            if idx_esperado < len(secuencia_esperada) and caracter == secuencia_esperada[idx_esperado]:
                estado_actual['Letra'] = 0
                estado_actual[caracter.upper()] = 1
                idx_esperado += 1
                estados.append(estado_actual.copy())
                
                # Paso 4: Mover a Fin si es la última letra
                if idx_esperado == len(secuencia_esperada):
                    estado_actual[caracter.upper()] = 0
                    estado_actual['Fin'] = 1
                    estados.append(estado_actual.copy())
            else:
                # Letra incorrecta
                estado_actual['Letra'] = 0
                estado_actual['Error'] = 1
                estados.append(estado_actual.copy())
                continuar_procesamiento = False
    
    # Generar visualizaciones
def generar_visualizaciones_completas(input_string, estados):
    secuencia_esperada = ['a', 'p', 'r', 'o', 'b', 'a', 'd', 'o']
    paso_global = 0
    
    for i, caracter in enumerate(input_string.lower()):
        # Estado inicial para este carácter
        estado_caracter = {
            'Inicio': 1,
            'Filtrar': 0,
            'Letra': 0,
            'A': 0, 'P': 0, 'R': 0, 'O': 0, 'B': 0, 'D': 0,
            'Fin': 0,
            'Error': 0
        }
        
        # Paso 1: Mostrar inicio del procesamiento del carácter
        dot = crear_red_petri()
        estado_caracter['Inicio'] = 1
        for lugar, tokens in estado_caracter.items():
            if tokens == 1:
                dot.node(lugar, style='filled', fillcolor='red')
        dot.render(f'caracter_{i}paso{paso_global}', format='png', cleanup=True)
        print(f'Generado caracter_{i}paso{paso_global}.png')
        paso_global += 1
        time.sleep(0.3)
        
        # Paso 2: Transición a Filtrar
        estado_caracter['Inicio'] = 0
        estado_caracter['Filtrar'] = 1
        dot = crear_red_petri()
        for lugar, tokens in estado_caracter.items():
            if tokens == 1:
                dot.node(lugar, style='filled', fillcolor='red')
        dot.render(f'caracter_{i}paso{paso_global}', format='png', cleanup=True)
        print(f'Generado caracter_{i}paso{paso_global}.png')
        paso_global += 1
        time.sleep(0.3)
        
        # Determinar si es número o letra
        if caracter.isdigit():
            # Paso 3a: Número - transición a Error
            estado_caracter['Filtrar'] = 0
            estado_caracter['Error'] = 1
            dot = crear_red_petri()
            for lugar, tokens in estado_caracter.items():
                if tokens == 1:
                    dot.node(lugar, style='filled', fillcolor='red')
            dot.render(f'caracter_{i}paso{paso_global}', format='png', cleanup=True)
            print(f'Generado caracter_{i}paso{paso_global}.png (Número detectado)')
            paso_global += 1
            time.sleep(0.3)
            break  # Terminar el procesamiento
            
        else:
            # Paso 3b: Letra - transición a Letra
            estado_caracter['Filtrar'] = 0
            estado_caracter['Letra'] = 1
            dot = crear_red_petri()
            for lugar, tokens in estado_caracter.items():
                if tokens == 1:
                    dot.node(lugar, style='filled', fillcolor='red')
            dot.render(f'caracter_{i}paso{paso_global}', format='png', cleanup=True)
            print(f'Generado caracter_{i}paso{paso_global}.png')
            paso_global += 1
            time.sleep(0.3)
            
            # Verificar si es letra esperada
            if i < len(secuencia_esperada) and caracter == secuencia_esperada[i]:
                # Paso 4: Letra correcta - transición a lugar específico
                estado_caracter['Letra'] = 0
                estado_caracter[caracter.upper()] = 1
                dot = crear_red_petri()
                for lugar, tokens in estado_caracter.items():
                    if tokens == 1:
                        dot.node(lugar, style='filled', fillcolor='red')
                dot.render(f'caracter_{i}paso{paso_global}', format='png', cleanup=True)
                print(f'Generado caracter_{i}paso{paso_global}.png (Letra correcta: {caracter.upper()})')
                paso_global += 1
                time.sleep(0.3)
                
                # Paso 5: Transición a Fin si es la última letra
                if i == len(secuencia_esperada) - 1:
                    estado_caracter[caracter.upper()] = 0
                    estado_caracter['Fin'] = 1
                    dot = crear_red_petri()
                    for lugar, tokens in estado_caracter.items():
                        if tokens == 1:
                            dot.node(lugar, style='filled', fillcolor='red')
                    dot.render(f'caracter_{i}paso{paso_global}', format='png', cleanup=True)
                    print(f'Generado caracter_{i}paso{paso_global}.png (Procesamiento completado)')
                    paso_global += 1
                    time.sleep(0.3)
            else:
                # Paso 4: Letra incorrecta - transición a Error
                estado_caracter['Letra'] = 0
                estado_caracter['Error'] = 1
                dot = crear_red_petri()
                for lugar, tokens in estado_caracter.items():
                    if tokens == 1:
                        dot.node(lugar, style='filled', fillcolor='red')
                dot.render(f'caracter_{i}paso{paso_global}', format='png', cleanup=True)
                print(f'Generado caracter_{i}paso{paso_global}.png (Letra incorrecta: {caracter})')
                paso_global += 1
                time.sleep(0.3)
                break  # Terminar el procesamiento

if __name__ == "__main__":
    input_str = "A1P2R3O4B5A6D7O8"
    
    # Primero: Procesamiento normal (para estados principales)
    estados_principales = simular_procesamiento(input_str)
    
    # Segundo: Visualización detallada por carácter
    generar_visualizaciones_completas(input_str, estados_principales)