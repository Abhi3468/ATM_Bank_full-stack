# routers.py

class AppRouter:
    """
    A router to control database operations for different apps.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'BankInterface':
            return 'BankInterface_db'
        elif model._meta.app_label == 'UserInterface':
            return 'UserInterface_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'BankInterface':
            return 'BankInterface_db'
        elif model._meta.app_label == 'UserInterface':
            return 'UserInterface_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in ('BankInterface', 'UserInterface') and
            obj2._meta.app_label in ('BankInterface', 'UserInterface')
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'BankInterface':
            return db == 'BankInterface_db'
        elif app_label == 'UserInterface':
            return db == 'UserInterface_db'
        return 'default'
