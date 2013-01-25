class Router(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    
    def _check_using(self,mode,model,**hints):
        using = None
        if hasattr(model,'using'):
            using =  model.using
        return using
    
    def db_for_read(self, model, **hints):
        return self._check_using('read',model, **hints)

    def db_for_write(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        return self._check_using('write',model, **hints)
        
    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_syncdb(self, db, model):
        return None