# Instagram Tool

## Overview

Instagram Tool is a Python-based application designed to help you follow people on Instagram based on their following. This tool allows accounts to find other accounts with similar interests using headless Selenium to access Instagram pages. 

## Features

- **Automated Following**: Automatically follow users based on specified criteria.
- **Headless Browsing**: Uses headless Selenium for efficient and invisible web automation.
- **Interest-Based Discovery**: Helps find and follow accounts with similar interests.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Omkar-Dh/Instagram-Tool.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Instagram-Tool
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    Ensure you have [Python](https://www.python.org/downloads/) installed.

4. Download the appropriate WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Chrome).

## Usage

1. Add your Instagram credentials and home page in the `main.py` file:
    ```python
    username = "your_username"
    password = "your_password"
    home_page = "https://www.instagram.com/your_home_page/"
    ```
2. Run the application:
    ```bash
    python main.py
    ```
3. The tool will start following users based on the specified criteria.

## Example

Here is an example of how to use the Instagram Tool to follow accounts:

```python
username = "your_username"
password = "your_password"
home_page = "https://www.instagram.com/your_home_page/"
