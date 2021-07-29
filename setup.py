import os
import shutil
from distutils.dir_util import copy_tree

from setuptools import find_packages, setup

# global variables
package_name = 'rfsoc_freqplan'
pip_name = 'rfsoc-freqplan'
data_files = ['info.html']

# heroku setup
if os.path.isfile('Procfile'):
    # heroku variables
    requirements = ['numpy>=1.19.0','ipywidgets>=7.5.1','plotly>=4.12.0','ipykernel>=5.3.0','voila>=0.2.6']

# Pynq setup
else:
    # pynq variables
    requirements = ['pynq>=2.6']
    board = os.environ['BOARD']
    repo_board_folder = f'boards/{board}/{package_name}'
    board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
    board_project_dir = os.path.join(board_notebooks_dir, 'frequency-planner')
    
    # check whether board is supported
    def check_env():
        if not os.path.isdir(repo_board_folder):
            raise ValueError("Board {} is not supported.".format(board))
        if not os.path.isdir(board_notebooks_dir):
            raise ValueError(
                "Directory {} does not exist.".format(board_notebooks_dir))
            
    # check if the path already exists, delete if so
    def check_path():
        if os.path.exists(board_project_dir):
            shutil.rmtree(board_project_dir)
    
    # copy notebooks to jupyter home
    def copy_notebooks():
        src_nb_dir = os.path.join(repo_board_folder, 'notebooks')
        dst_nb_dir = os.path.join(board_project_dir)
        copy_tree(src_nb_dir, dst_nb_dir)
        
    check_env()
    check_path()
    copy_notebooks()

setup(
    name=package_name,
    version='0.1.1',
    url='https://github.com/strath-sdr/rfsoc_frequency_planner',
    license='BSD 3-Clause License',
    author="Joshua Goldsmith",
    author_email="joshua.goldsmith@strath.ac.uk",
    packages=find_packages(),
    package_data={
        '': data_files,
    },
    description="RFSoC Frequency Planner.")
