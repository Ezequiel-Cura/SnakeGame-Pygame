import pygame
from data.constants import *
from data.game_config import Config
from data.utils import *
from data.select_btn import OptionBox,DropDown

from data.food import Food
from data.snake import Snake
from data.button import Button

class Game(Config):
    def __init__(self, W, H, FPS, caption="Snake Game",icon="" ) -> None:
        super().__init__((W,H),FPS,caption,icon)

        pygame.font.init()
        self.current_state = GameState.IN_MENU

        self.size = (W,H)

        self.tile_size = 50
        self.ROWS = H // self.tile_size
        self.COLS = W // self.tile_size


        self.font = pygame.font.Font(None, 36) 

        self.initial_options = {
            "infinte_border": False,
            "draw_grid": True,
            "color_snake": "GREEN",
            "num_color_snake_selected": 0,
            "snake_speed": "x1"
        }

        self.initial_options = read_options(self.initial_options)

        #Entities AND GAME BUTTONS
        self.food = Food(self.size)
        self.snake = Snake()

        self.back_menu_btn = Button(150,10,"",(50,25),"Menu")

        # BUTTONS MENU
        self.start_btn = Button(500,300,"",(250,100),"Play")
        self.leaderbord_btn = Button(500,600,"",(250,100),"Leaderboard")
        self.options_btn = Button(500,900,"",(250,100),"Options")

        #BUTTONS OPTIONS MENU
        self.infinte_border_btn = Button(250,200,"",(250,100),"Infinite border:")
        self.draw_grid_btn = Button(250,300,"",(250,100),"draw grid:")
        self.color_snake_btn = OptionBox(500, 200, 160, 40, GRAY, YELLOW1, ["GREEN","RED", "BLUE", "YELLOW1"],pygame.font.Font(None,36),"Snake color",self.initial_options["color_snake"])
        self.speed_snake_btn = OptionBox(700, 200, 160, 40, GRAY, YELLOW1, ["x2","x1,5","x1","x0,5"],pygame.font.Font(None,36),"Snake speed",self.initial_options["snake_speed"])




    def handle_events(self):
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # if self.color_snake_btn.rect.collidepoint(pygame.mouse.get_pos()):
                #     self.color_snake_btn.draw_menu = True
 
                print(event.pos)
            elif event.type == pygame.USEREVENT:
                self.snake.can_change = True

        

    def update(self):
        # Update game state
        if self.snake.is_dead == True:
            self.current_state = GameState.IN_MENU
            self.snake.reset_snake()
            
        if self.back_menu_btn.update():
            self.snake.reset_snake()
            self.current_state = GameState.IN_MENU

       

    def draw_grid(self):
        for y in range(self.ROWS):
            for x in range(self.COLS):
                pygame.draw.rect(self.SCREEN, BLUE, (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size), 1)


    def render_game(self):
        # Clear the screen


        if self.initial_options['draw_grid'] == True:
            self.draw_grid()

        self.snake.update(self.SCREEN,self.size,self.food,self.initial_options["infinte_border"],COLORS_SNAKE[self.initial_options["color_snake"]])
        self.food.update(self.SCREEN,self.size)

        score_text = self.font.render(f"score: {self.snake.score}",False,WHITE,False)
        self.SCREEN.blit(score_text,(0,0))
        self.back_menu_btn.draw(self.SCREEN)






    def render_menu(self):
        menu_text = self.font.render("MENU",False,WHITE,False)
        

        self.start_btn.draw(self.SCREEN)
        self.leaderbord_btn.draw(self.SCREEN)
        self.options_btn.draw(self.SCREEN)

        if self.start_btn.update():
            self.current_state = GameState.IN_GAME
        if self.leaderbord_btn.update():
            print("leaderboard")
        if self.options_btn.update():
            self.current_state = GameState.IN_OPTIONS
        

        # pygame.draw.rect(self.SCREEN,RED,play_rect)
        self.SCREEN.blit(menu_text,(self.size[0] // 2 - 50,50))

    
    def render_options_menu(self):
        
        value_infinte_border = self.font.render(f"{self.initial_options['infinte_border']}",False,WHITE,False)
        value_draw_grid = self.font.render(f"{self.initial_options['draw_grid']}",False,WHITE,False)


        self.infinte_border_btn.draw(self.SCREEN)
        self.draw_grid_btn.draw(self.SCREEN)
        self.back_menu_btn.draw(self.SCREEN)
        self.color_snake_btn.draw(self.SCREEN)
        self.speed_snake_btn.draw(self.SCREEN)


        self.SCREEN.blit(value_infinte_border,(self.infinte_border_btn.rect))
        self.SCREEN.blit(value_draw_grid,(self.draw_grid_btn.rect))

        
        if self.infinte_border_btn.update():
            self.initial_options["infinte_border"] = not self.initial_options["infinte_border"]
        
        if self.draw_grid_btn.update():
            self.initial_options["draw_grid"] = not self.initial_options["draw_grid"]

        self.color_snake_btn.update(pygame.event.get())
        self.initial_options["color_snake"] = self.color_snake_btn.txt_selected
        self.initial_options["num_color_snake_selected"] = self.color_snake_btn.selected

        self.speed_snake_btn.update(pygame.event.get())
        self.initial_options["snake_speed"] = self.speed_snake_btn.txt_selected
        self.snake.speed = SPEED_SNAKE[self.speed_snake_btn.txt_selected]


    def run(self):
        # Main game loop
        while self.running:

            self.SCREEN.fill((0, 0, 0))

            self.handle_events()
            self.update()

            if self.current_state == GameState.IN_GAME:
                self.render_game()
            elif self.current_state == GameState.IN_MENU:
                self.render_menu()
            elif self.current_state == GameState.IN_OPTIONS:
                self.render_options_menu()
            

            # Control frame rate
            self.clock.tick(self.FPS)

            # Update the display
            pygame.display.update()

        write_options(self.initial_options)
        # Quit Pygame
        pygame.quit()



