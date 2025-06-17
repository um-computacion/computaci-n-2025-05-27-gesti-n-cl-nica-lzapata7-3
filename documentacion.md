## Cómo se ejecuta el sistema

1. Asegurate de tener **Python 3** instalado.
2. Cloná el repositorio o descargá los archivos.
3. Abrí una terminal y ubicáte en la carpeta raíz del proyecto.
4. Ejecutá el sistema con:

```bash
python3 main.py
```

---

## Cómo se ejecutan las pruebas

Desde el primer directorio luego de realizar el git clone del proyecto se necesita ejecutar:

```bash
python3 -m unittest discover -s tests
```

Esto correrá automáticamente todas las pruebas unitarias que se encuentran en la carpeta `test`.

---

## Menú del sistema de gestión clínica

Las opciones disponibles son:

- **1) Agregar paciente:** Permite registrar un nuevo paciente en la clínica.
- **2) Agregar médico:** Permite registrar un nuevo médico.
- **3) Agendar turno:** Permite asignar un turno entre un paciente y un médico en una fecha y hora específica.
- **4) Agregar especialidad a médico:** Permite asignar una especialidad y días de atención a un médico existente.
- **5) Emitir receta:** Permite que un médico emita una receta para un paciente.
- **6) Ver historia clínica:** Permite consultar la historia clínica de un paciente, incluyendo turnos y recetas.
- **7) Ver todos los turnos:** Muestra la lista de todos los turnos agendados en la clínica.
- **8) Ver todos los pacientes:** Muestra la lista de pacientes registrados.
- **9) Ver todos los médicos:** Muestra la lista de médicos registrados.
- **0) Salir:** Vuelve al menú principal o cierra el sistema.

Cada opción te guiará paso a paso para ingresar los datos necesarios y te informará si ocurre algún error o si la operación fue exitosa.

## Flujo de uso recomendado

1. Registrar médicos (con sus especialidades y días de atención)
2. Registrar pacientes
3. Agendar turnos entre pacientes y médicos
4. Emitir recetas cuando sea necesario
5. Consultar historias clínicas


## Explicación del diseño general

El sistema está desarrollado de forma modular, utilizando programación orientada a objetos. Las clases están organizadas en carpetas según su responsabilidad:

```plaintext
📦 gestion_clinica/
├── models/         ← Contiene todas las clases del dominio (Paciente, Médico, Turno, Historia Clínica, Receta, etc.) y excepciones personalizadas
├── cli/            ← Contiene la interfaz de línea de comandos (CLI)
├── tests/           ← Contiene las pruebas unitarias escritas con unittest
└── main.py         ← Archivo principal que ejecuta la CLI del sistema
```

Cada componente está diseñado para cumplir una función específica dentro del sistema, facilitando su mantenimiento y escalabilidad.

