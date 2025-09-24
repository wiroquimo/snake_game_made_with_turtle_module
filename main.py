#!/usr/bin/env python3
"""
main.py

Launch fully asynchronous, OOP-pure Snake game.
"""

from game import Game

if __name__ == "__main__":
    game = Game()
    game.screen.mainloop()  # Start event loop
