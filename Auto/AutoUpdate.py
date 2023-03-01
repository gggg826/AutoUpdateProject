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
    # 没有外链库的Revert操作
    subprocess.check_call("svn update --accept=theirs-conflict", shell=True)

def updateGit():
    subprocess.check_call("git fetch --all & git reset --hard & git pull", shell=True)

def openUnity():
    subprocess.check_call(UNITY_PATH + ' -quit -projectPath ' + "./Unity ", shell=True)

if __name__ == "__main__":
    UNITY_PATH = getUnityPath()
    for line in open("project.txt"):
        print(line)
        path = line.replace("\n", "")
        os.chdir(path)
        updateSVN()
        updateGit()
        openUnity()