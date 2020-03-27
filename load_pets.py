# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:30:41 2020

@author: kathy
"""

"""NOTATION: I am not sure how to use the db file - but I do have a free database host for dummy projects, which I will be using to insert the below lines and query"""

import psycopg2


connection = psycopg2.connect(user = "zowglzqx",
                              password = "HinwKUQSD2t_10zuQK5Tln-us-7N9JsI",
                              host = "drona.db.elephantsql.com",
                              database = "zowglzqx")

cursor = connection.cursor()
print ( connection.get_dsn_parameters(),"\n")

cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")


query = """

DELETE FROM "public"."person";

DELETE FROM "public"."pet";

DELETE FROM "public"."person_pet";

INSERT INTO "public"."person" (id, first_name, last_name, age)
VALUES (1,'James','Smith',41),
(2,'Diana','Greene',23),
(3, 'Sara','White',27),
(4,'William','Gibson',23);

INSERT INTO "public"."pet" (id, name, breed, age, dead)
VALUES (1,'Rusty','Dalmation',4,1),
(2,'Bella','AlaskanMalamute',3,0),
(3,'Max','CockerSpaniel',1,0),
(4,'Rocky','Beagle',7,0),
(5,'Rufus','CockerSpaniel',1,0),
(6,'Spot','Bloodhound',2,1);

INSERT INTO "public"."person_pet"(person_id, pet_id)
VALUES (1,1), (1,2), (2,3), (2,4), (3,5), (4,6);
"""

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()

print("PostgreSQL connection is closed \n\nAnswer to Question #2: The purpose of person_pet table is to identify the pet and their respect owners without creating duplicate records.")


