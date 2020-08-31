# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""
import redis
r = redis.Redis(
    host="localhost",
    port=6379, 
    password=None,db=0)

movies = r.hgetall("Models:ModelA")
inception = r.hgetall("Inception")
darkknight = r.hgetall("DarkKnight")
ph = r.hgetall("ProductionHouse")
actors = r.hgetall("Actors")
genre = r.hgetall("Genre")
i_Ph = r.smembers("Inception:ProdcutionHouse")
i_Act = r.smembers("Inception:Actors")
i_G = r.smembers("Inception:Genre")

"""
for key in movies:
    movDetails= r.hgetall(movies{key})
    print(movDetails)
"""
print(movies)

#for key in inception:
#    movDetails= r.hgetall(inception{key})
#    print(movDetails)


