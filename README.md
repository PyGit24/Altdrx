Readme instructions on how to install, set up, and run the automated test scripts for the flows on Altdrx.com.

README: Automated Testing Scripts for Altdrx.com

 Introduction
This document provides stepbystep instructions for installing, setting up, and running automated test scripts using Python and Selenium for the Altdrx.com website. The flows covered include SignUp, Login, KYC Verification, Add Funds, and Tradex Buy.

 Prerequisites
 Python 3.x
 Google Chrome Browser
 ChromeDriver (compatible with your Chrome version)
 Pip (Python package installer)

 Installation

1. Install Python 3.x
   Download and install the latest version of Python from [here](https://www.python.org/downloads/).

2. Install Google Chrome
   Ensure you have the latest version of Google Chrome installed. If not, download it from [here](https://www.google.com/chrome/).

3. Download ChromeDriver
    Determine your Chrome browser version by navigating to `chrome://settings/help` in Chrome.
    Download the corresponding ChromeDriver version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    Extract the downloaded file and place it in a known directory.

4. Install Selenium
   Open a terminal or command prompt and run the following command:
   pip install selenium
   
 Setup

1. Clone the Repository
   Clone the repository containing the test scripts (or create a new directory and save the scripts provided above):
   git clone https://github.com/yourrepository/altdrxautomationtests.git
   
   Navigate to the directory:
   cd altdrxautomationtests
   

2. Update the ChromeDriver Path
   In each script file (`signup_Flow.py`, `login_Flow.py`, `kyc_VerificationFlow.py`, `add_fundsFlow.py`, `tradex_buyFlow.py`), ensure the path to `ChromeDriver` is correctly specified:
  
   driver = webdriver.Chrome('/path/to/chromedriver')
   
 Running the Scripts

1. SignUp Flow
   Run the following command to execute the SignUp flow test script:
   
   python signup_Flow.py
   

2. Login Flow
   Run the following command to execute the Login flow test script:
   
   python login_Flow.py
   

3. KYC Verification Flow
   Run the following command to execute the KYC Verification flow test script:
   
   python kyc_VerificationFlow.py
   

4. Add Funds Flow
   Run the following command to execute the Add Funds flow test script:
   
   python add_fundsFlow.py
   

5. Tradex Buy Flow
   Run the following command to execute the Tradex Buy flow test script:
   
   python tradex_buyFlow.py
   

Conclusion
By following the above instructions, you should be able to successfully install, set up, and run the automated test scripts for Altdrx.com. Feel free to reach out if you encounter any issues or need further assistance.
