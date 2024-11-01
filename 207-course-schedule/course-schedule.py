from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build graph
        edge_map = {i : [] for i in range(numCourses)}
        for prereq in prerequisites:
            req = prereq[1]
            target = prereq[0]
            edge_map[req].append(target)

        # 0: white (unseen), 1: grey (visitng), 2: black (visited)
        colors = [0] * numCourses

        # do dfs from a node
        def dfs(node):
            colors[node] = 1 # set node to grey
            for child in edge_map[node]: # visit each child of the node
                if colors[child] == 1: # if the child is grey, return False
                    return False
                elif colors[child] != 2: # if node is not black, recurse on it
                    ret = dfs(child)
                    if ret == False: # if a cycle was found in a child, return False
                        return False
            colors[node] = 2 # set current node to black
            return True
                
        
        # do DFS to find cycles
        for course in range(numCourses):
            if colors[course] != 2:
                if not dfs(course):
                    return False
                    
        return True

        
        