#!/usr/bin/python
# -*- coding:utf-8 -*-import os

import os
import subprocess

UNITY_PATH = ""

def getUnityPath():
    f = open("unityPath.txt")
    r = f.read()
    f.close()
    return r

def updateSVN():
    subprocess.check_call("svn update", shell=True)

def updateGit():
    subprocess.check_call("git pull", shell=True)

def openUnity():
    subprocess.check_call(UNITY_PATH + ' -projectPath ' + " ./Unity", shell=True)

if __name__ == "__main__":
    UNITY_PATH = getUnityPath()
    for line in open("project.txt"):
        print(line)
        os.chdir(line)
        updateSVN()
        updateGit()
        openUnity()