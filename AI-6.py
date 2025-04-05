class GameTree:
    def __init__(self):
        # Sample game tree with leaf values
        self.tree = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': [3, 5],
            'E': [6, 1],
            'F': [2, 4],
            'G': [5, 3]
        }

def alpha_beta(node, depth, alpha, beta, maximizing_player, game_tree):
    # Base case: if leaf node (terminal state)
    if isinstance(game_tree.tree[node], list) and all(isinstance(x, int) for x in game_tree.tree[node]):
        return game_tree.tree[node][0] if depth % 2 == 0 else game_tree.tree[node][1]
    
    if maximizing_player:
        value = float('-inf')
        for child in game_tree.tree[node]:
            value = max(value, alpha_beta(child, depth + 1, alpha, beta, False, game_tree))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Beta pruning
        return value
    else:
        value = float('inf')
        for child in game_tree.tree[node]:
            value = min(value, alpha_beta(child, depth + 1, alpha, beta, True, game_tree))
            beta = min(beta, value)
            if alpha >= beta:
                break  # Alpha pruning
        return value

# Main execution
if __name__ == "__main__":
    game = GameTree()
    # Start at root 'A', depth 0, initial alpha and beta values
    result = alpha_beta('A', 0, float('-inf'), float('inf'), True, game)
    print(f"The optimal value is: {result}")