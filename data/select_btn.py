


class Select_btn:
    def __init__(self) -> None:
        pass

    def draw(self):
        pass

    def update(self):
        pass

import pygame

class OptionBox1():

    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, selected = 0):

        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect)
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2)
        msg = self.font.render(self.option_list[self.selected], 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            print("hoa")
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))
            outer_rect = (self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.option_list))
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 2)

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        self.active_option = -1
        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False
 

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    return self.active_option
        return -1
    
# list1 = OptionBox(
#     40, 40, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30), 
#     ["option 1", "2nd option", "another option"])

# run = True
# while run:
#     clock.tick(60)
#     event_list = pygame.event.get()
#     for event in event_list:
#         if event.type == pygame.QUIT:
#             run = False

#     selected_option = list1.update(event_list)
#     if selected_option >= 0:
#         print(selected_option)

#     window.fill((255, 255, 255))
#     list1.draw(window)
#     pygame.display.flip()
    
# pygame.quit()
# exit()
    
class DropDown():

    def __init__(self, color_menu, color_option, x, y, w, h, font, main, options):
        self.color_menu = color_menu
        self.color_option = color_option
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.main = main
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
        msg = self.font.render(self.main, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, 0)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        # print(self.menu_active,"--")
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.main = self.options[i]
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        # Check if the mouse click occurs outside the box when the box is active
        if pygame.mouse.get_pressed()[0] and not self.rect.collidepoint(mpos):
            self.draw_menu = False

        # for event in event_list:
        #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #         if self.menu_active:
        #             self.draw_menu = not self.draw_menu
        #         elif self.draw_menu and self.active_option >= 0:
        #             self.draw_menu = False
        #             return self.active_option
        # return -1

# pg.init()
# clock = pg.time.Clock()
# screen = pg.display.set_mode((640, 480))

# COLOR_INACTIVE = (100, 80, 255)
# COLOR_ACTIVE = (100, 200, 255)
# COLOR_LIST_INACTIVE = (255, 100, 100)
# COLOR_LIST_ACTIVE = (255, 150, 150)

# list1 = DropDown(
#     [COLOR_INACTIVE, COLOR_ACTIVE],
#     [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
#     50, 50, 200, 50, 
#     pg.font.SysFont(None, 30), 
#     "Select Mode", ["Calibration", "Test"])

# run = True
# while run:
#     clock.tick(30)

#     event_list = pg.event.get()
#     for event in event_list:
#         if event.type == pg.QUIT:
#             run = False

#     selected_option = list1.update(event_list)
#     if selected_option >= 0:
#         list1.main = list1.options[selected_option]

#     screen.fill((255, 255, 255))
#     list1.draw(screen)
#     pg.display.flip()
    
# pg.quit()
# exit()
    

class OptionBox:
    def __init__(self,x,y,w,h,color_menu,color_option,option_list,font ,label,selected = 0) -> None:
        self.color_menu = color_menu
        self.color_option = color_option
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.expanded_rect = pygame.Rect(x,y,w,h * (len(option_list) + 1))

        self.options = option_list
        self.selected = selected
        self.txt_selected = selected
        self.draw_menu = False


        self.list_options =  [0] *  len(option_list) 

        for i,text in enumerate(self.options):
            rect = pygame.Rect(x, y + (( i + 1) * self.rect.height), self.rect.width, self.rect.height)
            self.list_options[i] = {
                "rect": rect,
                "text": text
            }

    def draw(self,screen):
        pygame.draw.rect(screen,self.color_menu,self.rect,0)
        msg = self.font.render(self.txt_selected,1,(0,0,0))
        screen.blit(msg,msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i in range(0,len(self.list_options)):
                rect = self.list_options[i]["rect"]
                text = self.list_options[i]["text"]
                pygame.draw.rect(screen,self.color_option,rect,0)
                msg = self.font.render(text,1,(0,0,0))
                screen.blit(msg,msg.get_rect(center = rect.center))

    def update(self, event_list: list[pygame.event.Event]):
        mouse_pos = pygame.mouse.get_pos()

    
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse_pos):
            self.draw_menu = True

        if pygame.mouse.get_pressed()[0] and not self.rect.collidepoint(mouse_pos):
            self.draw_menu = False

        for i in range(0,len(self.list_options)):
            if self.draw_menu:
                if self.list_options[i]["rect"].collidepoint(mouse_pos):
                    self.selected = i
                    self.txt_selected = self.options[self.selected]

