# Sun Devil Motorsports Data Studio
## Build Instructions
These instructions are for people developing SDM Data Studio.
If you wish to install it, follow the instructions at TODO.
### Linux
```bash
# Create virtual environment
$ python3 -m venv venv

# Start virtual environment
$ source venv/bin/activate

# Install requried packages (only required on first run)
$ pip install -r requirements.txt

# Run the program
$ python3 src/main.py

# Or, run pyqtgraph examples
$ python3 src/examples.py

# Build the installer
$ pyinstaller main.spec

# Leave the virtual environment
$ deactivate
```
### Windows
```bat
:: First time setup:
:: Create virtual environment
python -m venv venv

:: install requirements (if you have errors here, try python -m pip install -r requirements.txt)
:: (only required on first run)
pip install -r requirements.txt

:: Run instructions:
:: start virtual environment
call venv\Scripts\activate.bat

:: Run the program
python src\main.py

:: Or, run pyqtgraph examples
python src\examples.py

:: Build the executable
pyinstaller main.spec

:: Leave virtual environment
deactivate
```

### MacOS
```
# First time:
# For M1 chips follow: https://stackoverflow.com/questions/65901162/how-can-i-run-pyqt5-on-my-mac-with-m1chip-ppc64el-architecture

# Upgrade pip if necessary
$ python3 -m pip install --upgrade pip

# Run instructions:
# Create virual environment
$ /usr/bin/python3 -m venv venv

# Install required packages
$ python3 -m pip install -r requirements.txt

# Run the Plotter Utility
$ python3 main.py

# Or, run pyqtgraph examples
$ python3 examples.py

# Leave the virtual environment
$ deactivate
```