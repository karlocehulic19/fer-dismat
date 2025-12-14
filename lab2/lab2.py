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

    return [dict(edges), N]


def getCycleOfThree(adjList, size):
    # store each sorted list in a set, return the length of sets
    TARGET_SIZE = 3

    def testConnection(a, b):
        if a in adjList[b] and b in adjList[a]:
            return True
        if a in adjList[b] or b in adjList[a]:
            raise Exception("Invlid graph provided")
        return False

    path = []

    def testPath():
        for i in range(TARGET_SIZE):
            for j in range(i + 1, TARGET_SIZE):
                if not testConnection(path[i], path[j]):
                    return False
        return True

    def dfs(currSize, i):
        count = 0
        if currSize == TARGET_SIZE:
            path.append(i + 1)
            count += testPath()
            path.pop()
            return count

        for j in range(i, size):
            path.append(j + 1)
            count += dfs(currSize + 1, j + 1)
            path.pop()

        return count

    return dfs(0, 0)


if __name__ == "__main__":
    fileName = input()
    edges, n = getEdgesFromFile(fileName)
    result1 = getCycleOfThree(edges, n)
    print(result1)
