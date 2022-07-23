## AI Image Webscraper

The AI Image Webscraper is a simple command line interface webscraper that allows the user to easily and seamlessly download hundreds of images from the internet. It is currently compatible with Microsoft Edge, Mozilla Firefox, and Google Chrome, and is able to scrape images from DuckDuckGo images and Google images.  The motivation for writing this program was to easily acquire large numbers of relevant images to use for training an artificial intelligence.

### Installation Steps:

These packages/programs **must** be downloaded and installed for the webscraper program to function.

1.  **Python 3.7** or higher:  [https://www.python.org/downloads/](https://www.python.org/downloads/)
    *   Python must be installed on the computer.
2.  **AI Image Webscraper**:
    *   Download this project from github and place it in the desired destination folder.
3.  **Selenium Webdriver**: [https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)
    *   Download the webdriver software and place it in the same folder as the AI Image Webscraper program.
4.  Install the **selenium** python package
    *   From the command line, type: _pip install selenium_
5.  Install the **requests** python Package
    *   From the command line, type: _pip install requests_

### Usage:

1.  Open a command prompt.
2.  Change to the directory holding the webscraper program.
3.  To scrape Duckduckgo images, type: _python webscraping\_duckduckgo.py_
    1.  At the prompt, enter the type of image to scrape.
    2.  At the prompt, enter the number of pages of images to retrieve.
4.  To scrape Google images, type: _python webscraping\_google.py_
    1.  At the prompt, enter the type of image to scrape.
    2.  At the prompt, enter the number of pages of images to retrieve.

### Troubleshooting:

*   While downloading image files, the browser opened by the webscraper, the webscraper application, and the webdriver executable must be left open.
*   Verify that the Selenium webdriver and webscraper python programs are in the same directory.
*   Verify that you have one of the supported browsers installed.
*   From the webscraper program:
    *   The number of pages to scrape must be greater than one
    *   Do not use any characters that cannot be used in file names - doing so may result in a saving error (spaces are compatible)
    *   Verify that your search keyword query results in the desired images in the web browser
*   Some image files may not be compatible for downloading - attempting to download these files may cause lag in the download process.