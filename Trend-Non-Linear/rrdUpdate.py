import time
import logging
import rrdtool

from getSNMP import *

logging.basicConfig( level=logging.DEBUG,
    format='[%(levelname)s] - %(threadName)-10s : %(message)s')

init_time = 0

def graph(database_name, num_graphs, labels_name):
    for i in range(num_graphs):
        ret = rrdtool.graph("IMG/" + database_name + str(i+1) + ".png",
                                "--start", str(init_time - 100),
                                "--end", str(rrdtool.last("RRD/" + database_name + '.rrd') + 300),
                                "--vertical-label=" + labels_name[0],
                                "DEF:obs=" + "RRD/" + database_name + ".rrd:VALUES" + str(i+1) + ":AVERAGE",
                                "DEF:pred=" + "RRD/" + database_name + ".rrd:VALUES" + str(i+1) + ":HWPREDICT",
                                "DEF:dev=" + "RRD/" + database_name + ".rrd:VALUES" + str(i+1) + ":DEVPREDICT",
                                "DEF:fail=" + "RRD/" + database_name + ".rrd:VALUES" + str(i+1) + ":FAILURES",
                                "CDEF:scaledobs=obs,8,*",
                                "CDEF:upper=pred,dev,2,*,+",
                                "CDEF:lower=pred,dev,2,*,-",
                                "CDEF:scaledupper=upper,8,*",
                                "CDEF:scaledlower=lower,8,*",
                                "TICK:fail#FDD017:1.0: Failures",
                                "LINE1:scaledobs#00FF00:" + labels_name[1],
                                "CDEF:scaledpred=pred,8,*",                   
                                "LINE2:scaledpred#ee0099:Forecast",
                                "LINE1:scaledupper#FF000E:Upper Bound",
                                "LINE1:scaledlower#0012FF:Lower Bound")


def updateDirectGetDatabase(database_name, comunity_name, agent_ip, port, oid):
    variable_read = 0
    init_time = rrdtool.last("RRD/" + database_name + str(".rrd"))

    labels = input("Inserte el tipo de variable y el nombre: ").split(',')
    print(labels)

    if len(labels) == 2:
        while 1:
            variable_read = int(consultaSNMP(comunity_name, agent_ip, port, oid))
            value = "N:" + str(variable_read)
            logging.debug(value)
            ret = rrdtool.update("RRD/" + database_name + str(".rrd"), value)
            rrdtool.dump("RRD/" + database_name + str(".rrd"), "XML/" + database_name + str(".xml"))

            time.sleep(1)
            graph(database_name, 1, labels)


def updateDirectWalkDatabase(database_name, comunity_name, agent_ip, port, oid):
    variable_read = []
    init_time = rrdtool.last("RRD/" + database_name + str(".rrd"))
    
    labels = input("Inserte el tipo de variable y el nombre: ").split(',')
    print(labels)

    if len(labels) == 2:
        while 1:
            variable_read = consultaWALKSNMP(comunity_name, agent_ip, port, oid)
            value = "N"

            for variable in variable_read:
                value = value + ":" + str(variable)

            logging.debug(value)
            ret = rrdtool.update("RRD/" + database_name + str(".rrd"), value)
            rrdtool.dump("RRD/" + database_name + str(".rrd"), "XML/" + database_name + str(".xml"))

            time.sleep(1)
            graph(database_name, len(variable_read), labels)

def updatePercentageGetDatabase(database_name, comunity_name, agent_ip, port, oid_top, oid_variable):
    variable_read = 0
    init_time = rrdtool.last("RRD/" + database_name + str(".rrd"))

    variable_top =  int(consultaSNMP(comunity_name, agent_ip, port, oid_top))

    labels = input("Inserte el tipo de variable y el nombre: ").split(',')
    print(labels)

    if len(labels) == 2:
        while 1:
            variable_read = int(consultaSNMP(comunity_name, agent_ip, port, oid_variable))
            value = "N:" + str((variable*100)/variable_top)
            
            logging.debug(value)
            ret = rrdtool.update("RRD/" + database_name + str(".rrd"), value)
            rrdtool.dump("RRD/" + database_name + str(".rrd"), "XML/" + database_name + str(".xml"))

            time.sleep(1)
            graph(database_name, 1, labels)
'''
def updateWALKSVDatabase(database_name, comunity_name, agent_ip, oid):
    variable_read = 0

    init_time = rrdtool.last(database_name + str(".rrd"))

    while 1:
        variable_read = int(consultaSNMP(comunity_name, agent_ip, oid))
        value = "N:" + str(variable_read)
        print(value)
        ret = rrdtool.update(database_name + str(".rrd"), value)
        rrdtool.dump(database_name + str(".rrd"), database_name + str(".xml"))
        time.sleep(1)


    if ret:
        print print(rrdtool.error())
        time.sleep(300)


def updateGETMVDatabase(database_name, comunity_name, agent_ip, oid1, oid2):
    variable1_read = 0
    variable2_read = 0

    init_time = rrdtool.last(database_name + str(".rrd"))
    variable1_read = consultaWALKSNMP(comunity_name, agent_ip, oid1)

    while 1:
        variable2_read = consultaWALKSNMP(comunity_name, agent_ip, oid2)

        for i in range(len(consulta1)):
                valor = "N:" + str((consulta2[i]*100)/consulta1[i])
                print(valor)



        variable_read = int(consultaSNMP(comunity_name, agent_ip, oid))
        value = "N:" + str(variable_read)
        print(value)
        ret = rrdtool.update(database_name + str(".rrd"), value)
        rrdtool.dump(database_name + str(".rrd"), database_name + str(".xml"))
        time.sleep(1)


    if ret:
        print print(rrdtool.error())
        time.sleep(300)
'''