##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-11

import psycopg2
from parse_html import records_from_file
from LinearSpider.jt import *
import os, shutil

conn = psycopg2.connect(host = '10.0.80.180',  dbname = 'securiport', user = 'postgres', password = '')
c = conn.cursor()

def create_table():
    cmd = \
    """
    CREATE TABLE public.depart_from_flights
    (dpt_id varchar(32) PRIMARY KEY NOT NULL,
    origin varchar(3) NOT NULL,
    destination varchar(3) NOT NULL,
    flight varchar(16) NOT NULL,
    airline varchar(255) NOT NULL,
    scheduled_time timestamp NOT NULL,
    actual_time timestamp,
    Terminal_Gate varchar(16),
    status varchar(64),
    equip varchar(16));
    """
    c.execute(cmd) # flight_departure
    cmd = \
    """
    CREATE TABLE public.arrive_at_flights
    (arv_id varchar(32) PRIMARY KEY NOT NULL,
    origin varchar(3) NOT NULL,
    destination varchar(3) NOT NULL,
    flight varchar(16) NOT NULL,
    airline varchar(255) NOT NULL,
    scheduled_time timestamp NOT NULL,
    actual_time timestamp,
    Terminal_Gate varchar(16),
    status varchar(64),
    equip varchar(16));
    """
    c.execute(cmd) # flight_arrival
    conn.commit()
    
def push_departure(path_dpt, path_trash):
    ## push DEPARTURE
    for fname in os.listdir(path_dpt):
        records = records_from_file(os.path.join(path_dpt, fname), mode = 'departure')
        try:
            c.executemany("INSERT INTO public.depart_from_flights VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", records)
        except psycopg2.IntegrityError:
            conn.rollback()
            for record in records:
                try:
                    c.executemany("INSERT INTO public.depart_from_flights VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (record,) )
                except psycopg2.IntegrityError:
                    conn.rollback()
                else:
                    conn.commit()
        else:
            conn.commit()
    
        shutil.move(os.path.join(path_dpt, fname), os.path.join(path_trash, fname))
        print 'INSERT %s to DB success! %s records' % (os.path.join(path_dpt, fname), len(records) )

def push_arrival(path_arv, path_trash):
    ## push ARRIVAL
    for fname in os.listdir(path_arv):
        records = records_from_file(os.path.join(path_arv, fname), mode = 'arrival')
        try:
            c.executemany("INSERT INTO public.arrive_at_flights VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", records)
        except psycopg2.IntegrityError:
            conn.rollback()
            for record in records:
                try:
                    c.executemany("INSERT INTO public.arrive_at_flights VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (record,) )
                except psycopg2.IntegrityError:
                    conn.rollback()
                else:
                    conn.commit()
        else:
            conn.commit()
        shutil.move(os.path.join(path_arv, fname), os.path.join(path_trash, fname))
        print 'INSERT %s to DB success! %s records' % (os.path.join(path_arv, fname), len(records) )
        
if __name__ == '__main__':
    try:
        create_table()
    except:
        conn.rollback()
    push_departure(r'C:\HSH\DataWarehouse\TSA_flight\raw_html\departures', r'C:\HSH\DataWarehouse\TSA_flight\trash\dpt')
    push_arrival(r'C:\HSH\DataWarehouse\TSA_flight\raw_html\arrivals', r'C:\HSH\DataWarehouse\TSA_flight\trash\arv')