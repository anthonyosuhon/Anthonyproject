import cx_Oracle
con=cx_Oracle.connect('scott/tiger@localhost')
if con!=none:
    print('Connection established successfully')
    print('Version:', con.version)
else:
    print('Connection not established')
con.close()
