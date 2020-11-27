import random
import sys


misses=[]
hits=[]

_next_guesses=[]
potential_guesses=[
        
'A1',	'B1',	'C1',	'D1',	'E1',	'F1',	'G1',	'H1',	'I1',	'J1',
'A2',	'B2',	'C2',	'D2',	'E2',	'F2',	'G2',	'H2',	'I2',	'J2',
'A3',	'B3',	'C3',	'D3',	'E3',	'F3',	'G3',	'H3',	'I3',	'J3',
'A4',	'B4',	'C4',	'D4',	'E4',	'F4',	'G4',	'H4',	'I4',	'J4',
'A5',	'B5',	'C5',	'D5',	'E5',	'F5',	'G5',	'H5',	'I5',	'J5',
'A6',	'B6',	'C6',	'D6',	'E6',	'F6',	'G6',	'H6',	'I6',	'J6',
'A7',	'B7',	'C7',	'D7',	'E7',	'F7',	'G7',	'H7',	'I7',	'J7',
'A8',	'B8',	'C8',	'D8',	'E8',	'F8',	'G8',	'H8',	'I8',	'J8',
'A9',	'B9',	'C9',	'D9',	'E9',	'F9',	'G9',	'H9',	'I9',	'J9',
'A10',	'B10',	'C10',	'D10',	'E10',	'F10',	'G10',	'H10',	'I10',	'J10',
    ]

def incorrect_square(ship):
    ship=ship.upper()
    if ship == "EXIT":
        return False
    
    elif ship.upper() not in potential_guesses:
        return True

def remove_improper_move_choices(g):
    for item in g:
        if g.__contains__('none'):
            g.remove('none')

def invalid_move_check(_grid, _key):
    if _grid[_key] =="h" or _grid[_key] =="x":
        print("Sorry, invalid move.  Please try again.")





def play_again():
    
    play=input("Do you want to play again? (y/n) ")
    if play=="y":
        main()
    else:
        print("Goodbye")
        sys.exit(0)
        



def print_board(board):
    print('|  |A|B|C|D|E|F|G|H|I|J|')         
    print('-----------------------')
    print('| 1|' + board['1'] + '|' + board['2'] +    '|' + board['3'] + '|' + board['4'] +    '|' + board['5'] + '|' + board['6'] +    '|' + board['7'] + '|' + board['8'] +    '|' + board['9'] + '|' + board['10'] + '|')
    print('-----------------------')
    print('| 2|' + board['11'] + '|' + board['12'] +    '|' + board['13'] + '|' + board['14'] +    '|' + board['15'] + '|' + board['16'] +    '|' + board['17'] + '|' + board['18'] +    '|' + board['19'] + '|' + board['20'] + '|')
    print('-----------------------')
    print('| 3|' + board['21'] + '|' + board['22'] +    '|' + board['23'] + '|' + board['24'] +    '|' + board['25'] + '|' + board['26'] +    '|' + board['27'] + '|' + board['28'] +    '|' + board['29'] + '|' + board['30'] + '|')
    print('-----------------------')   
    print('| 4|' + board['31'] + '|' + board['32'] +    '|' + board['33'] + '|' + board['34'] +    '|' + board['35'] + '|' + board['36'] +    '|' + board['37'] + '|' + board['38'] +    '|' + board['39'] + '|' + board['40'] + '|')
    print('-----------------------') 
    print('| 5|' + board['41'] + '|' + board['42'] +    '|' + board['43'] + '|' + board['44'] +    '|' + board['45'] + '|' + board['46'] +    '|' + board['47'] + '|' + board['48'] +    '|' + board['49'] + '|' + board['50'] + '|')
    print('-----------------------') 
    print('| 6|' + board['51'] + '|' + board['52'] +    '|' + board['53'] + '|' + board['54'] +    '|' + board['55'] + '|' + board['56'] +    '|' + board['57'] + '|' + board['58'] +    '|' + board['59'] + '|' + board['60'] + '|')
    print('-----------------------')
    print('| 7|' + board['61'] + '|' + board['62'] +    '|' + board['63'] + '|' + board['64'] +    '|' + board['65'] + '|' + board['66'] +    '|' + board['67'] + '|' + board['68'] +    '|' + board['69'] + '|' + board['70'] + '|')
    print('-----------------------')
    print('| 8|' + board['71'] + '|' + board['72'] +    '|' + board['73'] + '|' + board['74'] +    '|' + board['75'] + '|' + board['76'] +    '|' + board['77'] + '|' + board['78'] +    '|' + board['79'] + '|' + board['80'] + '|')
    print('-----------------------')
    print('| 9|' + board['81'] + '|' + board['82'] +    '|' + board['83'] + '|' + board['84'] +    '|' + board['85'] + '|' + board['86'] +    '|' + board['87'] + '|' + board['88'] +    '|' + board['89'] + '|' + board['90'] + '|')
    print('-----------------------')
    print('|10|' + board['91'] + '|' + board['92'] +    '|' + board['93'] + '|' + board['94'] +    '|' + board['95'] + '|' + board['96'] +    '|' + board['97'] + '|' + board['98'] +    '|' + board['99'] + '|' + board['100'] + '|') 
    print('-----------------------')

