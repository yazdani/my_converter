#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import rospy
from std_msgs.msg import String

def Float2Degree(infile_name='/home/noentry/Desktop/test_FloatIntoDegree.csv', outfile_name='/home/noentry/Desktop/test_DegreeIntoFloat.csv'):
     
      print("Computing FloatIntoDegree")
      fobj_in = open(infile_name, 'r')
      fobj_out = open(outfile_name, 'w')
      time = fobj_in.read(47)
      fobj_out.write(time)
      for line in fobj_in :
           # print(line)
            counter = line.split(',')
            fobj_out.write(counter[0] + " ,")
            fobj_out.write(counter[1] + " , ")
            fobj_out.write(counter[2] + " , ")
            cnt1 = counter[3].split(".")
            cnt11 = counter[4].split(".")
            cnt2 = float(cnt1[0])
            cnt22 = float(cnt11[0])
            cnt3 = cnt1[-1]
            cnt33 = cnt11[-1]
            cnt4 = "0." + cnt3
            cnt44 = "0." + cnt33
            cnt5 = float(cnt4) * 60
            cnt55 = float(cnt44) * 60
            cnt6 = (cnt5 - int(cnt5)) * 60
            cnt66 = (cnt55 - int(cnt55)) * 60
            cnt7 = str(int(cnt5))
            cnt77 = str(int(cnt55))
            cnt8 = str(cnt1[0]) + "°" + str(cnt7) + "'" + str(cnt6) + '"' 
            cnt9 = str(cnt11[0]) + "°" + str(cnt77) + "'" + str(cnt66) + '"'
            fobj_out.write(cnt8 + ", ")
            fobj_out.write(cnt9 + ", ")
            fobj_out.write(counter[5] + ", ")
            fobj_out.write(counter[6] + ", " + "\n")
      fobj_in.close()
      fobj_out.close()

if __name__ == "__main__":
    Float2Degree()
