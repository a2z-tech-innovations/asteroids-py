# Asteroids Game

A modern Python implementation of the classic Asteroids arcade game using Pygame.

## Description

This is a recreation of the 1979 classic arcade game Asteroids. Players control a spaceship in an asteroid field, where they must shoot and destroy asteroids while avoiding collisions. As asteroids are shot, they split into smaller pieces, increasing the challenge.

## Features

- Classic arcade-style gameplay
- Vector-based physics movement
- Asteroid splitting mechanics
- Player ship with thrust and rotation controls
- Shooting mechanics
- Score tracking
- Lives system

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/asteroids-game.git
cd asteroids-game
```

2. Install the required dependencies:
```bash
pip install pygame
```

## How to Play

Run the game:
```bash
python main.py
```

### Controls

- **Arrow Up**: Thrust forward
- **Arrow Left/Right**: Rotate ship
- **Spacebar**: Fire bullets
- **ESC**: Quit game

### Game Rules

- Destroy asteroids to earn points
- Large asteroids split into smaller ones when shot
- Avoid colliding with asteroids
- You start with 3 lives
- Game ends when all lives are lost

## Project Structure

```
asteroids-game/
│
├── main.py              # Main game loop and initialization
├── player.py            # Player ship class
├── asteroid.py          # Asteroid class
├── bullet.py            # Bullet class
├── vector.py            # Vector mathematics
├── constants.py         # Game constants and settings
└── README.md           # This file
```

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for bugs or feature suggestions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Improvements

- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped
