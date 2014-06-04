import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="lighthouse", passwd="yellow1234", db="lighthousedb") 

cursor = conn.cursor()

##### ------------ for LAPACK_le tables ---------------- #####
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_driver")
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_expert")
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_simple")

    
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_computational")
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_condition_number")
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_equilibrate")
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_error_bound")
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_factor")
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_inverse")      
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_solve")


cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_only")


cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_arg")
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_le_arg_c")




##### ------------ for LAPACK_eigen tables ---------------- #####
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_eigen")



##### ------------ for LAPACK_svd tables ---------------- #####
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_svd")



##### ------------ for LAPACK routine information table ---------------- #####
cursor.execute("DROP TABLE IF EXISTS lighthouse_lapack_routineinfo")

conn.commit()

cursor.close()
conn.close()

