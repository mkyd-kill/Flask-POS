from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from . import app, db

# handles all database migrations
migrate = Migrate()
migrate.init_app(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()