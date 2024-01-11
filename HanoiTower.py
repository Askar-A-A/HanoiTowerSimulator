import pygame
import itertools
import time


msc_list = [
    "c:\\Users\\Askar\\Downloads\\undertale_015.sans.mp3", 
    "c:\\Users\\Askar\\Downloads\\undertale_021. Dogsong.mp3",
    "c:\\Users\\Askar\\Downloads\\undertale_003. Your Best Friend.mp3",
    "c:\\Users\\Askar\\Downloads\\undertale_025. Dating Start!.mp3",
    "c:\\Users\\Askar\\Downloads\\undertale_027. Dating Fight!.mp3",
    "c:\\Users\\Askar\\Downloads\\undertale_089. SAVE the World.mp3",
    "c:\\Users\\Askar\\Downloads\\undertale_059. Spider Dance.mp3",
    ]


# Pygame settings
WIDTH, HEIGHT = 1500, 700


# Pegs settings
PEGS = [WIDTH // 6, WIDTH // 2, 5 * WIDTH // 6]
DISK_HEIGHT = 20

def hanoi(n, source, target, auxiliary):
    if n > 0:
        yield from hanoi(n - 1, source, auxiliary, target)
        pegs[target].append(pegs[source].pop())
        yield
        yield from hanoi(n - 1, auxiliary, target, source)

def play_song(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def draw_tower(screen, pegs, peg_positions, disk_height, colors, HEIGHT):
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the base
    pygame.draw.rect(screen, (255, 255, 255), (0, HEIGHT - 20, WIDTH, 20))

    # Draw the pegs
    for x in peg_positions:
        pygame.draw.rect(screen, (255, 255, 255), (x, 0, 10, HEIGHT - 10))

    # Draw the disks
    for i, peg in enumerate(pegs):
        for j, disk in enumerate(peg):
            disk_width = disk * 20
            pygame.draw.rect(screen, colors[disk - 1],
                             (peg_positions[i] - disk_width // 2 + 10, HEIGHT - (j + 1) * disk_height, disk_width, disk_height))

def game():
    num_disks = int(input("Enter the number of disks: "))  # This line will prompt user for number of disks

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    global pegs
    pegs = [list(range(num_disks, 0, -1)), [], []]

    hanoi_gen = hanoi(num_disks, 0, 2, 1)

    
    font = pygame.font.Font(None, 36)
    move_count = 0

    
    background_color = (0, 0, 0)  
    text_box_width = 400
    text_box_height = 50

    
    if 1 < num_disks <= 3:
        play_song(msc_list[0])
    elif 3 < num_disks <= 5:
        play_song(msc_list[1])
    elif 5 < num_disks <= 7: 
        play_song(msc_list[2])   
    elif 7 < num_disks <= 10: 
        play_song(msc_list[3])   
    elif 10 < num_disks <= 15: 
        play_song(msc_list[4])   
    elif 15 < num_disks <= 25: 
        play_song(msc_list[5])   
    elif 25 < num_disks <= 50: 
        play_song(msc_list[6])  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        colors = [(255, 255, 0) for _ in range(num_disks)]

        draw_tower(screen, pegs, PEGS, DISK_HEIGHT, colors, HEIGHT)

        
        text = font.render(f"Move count: {move_count}", True, (255, 255, 255))
        screen.blit(text, (WIDTH - 200, 10))

        
        if move_count > 10:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("You spent minute playing, nothing significant happened", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))
        
        if move_count > 100:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("You are 10 minutes into a game, moving as fast as possible", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))

        if move_count > 250:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("You are playing 25 minutes, got bored", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))

        if move_count > 600:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("An hour passes you are getting tired", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))   

        if move_count > 1200:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("You are two hours in", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))     

        if move_count > 1800:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("Three hours in, your brain hurts", True, (255, 255, 255))
            screen.blit(text_example, (10, 10)) 

        if move_count > 3000:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("You are playing half of the day, you are getting hungry", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))

        if move_count > 4500:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("You want to go to the toilet", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))    

        if move_count > 6000:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("Your hands are in pain aswell", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))

        if move_count > 9000:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("What about sleep?", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))

        if move_count > 12000:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("You did not sleep, tired, hungry..", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))

        if move_count > 15000:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("Your urge to sleep is rising..", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))   

        if move_count > 18000:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("They don't let you do it even without leaving the game", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))   

        if move_count > 21000:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("The lack of energy is draining your brain even faster", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))          

        if move_count > 24000:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("You died because you did not eat and sleap", True, (255, 255, 255))
            screen.blit(text_example, (10, 10)) 

        if move_count > 25000:
            pygame.draw.rect(screen, background_color, pygame.Rect(10, 10, text_box_width + 750, text_box_height))
            text_example = font.render("The robot continues for you..", True, (255, 255, 255))
            screen.blit(text_example, (10, 10))                             

        pygame.display.flip()
        FPS = num_disks ** 2
        clock.tick(FPS)



        # Step through the Hanoi solution
        try:
            next(hanoi_gen)
            move_count += 1
        except StopIteration:
            break

        if 1 < num_disks <= 3:
           time.sleep(2.0)   
        elif 3 < num_disks <= 5:
           time.sleep(1.25)
        elif 5 < num_disks <= 7: 
           time.sleep(1/(num_disks/2)) 
        elif 7 < num_disks <= 10: 
           time.sleep(1/(num_disks/1.5)) 
        elif 10 < num_disks <= 15: 
           time.sleep(1/(num_disks)) 
        elif 15 < num_disks <= 25: 
           time.sleep(1/(num_disks * 2.2))   
        elif 25 < num_disks <= 50: 
           time.sleep(1/(num_disks * num_disks * 1.5)) 

if __name__ == "__main__":
    game()


 


    
 