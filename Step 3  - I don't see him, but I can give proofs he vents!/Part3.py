#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:02:35 2020

@author: lucas
"""
import sys
from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.vertices = v
        self.graph = [[0 for column in range(v)] for row in range(v)]
        self.pathlist = defaultdict(list)

    def insertedge(self, u, v, distance):
        u = int(u)
        v = int(v)
        self.graph[u][v] = distance

    def printshortestgraph(self, distance, src):
        # print("Room distance one from an other\n")
        distanceroom = self.pathlist
        for i in range(1, self.vertices):
            for j in range(len(self.pathlist[i])):
                distanceroom[i][j] = NumberToRoom(distanceroom[i][j])
            if i != src:
                print("From ", NumberToRoom(src), " to ", NumberToRoom(i), " - > ", distance[i], end=" ")
                print(distanceroom[i])

    def findmindistance(self, distance, shortesttree):
        minvalue = sys.maxsize
        minindex = 0
        for v in range(self.vertices):
            if distance[v] < minvalue and shortesttree[v] == False:
                minvalue = distance[v]
                minindex = v
        # print(minindex)
        return minindex

    def dijkstra(self, src):
        self.pathlist = defaultdict(list)
        distance = [sys.maxsize] * self.vertices
        distance[src] = 0
        self.pathlist[0].append(src)
        shortesttree = [False] * self.vertices
        for i in range(self.vertices):
            u = self.findmindistance(distance, shortesttree)
            shortesttree[u] = True
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and shortesttree[v] == False and distance[v] > distance[u] + self.graph[u][v]:
                    # print("Changing from  ", v, " : ", distance[v], " --> ", distance[u] + self.graph[u][v])
                    distance[v] = distance[u] + self.graph[u][v]
                    self.pathlist[v] = self.pathlist[u] + [v]
                # else:
                # print("Not changing from  ", v, " : ", distance[v], " --> ", distance[u] + self.graph[u][v])
        print("\n")
        self.printshortestgraph(distance, src)
        #print(distance)
        return distance


# Method to change name of rooms to int and int to rooms names
def RoomToNumber(room):
    """Return a room name corresponding to its number"""
    if room == 'Reactor':
        return 0
    elif room == 'Lower E':
        return 1
    elif room == 'Upper E':
        return 2
    elif room == 'Security':
        return 3
    elif room == 'Electrical':
        return 4
    elif room == 'Medbay':
        return 5
    elif room == 'Storage':
        return 6
    elif room == 'NoName South':
        return 7
    elif room == 'NoName Middle':
        return 8
    elif room == 'Cafeteria':
        return 9
    elif room == 'Shield':
        return 10
    elif room == 'O2':
        return 11
    elif room == 'Hall Est':
        return 12
    elif room == 'Navigations':
        return 13
    elif room == 'Weapons':
        return 14


def NumberToRoom(number):
    """Return a number corresponding to its room name"""
    if number == 0:
        return 'Reactor'
    elif number == 1:
        return 'Lower E'
    elif number == 2:
        return 'Upper E'
    elif number == 3:
        return 'Security'
    elif number == 4:
        return 'Electrical'
    elif number == 5:
        return 'Medbay'
    elif number == 6:
        return 'Storage'
    elif number == 7:
        return 'NoName South'
    elif number == 8:
        return 'NoName Middle'
    elif number == 9:
        return 'Cafeteria'
    elif number == 10:
        return 'Shield'
    elif number == 11:
        return 'O2'
    elif number == 12:
        return 'Hall Est'
    elif number == 13:
        return 'Navigations'
    elif number == 14:
        return 'Weapons'


# Creation of the graph

grcrewmate = Graph(15)

grimpostor = Graph(15)


# Method to print and write the result in a file


def read(filename):
    """Read the file and add the graph to """
    typegr = grcrewmate
    if filename == "GraphImpostor.txt":  # If the filename is the one of the Impostor change type of graog
        typegr = grimpostor
    with open(filename) as f:
        for li in f:
            line = (li.strip().split("\t"))
            # print("Adding",RoomToNumber(line[0]),"to",RoomToNumber(line[1]),"distance : ",line[2])
            typegr.insertedge(RoomToNumber(line[0]), RoomToNumber(line[1]), float(line[2]))
            typegr.insertedge(RoomToNumber(line[1]), RoomToNumber(line[0]), float(line[2]))


def writeres():
    alldistancecrew = []
    alldistanceimp = []
    original_stdout = sys.stdout
    with open('TravelDistances.txt', 'w') as f:
        sys.stdout = f
        print("\n\nCrewmate time to travel : ")
        read('GraphCrewmate.txt')
        for i in range(grcrewmate.vertices):
            print("\n From the room ", NumberToRoom(i))
            a = grcrewmate.dijkstra(i)
            alldistancecrew.append(a)
        print("\n\nImpostor time to travel : ")
        read('GraphImpostor.txt')
        for i in range(grimpostor.vertices):
            print("\n From the room ", NumberToRoom(i))
            b = grimpostor.dijkstra(i)
            alldistanceimp.append(b)
        print("\n\nDifference time to travel : ")
        for i in range(len(alldistanceimp)):
            print("\n From the room ", NumberToRoom(i))
            for j in range(len(alldistancecrew)):
                calculate = abs(int(alldistanceimp[i][j]) - int(alldistancecrew[i][j]))
                print(NumberToRoom(i), " to ", NumberToRoom(j), "- >", calculate)
        sys.stdout = original_stdout


if __name__ == "__main__":
    writeres()
