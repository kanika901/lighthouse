import csv


###----- Created le_solve_all.csv based on all le_driver_all.csv and le_solve.csv. -----###

f_le_driver_all = csv.reader(open('../Driver/dataBase/le_driver_all.csv', 'rb'), delimiter=',')
f_le_solve = csv.reader(open('../Computational/dataBase/le_solve.csv', 'rb'), delimiter=',')


f_le_solve_all = csv.writer(open('le_solve_all.csv', 'wb'), delimiter=',')


def writeRows(fileName, lineNumber):
    for row in fileName:
        row[0] = int(row[0]) + lineNumber
        f_le_solve_all.writerow(row)



writeRows(f_le_driver_all, 0)

writeRows(f_le_solve, f_le_driver_all.line_num)
