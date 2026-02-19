# Project3 done by Sharan Ravula
# Import necessary modules
import pygame

# Initialize Pygame
pygame.init()

# Global variables and constants
#WIDTH = 1000
#HEIGHT = 900
display_info = pygame.display.Info()  # Get display information
WIDTH = display_info.current_w  # Set WIDTH to the current screen width
HEIGHT = display_info.current_h  # Set HEIGHT to the current screen height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess.app')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

button_rect = pygame.Rect(WIDTH - 680, 20, 100, 30)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

# Class to handle rules text
class RulesText:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 16, bold=True)
    rules_text = [
        "",
        "",
        "The game is played on an 8x8 grid. So in total we have 64 squares",
        "Each player starts with 16 pieces: 1 king, 1 queen, 2 rooks, 2 knights, 2 bishops,", "and 8 pawns. So in total we have 32 pieces",
        "Pawns move forward two squares in the starting position but must only move one", "square from there after, They capture diagonally.",
        "Rooks move horizontally or vertically any number of squares.",
        "Knights move in a 'L' shape: two squares in one direction and one square perpendicular.",
        "Bishops move diagonally any number of squares.",
        "The queen moves in any direction any number of squares.",
        "The king moves one square in any direction.",
        "Special moves include castling, en passant, and pawn promotion.",
        "Stalemate occurs when a player has no legal moves and is not in check, resulting in a", "draw.",
        "En passant is when a pawn captures an opponent's pawn that has moved two squares", "forward from its original position.",
        "Castling allows the king to move two squares toward a rook and the rook to move to the", "other side of the king.",
        "Pawn promotion occurs when a pawn reaches the opponent's back rank and is", "promoted to any piece",
        "Check: The king is in a position to be captured. The player must make a move to remove", "the check.",
        "Checkmate: The king is in check and there are no legal moves to escape.",
        "The game is drawn if neither player has enough material to checkmate.",
        "Resign: Clicking this button ends the game, declaring the opponent as the winner.",
        "Draw: Click this button to propose a draw. The game ends in a tie if both players agree.",
        "Reset: Resets the game to its initial state with all pieces in their starting positions.",
        "Change Piece Set: Switches the visual style of the pieces on the board."
    ]

    def draw(self, surface, rect):
        y_offset = rect.y + 10
        for line in self.rules_text:
            text_surface = self.font.render(line, True, BLACK)
            surface.blit(text_surface, (rect.x + 10, y_offset))
            y_offset += 30

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
# Alternate pieces
alt_white_pieces = white_pieces  # These will reference alternate images when toggled
alt_black_pieces = black_pieces 

captured_pieces_white = []
captured_pieces_black = []



# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []

# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('../datasets/dataset_1/black_queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('../datasets/dataset_1/black_king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('../datasets/dataset_1/black_rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('../datasets/dataset_1/black_bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('../datasets/dataset_1/black_knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('../datasets/dataset_1/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('../datasets/dataset_1/white_queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('../datasets/dataset_1/white_king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('../datasets/dataset_1/white_rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('../datasets/dataset_1/white_bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('../datasets/dataset_1/white_knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('../datasets/dataset_1/white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

# Load and scale alternate images for black pieces
alt_black_queen = pygame.image.load('../datasets/dataset_2/alt_black_queen.svg')
alt_black_queen = pygame.transform.scale(alt_black_queen, (80, 80))
alt_black_queen_small = pygame.transform.scale(alt_black_queen, (45, 45))

alt_black_king = pygame.image.load('../datasets/dataset_2/alt_black_king.svg')
alt_black_king = pygame.transform.scale(alt_black_king, (80, 80))
alt_black_king_small = pygame.transform.scale(alt_black_king, (45, 45))

alt_black_rook = pygame.image.load('../datasets/dataset_2/alt_black_rook.svg')
alt_black_rook = pygame.transform.scale(alt_black_rook, (80, 80))
alt_black_rook_small = pygame.transform.scale(alt_black_rook, (45, 45))

alt_black_bishop = pygame.image.load('../datasets/dataset_2/alt_black_bishop.svg')
alt_black_bishop = pygame.transform.scale(alt_black_bishop, (80, 80))
alt_black_bishop_small = pygame.transform.scale(alt_black_bishop, (45, 45))

