Before running the following commands, make sure you have python virtual environment
installed in your computer. 


#NOTES#
=========
## If you already have python virtual environment:

1.  Open Powershell in Administrator mode or just cmd and then run these commands:
cd "C:\.........." (this is the directory where main.py is located)

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

9. It'll give you something like that 127.0.0.1:5000/ which will be your local host. Just copy /paste the link in your browser. 
