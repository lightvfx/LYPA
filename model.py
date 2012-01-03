# -*- coding: utf-8 -*-
from elixir import *
#from config import *
from LYPA_cfg import *
#from sqlalchemy.dialects.postgresql.base import dialect
<<<<<<< HEAD

cfg = config()
metadata.bind = cfg.DBbind

=======
#metadata.bind = "postgres://LYPA:zanetik@192.168.1.65/postgres"
cfg = config()
metadata.bind = cfg.DBbind
#metadata.bind = "postgres://LYPA:zanetik@192.168.1.65/postgres2"
>>>>>>> f1c10b68c824faa699084ac5119ba97047aa56ab
metadata.bind.echo = False
    
def saveData():
    session.commit()

class Shot(Entity):
    Name = Field(Unicode(40),required=True)
    
    In = Field(Unicode(4))
    Out = Field(Unicode(4))
    CutIn = Field(Integer)
    CutOut = Field(Integer)
    Scan = Field(UnicodeText)
    Description = Field(UnicodeText)
    Grade = Field(UnicodeText)
    Lut = Field(UnicodeText)
    Status = Field(Integer)
    Thumbnail = Field(UnicodeText)
    Renders = OneToMany('Render')
    Assets = OneToMany('Asset')
    Seq = ManyToOne('Sequence')
    def __repr__(self):
        #return '<Shot "%s" "%s" >' % (self.Name, self.Seq, self.In, self.Out, self.CutIn,self.CutOut, self.Scan, self.description, self.Grade, self.Lut, self.ShoppingList)
        return '<Shot "%s">' % (self.Name)


class Asset(Entity):
    Name = Field(Unicode(100),required=True)
    Textures = ManyToOne('Texture')
    PathLXL = Field(UnicodeText)
    PathOBJ = Field(UnicodeText)
    PathBGEO = Field(UnicodeText)
    version= Field(Integer)
    Description = Field(UnicodeText)
    type = Field(Unicode(40))
    Date = Field(DateTime,default=None,required=False)
    Shots = ManyToOne('Shot')
    Project = ManyToOne('Project')
    def __repr__(self):
        return '<Asset "%s"' % (self.Name)
        
class Texture(Entity):
    Name = Field(Unicode(100),required=True)
    Width = Field(Integer)
    Height = Field(Integer)
    Format = Field(Unicode(10))
    Path = Field(UnicodeText)
    Version = Field(Integer)
    Assets = OneToMany('Asset')
    def __repr__(self):
        return '<Texture "%s">' % (self.Name)
    
class Dailie(Entity):
    Name = Field(Unicode(100),required=True)
    Comments = Field(UnicodeText)
    Status = Field(Integer)
    Renders = ManyToOne('Render')
    Project = ManyToOne('Project')
    info = Field(UnicodeText)
    def __repr__(self):
        return '<Daily "%s">' % (self.Name)
        

class Render(Entity):
    ShotName = ManyToOne('Shot')
    SeqName = ManyToOne('Sequence')
    Name = Field(UnicodeText,required=True)
    Dailie = OneToMany('Dailie')
    In = Field(Integer)
    Out = Field(Integer)
    Path = Field(UnicodeText)
    version= Field(Integer)
    ScenePath = Field(UnicodeText)
    Type = Field(Unicode(40))
    Date = Field(DateTime,default=None,required=False)
    User = Field(Unicode(40))
    Width = Field(Integer)
    Height = Field(Integer)
    Format = Field(Unicode(10))  
    Job = Field(Unicode(100))
    Project = ManyToOne('Project')
    def __repr__(self):
        return '<Render "%s">' % (self.Name)
        
class Sequence(Entity):
    Name = Field(Unicode(100),required=True)
    Shots =  OneToMany('Shot')
    Renders =  OneToMany('Render')
    Project =  ManyToOne('Project')
    
    def __repr__(self):
        return '<Sequence "%s">' % (self.Name)
        
class User(Entity):
    Name = Field(Unicode(100),required=True)
    Password = Field(Unicode(100))
    email = Field(Unicode(100))
    info = Field(Unicode(100))
    #projects = OneToMany('Project')
    def __repr__(self):
        return '<User "%s">' % (self.Name)

class Job(Entity):
    Name = Field(Unicode(100),required=True)
    Tasks = OneToMany('Task')
    Status = Field(Integer)
    Type = Field(Unicode(40))
    
    def __repr__(self):
        return '<Shot "%s">' % (self.Name)


class Task(Entity):
    Name = Field(Unicode(100),required=True)
    ShortName = Field(Unicode(100))
    job = ManyToOne('Job')
    In = Field(Integer)
    Out = Field(Integer)
    Command =  Field(Unicode)
    Status = Field(Integer)
    Type = Field(Unicode(40))
    Log = Field(Unicode)
    Node = ManyToOne('Node')
    Pid = Field(Integer)
    #CurrentLog = Field(Unicode)
    def __repr__(self):
        return '<task "%s"' % (self.Name)
        
class Node(Entity):
    Name = Field(Unicode(100),required=True)
    Tasks = OneToMany('Task')
    Status = Field(Integer)
    def __repr__(self):
        return '<Node "%s">' % (self.Name)
        
class Project(Entity):
    Name = Field(Unicode(100),required=True)
    ConfigFile = Field(Unicode)
    Width = Field(Integer)
    Height = Field(Integer)
    Ratio = Field(Integer)
    Framerate = Field(Integer)
    LUT = Field(UnicodeText)
    Client = Field(Unicode)
    Seqs =  OneToMany('Sequence')
    Assets =  OneToMany('Asset')
    Dailies =  OneToMany('Dailie')
    Renders =  OneToMany('Render')
    #Users = ManyToOne('User')
    def __repr__(self):
        return '<Project "%s">' % (self.Name)
    

    
    