from collections import defaultdict


def getEdgesFromFile(fileName):
    edges = defaultdict(list)
    N = 0
    with open(fileName, "r") as file:
        N = int(file.readline())
        for i in range(N):
            line = file.readline()
            for j in range(N):
                if line[j] == "1":
                    edges[i + 1].append(j + 1)

    return [edges, N]


def getCyclesNumer(targetSize, adjList, size):
    def testConnection(a, b):
        if a in adjList[b] and b in adjList[a]:
            return True
        if a in adjList[b] or b in adjList[a]:
            raise Exception("Invlid graph provided")
        return False

    path = []

    def dfs(i):
        if len(path) > 1 and not testConnection(path[-2], path[-1]):
            return 0
        if len(path) == targetSize:
            return testConnection(path[0], path[-1])

        count = 0

        for j in range(i, size):
            path.append(j + 1)
            count += dfs(j + 1)
            path.pop()

        return count

    return dfs(0)


if __name__ == "__main__":
    fileName = input("Unesite ime datoteke s podacima o grafu: ")
    edges, n = getEdgesFromFile(fileName)
    CYCLE_LENGTH = 3
    result1 = getCyclesNumer(CYCLE_LENGTH, edges, n)
    print("Rjesenje:", result1)
