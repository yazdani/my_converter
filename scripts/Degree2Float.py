#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import rospy
from std_msgs.msg import String

def Degree2Float(infile_name='/home/noentry/Desktop/test_DegreeIntoFloat.csv', outfile_name='/home/noentry/Desktop/test_FloatIntoDegree.csv'):

      print("Computing DegreeIntoFloat")
      fobj_in = open(infile_name, 'r')
      fobj_out = open(outfile_name, 'w')
      time = fobj_in.read(47)
      fobj_out.write(time)
      for line in fobj_in :
            counter = line.split(',')
            fobj_out.write(counter[0] + " ,")
            fobj_out.write(counter[1] + " ,")
            fobj_out.write(counter[2] + " ,")
            cnt1 = counter[3].split("°")
            cnt11 = counter[4].split("°")
            cnt2 = float(cnt1[0]) # erste ziffer
            # print cnt2
            cnt22 = float(cnt11[0]) # zweite ziffer
            # print cnt22
            # print "hso"
            cnt3 = cnt1[1].split("'") # letzter wertz
            cnt33 = cnt11[1].split("'") # letzter wert
            cnt5 = float(cnt3[0]) # vorletzer #
            cnt55 = float(cnt33[0]) #virletzer
            # print "mido"
            cnt4 = cnt3[1].split('"')
            # print cnt4[0]
            cnt44 = cnt33[1].split('"')
            # print "haha"
            # print counter[5]
            cnt6 = (((float(cnt4[0]) / 60) + cnt5) / 60) + cnt2 #zweite ziffer
            cnt66 = (((float(cnt44[0]) / 60) + cnt55) / 60) + cnt22 # zweite ziffer
            # print "mama"     
            fobj_out.write(str(cnt6) + ", ")
            fobj_out.write(str(cnt66) + ", ")
            fobj_out.write(counter[5] + ", ")
            fobj_out.write(counter[6] + ", " + "\n")
      fobj_in.close()
      fobj_out.close()

if __name__ == "__main__":
    Degree2Float()
