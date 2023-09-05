import mysql.connector

conexion = mysql.connector.connect(user='root', password='edgos97', host='192.168.30.32', database='erpweb', port='3306')

print(conexion)
