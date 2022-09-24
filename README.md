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
```
python -m venv venv
call venv\Scripts\activate.bat
python main.py

deactivate
```

### MacOS
# First time:
# For M1 chips follow: https://stackoverflow.com/questions/65901162/how-can-i-run-pyqt5-on-my-mac-with-m1chip-ppc64el-architecture

# Upgrade pip if necessary
$ python3 -m pip install --upgrade pip

# Run instr:
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
