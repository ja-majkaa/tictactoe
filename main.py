import pygame
from game import Game
from draw import draw_board, draw_restart_button, draw_winning_line, display_scores, display_current_player

# Główna funkcja programu
def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 460))
    pygame.display.set_caption('Kółko i Krzyżyk')

    game = Game()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.winner is not None:
                    if 100 <= event.pos[0] <= 200 and 320 <= event.pos[1] <= 370:
                        game.reset()
                else:
                    game.handle_click(event.pos)

        draw_board(screen, game)
        draw_restart_button(screen)
        display_scores(screen, game)
        display_current_player(screen, game)

        if game.winner:
            if game.winner == 'row':
                row = game.winner['index']
                start_pos, end_pos = (0, row * 100 + 50), (300, row * 100 + 50)
            elif game.winner == 'col':
                col = game.winner['index']
                start_pos, end_pos = (col * 100 + 50, 0), (col * 100 + 50, 300)
            elif game.winner == 'diag':
                if game.winner['index'] == 0:
                    start_pos, end_pos = (0, 0), (300, 300)
                else:
                    start_pos, end_pos = (300, 0), (0, 300)
            draw_winning_line(screen, (start_pos, end_pos))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
