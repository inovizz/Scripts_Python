#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Sanchit"


class DBConnection:
    instance = None
    con = None

    def __new__(cls):
        if DBConnection.instance is None:
            DBConnection.instance = object.__new__(cls)
        return DBConnection.instance

    def __init__(self):
        if DBConnection.con is None:
            try:
                DBConnection.con = psycopg2.connect(database='...', user='...', password='...')
                print('Database connection opened.')
            except psycopg2.DatabaseError as db_error:
                print("Erreur :\n{0}".format(db_error))

    def __del__(self):
        if DBConnection.con is not None:
            DBConnection.close()
            print('Database connection closed.')