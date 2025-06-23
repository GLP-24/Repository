@@ -0,0 +1,69 @@
# Tarea: Implementación de CRUD para Task

## Objetivo
Implementar operaciones CRUD (Create, Read, Update, Delete) para el modelo Task siguiendo el patrón implementado en UserF.

## Requisitos

1. Crear clase TaskF que herede de Resource (flask_restful)
2. Implementar los siguientes métodos:

### Método GET
- Obtener tarea por ID
- Listar todas las tareas de un usuario específico
- Incluir manejo de errores

### Método POST
- Crear nueva tarea
- Validar datos requeridos:
  - title (obligatorio)
  - description
  - user_id (obligatorio)
  - status (default: 'pending')
- Implementar manejo de errores y rollback

### Método PUT
- Actualizar tarea existente por ID
- Validar existencia de la tarea
- Permitir actualización de:
  - title
  - description
  - status
- Implementar manejo de errores y rollback

### Método DELETE
- Eliminar tarea por ID
- Validar existencia de la tarea
- Implementar manejo de errores y rollback

## Estructura Sugerida
```python
class TaskF(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # Definir argumentos necesarios

    def get(self, task_id=None, user_id=None):
        # Implementar obtención de tarea(s)

    def post(self):
        # Implementar creación de tarea

    def put(self, task_id):
        # Implementar actualización de tarea

    def delete(self, task_id):
        # Implementar eliminación de tarea
```

## Rutas API a Implementar
- GET /api/tasks/<task_id> - Obtener tarea específica
- GET /api/tasks/user/<user_id> - Listar tareas de un usuario
- POST /api/tasks - Crear nueva tarea
- PUT /api/tasks/<task_id> - Actualizar tarea
- DELETE /api/tasks/<task_id> - Eliminar tarea

## Bonus
- Agregar filtros por status
- Implementar paginación para el listado de tareas
- Agregar validación de user_id existente al crear tarea