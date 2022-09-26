# Sun Devil Motorsports Plotter Utility
## Instructions
### Linux
```bash
# Create virtual environment
$ python3 -m venv venv

# Start virtual environment
$ source venv/bin/activate

# Install requried packages
$ pip install -r requirements.txt

# Run the Plotter Utility
$ python3 main.py

# Or, run pyqtgraph examples
$ python3 examples.py

# Leave the virtual environment
$ deactivate
```
### Windows
```bat
:: First time setup:
:: Create virtual environment
python -m venv venv

:: install requirements (if you have errors here, try python -m pip install -r requirements.txt)
pip install -r requirements.txt

:: Run instructions:
:: start virtual environment
call venv\Scripts\activate.bat

:: Run the Plotter Utility
python main.py

:: Or, run pyqtgraph examples
python examples.py

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