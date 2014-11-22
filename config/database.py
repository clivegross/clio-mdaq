#!/usr/bin/python
#
# database.py
#
# description

DB_CONFIG = {
 'ENGINE' : 'mysql',
 'NAME' : 'clio',
 'USER' : 'clio',
 'PASSWORD' : 'clio',
 'HOST' : 'localhost',
 'PORT' : '3306'
}

class Singleton(object):
  _instance = None
  def __new__(class_, *args, **kwargs):
    if not isinstance(class_._instance, class_):
        class_._instance = object.__new__(class_, *args, **kwargs)
    return class_._instance

class Database(Singleton):
 _db_connection = None

 def create_connection_string(self): #, DB_CONFIG):
  #  connection_string = DB_CONFIG['ENGINE']+"://"+DB_CONFIG['NAME']+":"+DB_CONFIG['PASSWORD']+"@"+DB_CONFIG['HOST']+":"+DB_CONFIG['PORT']+"/"+DB_CONFIG['NAME']
  connection_string = ""
  return connection_string

 def create_connection(self):
  if is_none(_db_connection):
   engine = create_engine(self.create_connection_string())
   self._db_connection = engine.connect()
   return self._db_connection

 def query(self, query)
  self.create_conn()
  self._db_conn.execute(query)

 # db = Database()
 # db.query('jyghjyf
connection_string = create_connection_string(DB_CONFIG)

print(connection_string)
