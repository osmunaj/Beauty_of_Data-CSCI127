import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# CSCI 127, Lab 12                                |
# November 29, 2022                               |
# Ari Osmun                                       |
# -------------------------------------------------

def read_file(file_name):
    read = open(file_name)
    read.readline()
    names = []
    enrollments = []
    for line in read:
        listing = line.rstrip('\n').split(',')
        enrollments.append(int(listing[0]))
        names.append(listing[1])
    return (np.array(names), np.array(enrollments))
    
# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)
    fig, ax= plt.subplots()
    col = ['gold','blue']
    ax.bar(college_names, college_enrollments, label = None, color = col)

    ax.set_ylabel('Enrollments')
    ax.set_xlabel('College')
    ax.set_title('Fall 2020')

    ax.set_ylim(0,5000)
    
    plt.show()
    

# -------------------------------------------------

main("fall-2020.csv")
