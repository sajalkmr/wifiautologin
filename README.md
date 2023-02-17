<h1>Wifi Login Automation with Selenium</h1>
<p>A script that automates the login process of a website using Selenium webdriver. Originally built to login to my hostel wifi automatically.</p>
<br>
<h1>Getting Started</h1>

<br>
<br>

<h2>Requirements</h2>
<ul>
  <li>Latest version of <a href="https://www.python.org/downloads/">Python</a> installed and added to PATH</li>
  <li>Google Chrome <a href="https://www.google.com/intl/en_in/chrome/">Browser</a></li>
  <li>Chromedriver.exe (Get the version compatible with your Chrome Version <a href="https://chromedriver.chromium.org/downloads">here</a>)</li>
  <li><a href="https://pip.pypa.io/en/stable/installation/">pip</a> installed
  <li>Selenium library (Install using <code>pip install selenium</code> in command prompt or terminal)</li>
  
</ul>



<br>

<h2>How to Run</h2>
<ol>
  <li>Clone or download the repository to your local machine</li>
  <li>Update the path to the Chrome Web Driver executable in the .py script (currently set to <code>D:\\Coding\\py\\chromedriver.exe)</code></li>
 
  <li>Replace the URL with the URL of your wifi login page</li>
  <li>Replace the username and password fields with your login credentials</li>
  <li>Replace the ID's of the elements in the script with the actual ID's of the elements on the login page (username field, password field, checkbox, submit button etc.)</li>
  <li>Save the changes to the script</li>
  
  <li>Open a command prompt in the same directory and Run the script using <code>python loginwifi.py</code></li>
</ol>

<br>

<h2>Running the script on Windows Boot (Startup) - Method 1</h2>
<ol>
  <li>Create a shortcut of the .py file</li>
  <li>Locate the startup folder in Windows:
    <ul>
      <li>Press the Windows key + R to open the Run dialog box</li>
      <li>Type <code>shell:startup</code> and press Enter</li>
    </ul>
  </li>
  <li>Move the shortcut of the .py file to the Startup folder</li>
  
  <li>The script will now run every time your Windows boot (Not when you log out)</li>
</ol>
<br>
<h2>Running the script on Windows Login & Boot - Method 2</h2>
<ol>

<li>Search and select "Task Scheduler" from the start menu.</li>
<li>Click "Create Task..." in the "Actions" pane on the right.</li>
<li>Fill in the "General" tab with a name and description for the task. Check "Run with highest privileges"</li>
<li>Change "Configure for" to "Windows 10" or your version of Windows.</li>
<li>Select the "Triggers" tab, click "New", and set the desired frequency (e.g. "At log on" or You can also use this to run it "At startup").</li>
<li>Select the "Actions" tab, click "New", and choose "Start a program".</li>
<li>Enter the full path to your pythonw.exe file in the "Program/script" field. </li>
<li>You can find the location by typing "where python" in cmd. pythonw.exe will be in same folder.
For me it was <code>C:\Users\Sajal\AppData\Local\Programs\Python\Python311\pythonw.exe</code></li>
<li> Enter the full path to your script in the "Start in (optional)" field. For me it was <code>D:\code\py</code></li>
<li>Enter the name of your script in the "Add arguments (optional)" field. For me it was <code>loginwifi.pyw</code> (Rename the .py file to .pyw)</li>
<li>In Conditions, uncheck "Start the task only if the computer is on AC power".</li>
<li>Click "OK" to save the task.</li>

</ol>
<br>

<h2>Running the script on Linux Boot (Startup)</h2>
<ol>
<p>You can automate this Python script to run on Linux login by adding it to the <code>~/.bashrc</code> file or the appropriate session startup script.</p>
<p>Here are the steps to do this:</p>

  <li>Open the terminal and enter the following command: <code>nano ~/.bashrc</code></li>
  <li>Add the following line to the end of the file: <code>python3 /path/to/your/script.py &</code></li>
  <li>Save the file and exit nano editor by pressing <kbd>Ctrl</kbd> + <kbd>X</kbd> then <kbd>Y</kbd> and then <kbd>Enter</kbd>.</li>
  <li>Logout and log back in to your session for the changes to take effect.</li>
<br>
<p><strong>Note:</strong> Replace the <code>/path/to/your/script.py</code> with the actual path to your script.</p>

</ol>

<br>

<h2>Running the script on MacOS boot- Not tested (Startup)</h2>
<ol>
  <li>Create a new file in the following directory: <code>/Library/LaunchDaemons</code></li>

<li>You can use the Terminal to create the file by typing: <code>sudo nano /Library/LaunchDaemons/[filename].plist</code></li>
<li>Add the following content to the file, replacing the paths and script name with the appropriate information for your script:</li>
  <br>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>[filename]</string>
    <key>ProgramArguments</key>
    <array>
      <string>/usr/bin/python</string>
      <string>[full path to script].py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
  </dict>
</plist>
```

  
  <li>Save and exit the file, then restart your Mac.</li> 
  <li>This should run your Python script on every boot.</li>
  </ol>
  <br>










<h2>Working of the Script</h2>
<p>The script uses Selenium to automate the login process of a website. It first opens the website using the webdriver, finds the required fields (username, password, checkbox, submit button) using the element ID's, enters the login credentials, clicks the checkbox (if there is one) and finally clicks the submit button to complete the login process.</p>


<br>

<h2> Showcase </h2>
<p>Here is a demo of the script in action:</p>

<img src="/demo.gif" alt="Demo">

<br>

<h2>Note</h2>

<li>The script assumes that the elements in the wifi login page (username field, password field, submit button) can be located using the ID selector. If the elements have different selectors (e.g. class name, name), the code needs to be updated accordingly.</li>
<li> Also it is assumed that the Wifi is open and your laptop is getting connected to it on boot.</li>
<li> The script is tested on Windows 11 and Ubuntu 22.04.1 . It should work on other versions of Windows & Linux as well. It is not tested on MacOS.    </li>

<li> Let me know if you face any issues. </li>

<h2>Limitation</h2>
<li> If you are using the shortcut method, it will only run on startup </li>
<li> If you are using the Task Scheduler method, it will work on startup and when you log out.  </li>
<li> Not working after laptop goes to sleep automatically</li>



<br>

<h2>Contributing</h2>

<p>Any Contribution in the form of issues and pull requests are welcome. If you have an idea for a new feature or found a bug, please open an issue. If you have already fixed the issue, please create a pull request with your changes.</p>
<br>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="https://github.com/sajalkmr/wifiautologin/blob/main/LICENSE">LICENSE</a> file for details.</p>


