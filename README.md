<h1>Wifi Login Automation with Selenium</h1>
<p>A script that automates the login process of a website using Selenium webdriver.</p>

<h1>Getting Started</h1>
These instructions will get you a copy of the project up and running on your local machine.



<h2>Requirements</h2>
<ul>
  <li>Latest version of <a href="https://www.python.org/downloads/">Python</a> installed and added to PATH</li>
  <li>Google Chrome <a href="https://www.google.com/intl/en_in/chrome/">Browser</a></li>
  <li>Chromedriver.exe (Get the version compatible with your Chrome Version <a href="https://chromedriver.chromium.org/downloads">here</a>)</li>
  <li><a href="https://pip.pypa.io/en/stable/installation/">pip</a> installed
  <li>Selenium library (Install using <code>pip install selenium</code> in command prompt or terminal)</li>
  
</ul>





<h2>How to Run</h2>
<ol>
  <li>Clone or download the repository to your local machine</li>
  <li>Update the path to the Chrome Web Driver executable in the .py script (currently set to <code>D:\\Coding\\py\\chromedriver.exe)</code></li>
 
  <li>Replace the URL with the URL of your wifi login page</li>
  <li>Replace the username and password fields with your login credentials</li>
  <li>Replace the ID's of the elements in the script with the actual ID's of the elements on the login page (username field, password field, checkbox, submit button etc.)</li>
  <li>Save the changes to the script</li>
  
  <li>Open a command prompt in the same directory and Run the script using <code>python3 loginwifi.py</code></li>
</ol>



<h2>Running the script on Windows Login (Startup)</h2>
<ol>
  <li>Create a shortcut of the .py file</li>
  <li>Locate the startup folder in Windows:
    <ul>
      <li>Press the Windows key + R to open the Run dialog box</li>
      <li>Type <code>shell:startup</code> and press Enter</li>
    </ul>
  </li>
  <li>Move the shortcut of the .py file to the Startup folder</li>
  
  <li>The script will now run every time you log in to Windows</li>
</ol>




<h2>Running the script on Linux login (Startup)</h2>
<ol>
<p>You can automate this Python script to run on Linux login by adding it to the <code>~/.bashrc</code> file or the appropriate session startup script.</p>
<p>Here are the steps to do this:</p>
<ol>
  <li>Open the terminal and enter the following command: <code>nano ~/.bashrc</code></li>
  <li>Add the following line to the end of the file: <code>python3 /path/to/your/script.py &</code></li>
  <li>Save the file and exit nano editor by pressing <kbd>Ctrl</kbd> + <kbd>X</kbd> then <kbd>Y</kbd> and then <kbd>Enter</kbd>.</li>
  <li>Logout and log back in to your session for the changes to take effect.</li>

<p><strong>Note:</strong> Replace the <code>/path/to/your/script.py</code> with the actual path to your script.</p>
</ol>




<h2>Working of the Script</h2>
<p>The script uses Selenium to automate the login process of a website. It first opens the website using the webdriver, finds the required fields (username, password, checkbox, submit button) using the element ID's, enters the login credentials, clicks the checkbox (if there is one) and finally clicks the submit button to complete the login process.</p>



<h2> Showcase </h2>
<p>Here is a demo of the script in action:</p>

<h3>Demo</h3>
<img src="/demo.gif" alt="Demo">



<h2>Note</h2>

<p>The script assumes that the elements in the wifi login page (username field, password field, submit button) can be located using the ID selector. If the elements have different selectors (e.g. class name, name), the code needs to be updated accordingly.</p>



<h2>Contributing</h2>
<p>Any Contribution in the form of issues and pull requests are welcome. If you have an idea for a new feature or found a bug, please open an issue. If you have already fixed the issue, please create a pull request with your changes.</p>
<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="https://github.com/sajalkmr/wifiautologin/blob/main/LICENSE">LICENSE</a> file for details.</p>


