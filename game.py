class Game:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.player1_score = 0
        self.player2_score = 0
        self.round = 0

    def reset(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.round += 1
        self.current_player = 'O' if self.round % 2 == 1 else 'X'

    def handle_click(self, pos):
        if self.winner is not None:
            return
        x, y = pos[0] // 100, pos[1] // 100
        if self.board[y][x] == '':
            self.board[y][x] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                if self.current_player == 'X':
                    self.player1_score += 1
                else:
                    self.player2_score += 1
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Sprawdzenie wygranej (poziomo, pionowo, na skos)
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != '':
            return True
        return False

    def is_board_full(self):
        return all(self.board[y][x] != '' for x in range(3) for y in range(3))
