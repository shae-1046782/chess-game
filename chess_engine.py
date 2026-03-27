"""
Engine file.
Responsible for:
- storing current game state information
- determining valid moves
- keeping move log
"""


class GameState():
    def __init__(self):
        self.board: list[list[str]] = [
            ["black_rook", "black_knight", "black_bishop", "black_queen",
                "black_king", "black_bishop", "black_knight", "black_rook"],
            ["black_pawn", "black_pawn", "black_pawn", "black_pawn",
             "black_pawn", "black_pawn", "black_pawn", "black_pawn"],
            ["", "", "", "", "", "", "", "",],
            ["", "", "", "", "", "", "", "",],
            ["", "", "", "", "", "", "", "",],
            ["", "", "", "", "", "", "", "",],
            ["white_pawn", "white_pawn", "white_pawn", "white_pawn",
             "white_pawn", "white_pawn", "white_pawn", "white_pawn"],
            ["white_rook", "white_knight", "white_bishop", "white_queen",
                "white_king", "white_bishop", "white_knight", "white_rook"]
        ]
