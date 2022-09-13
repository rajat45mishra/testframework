from genericpath import exists
from testee import MakeFile
import os
import subprocess
import json


import argparse

# geting config
with open('project_config.json','rb') as fp:
    data=json.loads(fp.read())
print('-------------project_setting_up---------------')
project_path=data['project_path']
projectname=data['projectname']
os.makedirs(f'{project_path}{projectname}',exist_ok=True)
os.chdir(f'{project_path}{projectname}')
os.makedirs('adaptors',exist_ok=True)
os.makedirs('modules',exist_ok=True)
os.makedirs('common_utilities',exist_ok=True)
os.makedirs('infrastructure',exist_ok=True)
os.makedirs('tests',exist_ok=True)
print('-------------creating_adaptors---------------')
parser = argparse.ArgumentParser()
parser.add_argument("-P", "--ProjectPath", help="Project Path where you want your project folder", type=str, default=".")
parser.add_argument("-N", "--ProjectName", help="Project name", type=str, default="testproject")
parser.add_argument("-V", "--Version", help="Project version", type=float, default=1.0)
parser.add_argument("-D", "--Deployment", help="Deployment config ex.type,satic_server", type=dict, default={})
parser.add_argument("-R", "--Requirenments", help="Requirenments list ex.['pytest','flask']", type=list, default=[])
parser.add_argument("-PD", "--ProjectDetails", help="Project Details Like", type=dict, default={})
parser.add_argument("-CU", "--CommonUtilities", help="Common Utilities", type=dict, default={})
parser.add_argument("-U", "--Utilities", help="Utilities", type=list, default=[])
os.chdir('adaptors')
adaptors=os.listdir('/Users/apple/ed/baseproject/adaptors/')
adaptors=adaptors[0:]
import inspect
import importlib
def generate_adaptors(**kwargs):
    """_summary_
    """
    return True
def generate_application(**kwargs):
    """_summary_
    """
    pass
def generate_tests(**kwargs):
    """_summary_
    """
    pass
def generate_docker_config(**kwargs):
    """_summary_
    """
    pass
def generate_pytest_config(**kwargs):
    """_summary_
    """
    pass

def setup_web_server(**kwargs):
    """_summary_
    """
    pass

def generate_deployment_config(**kwargs):
    """_summary_
    """
    pass

# import inspect
# import importlib
# final={}
# filepath=''
# listf=[]
# for i in adaptors:
#     path='adaptors.'
#     if i!='__pycache__':
#         base=f'{path}{i}'
#     if i!='__init__.py':
#         file_list=os.listdir('/Users/apple/ed/baseproject/adaptors/'+i)
#     else:
#         file_list=[]
#     filepath=f'{path}.{i}'.replace('.','/')
#     filepath='/Users/apple/ed/baseproject'+filepath
#     listf.append(filepath)
#     for ii in file_list:
#         os.chdir('/Users/apple/ed/baseproject/adaptors/')
#         ff=ii.replace('.py','')
#         if not ff.startswith('__init__'):
#             module=importlib.__import__(f'baseproject.{base}.{ff}')
#             code=inspect.getsource(module)
#             final[ii]=code

# from .testee import MakeFile
# for c in listf:
#     for k,v in final.items():
#         MakeFile(k,v,c)