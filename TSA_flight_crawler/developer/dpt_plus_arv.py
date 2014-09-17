##encoding=utf8
'''
例：搜索2014-09-11出发的航班，找到对应的到达航班，并匹配
1.2014-09-11出发的所有航班，取得dpt_id = md5( origin, destination, flight, equip )
2.找到2014-09-11和2014-09-12到达的所有航班
'''



cmd = \
"""
SELECT 
depart_from_flights.id, 
depart_from_flights.origin, 
depart_from_flights.destination, 
depart_from_flights.scheduled_time, 
depart_from_flights.actual_time
arrive_at_flights.scheduled_time
arrive_at_flights.actual_time


FROM depart_from_flights INNER JOIN arrive_at_flights
ON depart_from_flights.id = arrive_at_flights.id
"""


# c.execute("SELECT arv_id, origin, destination, flight, scheduled_time, equip FROM arrive_at_flights")
# counter = 0
# for arv_id, origin, destination, flight, scheduled_time, equip in c.fetchall():
#     cmd = \
#     """
#     UPDATE arrive_at_flights
#     SET arv_id = '%s'
#     WHERE arv_id = '%s';
#     """ % (md5_obj( (origin, destination, flight, scheduled_time) ), arv_id)
#     c.execute(cmd)
#     counter += 1
#     print counter 
# conn.commit() # 68863