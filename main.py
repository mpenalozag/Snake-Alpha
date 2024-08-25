from time import sleep
from game import Game

game = Game()

import curses


def pbar(window):
    curses.cbreak()
    window.nodelay(True)
    last_key = 100
    while True:
        window.clear()
        if game.player.alive == False:
            break
        window.addstr("Score: " + str(game.player.size) + "\n")
        window.addstr(game.map.__str__())
        key = window.getch()
        if key != -1: 
            last_key = key
        if last_key == 119:
            game.move_player("up")
        elif last_key == 115:
            game.move_player("down")
        elif last_key == 97:
            game.move_player("left")
        elif last_key == 100:
            game.move_player("right")
        window.refresh()
        sleep(0.065)
    window.clear()
    window.addstr("Game Over!")
    window.refresh()
    sleep(2)

curses.wrapper(pbar)