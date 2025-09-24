# 🐍 Snake Game (Python, Turtle, OOP)

This project is a modern, event-driven, **Object-Oriented** implementation of the classic Snake Game using Python’s `turtle` graphics.  

It follows **OOP best practices**:  
- **Data Abstraction**: Game logic is encapsulated in classes (`Snake`, `Food`, `Scoreboard`, `Game`).  
- **Encapsulation & Information Hiding**: Internal state is private (`_attributes`), exposed only via properties/methods.  
- **Pythonic getters/setters**: Read-only access is provided via `@property` (e.g. `snake.head`, `food.position`), instead of explicit getters and setters.  

---

## 📂 Modules Overview

- **`snake.py`** → Snake body, movement, growth, collision detection.  
- **`food.py`** → Food item that spawns randomly.  
- **`scoreboard.py`** → Score tracking and game over messages (with blinking text).  
- **`game.py`** → Orchestrates the game: screen setup, loop, event handling.  
- **`main.py`** → Entry point (launches the game).  

---

## Installation

- Clone this repo and navigate to the project folder
- Use Python 3.8.5 from [pyenv] [pip](https://github.com/pyenv/pyenv)
- Create a virtual environment usinng [venv](https://docs.python.org/3/library/venv.html)
- Install requirements.txt

```bash
python3 -m pip install -r requirements.txt
```
- Enjoy

```bash
python3 main.py
```

## UML Class Diagram

```mermaid
classDiagram
    class Game {
        - Screen _screen
        - Snake _snake
        - Food _food
        - Scoreboard _scoreboard
        - int _speed
        - bool _paused
        + screen
        + __init__(width, height, bg_color, title, speed)
        + _setup_controls()
        + _unpause()
        + _check_collisions()
        + _game_loop()
    }

    class Snake {
        - List<Turtle> _segments
        - Turtle _head
        + head
        + __init__()
        - _create_snake()
        - _add_segment(position)
        + reset()
        + extend()
        + move()
        + up()
        + down()
        + left()
        + right()
        + collided_with_wall() bool
        + collided_with_self() bool
    }

    class Food {
        - Turtle _turtle
        + position
        + __init__()
        + refresh()
        + distance_to(other) float
    }

    class Scoreboard {
        - int _score
        + __init__()
        + increase_score()
        + reset()
        + game_over(screen)
    }

    Game --> Snake
    Game --> Food
    Game --> Scoreboard
```

## Sequence Diagram – Game Loop Iteration

```mermaid

sequenceDiagram
    participant User as Player
    participant Game as Game
    participant Snake as Snake
    participant Food as Food
    participant Scoreboard as Scoreboard
    participant Screen as Screen

    User->>Game: (Timer triggers _game_loop)
    Game->>Snake: move()
    Snake-->>Game: (snake advanced)
    
    Game->>Food: distance_to(Snake.head)
    Food-->>Game: < 15 ? (True/False)

    alt Snake eats food
        Game->>Food: refresh()
        Game->>Snake: extend()
        Game->>Scoreboard: increase_score()
    end

    Game->>Snake: collided_with_wall()
    Snake-->>Game: True/False
    Game->>Snake: collided_with_self()
    Snake-->>Game: True/False

    alt Collision detected
        Game->>Scoreboard: game_over(Screen)
        Game->>Game: set _paused = True
    end

    Game->>Screen: update()
    Game->>Game: schedule next _game_loop via ontimer
```

## State Diagram – Gameplay Lifecycle

```mermaid

stateDiagram-v2
    [*] --> Running : Game starts

    Running --> Paused : Snake hits wall or self
    Paused --> Running : Player presses any key (restart)

    Running --> Running : Snake eats food / moves
    Paused --> [*] : Player closes window
```

## License

[MIT](https://choosealicense.com/licenses/mit/)