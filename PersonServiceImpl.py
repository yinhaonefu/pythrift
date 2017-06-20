# -*- coding:utf-8 -*-
__author__ = '作者'
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from py.thrift.generated import ttypes

class PersonServiceImpl:

    def getPersonByUsername(username):
        return ttypes.Person()