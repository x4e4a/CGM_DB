from pydexcom import Dexcom
import sqlite3

conn = sqlite3.connect('newdb.db')

dexcom = Dexcom("##EMAIL##","##PASSWORD##")
bg = dexcom.get_current_glucose_reading()
readings = dexcom.get_glucose_readings()

print(f'Blook Glucose = {bg.value}')
print(f'Trending = {bg.trend_description}')
print(f'history = {bg.time}')
for x in readings:
    print(f'Time {x.time} - Value {x.value}')
    query = 'INSERT INTO BSREADINGS (DATETIME,READING) VALUES' + '("' + str(x.time)+ '",' + str(x.value) +');'
    conn.execute(query)
conn.commit()

print("RECORD Created successfully")
''' Deletes the Duplicates from the records due to overlap '''
conn.execute('''DELETE FROM BSREADINGS WHERE  ID not in (SELECT min(ID) from BSREADINGS GROUP BY BSREADINGS.DATETIME)''')

print("Duplicates Deleted")
conn.commit()