def cpu_guess(potential_guesses):

    guess=random.choice(potential_guesses)
    #potential_guesses.remove(guess)
    return guess

def remove_from_next_guesses_if_exist(_choice):
   
    hits_and_misses=hits + misses
    for item in _next_guesses:
        if item in hits_and_misses:
            _next_guesses.remove(item)
            
            

def sink_pb(_pb_count, _grid, _key, _pb_squares, _choice):
    _pb_count=len(_pb_squares)
    if _grid[_key]=="p":
        _pb_count-=1
        _pb_squares.remove(_choice)
        if _pb_count==0:
            return True

def sink_destroyer(_dest_count, _grid, _key, _des_squares, _choice):
    _dest_count=len(_des_squares)
    if _grid[_key]=="d":
        _dest_count-=1
        _des_squares.remove(_choice)
        if _dest_count==0:
            return True

def sink_battleship(_bat_count, _grid, _key, _bat_squares, _choice):
    _bat_count=len(_bat_squares)
    if _grid[_key]=="b":
        _bat_count-=1
        _bat_squares.remove(_choice)
        if _bat_count==0:
            return True
        
def sink_carrier(_car_count, _grid, _key, _car_squares, _choice):
    _car_count=len(_car_squares)
    if _grid[_key]=="c":
        _car_count-=1
        _car_squares.remove(_choice)
        if _car_count==0:
            return True

def sink_submarine(_sub_count, _grid, _key, _sub_squares, _choice):
    _sub_count=len(_sub_squares)
    if _grid[_key]=="s":
        _sub_count-=1
        _sub_squares.remove(_choice)
        if _sub_count==0:
            return True

def sink_check(_ship_squares):
    if len(_ship_squares)==0:
        return True

def duplicate_square(ship, _ship_squares):
    ship=ship.upper()
    if ship in _ship_squares:
        return True




