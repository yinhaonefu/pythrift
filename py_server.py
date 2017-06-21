# -*- coding:utf-8 -*-
__author__ = '作者'

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
from py.thrift.generated import PersonService
from PersonServiceImpl import PersonServiceImpl

try:
    personServiceHandler = PersonServiceImpl()
    processor = PersonService.Processor(personServiceHandler)

    serverSocket = TSocket.TServerSocket(port=8899)
    transportFactory = TTransport.TFramedTransportFactory()
    protocolFactoty = TCompactProtocol.TCompactProtocolFactory()

    server = TServer.TSimpleServer(processor, serverSocket, transportFactory, protocolFactoty)
    server.serve()

except Thrift.TException, ex:
    print '%s' % ex.message