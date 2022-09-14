from email.mime import application
from genericpath import exists
from mimetypes import common_types
from testee import MakeFile
import os
import subprocess
import json
import inspect
import importlib
import shutil
from distutils.dir_util import copy_tree
import argparse

# geting config
with open("project_config.json", "rb") as fp:
    data = json.loads(fp.read())
print("-------------project_setting_up---------------")
project_path = data["project_path"]
projectname = data["projectname"]
os.makedirs(f"{project_path}{projectname}", exist_ok=True)
os.chdir(f"{project_path}{projectname}")
print("-------------creating_adaptors---------------")
parser = argparse.ArgumentParser()
parser.add_argument(
    "-P",
    "--ProjectPath",
    help="Project Path where you want your project folder",
    type=str,
    default=".",
)
parser.add_argument(
    "-N", "--ProjectName", help="Project name", type=str, default="testproject"
)
parser.add_argument("-V", "--Version", help="Project version", type=float, default=1.0)
parser.add_argument(
    "-D",
    "--Deployment",
    help="Deployment config ex.type,satic_server",
    type=dict,
    default={},
)
parser.add_argument(
    "-R",
    "--Requirenments",
    help="Requirenments list ex.['pytest','flask']",
    type=list,
    default=[],
)
parser.add_argument(
    "-PD", "--ProjectDetails", help="Project Details Like", type=dict, default={}
)
parser.add_argument(
    "-CU", "--CommonUtilities", help="Common Utilities", type=dict, default={}
)
parser.add_argument("-U", "--Utilities", help="Utilities", type=list, default=[])
adaptors = os.listdir("/Users/apple/ed/baseproject/adaptors/")
adaptors = data.get("projectdetails")
applications=adaptors.get('default_applications')
common_utilities=adaptors.get('common_utilities')
adaptors = adaptors.get("adaptors")


def generate_adaptors(**kwargs):
    """_summary_
    """
    os.makedirs("adaptors")
    data = copy_tree(
        "/Users/apple/ed/baseproject/adaptors", "/Users/apple/testproject/adaptors/"
    )
    fr = kwargs.get("adaptors")
    data = os.listdir("adaptors")
    for i in data:
        if i not in fr:
            os.chdir("adaptors")
            if i != "__init__.py":
                shutil.rmtree(i)
            os.chdir("../")
    return True, "adaptors created"


def generate_application(**kwargs):
    """_summary_
    """
    os.makedirs("infrastructure",exist_ok=True)
    os.makedirs("modules",exist_ok=True)
    os.makedirs('common_utilities',exist_ok=True)
    os.makedirs('tests',exist_ok=True)
    copy_tree(
        "/Users/apple/ed/baseproject/infrastructure", "/Users/apple/testproject/infrastructure/"
    )
    copy_tree(
        "/Users/apple/ed/baseproject/modules", "/Users/apple/testproject/modules/"
    )
    copy_tree(
        "/Users/apple/ed/baseproject/common_utilities", "/Users/apple/testproject/common_utilities/"
    )
    copy_tree(
        "/Users/apple/ed/baseproject/tests", "/Users/apple/testproject/tests/"
    )
    os.chdir('modules')
    fs=os.listdir('/Users/apple/testproject/modules')
    fs.remove('__init__.py')
    for i in fs:
        if i not in kwargs['modules']:
            shutil.rmtree(f'/Users/apple/testproject/modules/{i}')     
    return True


def generate_tests(**kwargs):
    """_summary_
    """

    pass


def generate_docker_config(**kwargs):
    """_summary_
    """
    print(os.getcwd())
    with open('Dockerfile','w+') as fs:
        fs.write('test')
        fs.close()
    with open('docker-compose.yml','w+') as ft:
        ft.write('teste')
        ft.close()

    with open('setup.py','w+') as ft:
        ft.write('teste')
        ft.close()
    return True,'Created'


def generate_pytest_config(**kwargs):
    """_summary_
    """
    os.chdir('../')
    with open('pytest.ini','w+') as frt:
        frt.write(kwargs['pytest'])
        frt.close()
    return True,"Generated"


def setup_web_server(**kwargs):
    """_summary_
    """
    pass


def generate_deployment_config(**kwargs):
    """_summary_
    """
    os.makedirs('config',exist_ok=True)
    os.makedirs('deployment',exist_ok=True)
    return True,"Generated"


def generate_microservices(**kwargs):
    """_summary_
    """

    return

def create_project(**kwargs):
    generate_adaptors(adaptors=adaptors)
    generate_application(modules=data['projectdetails']['default_applications'])
    generate_tests()
    generate_pytest_config(pytest="ce")
    generate_docker_config()

    generate_deployment_config()
    return f"project created {projectname}"


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
