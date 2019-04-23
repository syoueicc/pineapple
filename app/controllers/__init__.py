import os
import importlib


def create_controller(app):
    current_dir = os.path.dirname(__file__)
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                controller_name = file.replace('.py', '')
                module_path = root.replace(current_dir, '.controllers').replace(os.sep, '.')
                controller = importlib.import_module('%s.%s' % (module_path, controller_name), package='app')
                app.register_blueprint(getattr(controller, '%s_blueprint' % controller_name))