alt_black_knight = pygame.image.load('../datasets/dataset_2/alt_black_knight.svg')
alt_black_knight = pygame.transform.scale(alt_black_knight, (80, 80))
alt_black_knight_small = pygame.transform.scale(alt_black_knight, (45, 45))

alt_black_pawn = pygame.image.load('../datasets/dataset_2/alt_black_pawn.svg')
alt_black_pawn = pygame.transform.scale(alt_black_pawn, (65, 65))
alt_black_pawn_small = pygame.transform.scale(alt_black_pawn, (45, 45))

# Load and scale alternate images for white pieces
alt_white_queen = pygame.image.load('../datasets/dataset_2/alt_white_queen.svg')
alt_white_queen = pygame.transform.scale(alt_white_queen, (80, 80))
alt_white_queen_small = pygame.transform.scale(alt_white_queen, (45, 45))

alt_white_king = pygame.image.load('../datasets/dataset_2/alt_white_king.svg')
alt_white_king = pygame.transform.scale(alt_white_king, (80, 80))
alt_white_king_small = pygame.transform.scale(alt_white_king, (45, 45))

alt_white_rook = pygame.image.load('../datasets/dataset_2/alt_white_rook.svg')
alt_white_rook = pygame.transform.scale(alt_white_rook, (80, 80))
alt_white_rook_small = pygame.transform.scale(alt_white_rook, (45, 45))

alt_white_bishop = pygame.image.load('../datasets/dataset_2/alt_white_bishop.svg')
alt_white_bishop = pygame.transform.scale(alt_white_bishop, (80, 80))
alt_white_bishop_small = pygame.transform.scale(alt_white_bishop, (45, 45))

alt_white_knight = pygame.image.load('../datasets/dataset_2/alt_white_knight.svg')
alt_white_knight = pygame.transform.scale(alt_white_knight, (80, 80))
alt_white_knight_small = pygame.transform.scale(alt_white_knight, (45, 45))

alt_white_pawn = pygame.image.load('../datasets/dataset_2/alt_white_pawn.svg')
alt_white_pawn = pygame.transform.scale(alt_white_pawn, (65, 65))
alt_white_pawn_small = pygame.transform.scale(alt_white_pawn, (45, 45))

# List of possible promotions for both white and black
white_promotions = ['bishop', 'knight', 'rook', 'queen']
black_promotions = ['bishop', 'knight', 'rook', 'queen']

# Moved tracking lists for each piece
white_moved = [False] * 16
black_moved = [False] * 16

# Lists for main and alternate images for white and black pieces
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]

# Alternative piece images for white and black pieces
alt_white_images = [alt_white_pawn, alt_white_queen, alt_white_king, alt_white_knight, alt_white_rook, alt_white_bishop]
alt_black_images = [alt_black_pawn, alt_black_queen, alt_black_king, alt_black_knight, alt_black_rook, alt_black_bishop]

# Define small versions of main images for displaying captured pieces
small_white_images = [pygame.transform.scale(img, (45, 45)) for img in white_images]
small_black_images = [pygame.transform.scale(img, (45, 45)) for img in black_images]

# Define small versions of alternate images for displaying captured pieces
alt_small_white_images = [pygame.transform.scale(img, (45, 45)) for img in alt_white_images]
alt_small_black_images = [pygame.transform.scale(img, (45, 45)) for img in alt_black_images]

# List of piece types for reference
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# check variables/ flashing counter
counter = 0
winner = ''
game_over = False
game_draw = False
game_reset = False
game_checkmate = False
white_ep = (100, 100)
black_ep = (100, 100)
white_promote = False
black_promote = False
promo_index = 100
check = False
castling_moves = []
use_alternate_images = False

# Toggle between main and alternate image sets
# Toggle between main and alternate image sets for all pieces, including pawns
def toggle_image_set():
    global white_images, black_images, use_alternate_images

    if use_alternate_images:
        # Switch to primary images
        white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
        black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
    else:
        # Switch to alternate images
        white_images = [alt_white_pawn, alt_white_queen, alt_white_king, alt_white_knight, alt_white_rook, alt_white_bishop]
        black_images = [alt_black_pawn, alt_black_queen, alt_black_king, alt_black_knight, alt_black_rook, alt_black_bishop]

    # Toggle the state
    use_alternate_images = not use_alternate_images

# draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light grey', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light grey', [700 - (column * 200), row * 100, 100, 100])
            # White select piece message - Blue
            pygame.draw.rect(screen, 'blue', [0, 800, 800, 100], 5)
            # Reset button - Green
            pygame.draw.rect(screen, 'green', [0, 900, 800, 97], 5)
            # Resign button - Red
            pygame.draw.rect(screen, 'red', [800, 800, 200, 100], 5)
            # Draw button - Gold
            pygame.draw.rect(screen, 'gold', [800, 900, 200, 97], 5)
            # Piece list and rules panel - Black border
            pygame.draw.rect(screen, 'black', [800, 0, 200, 800], 5)
            # Change Piece Set Button - Orange
            pygame.draw.rect(screen, 'orange', [1000, 900, 680, 97], 5)

        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (30, 830))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(big_font.render('Resign', True, 'black'), (815, 830))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(big_font.render('Draw', True, 'black'), (835, 925))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(big_font.render('Reset', True, 'black'), (330, 925))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(big_font.render('Change Piece Set', True, 'black'), (1130, 925))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(big_font.render('Chess Rules', True, 'black'), (1200, 15))
        if white_promote or black_promote:
            pygame.draw.rect(screen, 'white', [5, 805, 790, 90])
            pygame.draw.rect(screen, 'pink', [5, 805, 790, 90], 5)
            screen.blit(big_font.render('Select Piece to Promote Pawn', True, 'black'), (50, 830))
        
        # Draw a large button for rules and display the rules text
    pygame.draw.rect(screen,"dark grey", button_rect)
    rules = RulesText()
    rules.draw(screen, button_rect)

# Draw pieces onto the board with support for alternate images
def draw_pieces():
    # Choose the appropriate image set based on the toggle
    current_white_images = alt_white_images if use_alternate_images else white_images
    current_black_images = alt_black_images if use_alternate_images else black_images

    # Draw white pieces
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        # Draw pawns and other pieces from the current white image set
        if white_pieces[i] == 'pawn':
            screen.blit(current_white_images[0], (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(current_white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        
        # Highlight selected piece for white
        if turn_step < 2 and selection == i:
            pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                             100, 100], 2)

    # Draw black pieces
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        # Draw pawns and other pieces from the current black image set
        if black_pieces[i] == 'pawn':
            screen.blit(current_black_images[0], (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(current_black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        
        # Highlight selected piece for black
        if turn_step >= 2 and selection == i:
            pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                              100, 100], 2)

# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    global castling_moves
    moves_list = []
    all_moves_list = []
    castling_moves = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list, castling_moves = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# check king valid moves
def check_king(position, color):
    moves_list = []
    castle_moves = check_castling()
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
            
    return moves_list, castle_moves

# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# check rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
            # indent the check for two spaces ahead, so it is only checked if one space ahead is also open
            if (position[0], position[1] + 2) not in white_locations and \
                    (position[0], position[1] + 2) not in black_locations and position[1] == 1:
                moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
        # add en passant move checker
        if (position[0] + 1, position[1] + 1) == black_ep:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) == black_ep:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
            # indent the check for two spaces ahead, so it is only checked if one space ahead is also open
            if (position[0], position[1] - 2) not in white_locations and \
                    (position[0], position[1] - 2) not in black_locations and position[1] == 6:
                moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
        # add en passant move checker
        if (position[0] + 1, position[1] - 1) == white_ep:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) == white_ep:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# Integrate into check_valid_moves by applying the filter for king moves
def check_valid_moves():
    global check
    valid_options = []

    if check:
        attacking_pieces = identify_attacking_pieces()
        blocking_squares = identify_blocking_squares(attacking_pieces)
        
        if turn_step < 2:  # White's turn
            if white_pieces[selection] == 'king':
                # Get initial king moves and filter them for safety
                king_position = white_locations[white_pieces.index('king')]
                king_moves, castle_moves = check_king(king_position, 'white')
                valid_options = filter_safe_king_moves(king_moves, king_position, 'white')
                valid_options.extend(castle_moves)  # Include valid castling moves if any
            else:
                valid_options = [
                    move for move in white_options[selection]
                    if move in blocking_squares or move_captures_attacker(move, attacking_pieces, 'white')
                ]
        else:  # Black's turn
            if black_pieces[selection] == 'king':
                king_position = black_locations[black_pieces.index('king')]
                king_moves, castle_moves = check_king(king_position, 'black')
                valid_options = filter_safe_king_moves(king_moves, king_position, 'black')
                valid_options.extend(castle_moves)  # Include valid castling moves if any
            else:
                valid_options = [
                    move for move in black_options[selection]
                    if move in blocking_squares or move_captures_attacker(move, attacking_pieces, 'black')
                ]
    else:
        if turn_step < 2:
            valid_options = white_options[selection]
        else:
            valid_options = black_options[selection]

    return valid_options

