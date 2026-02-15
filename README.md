Run these commands in terminal/powershell ;)

1. Create a Virtual Environment in the path you open the file:
	
	a. macOS / Linux:
		
		python3 -m venv venv
		source venv/bin/activate
	
	b. Windows:
		
		python -m venv venv
		.\venv\Scripts\activate

2. Install Homebrew (optional but recommended):

	a. macOS:
	
		/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

	b. Windows: On Windows, you can use Chocolatey as a package manager. (Note: If you prefer to use Homebrew on Windows, consider installing it via WSL (Windows Subsystem for Linux) and following the macOS instructions within your WSL terminal.)

	   1. Open PowerShell as Administrator.
	   2. Run the following command to install Chocolatey:
	
		Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

	   3. Close and reopen your PowerShell, then verify Chocolatey is installed:

		choco --version

3. Install Dependencies: First, make sure pip is updated:
		
	a. macOS/Linux
		
		python3 -m pip install --upgrade pip
		pip --version
		pip install pygame

	b. Windows
		
		python -m pip install --upgrade pip
		pip --version
		pip install pygame

4. To run the code:
	
	a. macOS/Linux
		
		python3 Project3.py

	b. Windows

		python Project3.py 

#To exit from the virtual environment just type "deactivate" in the command shell and press enter
