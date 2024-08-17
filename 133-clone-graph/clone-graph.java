/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {

        if (node == null) {
            return null;
        }

        // hashmap of form <original node : copy node> to keep track of already copied nodes
        Map<Node, Node> clones = new HashMap<>();

        // add head node to list
        clones.put(node, new Node(node.val));

        // queue to hold next level
        Queue<Node> next = new LinkedList<>();
        next.add(node);

        // bfs traversal
        while (!next.isEmpty()) {
            Node curr = next.remove();

            for (Node neighbor : curr.neighbors) {

                // if neighbor not in map yet, put in map
                if (!clones.containsKey(neighbor)) {
                    clones.put(neighbor, new Node(neighbor.val));

                    // enqueue neighbor
                    next.add(neighbor);
                }

                // add clone of neighbor to neighbor list for clone of curr
                clones.get(curr).neighbors.add(clones.get(neighbor));
            }
        }

        // return head node
        return clones.get(node);
    }
}