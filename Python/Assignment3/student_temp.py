import numpy as np
import csv


def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################
    # rows = zip(time,amplitude)
    # with open("temp.csv", "w") as f:
        # writer = csv.writer(f)
        # for row in rows:
            # writer.writerow(row)
        
    ######################################
    temperature = int(round(1.644985924*sum(amplitude)/len(amplitude) + 33.92887739))
    
    return temperature
        
