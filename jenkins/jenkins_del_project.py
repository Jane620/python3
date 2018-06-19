# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午12:28
# @Author  : Jane
# @Site    : 
# @File    : jenkins_del_project.py
# @Software: PyCharm

import os,logging,shutil
from jenkins import Jenkins

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)

def get_jenkins_instance():
    jenkins_url = 'http://ci.yst.com.cn'
    jenkins_username = 'jfwang001'
    jenkins_passwd = '123456'
    return Jenkins(jenkins_url,username=jenkins_username,password=jenkins_passwd)

def clean_workspace():
    jenkins_instance = get_jenkins_instance()

    jenkins_workspace_path = ''