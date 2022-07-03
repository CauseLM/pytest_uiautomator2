# _*_ coding：utf-8 _*_


import os

"""
project dir and path
"""
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(ROOT_DIR, "Output\\log\\")
IMAGE_DIR = os.path.join(ROOT_DIR, "Output\\image\\")
CONFIG_DIR = os.path.join(ROOT_DIR, "Config")
CONFIG_PATH = os.path.join(CONFIG_DIR, "desired_caps.yml")
