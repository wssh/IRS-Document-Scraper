IRS Document Webscraper

Python Version: Python 3.95

Requirements:
Requests 2.25.1
BeautifulSoup 4.9.3


Min + Max Date Scrape:
Input Method: 
To input data into the script, you enter one form number (i.e Form W-2 or Publ 17) that you want to fetch the data of on a line of the input text file (input.txt).
Every input is separated by a new line, so you may enter multiple forms names on input.txt

Output Method:
All of the requested data will be outputted into a json object inside the "json" folder, formatted as requested.

Document Download:
Input Method:
Using the same input.txt file, you enter one form number (i.e Form W-2 or Publ 17), followed by the minimum year of the document that you want, followed by the maximum year of the document that you want.
In reality, it input orders of the years do not matter since my script will run a min() function to separate the minimum year and maximum year.
These three values are to be inputted on the same line, separated by commas. You may enter spaces in between the commas, but they will be stripped by the script if they exist.

Output Method:
All of the requested PDF documents will be downloaded, and placed in the "download" folder, with their names formatted as requested.