def hit(_choice, _ship_squares, _hits, _grid, _key, _last_hit, _pb_count, _pb_squares, _dest_count, _des_squares, _bat_count, _battle_squares, _car_count, _car_squares, _sub_count, _sub_squares ):
    
    print("hit")
    if sink_pb(_pb_count, _grid, _key, _pb_squares, _choice):
        print("You have sunk my patrol boat!")
        
    elif sink_destroyer(_dest_count, _grid, _key, _des_squares, _choice):
        print("You have sunk my destroyer!")
    elif sink_battleship(_bat_count, _grid, _key, _battle_squares, _choice):
        print("You've sunk my battleship!")
    elif sink_carrier(_car_count, _grid, _key, _car_squares, _choice):
        print("You've sunk my carrier!")
    elif sink_submarine(_sub_count, _grid, _key, _sub_squares, _choice):
        print("You've sunk my submarine!")

    _grid[_key]="h"
    _hits.append(_choice)
    _ship_squares.remove(_choice)
    remove_from_next_guesses_if_exist(_choice)
    

    if sink_check(_ship_squares):
       print("You have sunk all my ships!  Game Over")
       print_board(_grid)
       play_again()

    #get cpu to guess smarter!
    _last_hit.append(_choice)
    
    _index=retrieve_key_value(_grid, _last_hit[-1])
    _next=(convert_str_to_int(_index)) + 1
    _prev=(convert_str_to_int(_index)) - 1
    _one_down=(convert_str_to_int(_index)) + 10
    _one_up=(convert_str_to_int(_index)) - 10
    
    _next_right=get_grid_number(_grid, _next)
    _next_left=get_grid_number(_grid, _prev)
    _up_one=get_grid_number(_grid, _one_up)
    _down_one=get_grid_number(_grid, _one_down)
    
    _next_guesses.extend( [ _next_right, _next_left, _up_one, _down_one] )

    remove_improper_move_choices(_next_guesses)
    remove_from_next_guesses_if_exist(_choice)
    
    
    
    
    print_board(_grid)
        

    

def next_guess(_next_guesses):
    next=random.choice(_next_guesses)
    return next


def convert_str_to_int(num):
    int_num=int(num)
    return int_num

    

def retrieve_key_value(sq, value):

    sq={'1': "A1", '2': "B1", '3': "C1", '4': "D1", '5': "E1", '6': "F1", '7': "G1", '8': "H1", '9': "I1", '10': "J1",
           '11': "A2", '12': "B2", '13': "C2", '14': "D2", '15': "E2", '16': "F2", '17': "G2", '18': "H2", '19': "I2", '20': "J2",
               '21': "A3", '22': "B3", '23': "C3", '24': "D3", '25': "E3", '26': "F3", '27': "G3", '28': "H3", '29': "I3", '30': "J3",
                  '31':"A4", '32': "B4", '33': "C4", '34': "D4", '35': "E4", '36': "F4", '37': "G4", '38': "H4", '39': "I4", '40': "J4" ,
                       '41':"A5", '42': "B5", '43': "C5", '44': "D5", '45': "E5", '46': "F5", '47': "G5", '48': "H5", '49': "I5", '50': "J5",
                           '51':"A6", '52': "B6", '53': "C6", '54': "D6", '55': "E6", '56': "F6", '57': "G6", '58': "H6", '59': "I6", '60': "J6" ,
                              '61':"A7", '62': "B7", '63': "C7", '64': "D7", '65': "E7", '66': "F7", '67': "G7", '68': "H7", '69': "I7", '70': "J7" ,
                                   '71':"A8", '72': "B8", '73': "C8", '74': "D8", '75': "E8", '76': "F8", '77': "G8", '78': "H8", '79': "I8", '80': "J8" ,
                                      '81':"A9", '82': "B9", '83': "C9", '84': "D9", '85': "E9", '86': "F9", '87': "G9", '88': "H9", '89': "I9", '90': "J9" ,
                                          '91':"A10", '92': "B10", '93': "C10", '94': "D10", '95': "E10", '96': "F10", '97': "G10", '98': "H10", '99': "I10", '100': "J10"  }
    
    return(list(sq.keys())[list(sq.values()).index(value)])


