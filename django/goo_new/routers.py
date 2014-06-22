class MasterSlaveRouter(object):
    def db_for_read(self, model, **hints):
        """
        Reads always go to slave.
        """
        return 'slave'

    def db_for_write(self, model, **hints):
        """
        Writes always go to master.
        """
        return 'master'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the master/slave pool.
        """
        return None

    def allow_syncdb(self, db, model):
        """
        All models end up in this pool.
        """
        return True