from collections import defaultdict


def getEdgesFromFile(fileName):
    edges = defaultdict(list)
    with open(fileName, "r") as file:
        N = int(file.readline())
        for i in range(N):
            line = file.readline()
            for j in range(N):
                if line[j] == "1":
                    edges[i + 1].append(j + 1)

    return dict(edges)


def getCycleOfThree(adjList):
    # store each sorted list in a set, return the length of sets
    TARGET_SIZE = 3

    cycles = set()
    done = set()
    path = []

    def dfs(currSize, currElement):
        if currElement in done:
            return

        if currSize == TARGET_SIZE:
            first = path[0]
            if first in adjList[currElement]:
                sortedStringPath = []
                for elem in sorted(path + [currElement]):
                    sortedStringPath.append(str(elem))

                cycles.add(",".join(sortedStringPath))

        path.append(currElement)
        done.add(currElement)
        for nei in adjList[currElement]:
            dfs(currSize + 1, nei)

        path.pop()
        done.remove(currElement)

    for v in adjList:
        dfs(1, v)

    return cycles


if __name__ == "__main__":
    fileName = input()
    edges = getEdgesFromFile(fileName)
    result = getCycleOfThree(edges)
    print(len(result))
