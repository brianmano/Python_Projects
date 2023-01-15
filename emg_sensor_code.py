from sensor_library import *
from gpiozero import Button
import time


def main ():

values = initial_data()
RA_graph_total = []

while True:
    values = add_data(values) 
    RA = rolling_avg(values)
    check1 = threshold_value (RA)
    if check1 == True:
        RA_graph, values, check1 = check_irregular (values)
        RA_graph_total += RA_graph
        if check1 == True: 
            buzzer_output ()#Indicated to the user that something is wrong
            real = false_alarm ()
                if real == True:
                    vibration_output()
                    RA_graph, check1 = check_irregular (values)
                    RA_graph_total += RA_graph
                    while check1 == True:
                        RA_graph, check1 = check_irregular (values)
                        RA_graph_total += RA_graph
                        if check1 == False:
                            vibration_off()
                            grapher (RA_graph_total)
                            RA_graph_total = []
                   

def initial_data ():
    sensor = Muscle_Sensor (0)
    values = []*10
    for i in range(len(values)):
        data = sensor.muscle_raw()
        values[i] = data
    return values
                
def add_data (values):
    values[-1] = sensor.muscle_raw

def rolling_avg (values):
    sum_values = sum(values)
    average = sum_values / len(values)
    return average

def check_irregular (values):
    checkl_list = []
    RA_graph = []
    for i in range (4):
        values = add_data(values)
        RA = rolling_avg(values)
        RA_graph.append(RA)
        check1 = threshold_value (RA)
        check_list.append (check1)
    count = 0
    for i in check_list:
        if i == True:
            count += 1
    if count >= 3:
        return RA_graph, values, True
    return RA_graph, values, False
    

def threshold_value (RA):
    TV = 75
    if RA > threshold value:
        return (True)
    else:
        return False

def buzzer_output ():
    #initializing buzzer; 27 is the pin number
    buzzer_object = Buzzer(27)
    for i in range (2):
       buzzer_object.on() #turns buzzer on
       time.sleep(1)
       buzzer_object.off()
       time.sleep(1)
       
def false_alarm ():
    push_button = Button (pin_number) 
    for i in range (50): #try with elapsed time 
        if button.is_pressed:
            return False 
        time.sleep(0.01)
    return True 

def vibration_output():
    #vibration motor initalzation
    vibration_motor = Buzzer(26)
    vibration_motor.on() #turns buzz on

def vibration_off():
    vibration_motor.off()