def filter_safe_king_moves(king_moves, king_position, color):
    """Filter out moves where the king would still be in check or capture protected pieces."""
    safe_moves = []
    opponent_pieces = black_pieces if color == 'white' else white_pieces
    opponent_locations = black_locations if color == 'white' else white_locations
    opponent_options = black_options if color == 'white' else white_options
    friendly_locations = white_locations if color == 'white' else black_locations

    for move in king_moves:
        is_safe = True

        # Check if the move captures a protected piece
        if move in opponent_locations:
            is_safe = all(move not in opponent_options[i] for i, loc in enumerate(opponent_locations) if move == loc)

        # Check if the move is guarded by any opponent's options
        is_guarded = any(move in opponent_options[i] for i in range(len(opponent_pieces)))

        # Ensure the move does not overlap with friendly pieces
        if move in friendly_locations:
            is_safe = False

        # Add to safe moves only if move is safe and not guarded
        if is_safe and not is_guarded:
            safe_moves.append(move)

    return safe_moves


def identify_attacking_pieces():
    """Identify pieces putting the king in check."""
    attacking_pieces = []

    if turn_step < 2:  # White's turn; check if White's king is in check
        king_pos = white_locations[white_pieces.index('king')]
        opponent_pieces = black_pieces
        opponent_locations = black_locations
        opponent_options = black_options
    else:  # Black's turn; check if Black's king is in check
        king_pos = black_locations[black_pieces.index('king')]
        opponent_pieces = white_pieces
        opponent_locations = white_locations
        opponent_options = white_options

    # Check if any opponent piece attacks the king's position
    for i, piece in enumerate(opponent_pieces):
        if king_pos in opponent_options[i]:  # If an opponent piece attacks the king
            attacking_pieces.append(opponent_locations[i])

    return attacking_pieces


def identify_blocking_squares(attacking_pieces):
    """Identify the squares between the attacking piece and the king for potential blocking."""
    blocking_squares = []
    if turn_step < 2:  # White's king
        king_pos = white_locations[white_pieces.index('king')]
        for attacker in attacking_pieces:
            if is_sliding_piece(attacker, 'black'):
                blocking_squares.extend(get_path_between(attacker, king_pos))
    else:  # Black's king
        king_pos = black_locations[black_pieces.index('king')]
        for attacker in attacking_pieces:
            if is_sliding_piece(attacker, 'white'):
                blocking_squares.extend(get_path_between(attacker, king_pos))
    return blocking_squares

def is_sliding_piece(piece_location, color):
    """Check if the piece at the given location is a sliding piece (rook, bishop, or queen)."""
    if color == 'white':
        index = white_locations.index(piece_location)
        piece = white_pieces[index]
    else:
        index = black_locations.index(piece_location)
        piece = black_pieces[index]
    
    return piece in ['rook', 'bishop', 'queen']

def get_path_between(start, end):
    """Get the path between two points on the board (for blocking checks)."""
    path = []
    x1, y1 = start
    x2, y2 = end
    
    if x1 == x2:  # Vertical line
        step = 1 if y2 > y1 else -1
        for y in range(y1 + step, y2, step):
            path.append((x1, y))
    elif y1 == y2:  # Horizontal line
        step = 1 if x2 > x1 else -1
        for x in range(x1 + step, x2, step):
            path.append((x, y1))
    elif abs(x2 - x1) == abs(y2 - y1):  # Diagonal line
        x_step = 1 if x2 > x1 else -1
        y_step = 1 if y2 > y1 else -1
        for i in range(1, abs(x2 - x1)):
            path.append((x1 + i * x_step, y1 + i * y_step))

    return path

def move_captures_attacker(move, attacking_pieces, color):
    """Check if a move captures an attacking piece."""
    if color == 'white':
        return move in attacking_pieces  # Valid if the move captures an attacking black piece
    else:
        return move in attacking_pieces  # Valid if the move captures an attacking white piece

# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)

