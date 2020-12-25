# Table of Contents
1. [About The Project](#project)
    - [Built With](#built)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Usage](#usage)
4. [Contact](#contact)

## About the Project <a name=project></a>
-------------------------------
![scraping image](https://miro.medium.com/max/486/1*lWPJJxqnFBA54PB6vyHlRg.gif)

This project scrapes data from *[coinranking.com](#https://coinranking.com)* handles pagination, cleans up the data and saves it to a data set that can be stored as a **csv** or **json** file.

The aspect that I'm most proud of is that this **spider crawls on 215 pages** and gets information on over **10,730 different cryptocurrencies.** To achive this I used the *[xpath](https://www.w3schools.com/xml/xpath_intro.asp)* syntax which in my opinion is much more powerful than css selectors on querying data from a website and also transforming and cleaning up the information regardless of the programming language used to fetch the information.

## Getting Started <a name=getting-started></a>
-------------------------------------
To get a local copy up and running follow these simple example steps.

### Built With <a name=built></a>
I used mostly scrapy, An open source and collaborative python framework for extracting the from website. Scrapy is fast, simple and extensible. Also venv  was used to create a virtual environment and handle dependencies.
 
 - [scrapy](#https://scrapy.org/)
 - [venv](#https://docs.python.org/3/library/venv.html)

 ### Prerequisites <a name=prerequisites></a>
 - [Python 3](#https://www.python.org/downloads/)
 - the latest version of [pip](#https://pip.pypa.io/en/stable/installing/)

 ### Installation <a name=installation></a>
  1. Clone the Repo
  ``` 
    git clone https://github.com/your_username_/Project-Name.git
  ```
  2. Install the Python Modules
  ```python
    pip install -r requirements.txt
  ```
## Usage <a name=usage></a>
-----------------
  cd into the project folder **coinranking** and run the command in your terminal: 
  ```
    scrapy crawl coin -o dataset.json
  ``` 
  You could also change the file extension to **.csv** if you rather have a spreadsheets with all the values.

## Contact <a name=contact></a>
---------------------
Bryant Novas - [Linkedin](#https://www.linkedin.com/in/bryantnovas/)
