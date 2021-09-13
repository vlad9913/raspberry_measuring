import sys
import csv
while True:
    filename = input("Numele fisierului cu coordonate:")
    new_filename = filename.replace(".csv",".txt")
    dict_list = []
    with open (filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                dict_list.append({"X":row[1] , "Y":row[2] , "Z":row[3]})
                line_count += 1
        print(f'Processed {line_count} lines.')
    with open (new_filename,"w") as cnc_file:
        cnc_file.write("G00G21G17G90G40G49G80G91.1G94" + '\n')
        cnc_file.write("S12000 M3" + '\n')
        cnc_file.write("" +'\n')
        for dictt in dict_list:      
            zetu = float(dictt["Z"])*4
            cnc_file.write("N"+(str(zetu)).split('.')[0]+" G00X"+str(float(dictt["X"])*4)+"Y"+str(float(dictt["Y"])*4)+'\n')
            cnc_file.write("M00"+'\n')
            cnc_file.write("G1Z-5.00F1000"+'\n')
            cnc_file.write("G0Z0"+'\n')
        
        cnc_file.write("G00Z40.000" +'\n'+"M5"+'\n'+"M30"+'\n'+"%"+'\n')