# Draw captured pieces on the side of the screen with alternate image support
def draw_captured():
    # Determine which image sets to use based on the alternate toggle
    current_small_black_images = alt_small_black_images if use_alternate_images else small_black_images
    current_small_white_images = alt_small_white_images if use_alternate_images else small_white_images

    # Display captured white pieces on the side using black-themed images
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(current_small_black_images[index], (825, 5 + 50 * i))

    # Display captured black pieces on the side using white-themed images
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(current_small_white_images[index], (925, 5 + 50 * i))


# draw a flashing square around king if in check
def draw_check():
    global check
    check = False
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    check = True
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    check = True
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)

def draw_game_over():
    # Define board center coordinates (assuming an 800x800 board)
    board_center_x = 400
    board_center_y = 400

    # Calculate size of the game over message box
    rect_width = 450
    rect_height = 70
    rect_x = board_center_x - (rect_width // 2)
    rect_y = board_center_y - (rect_height // 2)

    # Draw the rectangle and display text
    pygame.draw.rect(screen, 'black', [rect_x, rect_y, rect_width, rect_height])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (rect_x + 10, rect_y + 10))
    screen.blit(font.render(f'Press "ENTER" to Restart! or "n" to Resume!', True, 'white'), (rect_x + 10, rect_y + 40))

def draw_game_draw():
    # Define board center coordinates (assuming an 800x800 board)
    board_center_x = 400
    board_center_y = 400

    # Calculate size of the game over message box
    rect_width = 450
    rect_height = 70
    rect_x = board_center_x - (rect_width // 2)
    rect_y = board_center_y - (rect_height // 2)

    # Draw the rectangle and display text
    pygame.draw.rect(screen, 'black', [rect_x, rect_y, rect_width, rect_height])
    screen.blit(font.render(f'Its a draw! 1/2 - 1/2', True, 'white'), (rect_x + 10, rect_y + 10))
    screen.blit(font.render(f'Press "ENTER" to Restart! or "n" to Reject!', True, 'white'), (rect_x + 10, rect_y + 40))

def draw_game_reset():
    # Define board center coordinates (assuming an 800x800 board)
    board_center_x = 400
    board_center_y = 400

    # Calculate size of the game over message box
    rect_width = 450
    rect_height = 70
    rect_x = board_center_x - (rect_width // 2)
    rect_y = board_center_y - (rect_height // 2)

    # Draw the rectangle and display text
    pygame.draw.rect(screen, 'black', [rect_x, rect_y, rect_width, rect_height])
    screen.blit(font.render(f'Are you Sure you want to Reset?', True, 'white'), (rect_x + 10, rect_y + 10))
    screen.blit(font.render(f'Press "ENTER" to Reset! or "n" to Resume!', True, 'white'), (rect_x + 10, rect_y + 40))

def display_victory_message(winner):
    """Displays a victory message and prompts to press Enter to reset."""
    # Define the board center coordinates
    board_center_x = 400
    board_center_y = 400
    
    # Set up the size and position of the message box
    rect_width = 450
    rect_height = 70
    rect_x = board_center_x - (rect_width // 2)
    rect_y = board_center_y - (rect_height // 2)
    
    # Draw the rectangle and display the victory text
    pygame.draw.rect(screen, 'black', [rect_x, rect_y, rect_width, rect_height])
    screen.blit(font.render(f'{winner} Won! by Checkmate! ', True, 'white'), (rect_x + 10, rect_y + 10))
    screen.blit(font.render('Click on Reset Button', True, 'white'), (rect_x + 10, rect_y + 40))

# check en passant
def check_ep(old_coords, new_coords):
    if turn_step <= 1:
        index = white_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] - 1)
        piece = white_pieces[index]
    else:
        index = black_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] + 1)
        piece = black_pieces[index]
    if piece == 'pawn' and abs(old_coords[1] - new_coords[1]) > 1:
        # if piece was pawn and moved two spaces, return EP coords as defined above
        pass
    else:
        ep_coords = (100, 100)
    return ep_coords

# add castling
def check_castling():
    # king must not currently be in check, neither the rook nor king has moved previously, nothing between
    # and the king does not pass through or finish on an attacked piece
    castle_moves = []  # store each valid castle move as [((king_coords), (castle_coords))]
    rook_indexes = []
    rook_locations = []
    king_index = 0
    king_pos = (0, 0)
    if turn_step > 1:
        for i in range(len(white_pieces)):
            if white_pieces[i] == 'rook':
                rook_indexes.append(white_moved[i])
                rook_locations.append(white_locations[i])
            if white_pieces[i] == 'king':
                king_index = i
                king_pos = white_locations[i]
        if not white_moved[king_index] and False in rook_indexes and not check:
            for i in range(len(rook_indexes)):
                castle = True
                if rook_locations[i][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]), (king_pos[0] + 2, king_pos[1]),
                                     (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]), (king_pos[0] - 2, king_pos[1])]
                for j in range(len(empty_squares)):
                    if empty_squares[j] in white_locations or empty_squares[j] in black_locations or \
                            empty_squares[j] in black_options or rook_indexes[i]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    else:
        for i in range(len(black_pieces)):
            if black_pieces[i] == 'rook':
                rook_indexes.append(black_moved[i])
                rook_locations.append(black_locations[i])
            if black_pieces[i] == 'king':
                king_index = i
                king_pos = black_locations[i]
        if not black_moved[king_index] and False in rook_indexes and not check:
            for i in range(len(rook_indexes)):
                castle = True
                if rook_locations[i][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]), (king_pos[0] + 2, king_pos[1]),
                                     (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]), (king_pos[0] - 2, king_pos[1])]
                for j in range(len(empty_squares)):
                    if empty_squares[j] in white_locations or empty_squares[j] in black_locations or \
                            empty_squares[j] in white_options or rook_indexes[i]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    return castle_moves

