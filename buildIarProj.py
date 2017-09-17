import os
import sys

iar_path = "C:\Program Files (x86)\IAR Systems\Embedded Workbench 8.0\common\bin"
sys.path.append(iar_path)

def clean(target_filename, mode):
    if mode != r'Release':
        mode = "Debug"
    iar_bulid_param = "-clean %s -log all" %mode
    iar_command = "IarBuild %s %s" % (target_filename, iar_bulid_param)
    print(iar_command)
    os.system(iar_command)

def make(target_filename, mode):
    if mode != r'Release':
        mode = "Debug"
    iar_bulid_param = "-make %s -log all" %mode
    iar_command = "IarBuild %s %s" % (target_filename, iar_bulid_param)
    print(iar_command)
    os.system(iar_command)

def build(target_filename, mode):
    if mode != r'Release':
        mode = "Debug"
    iar_bulid_param = "-build %s -log all" %mode
    iar_command = "IarBuild %s %s" % (target_filename, iar_bulid_param)
    print(iar_command)
    os.system(iar_command)