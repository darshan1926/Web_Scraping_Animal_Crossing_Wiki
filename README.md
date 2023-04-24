# Web scraping using bautiulsoupgit 
## Agenda:
        What is web scraping?
        What is Beautifullsoup?
        Creating a Python environment?
        Connect with github?
        Creating custom exception handaling file with logger file?
        Build Web scraping program using Beautifulsoup?
## What is web Scraping?
    Web scraping is the process of extracting data from websites by using automated software tools. The data that is extracted can be in various formats such as HTML, XML, or other structured data formats. The goal of web scraping is to collect large amounts of data quickly and efficiently, which can then be used for analysis, research, or any other purpose.

    Web scraping involves sending requests to a website and parsing the HTML or XML content to extract the desired information. This can be done using programming languages like Python, Java, or Ruby, and popular libraries such as Beautiful Soup, Scrapy, and Selenium. However, it is important to note that web scraping can sometimes be illegal or unethical if it violates a website's terms of service or involves collecting personal information without permission.
## What is Beautifulsoup?
    Beautiful Soup is a popular Python library used for web scraping purposes. It is used to extract data from HTML and XML documents by providing methods for parsing and traversing the DOM tree (Document Object Model) of the HTML/XML file.

    Beautiful Soup makes it easy to extract specific pieces of data from a web page by allowing users to search the DOM tree using CSS selectors, regular expressions, or by the tag name. It also provides methods for modifying the parsed HTML/XML data if needed.
## Creating Python environment in anaconda promte?
    Creating a Python environment in Anaconda is useful when you want to have multiple Python environments with different versions and packages installed on the same machine. This can be particularly helpful when working on different projects that require different versions of Python and different sets of packages.

    To create a new Python environment in Anaconda, I am useing the following steps:

    Open the Anaconda prompt or terminal window.

    Type the following command to create a new environment with a specified Python version (replace <env_name> with your desired environment name and <python_version> with the version you want to use):

    conda create --name <env_name> python=<python_version>

    Press Enter to create the new environment. Once it's created, you can activate it using the following command:

    conda activate <env_name>

    Now you can install the packages required for your project within this environment, without worrying about affecting the other  environments or the system-wide Python installation.

    By creating a separate environment for each project, you can avoid version conflicts between packages, which can be a common issue when working with Python projects. This allows you to maintain a clean and organized development environment that can be easily replicated on other machines.
## Connecting Github repository to the project in visual code?
    To connect a Github repository to a project in Visual Studio Code, you can follow these steps:

    Open Visual Studio Code and navigate to your project.
    Click on the Source Control icon on the left-hand side of the window (it looks like a branch with a circle around it).
    Click the "Initialize Repository" button to initialize a new Git repository for your project.
    Once the repository has been initialized, click the ellipsis button (...) next to the "Changes" heading and select "Publish to Github".
    If you are not already logged in to Github, you will be prompted to log in. Once you have logged in, you can select the repository you want to publish your code to, or create a new repository if needed.
    Once you have selected the repository, click the "Publish Repository" button to push your code to Github.
## Creating custom exception handaling file with logger file?
    Custom exception handling allows you to handle errors and exceptions in a way that is specific to your project's needs. By defining your own custom exceptions, you can provide more meaningful error messages to your users and handle errors in a way that is consistent with the rest of your project.

    A logger file is important for recording events, errors, and other information about your project. By using a logger, you can track how your code is performing, debug errors more easily, and monitor system performance.
    

    Custom Exception program:
        import sys
        from src.logger import logging

        def error_message_detail(error,error_detail:sys):
        _,_,exc_tb=error_detail.exc_info()
            file_name=exc_tb.tb_frame.f_code.co_filename
            error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
            file_name,exc_tb.tb_lineno,str(error))

        return error_message

    

        class CustomException(Exception):
            def __init__(self,error_message,error_detail:sys):
            super().__init__(error_message)
            self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
            def __str__(self):
            return self.error_message
    Logger program:
        import logging
        import os
        from datetime import datetime

        LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
        os.makedirs(logs_path,exist_ok=True)    

        LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

        logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,


        )
## Build Web scraping program using Beautifulsoup?
    Install the required libraries: requests and BeautifulSoup.
    Retrieve the HTML content of the Animal Crossing Wiki page.
    Parse the HTML content using BeautifulSoup to extract the URLs of all articles on the page.
    Retrieve the HTML content of each article URL and parse it using BeautifulSoup to extract the title, summary, and content of the article.
    Store the extracted data in a collection of documents.
    Set up the scraper to run weekly and report any changes.