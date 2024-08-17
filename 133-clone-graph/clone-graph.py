"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if node == None:
            return None

        # map to keep track of cloned nodes
        clones = dict()

        # copy input node
        clones[node] = Node(node.val)

        # queue to hold next nodes to visit
        queue = list()
        queue.append(node)

        # bfs traversal
        while len(queue) > 0:

            # get next node to visit
            curr = queue.pop(0)

            # process neighbors of curr
            for neighbor in curr.neighbors:

                # if neighbor not cloned/visited yet -> clone, add to map, add to queue to visit later
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # add clone of neighbor to neighbor list of clone of curr
                clones[curr].neighbors.append(clones[neighbor])
        
        return clones[node]
                
