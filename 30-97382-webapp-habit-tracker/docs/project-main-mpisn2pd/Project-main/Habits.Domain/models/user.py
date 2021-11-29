from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta

users = Table(
  'users',meta,
  Column('id',Integer,primary_key=True),
  Column('username',String(255)),
  Column('firstName',String(255)),
  Column('lastName',String(255)),
  Column('email',String(255)),
  Column('password',String(255)),
)