# YouTube Video Viewer Bot

## Description

This is an automated bot that repeatedly plays a YouTube video using Selenium WebDriver. It opens an incognito Chrome browser, navigates to the specified video, plays it for a short duration, then closes the browser and repeats the process.

## Requirements

- Python 3
- Google Chrome
- Chrome WebDriver
- Selenium
- PyAutoGUI

## Installation

1. Install the required Python libraries:

   ```sh
   pip install selenium pyautogui
   ```

2. Download and install [Chrome WebDriver](https://sites.google.com/chromium.org/driver/).
   Ensure it matches your installed Chrome version and add it to your system PATH.

## Usage

Save the following script as `youtube_viewer.py`:

```python
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.chrome.options import Options

while True:
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  
    pyautogui.moveTo(1052, 555)
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_position(-2000, 0)
    driver.get("https://www.youtube.com/watch?v=rhktxR2qrZ0")
    
    driver.find_element(By.CSS_SELECTOR, ".ytp-play-button").click()

    time.sleep(15)
    driver.quit()

    pyautogui.moveTo(1035, 467, duration=0.8)
```

Run the script with:

```sh
python youtube_viewer.py
```

## Disclaimer

This script is for educational purposes only. Using automated bots to manipulate YouTube views may violate YouTube's terms of service and could result in penalties, including bans. Use responsibly.

## License

This project is licensed under the MIT License.

