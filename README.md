<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>ISS Overhead Notifier</h1>

<p>This is a Python application that notifies you when the International Space Station (ISS) is passing overhead during the night. It uses real-time data from public APIs and sends you an email notification when conditions are met.</p>

<h2>Features</h2>
<ul>
    <li><strong>Real-time ISS Tracking:</strong> Checks if the ISS is overhead based on your location.</li>
    <li><strong>Night Detection:</strong> Only notifies when it's nighttime at your location.</li>
    <li><strong>Email Notification:</strong> Sends an email when the ISS is visible in the sky.</li>
</ul>

<h2>Installation</h2>
<ol>
    <li><strong>Clone the repository:</strong>
        <pre><code>git clone https://github.com/your-username/ISS_Overhead_Notifier.git</code></pre>
    </li>
    <li><strong>Install dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Update your email credentials:</strong> Replace `my_email` and `my_password` in the script with your Gmail details.</li>
</ol>

<h2>Usage</h2>
<ol>
    <li><strong>Run the application:</strong>
        <pre><code>python main.py</code></pre>
    </li>
    <li><strong>Wait for notifications:</strong> The script will run in the background, checking the ISS position and sending notifications when overhead.</li>
</ol>

<h2>Code Explanation</h2>
<ul>
    <li><strong>is_iss_overhead():</strong> Checks if the ISS is within a certain range of your location.</li>
    <li><strong>is_night():</strong> Determines if it's nighttime using sunrise and sunset times.</li>
    <li><strong>Email notification:</strong> Sends an email when both conditions are met.</li>
</ul>

<h2>Contributing</h2>
<p>Contributions are welcome! Feel free to open an issue or submit a pull request.</p>

<h2>Thank You!!</h2>
</body>
</html>
