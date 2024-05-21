from mygame import init, create_ship, create_bullet, create_aliens, handle_event, update_object, render_object
import pygame

pygame.init()


#game_over_msg = pygame.font.Font(None, 64)
# screen_surf = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screen_surf = init()

ship_rect = create_ship(screen_surf)  
aliens = create_aliens()

bullet_rect = None
bullets = []

clock = pygame.time.Clock()

left_pressed = False
right_pressed = False
alien_x_direction = 1 # False: -1, 1: right
alien_x_direction_changed = False
is_running = True


while True:
    # Process player inputs.
    handle_event()
    update_object(screen_surf, aliens)
    render_object(screen_surf)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)

       
    #game_over_msg.render('Game Over!', True, (0, 0, 0))