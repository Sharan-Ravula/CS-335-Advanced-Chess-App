# Advanced Chess App: By Sharan Ravula

---

> Run these commands in terminal/powershell ;)

---

1. Create a Virtual Environment in the path you open the file:
	
	- macOS / Linux:

	  ```bash	
	  python3 -m venv venv
	  source venv/bin/activate
	
	- Windows:

	  ```powershell	
	  python -m venv venv
	  .\venv\Scripts\activate

2. Install Homebrew (optional but recommended):

   - macOS:
     
	 ```bash
	 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   - Windows: On Windows, you can use Chocolatey as a package manager.
     	
		> (Note: If you prefer to use Homebrew on Windows, consider installing it via WSL (Windows Subsystem for Linux) and following the macOS instructions within your WSL terminal.)
     
	    - Open PowerShell as Administrator.
	    - Run the following command to install Chocolatey:
        
	      ```powershell
		  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

	 	- Close and reopen your PowerShell, then verify Chocolatey is installed:
   	  
          ```powershell
		  choco --version

3. Install Dependencies: First, make sure pip is updated:
		
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
	   python3 Project3.py

	- Windows:

	  ```powershell
	  python Project3.py 

> To exit from the virtual environment just type `deactivate` in the command shell and press enter
