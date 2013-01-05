class Router(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        if hasattr(model,'using'):
            return model.using
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if hasattr(model,'using'):
            return model.using
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_syncdb(self, db, model):
        return None