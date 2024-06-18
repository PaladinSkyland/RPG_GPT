# RPGPT

## Overview

RPGPT is a Python console-based role-playing game that integrates OpenAI's GPT to create a dynamic and interactive text adventure experience. The game features a rich environment where players can interact with the world, engage in combat with enemies, and progress through various levels.

## Game Features

- **Dynamic Story Generation**: Utilizes OpenAI's GPT to generate the story elements and game responses dynamically based on the player choices. This provides a really unique narrative experience where no two games will ever be the same and where the player can continue to explore for as long as he wants.
  
- **Combat System**: Engage in battles with enemies, each one being unique as they are also generated on the fly by the AI. The player can earn experience points and gold by defeating enemies, helping him progress through the game.
  
- **Player Progression**: Level up your character by gaining experience points, increasing your health, attack, and defense attributes.

## Project Architecture

### Files and Modules

- **Context.py**: Manages the overall game context, including the current state, environment descriptions, and an history of the last choosen actions.

- **CustomLiveable.py**: handles rendering the game state to the console using the `rich` library for enhanced text formatting.

- **Enemy.py**: Contains the logic and attributes for enemy characters within the game, including their health, attack, defense, and experience points. This module uses classes to encapsulate enemy behavior and state.

- **Player.py**: Manages the player character, including attributes such as health, attack, defense, level, experience, and gold. It also defines player actions and interactions with the game world.

- **KeyboardInput.py**: Handles keyboard inputs from the user, interpreting them to control the player or other aspects of the game. It uses multiple native libraries like `msvcrt` and `termios` to capture and process keypress events on different types of OS.

- **OpenAI.py**: Integrates OpenAI functionalities to generate dynamic story elements and game responses based on player input. This module uses the `openai` library to interact with the GPT API and generate custom responses using some predefined prompts.

- **prompt.json**: Contains predefined prompts and configurations used by the OpenAI module to generate responses and shape the game narrative.

- **.env.example**: Provides an example environment file to configure the OpenAI API key.

- **main.py**: The entry point of the application. It initializes the game context, sets up the player, and starts the main game loop. This script is responsible for orchestrating the overall flow of the game.


### Technologies Used

- **Python**: The programming language used for developing the game.
  
- **Rich**: A Python library used for rendering rich text and beautiful formatting in the terminal. It is utilized in `CustomLiveable.py` for displaying game information, player and enemy stats, and other text-based UI elements.
  
- **OpenAI API**: The API used to interact with OpenAI's GPT-3.5 model. This integration is managed in `OpenAI.py` with the `openai` python library and allows the game to generate dynamic story elements and responses based on player input.

## How to Use

### Prerequisites

Ensure you have Python and git installed on your system.

### Setup

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```sh
   git clone https://github.com/PaladinSkyland/RPG_GPT.git
   ```

2. **Navigate to the Project Directory**

   ```sh
   cd RPG_GPT
   ```

3. **Install Dependencies**

   Install the necessary dependencies. You might have a `requirements.txt` or a `Pipfile` for this. For example:

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Copy the `.env.example` file to `.env` and update it with your OpenAI API key:

   ```sh
   cp .env.example .env
   ```

   Open the `.env` file in a text editor and replace `<your-api-key>` with your actual OpenAI API key:

   ```env
   OPENAI_API_KEY=<your-api-key>
   ```

### Running the Project

To start the game, execute the `main.py` script:

```sh
python main.py
```

This will initialize the game context and enter the main game loop where you can interact with the game using your keyboard.

### Game Controls

Controls for the game will be handled via keyboard input. The following controls are available:
- Numbers (1-9): Select an action from the list of possible actions.
- Up/Down Arrows: Navigate through the list of actions.
- Return/Enter: Validate and execute the chosen action.
- Escape (Esc): Quit the game.
- Delete/Suppr: Clear the current selection.
