#!/usr/bin/env python3

import urllib.request
import time
import os
import anki_vector
from anki_vector.util import degrees, Angle, Pose
from anki_vector.events import Events

try:
#    change to your Vectors IP address
    os.system("ssh -M -S Vector_console -fNT -L 8889:localhost:8889 root@192.168.0.74")
except:
    pass

n = 0
wait = 1

def Angry_Eyes():
    console_var1 = urllib.request.urlopen('http://localhost:8889/consolevarset?key=ProcFace_Display&value=4&key=Left_UpperLidY&value=0.5&key=Left_UpperLidAngle&value=33&key=Left_LowerLidAngle&value=40&key=ProcFace_Hue&value=1&key=ProcFace_Saturation&value=1&key=ProcFace_EyeLightnessMultiplier&value=1&key=ProcFace_AntiAliasingSize&value=3&key=ProcFace_HotspotFalloff&value=0.48')
    
def Default_Eyes():
    console_var2 = urllib.request.urlopen('http://localhost:8889/consolevarset?key=KeepAliveEyeDart_MaxDistFromCenter_pix&value=15&key=Left_EyeScaleX&value=1&key=Left_EyeScaleY&value=1&key=Left_LowerInnerRadiusX&value=0&key=Left_LowerInnerRadiusY&value=0&key=Left_UpperOuterRadiusX&value=0&key=Left_UpperOuterRadiusY&value=0&key=ProcFace_Display&value=4&key=Left_UpperLidY&value=0&key=Left_UpperLidAngle&value=0&key=Left_LowerLidAngle&value=0&key=ProcFace_Hue&value=0&key=ProcFace_Saturation&value=0&key=ProcFace_EyeLightnessMultiplier&value=1&key=ProcFace_AntiAliasingSize&value=3&key=ProcFace_HotspotFalloff&value=0.48')

def Feline_Eyes():
    console_var2 = urllib.request.urlopen('http://localhost:8889/consolevarset?key=KeepAliveEyeDart_MaxDistFromCenter_pix&value=10&key=Left_EyeScaleX&value=1.35&key=Left_EyeScaleY&value=1&key=Left_LowerInnerRadiusX&value=0.01&key=Left_LowerInnerRadiusY&value=0.01&key=Left_UpperOuterRadiusX&value=0.01&key=Left_UpperOuterRadiusY&value=0.01&key=ProcFace_Display&value=4&key=Left_UpperLidY&value=0&key=Left_UpperLidAngle&value=10.5&key=Left_LowerLidAngle&value=0&key=ProcFace_Hue&value=0.9&key=ProcFace_Saturation&value=1&key=ProcFace_EyeLightnessMultiplier&value=1.6&key=ProcFace_AntiAliasingSize&value=10&key=ProcFace_HotspotFalloff&value=0.9')
    
def Crazy_Eyes():
    console_var2 = urllib.request.urlopen('http://localhost:8889/consolevarset?key=ProcFace_Display&value=4&key=Left_UpperLidY&value=.75&key=Left_UpperLidAngle&value=10&key=Left_LowerLidAngle&value=10&key=ProcFace_Hue&value=0.3&key=ProcFace_Saturation&value=0.5&key=ProcFace_EyeLightnessMultiplier&value=1&key=ProcFace_AntiAliasingSize&value=3&key=ProcFace_HotspotFalloff&value=0.48')
    
def Cartoon_Eyes():
    console_var2 = urllib.request.urlopen('http://localhost:8889/consolevarset?key=KeepAliveEyeDart_MaxDistFromCenter_pix&value=15&key=Left_EyeScaleX&value=1&key=Left_EyeScaleY&value=1&key=Left_LowerInnerRadiusX&value=0&key=Left_LowerInnerRadiusY&value=0&key=Left_UpperOuterRadiusX&value=0&key=Left_UpperOuterRadiusY&value=0&key=ProcFace_Display&value=4&key=Left_UpperLidY&value=0.16&key=Left_UpperLidAngle&value=-2&key=Left_LowerLidAngle&value=0&key=ProcFace_Hue&value=0&key=ProcFace_Saturation&value=0&key=ProcFace_EyeLightnessMultiplier&value=1.11&key=ProcFace_AntiAliasingSize&value=3&key=ProcFace_HotspotFalloff&value=0.48')
    
def cycle(n):
    while True:
        if robot.touch.last_sensor_reading.is_being_touched:
            if n == 0:
                Cartoon_Eyes()
                print("Cartoon Eyes")
                n = n+1
                time.sleep(wait)
                cycle(n)
            
            if n == 1:
                Default_Eyes()
                print("Default Eyes")
                n = n+1 
                time.sleep(wait)
                cycle(n)
                
            if n == 2:
                Feline_Eyes()
                print("Feline Eyes")
                n = n+1
                time.sleep(wait)
                cycle(n)
                
            if n == 3:
                Crazy_Eyes()
                print("Crazy Eyes")
                n = n+1
                time.sleep(wait)
                cycle(n)
                
            if n == 4:
                Angry_Eyes()
                print("Devil Eyes")
                n = 0
                time.sleep(wait)
                cycle(n)
                
#                Enter your Vectors serial number below (or leave blank if you only have one Vector)
with anki_vector.Robot('0050169f', behavior_control_level=None) as robot:
    cycle(n)