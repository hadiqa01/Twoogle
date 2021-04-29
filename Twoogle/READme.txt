
First, you'll need to install python virtual environment with:
```
install python-venv
```


#NOTES#
=========
## Assuming you already have python virtual environment:
1.  Open Powershell in Administrator mode or just cmd and then run these commands:
cd "C:\Users\Hadiqa\Documents\ECU courses\Fall2021\Web app\hw5\hw5" (this is the directory where main.py is located)

2.  Create a virtual environment:
	  python -m venv python_venv

3.  set-executionpolicy remotesigned

4.  activate the virtual environment	
	  .\python_venv\Scripts\activate

5.  To fufil all the requirements for the python server, you need to run:
	   pip3 install -r requirements.txt

6.  pip install --upgrade pip

7.  source python_venv/bin/activate

8.  python main.py