def get_grid_number(sq, value):
    sq={'1': "A1", '2': "B1", '3': "C1", '4': "D1", '5': "E1", '6': "F1", '7': "G1", '8': "H1", '9': "I1", '10': "J1",
        '11': "A2", '12': "B2", '13': "C2", '14': "D2", '15': "E2", '16': "F2", '17': "G2", '18': "H2", '19': "I2", '20': "J2",
            '21': "A3", '22': "B3", '23': "C3", '24': "D3", '25': "E3", '26': "F3", '27': "G3", '28': "H3", '29': "I3", '30': "J3",
                '31':"A4", '32': "B4", '33': "C4", '34': "D4", '35': "E4", '36': "F4", '37': "G4", '38': "H4", '39': "I4", '40': "J4" ,
                    '41':"A5", '42': "B5", '43': "C5", '44': "D5", '45': "E5", '46': "F5", '47': "G5", '48': "H5", '49': "I5", '50': "J5",
                        '51':"A6", '52': "B6", '53': "C6", '54': "D6", '55': "E6", '56': "F6", '57': "G6", '58': "H6", '59': "I6", '60': "J6" ,
                            '61':"A7", '62': "B7", '63': "C7", '64': "D7", '65': "E7", '66': "F7", '67': "G7", '68': "H7", '69': "I7", '70': "J7" ,
                                '71':"A8", '72': "B8", '73': "C8", '74': "D8", '75': "E8", '76': "F8", '77': "G8", '78': "H8", '79': "I8", '80': "J8" ,
                                    '81':"A9", '82': "B9", '83': "C9", '84': "D9", '85': "E9", '86': "F9", '87': "G9", '88': "H9", '89': "I9", '90': "J9" ,
                                        '91':"A10", '92': "B10", '93': "C10", '94': "D10", '95': "E10", '96': "F10", '97': "G10", '98': "H10", '99': "I10", '100': "J10"  }

    return sq.get(str(value), "none")





def add_battleship(bat_squares, _grid):
    
    arr_ships=True
    while arr_ships:
        _sq=input("Player One, add your battleship (press exit to finish): ")
        _sq=_sq.upper()
        if incorrect_square(_sq):
            print("Invalid square.  Please try again")
            continue

                
        if _sq.upper()=="EXIT":
            arr_ships=False
            break

        bat_squares.append(_sq)
        continue
        
    for _key in _grid.keys():

        for item in bat_squares:


            if _grid[_key]==item:
                _grid[_key]="b"


def add_submarine(_sub_squares, _grid):
    arr_ships=True
    while arr_ships:
        _sq=input("Player One, add your submarine (press exit to finish): ")
        _sq=_sq.upper()  
        
        if _sq=="EXIT":
            arr_ships=False
            break

        _sub_squares.append(_sq)
        continue

    for _key in _grid.keys():

        for item in _sub_squares:


            if _grid[_key]==item:
                _grid[_key]="s"


def add_carrier(_car_squares, _grid):
    arr_ships=True
    while arr_ships:
        _sq=input("Player One, add your carrier (press exit to finish): ")
        _sq=_sq.upper()  
        
        if _sq=="EXIT":
            arr_ships=False
            break

        _car_squares.append(_sq)
        continue

    for _key in _grid.keys():

        for item in _car_squares:


            if _grid[_key]==item:
                _grid[_key]="c"


def add_patrol_boat(_pb_squares, _grid):
    arr_ships=True
    while arr_ships:
        _sq=input("Player One, add your patrol boat (press exit to finish): ")
        _sq=_sq.upper()  
        
        if _sq=="EXIT":
            arr_ships=False
            break

        _pb_squares.append(_sq)
        continue

    for _key in _grid.keys():

        for item in _pb_squares:


            if _grid[_key]==item:
                _grid[_key]="p"


def add_destroyer(_des_squares, _grid):
    arr_ships=True
    while arr_ships:
        _sq=input("Player One, add your destroyer (press exit to finish): ")
        _sq=_sq.upper()  
        
        if _sq=="EXIT":
            arr_ships=False
            break

        _des_squares.append(_sq)
        continue

    for _key in _grid.keys():

        for item in _des_squares:


            if _grid[_key]==item:
                _grid[_key]="d"

def display_ships(_grid):
    for _key in _grid.keys():
        if _grid[_key] !="b" and _grid[_key] !="s" and _grid[_key] !="c" \
            and _grid[_key] !="p" and _grid[_key] !="d":
            _grid[_key]=" "
    print("Here are your ships:")
    print_board(_grid)
    input("Press enter to continue")



