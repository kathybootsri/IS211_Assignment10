# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:40:51 2020

@author: kathy
"""

import psycopg2
import pandas as pd


connection = psycopg2.connect(user = "zowglzqx",
                              password = "HinwKUQSD2t_10zuQK5Tln-us-7N9JsI",
                              host = "drona.db.elephantsql.com",
                              database = "zowglzqx")

cursor = connection.cursor()


print ("What person ID do you want to know about?")

stop = '-1'

person_id = input()

while person_id != stop:
    query = f"""
    SELECT p.first_name, p.last_name, p.age, pet.name, pet.breed, pet.age, pet.dead
    FROM "public"."person" p
    LEFT JOIN "public"."person_pet" pp on pp.person_id = p.id
    LEFT JOIN "public"."pet" pet on pet.id = pp.pet_id
    WHERE p.id = {person_id}"""
    
    cursor.execute(query)
    
    data = cursor.fetchall()
    
    df = pd.read_sql_query(query, connection)
    

    
    #First Name
    first_name = df.loc[0][0]
    last_name = df.loc[0][1]
    age = df.loc[0][2]
    
    print(f"{first_name} {last_name}, {age} years old.")
    

    for x in range(len(df)):
        if df.loc[x][6] == 0:
            print(f"{first_name} {last_name} owns {df.loc[x][3]}, a {df.loc[x][4]}, that is {df.loc[x][5]} years old.")
        else:
            print(f"{first_name} {last_name} owned {df.loc[x][3]}, a {df.loc[x][4]}, that was {df.loc[x][5]} years old.")

    print ("What person ID do you want to know about?")
    
    person_id = input()

    if person_id == stop: 
        cursor.close()
        connection.close()
        print("Exiting program.")
        break
    
    else:
        continue
