#
# Model Archivetbl
#
from sqlalchemy import Column, Integer, String, Boolean, Sequence
from sqlalchemy import BigInteger, Date, DateTime, Float, Numeric, Unicode, Text
from scrat.lib.powlib import relation
from scrat.database.sqldblib import Base 
from scrat.lib.powlib import PowBaseMeta

#@relation.has_many("<plural_other_models>")
@relation.setup_sql_schema()
class Archivetbl(Base, metaclass=PowBaseMeta):
    
    #
    # cerberus style schema
    #
    schema = {        
        'title' :   { 'type' : 'string', 'maxlength' : 35 },
        'path'  :   { 'type' : 'string' },
        'username'  :   { 'type' : 'string' },
        "filetype" :   { "type" : "integer", "default" : 0 }  ,
        "create_date" : {"type" : "datetime" }
    }

    # if you want to define a custom tablename for this model:
    #__tablename__ = "archivetbls"
    
    # if you dont want to use the pow schema extension
    #_use_pow_schema_attrs= False

    # define class attributes/variables here that should be included in to_dict() 
    # conversion and also handed to the encoders but that are NOT part of the schema.
    include_attributes=[]

    # Add sqlalchemy table_args here. Add "autoload" : True for database reflection
    __table_args__ = { "extend_existing": True  }
    
    #
    # init
    #
    def __init__(self, **kwargs):
        self.setup_instance_values()
        self.init_on_load(**kwargs)
    #
    # your model's methods down here
    #
