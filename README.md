# Advanced Chess App (Pygame)

---

## 📌 Project Overview

This project is a feature-rich, 2-player Chess Application built using Python and Pygame. Originally developed as a university project (Project 3), it focuses on creating a functional game interface with consistent physical-world rules, custom graphics, and an intuitive user experience.

The app features a complete implementation of chess logic, including special moves like castling and en passant, a side panel for game rules, and the ability to toggle between different aesthetic piece sets.

---

## 🎓 Acknowledgments & Assets

A huge shout-out to the following resources that provided the foundation and assets for this project:

- Logic & Foundation: Inspired by `LeMaster Tech`. While the base code was used as a starting point, I heavily modified and expanded it to include complex game rules (illegal moves, castling, promotion) and UI enhancements.
  
- Video Link: [How to Make Chess in Python! - LeMaster Tech](https://youtu.be/X-e0jk4I938)
  
- Github: [pygameChess - LeMaster Tech](https://github.com/plemaster01/pygameChess.git)
  
- Primary Assets: Graphics for the standard piece set were provided by `LeMaster Tech`.
  
- Alternate Assets: The SVG piece set was sourced from [`Green Chess`](https://greenchess.net/info.php?item=downloads), specifically the `Standard chess pieces [SVG]`.

---

## 🛠 Tech Stack

- Language: `Python`

- Library: `Pygame` (for graphics, event handling, and game loop)

- Graphics: `PNG` & `SVG` (Standard and Alternate piece sets)

- Environment: `Virtual Environment` (venv)

---

## 🚀 Key Features

I implemented several advanced features that were missing from the original foundation to meet uni project requirements:

- Complete Chess Rules:

	- Illegal Move Prevention: The system calculates valid moves and prevents any piece from moving to a square that violates chess rules or leaves the king in check.

	- Castling: Support for both Short Castling (King-side) and Long Castling (Queen-side).

	- En-Passant: Fully functional pawn capture mechanics.

	- Pawn Promotion: When a pawn reaches the back rank, a UI menu allows the player to choose a new piece.

- Enhanced UI/UX:

	- Side Panel Instructions: A dedicated area displaying rules and game status.

	- Change Piece Set: A toggle button to switch between the default PNG set and the alternate SVG set.

	- Game Controls:

		- Reset Button: Quickly restarts the game to the initial state.
		
		- Resignation/Draw: Functional buttons and logic for ending games.

	- Check/Checkmate Indicators: Visual flashing and victory messages.

- Demo Video: [CS 335 Advanced Chess App DEMO](https://youtu.be/bkTYcTyMHc0)

---

## 🏗 Setup & Implementation Guide

1. Create a Virtual Environment in the path you open the file:
	
	- macOS/Linux:

	  ```bash	
	  python3 -m venv venv
	  source venv/bin/activate

   	> To exit from the virtual environment just type `deactivate` in the command shell and press enter
	
	- Windows:

	  ```powershell	
	  python -m venv venv
	  .\venv\Scripts\activate

2. Install Homebrew (optional but recommended):

   - macOS/Linux:
     
	 ```bash
	 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   - Windows: On Windows, you can use Chocolatey as a package manager.
     	
		> Note: If you prefer to use Homebrew on Windows, consider installing it via WSL (Windows Subsystem for Linux) and following the macOS instructions within your WSL terminal.
     
	    > Open PowerShell as Administrator.
     
	    - Run the following command to install Chocolatey:
        
	      ```powershell
		  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

	 	- Close and reopen your PowerShell, then verify Chocolatey is installed:
   	  
          ```powershell
		  choco --version

3. Install Dependencies:

   > First, make sure pip is updated:
		
   - macOS/Linux:
     
	 ```bash	
	 python3 -m pip install --upgrade pip
	 pip --version
	 pip install pygame

   - Windows:
     
	 ```powershell	
	 python -m pip install --upgrade pip
	 pip --version
	 pip install pygame

4. To run the code:
   
	 - macOS/Linux:

	   ```bash	
	   python3 chess_app.py

	- Windows:

	  ```powershell
	  python chess_app.py

---

## 📂 Repository Structure

```text
CS-335-Advanced-Chess-App/
│
├── datasets/                 
│   ├── dataset_1/           	# Standard PNG piece set (from LeMaster Tech)
│   └── dataset_2/           	# Alternate SVG piece set (from Green Chess)
│
├── docs/                    
│   └── project_3.docx       	# Original University Project Requirements
│
├── scripts/                 
│   └── chess_app.py         	# Main Game Engine and Logic
│
├── README.md                	# Project overview and instructions
└── LICENSE         			# License information for the repository
```

---

## 📊 Project Grading Criteria (Project 3)

The project was designed to satisfy the following university requirements:

|Category | Description| Points|
| :--- | :---: | ---: |
|Game Play| "Rules consistency, Repeated play, Reset option" | 20 |
|Ease of Use | "Instructions, Labeled Buttons, Side Panel" |10 |
|Graphics | "Differentiated pieces, Graphic images, Changing board" | 25 |
|Comments | Code documentation and group listing | 5 |

> I got a 113.3% on this project!

---

> Developed as part of my Software Engineering CourseWork at the University of Kentucky
