from app.conf.settings import Dev
from app.utils.db_helper import DBHelper

db = DBHelper(
    host=Dev.host,
    port=Dev.port,
    user=Dev.user,
    password=Dev.password,
    database=Dev.database
)