def main():
    print("Welcome")
    
    grid={'1': "A1", '2': "B1", '3': "C1", '4': "D1", '5': "E1", '6': "F1", '7': "G1", '8': "H1", '9': "I1", '10': "J1",
           '11': "A2", '12': "B2", '13': "C2", '14': "D2", '15': "E2", '16': "F2", '17': "G2", '18': "H2", '19': "I2", '20': "J2",
               '21': "A3", '22': "B3", '23': "C3", '24': "D3", '25': "E3", '26': "F3", '27': "G3", '28': "H3", '29': "I3", '30': "J3",
                  '31':"A4", '32': "B4", '33': "C4", '34': "D4", '35': "E4", '36': "F4", '37': "G4", '38': "H4", '39': "I4", '40': "J4" ,
                       '41':"A5", '42': "B5", '43': "C5", '44': "D5", '45': "E5", '46': "F5", '47': "G5", '48': "H5", '49': "I5", '50': "J5",
                           '51':"A6", '52': "B6", '53': "C6", '54': "D6", '55': "E6", '56': "F6", '57': "G6", '58': "H6", '59': "I6", '60': "J6" ,
                              '61':"A7", '62': "B7", '63': "C7", '64': "D7", '65': "E7", '66': "F7", '67': "G7", '68': "H7", '69': "I7", '70': "J7" ,
                                   '71':"A8", '72': "B8", '73': "C8", '74': "D8", '75': "E8", '76': "F8", '77': "G8", '78': "H8", '79': "I8", '80': "J8" ,
                                      '81':"A9", '82': "B9", '83': "C9", '84': "D9", '85': "E9", '86': "F9", '87': "G9", '88': "H9", '89': "I9", '90': "J9" ,
                                          '91':"A10", '92': "B10", '93': "C10", '94': "D10", '95': "E10", '96': "F10", '97': "G10", '98': "H10", '99': "I10", '100': "J10"  }
              
    game_on=True
    
    ship_squares=[]
    battle_squares=[]
    sub_squares=[]
    car_squares=[]
    pb_squares=[]
    des_squares=[]
    
    
    

    pb_count=None
    dest_count=None
    bat_count=None
    sub_count=None
    car_count=None
    
    
    add_battleship(battle_squares, grid)
    add_submarine(sub_squares, grid)
    add_carrier(car_squares, grid)
    add_patrol_boat(pb_squares, grid)
    add_destroyer(des_squares, grid)

    ship_squares=list(set(battle_squares +  car_squares + \
         pb_squares+ des_squares))

    

    display_ships(grid)
    
    choice=""
    
    last_hit=[]
    ship_not_hit=True
    
    #cpu guesses squares
    while game_on:
        
        if ship_not_hit or _next_guesses==[]:
            choice=cpu_guess(potential_guesses)
            
            

        else:
            choice=next_guess(_next_guesses)
        #choice="A1"
        key=retrieve_key_value(grid, choice)
        invalid_move_check(grid, key)    
        print_board(grid)
        
        
        ######T test sinking section ########
        # hits=['A2' ]
        # grid['11']="h"
        # # # grid['7']="h"
        # grid['1']="p"
        # grid['46']="b"
        # # # # grid['48']="h"
        # # # # grid['44']="x"
        # # # # grid['50']="x"
        #choice="A1"
        # ship_squares.append(choice)
        # print_board(grid)

        ######T test sinking section ########
        
        print("The computer guesses: ", choice)
        
        
        if choice in ship_squares:
            ship_not_hit=False
            hit(choice, ship_squares, hits, grid, key, last_hit, pb_count, pb_squares, dest_count, des_squares, bat_count, battle_squares, car_count, car_squares, sub_count, sub_squares)
        else:
            print("miss!")

            misses.append(choice)
            remove_from_next_guesses_if_exist(choice)
        
            if grid[key]==" ":
                grid[key]="x"



        input("Press enter to continue")
        
    print_board(grid)
    
    
main()
