from flask_restful import Resource, reqparse
from models import db, Task, User

class TaskF(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, required=True, help='El título es obligatorio', location='json')
        self.parser.add_argument('description', type=str, required=False, location='json')
        self.parser.add_argument('user_id', type=int, required=True, help='El user_id es obligatorio', location='json')
        self.parser.add_argument('status', type=str, required=False, default='pending', location='json')

    def get(self, task_id=None, user_id=None):
        try:
            if task_id:
                task = Task.query.get(task_id)
                if not task:
                    return {'error': 'Tarea no encontrada'}, 404
                return task.to_dict(), 200
            elif user_id:
                tasks = Task.query.filter_by(user_id=user_id).all()
                return [t.to_dict() for t in tasks], 200
            else:
                tasks = Task.query.all()
                return [t.to_dict() for t in tasks], 200
        except Exception as e:
            return {'error': f'Error al obtener tareas: {str(e)}'}, 500

    def post(self):
        args = self.parser.parse_args()
        try:
            user = User.query.get(args['user_id'])
            if not user:
                return {'error': 'El usuario no existe'}, 400
            task = Task(
                title=args['title'],
                description=args.get('description'),
                user_id=args['user_id'],
                status=args.get('status', 'pending')
            )
            db.session.add(task)
            db.session.commit()
            return task.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': f'Error al crear la tarea: {str(e)}'}, 500

    def put(self, task_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=False, location='json')
        parser.add_argument('description', type=str, required=False, location='json')
        parser.add_argument('status', type=str, required=False, location='json')
        parser.add_argument('user_id', type=int, required=False, location='json')
        args = parser.parse_args()
        try:
            task = Task.query.get(task_id)
            if not task:
                return {'error': 'Tarea no encontrada'}, 404
            if args['title'] is not None:
                task.title = args['title']
            if args['description'] is not None:
                task.description = args['description']
            if args['status'] is not None:
                task.status = args['status']
            if args['user_id'] is not None:
                user = User.query.get(args['user_id'])
                if not user:
                    return {'error': 'El usuario no existe'}, 400
                task.user_id = args['user_id']
            db.session.commit()
            return task.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {'error': f'Error al actualizar la tarea: {str(e)}'}, 500

    def delete(self, task_id):
        try:
            task = Task.query.get(task_id)
            if not task:
                return {'error': 'Tarea no encontrada'}, 404
            db.session.delete(task)
            db.session.commit()
            return {'message': 'Tarea eliminada correctamente'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': f'Error al eliminar la tarea: {str(e)}'}, 500

if not hasattr(Task, 'to_dict'):
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'user_id': self.user_id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None
        }
    Task.to_dict = to_dict
