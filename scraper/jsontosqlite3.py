#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:45:44 2018

@author: allee
"""

import json
import sqlite3

with open("/home/allee/Mercury/mercury-challenge/data/gsr/cu_gsr/CU_April_2016.json", "r") as read_file:
    data = json.load(read_file)
    
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "pythonsqlite.db"
 
    sql_create_gskeyword_table = """ CREATE TABLE IF NOT EXISTS gold_standard_keywords (
                                        Event_ID,
                                        keyword
                                    ); """
 
    sql_create_gsarticle_table = """ CREATE TABLE IF NOT EXISTS gold_standard_article (
                                        Event_ID,
                                        title,
                                        text
                                    );"""
    
    sql_create_gsreport_table = """CREATE TABLE IF NOT EXISTS gold_standard_report (
                                        Approximate_Location text,
                                        City text,
                                        Country text,
                                        Crowd_Size,
                                        Crowd_Size_Description text,
                                        Earliest_Reported_Date text,
                                        Encoding_Comment text,
                                        Event_Date text,
                                        Event_ID text,
                                        Event_Type text,
                                        First_Reported_Link text,
                                        GSS_Link text,
                                        Latitude text,
                                        Longitude text,
                                        News_Source text,
                                        Other_Links text,
                                        Population text,
                                        Reason text,
                                        Revision_Date text,
                                        State text
                                );"""
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_gskeyword_table)
        # create tasks table
        create_table(conn, sql_create_gsarticle_table)
        create_table(conn, sql_create_gsreport_table)
    else:
        print("Error! cannot create the database connection.")
     
    c = conn.cursor()
    for record in data:
        print(record['GSS_Link'])
        query = '(Approximate_Location, City, Country, Crowd_Size, Crowd_Size_Description,Earliest_Reported_Date,Encoding_Comment,Event_Date,Event_ID,Event_Type, \
		First_Reported_Link,GSS_Link,Latitude,Longitude,News_Source,Other_Links,Population,Reason,Revision_Date,State)'
        c.execute('INSERT INTO gold_standard_report ' + query + ' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', \
		(record['Approximate_Location'],record['City'], record['Country'], record['Crowd_Size'], record['Crowd_Size_Description'], \
		record['Earliest_Reported_Date'],record['Encoding_Comment'], record['Event_Date'], record['Event_ID'], record['Event_Type'], \
		record['First_Reported_Link'],record['GSS_Link'], record['Latitude'], record['Longitude'], record['News_Source'], \
		record['Other_Links'],record['Population'], record['Reason'], record['Revision_Date'], record['State']))
        
    conn.commit()
    
#if __name__ == '__main__':
#    main()
        
main()




