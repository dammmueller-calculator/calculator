build:
	python setup.py install 
	pyinstaller --onefile --noconsole --name=calculator --hidden-import=PyQt6.sip main.py
