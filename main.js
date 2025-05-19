import { createInterface } from "readline";

const readline = createInterface({
  input: process.stdin,
  output: process.stdout,
});

const preguntar = (query) => {
  return new Promise((resolve) => {
    readline.question(query, (answer) => {
      resolve(answer);
    });
  });
};

const registrarCalificaciones = async () => {
  const informacionAlumnos = [];

  try {
    while (true) {
      const nombre = await preguntar(
        "Ingrese su nombre: (o ingrese 'salir' para terminar) "
      );

      if (nombre.toLowerCase() === "salir") {
        break;
      }

      const informacionAlumno = [];
      console.log(
        `Ingrese las materias y calificaciones del alumno ${nombre}:`
      );

      while (true) {
        const materia = await preguntar(
          "Ingrese la materia: (o 'fin' para terminar) "
        );

        if (materia.toLowerCase() === "fin") {
          break;
        }

        const calificacion = await preguntar(
          `Ingrese la calificacion de ${materia}: `
        );

        if (isNaN(calificacion)) {
          console.log("La calificacion debe ser un numero.");
          continue;
        }

        if (calificacion >= 0 && calificacion <= 10) {
          informacionAlumno.push([materia, calificacion]);
        } else {
          console.log("La calificacion debe estar entre 0 y 10.");
        }
      }
      if (informacionAlumno.length === 0) {
        console.log("Debe ingresar al menos una materia y calificacion.");
      } else {
        informacionAlumnos.push([nombre, informacionAlumno]);
      }

      mostrarFormatoMatriz(informacionAlumnos);
    }
  } catch (error) {
    console.error("Erros inesperado: ", error);
  } finally {
    readline.close();
  }
};

const mostrarFormatoMatriz = (informacionAlumnos) => {
  if (informacionAlumnos.length === 0) {
    console.log("No hay alumnos registrados.");
    return;
  }

  console.log("\n--- Matriz de Alumnos (Formato solicitado) ---");
  console.log("[");

  informacionAlumnos.forEach((alumno, index) => {
    const nombre = alumno[0];
    const materias = alumno[1];

    // Formato: ['Nombre', [['Materia1', nota1], ['Materia2', nota2], ...]]
    const materiasStr = materias.map((m) => `['${m[0]}', ${m[1]}]`).join(", ");

    // Agrega coma al final excepto para el último elemento
    const finLinea = index < informacionAlumnos.length - 1 ? "," : "";
    console.log(`    ['${nombre}', [${materiasStr}]]${finLinea}`);
  });

  console.log("]");
};

registrarCalificaciones();
