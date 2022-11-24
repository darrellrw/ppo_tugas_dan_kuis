from tabulate import tabulate

class Dijkstra:
    def __init__(self, start, end):
        self.node = ["A", "B", "C", "D", "E"]

        self.graph = {
            "A" : {"B" : 3},
            "B" : {"D" : 5, "E" : 1},
            "C" : {"A" : 1, "B" : 7, "D" : 2},
            "D" : {"E" : 7},
            "E" : {}
        }

        self.distance = {}
        self.point = {}

        self.start = start
        self.end = end

        for point in self.graph:
            self.distance[point] = 99
            self.point[point] = {}
        self.distance[self.start] = 0

        self.notVisited = [node for node in self.distance]
    
    def shortestRoute(self, distance, notVisited):
        fartestPoint = 99
        shortestPoint = ""

        for self.point in distance:
            if(self.point in notVisited and distance[self.point] <= fartestPoint):
                fartestPoint = distance[self.point]
                shortestPoint = self.point
        
        return shortestPoint

    def shortest(self):
        while self.notVisited:
            kjkk = self.shortestRoute(self.distance, self.notVisited)
            dist = self.distance[kjkk]
            dd = self.graph[kjkk]
            for test in dd:
                print(kjkk)
                print(test)
                if(self.distance[test] > dist + dd[test]):
                    self.distance[test] = dist + dd[test]
                    self.point[test] = str(kjkk)
            self.notVisited.pop(self.notVisited.index(kjkk))

        route = [self.end]

        i = 0
        while(self.start not in route):
            route.append(self.point[route[i]])
            i += 1

pp = Dijkstra("C", "E")
pp.shortest()