import numpy as np
import csv

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################
    # rows = zip(time,amplitude)
    # with open("heart.csv", "w") as f:
        # writer = csv.writer(f)
        # for row in rows:
            # writer.writerow(row)
            
    i = 0
    avg = 0
    bpm = 0
    t1 = 0
    t2 = 0
    period = []
    
    while i < len(time):
        if i > 1000 and amplitude[i] - amplitude[i-1] > 4:
            t1 = t2
            t2 = time[i]
            if t2 - t1 > 0.15 and t1 != 0 and t2 != 0:
                period.append(t2 - t1)
        i += 1
        
    if len(period) != 0:
        avg = sum(period)/len(period)
    
    if avg != 0:
        bpm = int(round(1 / avg * 60))
    
    ######################################
        
    return bpm
        
