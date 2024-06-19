import pygame

def draw_board(screen, game):
    screen.fill((255, 255, 255))
    for y in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (0, y * 100), (300, y * 100), 5)
    for x in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (x * 100, 0), (x * 100, 300), 5)

    font = pygame.font.Font(None, 74)
    for y in range(3):
        for x in range(3):
            if game.board[y][x] != '':
                text = font.render(game.board[y][x], True, (0, 0, 0))
                screen.blit(text, (x * 100 + 25, y * 100 + 10))

def draw_restart_button(screen):
    font = pygame.font.Font(None, 36)
    text = font.render('Restart', True, (255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (100, 320, 100, 50))
    screen.blit(text, (110, 330))

def draw_winning_line(screen, winner_info):
    if winner_info is None:
        return
    start_pos, end_pos = winner_info
    pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 5)

def display_scores(screen, game):
    font = pygame.font.Font(None, 24)
    score_text = f"Player 1 (X): {game.player1_score}  Player 2 (O): {game.player2_score}"
    text = font.render(score_text, True, (0, 0, 0))
    screen.blit(text, (10, 380))

def display_current_player(screen, game):
    font = pygame.font.Font(None, 36)
    player_text = f"Current Player: {game.current_player}"
    text = font.render(player_text, True, (0, 0, 0))
    screen.blit(text, (10, 420))
