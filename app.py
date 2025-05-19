def registrar_calificaciones():
    matriz_alumnos = []
    
    while True:
        nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        
        materias_alumno = []
        
        print(f"Ingrese las materias y calificaciones para {nombre}:")
        while True:
            try:
                materia = input("Ingrese el nombre de la materia (o 'fin' para terminar con este alumno): ")
                if materia.lower() == 'fin':
                    break
                
                if not materia.strip() or not all(c.isalpha() or c.isspace() for c in materia):
                    print("La materia debe contener solo letras y espacios.")
                    continue
                
                calificacion = float(input(f"Ingrese la calificación de {materia}: "))
                if 0 <= calificacion <= 10:
                    materias_alumno.append([materia, calificacion])
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número para la calificación.")
        
        if materias_alumno:
            matriz_alumnos.append([nombre, materias_alumno])
        else:
            print("No se registraron materias para este alumno.")
    
    return matriz_alumnos

def mostrar_calificaciones(matriz_alumnos):
    if not matriz_alumnos:
        print("No hay alumnos registrados.")
        return
    
    print("\n--- Calificaciones Registradas ---")
    for alumno in matriz_alumnos:
        nombre = alumno[0]
        materias = alumno[1]
        
        print(f"\nAlumno: {nombre}")
        print("Materias y calificaciones:")
        for materia in materias:
            print(f"  - {materia[0]}: {materia[1]}")

def mostrar_formato_matriz(matriz_alumnos):
    if not matriz_alumnos:
        print("No hay alumnos registrados.")
        return
    
    print("\n--- Matriz de Alumnos (Formato solicitado) ---")
    print("[")
    for i, alumno in enumerate(matriz_alumnos):
        nombre = alumno[0]
        materias = alumno[1]
        
        # Formato: ['Nombre', [['Materia1', nota1], ['Materia2', nota2], ...]]
        materias_str = ", ".join([f"['{materia[0]}', {materia[1]}]" for materia in materias])
        
        # Agrega coma al final excepto para el último elemento
        fin_linea = "," if i < len(matriz_alumnos) - 1 else ""
        print(f"    ['{nombre}', [{materias_str}]]{fin_linea}")
    print("]")

def main():
    print("=== Sistema de Registro de Calificaciones ===")
    matriz_alumnos = registrar_calificaciones()
    mostrar_calificaciones(matriz_alumnos)
    mostrar_formato_matriz(matriz_alumnos)

if __name__ == "__main__":
    main()