def draw_castling(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0][0] * 100 + 50, moves[i][0][1] * 100 + 70), 8)
        screen.blit(font.render('king', True, 'black'), (moves[i][0][0] * 100 + 30, moves[i][0][1] * 100 + 70))
        pygame.draw.circle(screen, color, (moves[i][1][0] * 100 + 50, moves[i][1][1] * 100 + 70), 8)
        screen.blit(font.render('rook', True, 'black'),
                    (moves[i][1][0] * 100 + 30, moves[i][1][1] * 100 + 70))
        pygame.draw.line(screen, color, (moves[i][0][0] * 100 + 50, moves[i][0][1] * 100 + 70),
                         (moves[i][1][0] * 100 + 50, moves[i][1][1] * 100 + 70), 2)

# add pawn promotion
def check_promotion():
    pawn_indexes = []
    white_promotion = False
    black_promotion = False
    promote_index = 100
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if white_locations[pawn_indexes[i]][1] == 7:
            white_promotion = True
            promote_index = pawn_indexes[i]
    pawn_indexes = []
    for i in range(len(black_pieces)):
        if black_pieces[i] == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if black_locations[pawn_indexes[i]][1] == 0:
            black_promotion = True
            promote_index = pawn_indexes[i]
    return white_promotion, black_promotion, promote_index

def draw_promotion():
    pygame.draw.rect(screen, 'dark gray', [800, 0, 200, 420])

    # Determine color and image set based on promotion side and alternate toggle
    if white_promote:
        color = 'white'
        current_images = alt_white_images if use_alternate_images else white_images
        promotions = white_promotions
    elif black_promote:
        color = 'black'
        current_images = alt_black_images if use_alternate_images else black_images
        promotions = black_promotions

    # Display promotion options
    for i, piece in enumerate(promotions):
        index = piece_list.index(piece)
        screen.blit(current_images[index], (860, 5 + 100 * i))

    # Draw border
    pygame.draw.rect(screen, color, [800, 0, 200, 420], 8)

def check_promo_select():
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    x_pos = mouse_pos[0] // 100
    y_pos = mouse_pos[1] // 100
    if white_promote and left_click and x_pos > 7 and y_pos < 4:
        white_pieces[promo_index] = white_promotions[y_pos]
    elif black_promote and left_click and x_pos > 7 and y_pos < 4:
        black_pieces[promo_index] = black_promotions[y_pos]

