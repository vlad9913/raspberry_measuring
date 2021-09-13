import serial
import csv
import winsound
print("Hai baga si masoara!")
arduino = serial.Serial('COM3', 9600, timeout=.1)
file_name = 'coordonate.csv'
last_data=''
index = -1 
keys = ["id","X","Y","Z"]
my_dict = {key: None for key in keys}
while True:
            data = arduino.readline()[:-2]
            if data:
                    if last_data == 'id=':
                        my_dict["id"] = data.decode('UTF-8')
                    if last_data == 'X=':
                        my_dict["X"] = float(data.decode('UTF-8')) 
                    if last_data == 'Y=':
                        my_dict["Y"] = float(data.decode('UTF-8')) 
                    if last_data == 'Z=':
                        my_dict["Z"] = float(data.decode('UTF-8')) * -1
                        index+=1
                        print(my_dict)
                        if index == 0 :
                            my_dict1 = my_dict

                        if index == 1 :
                            my_dict2 = my_dict

                        if index == 2 : #End of three readings
                            index = -1    
                            if (((str(my_dict["X"]).split('.')[0]) == (str(my_dict1["X"]).split('.')[0]) == (str(my_dict2["X"]).split('.')[0])) and ((str(my_dict["Y"]).split('.')[0]) == (str(my_dict1["Y"]).split('.')[0]) == (str(my_dict2["Y"]).split('.')[0])) and ((str(my_dict["Z"]).split('.')[0]) == (str(my_dict1["Z"]).split('.')[0]) == (str(my_dict2["Z"]).split('.')[0]))):
                                   #E bine
                                print("Ok")
                                winsound.Beep(1000, 500) 
                                with open('coords.csv', 'a', newline='') as file:
                                    fieldnames = keys
                                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                                    writer.writerow(my_dict)
                            else:
                                print("NOT OK RETRY!!!!!!!!!!!!!!.")
                                
                                winsound.Beep(2000, 500)  
                        my_dict = {key: None for key in keys}                  
                    
                    last_data = data.decode('UTF-8')














