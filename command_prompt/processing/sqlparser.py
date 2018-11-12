#!/usr/bin/env python3
import re
import shlex
#Example inputs here:
inputRead = "select id1 from pokemon"
inputWrite = "insert into pokemon (id, val) values (9, \"hey listen\")"
inputCondition = "select * from pokemon where id=1"

def clean_statement(rawSQL):
    statement = shlex.split(rawSQL.lower())
    return statement

def select_sql(statement):
    # extract column(s) selecting
    colStart = statement.index('select')+1
    colEnd = statement.index('from')
    columns = statement[colStart:colEnd]

    # extract table(s) selecting
    tableStart = colEnd+1
    try:
        tableEnd = statement.index('where')
    except:
        tableEnd = None
    tables = statement[tableStart:tableEnd]

    # extract extras ('where' statement)
    if tableEnd:
        extraStart = tableEnd
        extras = statement[extraStart:]
    else:
        extras = None
    if extras:
        return columns, tables, extras
    else:
        return columns, tables

def insert_sql(statement):
    tableStart = statement.index('into')+1
    tableEnd = statement.index('values')
    table = statement[tableStart]
    tableCols = statement[tableStart+1:tableEnd]
    tableCols = [c.strip("(").strip(")") for c in tableCols]
    values = statement[tableEnd+1:]
    values = [v.strip("(").strip(")") for v in values]
    return table, values

def parse(SQLstatement):
    statement = clean_statement(SQLstatement)
    if 'select' in statement:
        operation = select_sql(statement)
    elif 'insert' in statement:
        operation = insert_sql(statement)
    return operation
print(inputRead)
print(inputWrite)
print(inputCondition)
print("read input: ", parse(inputRead))
print("write input: ", parse(inputWrite))
print("condition input: ", parse(inputCondition))

# Transactions
# SELECT/READ = id, id, id
# INSERT/WRITE = id, val
# SQL parsed to know if you are reading or writing to the database
# row id's for reading, id and values for writing

#SELECT * FROM Table WHERE ID=9     =>    READ 9
#INSERT into Table (ID, VAL) values (9, "HEY LISTEN!")   =>  WRITE id, val
# Actual output: "WRITE 9 'hey listen'"
#                "READ 9"
#        Format: {function} {id} {val}.....{val_n}
# pass this info to Katie's Listener



# POKEMON
# ID, pokemon_name, level, attributes
# 56, Bulbasaur, 3, greenGroundWild