def reset_game():
    global game_over, draw_game, winner, game_reset, white_pieces, white_locations, white_moved
    global black_pieces, black_locations, black_moved, captured_pieces_white, captured_pieces_black
    global turn_step, selection, valid_moves, black_options, white_options, use_alternate_images

    # Reset game status and settings
    game_over = False
    draw_game = False
    game_reset = False
    winner = ''
    use_alternate_images = False  # Reset to primary images upon game reset

    # Initialize white and black pieces and locations
    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
    white_moved = [False] * 16

    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                       (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
    black_moved = [False] * 16

    # Reset captured pieces and game state
    captured_pieces_white = []
    captured_pieces_black = []
    turn_step = 0
    selection = 100
    valid_moves = []

    # Recalculate initial move options
    black_options = check_options(black_pieces, black_locations, 'black')
    white_options = check_options(white_pieces, white_locations, 'white')

# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    
    if not game_over:
        white_promote, black_promote, promo_index = check_promotion()
        if white_promote or black_promote:
            draw_promotion()
            check_promo_select()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
        if selected_piece == 'king':
            draw_castling(castling_moves)
    # In the main game loop
    if 'king' in captured_pieces_white:
        display_victory_message('White')
        game_checkmate = True
    elif 'king' in captured_pieces_black:
        display_victory_message('Black')
        game_checkmate = True

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            # Check if "Resign" was clicked
            if 800 <= mouse_x <= 1000 and 800 <= mouse_y <= 900:
                game_over = True
                winner = 'Black' if turn_step < 2 else 'White'  # Set winner based on turn
            # Check if "Draw" was clicked
            elif 800 <= mouse_x <= 1000 and 900 <= mouse_y <= 997:
                game_draw = True
            # Check if "Reset" was clicked
            elif 0 <= mouse_x <= 800 and 900 <= mouse_y <= 997:
                game_reset = True
            # Check if "Change Piece Set" was clicked
            elif 1000 <= mouse_x <= 1680 and 900 <= mouse_y <= 997:
                toggle_image_set()  # Call function to toggle between image sets

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    # check what piece is selected, so you can only draw castling moves if king is selected
                    selected_piece = white_pieces[selection]
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_ep = check_ep(white_locations[selection], click_coords)
                    white_locations[selection] = click_coords
                    white_moved[selection] = True
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                        black_moved.pop(black_piece)
                    # adding check if en passant pawn was captured
                    if click_coords == black_ep:
                        black_piece = black_locations.index((black_ep[0], black_ep[1] - 1))
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                        black_moved.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

                # add option to castle
                elif selection != 100 and selected_piece == 'king':
                    for q in range(len(castling_moves)):
                        if click_coords == castling_moves[q][0]:
                            white_locations[selection] = click_coords
                            white_moved[selection] = True
                            if click_coords == (1, 0):
                                rook_coords = (0, 0)
                            else:
                                rook_coords = (7, 0)
                            rook_index = white_locations.index(rook_coords)
                            white_locations[rook_index] = castling_moves[q][1]
                            black_options = check_options(black_pieces, black_locations, 'black')
                            white_options = check_options(white_pieces, white_locations, 'white')
                            turn_step = 2
                            selection = 100
                            valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    # check what piece is selected, so you can only draw castling moves if king is selected
                    selected_piece = black_pieces[selection]
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_ep = check_ep(black_locations[selection], click_coords)
                    black_locations[selection] = click_coords
                    black_moved[selection] = True
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                        white_moved.pop(white_piece)
                    if click_coords == white_ep:
                        white_piece = white_locations.index((white_ep[0], white_ep[1] + 1))
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                        white_moved.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

                # add option to castle
                elif selection != 100 and selected_piece == 'king':
                    for q in range(len(castling_moves)):
                        if click_coords == castling_moves[q][0]:
                            black_locations[selection] = click_coords
                            black_moved[selection] = True
                            if click_coords == (1, 7):
                                rook_coords = (0, 7)
                            else:
                                rook_coords = (7, 7)
                            rook_index = black_locations.index(rook_coords)
                            black_locations[rook_index] = castling_moves[q][1]
                            black_options = check_options(black_pieces, black_locations, 'black')
                            white_options = check_options(white_pieces, white_locations, 'white')
                            turn_step = 0
                            selection = 100
                            valid_moves = []
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_over or game_draw or game_reset:
                    reset_game()  # Reset the game when ENTER is pressed
                    game_over = False
                    game_draw = False
                    game_reset = False
            elif event.key == pygame.K_n:
            # Pressing 'N' cancels any game-ending prompts (reset, draw, resign)
                game_over = False
                game_draw = False
                game_reset = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_over or game_draw or game_reset:
                    reset_game()
                    game_over = False
                    game_draw = False
                    game_reset = False

    # Draw messages for game over and draw
    if game_draw:
        draw_game_draw()
    elif game_over:
        draw_game_over()
    elif game_reset:
        draw_game_reset()

    pygame.display.flip()
pygame.quit()