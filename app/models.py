import MySQLdb
from datetime import datetime
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASS,MYSQL_DB
from app import app

@app.before_request
def before_request():
    g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,MYSQL_DB)

def save_data(name,words,create_at):
    #sava the comment data
    visit_info=[name,words,create_at]
    #use mysql database
    #get a cursor
    curs=g.db.cursor()
    curs.execute("insert into content values(%s,%s,%s)",visit_info)
    curs.execute('alter table content order by visit_at desc')
    g.db.commit()
    curs.close()
    g.db.close()
    
def  load_data():
        #return the comments savaed before
        #open the shelve module database file
        #use mysql to return
        curs=g.db.cursor()
        curs.execute("select * from content")
        visit_info=curs.fetchall()
        curs.close()
        g.db.close()
        return visit_info
