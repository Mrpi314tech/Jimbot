<body style="background-color:lightblue;">
<h1>Jimbot</h1>
"Control your computer, with your voice."
<h1></h1>
<img src="https://raw.githubusercontent.com/Mrpi314tech/Jimbot/main/images/Jimbot.png" alt="Jimbot logo">
<br>
<a href='https://github.com/Mrpi314tech/Jimbot'><button>Github</button></a>
<br>
Welcome to Jimbot!
Jimbot is a virtual assistant for your computer. It can do many things, like open an application, run a command, type with your voice, search things on google, and much more.
<br>
<h1>Supported Systems</h1>
-Raspberry pi OS
<br>
-Ubuntu
<br>
-Chrome OS
<br>
*It should work on all linux based operating systems
<br>
<h2>To install:</h2>
  Download <a href='https://github.com/Mrpi314tech/Jimbot/releases/download/v1.0.2/Install.sh'>this file</a> and execute it.
  <br>
  Or run this command:
  <pre><code>wget https://github.com/Mrpi314tech/Jimbot/releases/download/v1.0.2/Install.sh
chmod +x Install.sh
./Install.sh</code></pre>
<h3>To Update</h3>
Presss the icon in the lower right corner
<h3>To uninstall</h3>
<pre><code>~/Jimbot/Jimbot_remove.sh</code></pre>
<h1>To use:</h1>
Say the hotword "Jimbot" and it will start listening
<h2>Buttons</h2>
<h3>Edit **</h3>
Allows you to add your own responses/bash commands
<h3>Info</h3>
Basically an instruction manual
<h3>History</h3>
Shows conversation history
<h3>Stats</h3>
Shows system statistics
<h3>Github</h3>
Opens Jimbot Github repository
<h3>Jimbot logo</h3>
Press this button to speak voice commands
<h2>Useful Commands:</h2>
<h3>Spell</h3>
Spell words
<h3>Kill/Close</h3>
Kills a process
<h3>Run/Open</h3>
Runs a command
<h3>Voice Type</h3>
Allows the user to type with their voice.
<h3>Joke</h3>
Tells a joke
<h3>Time</h3>
Tells the time
<h3>Google Search</h3>
Say "Google Search" and then say what you want to search
<h3>General Insults</h3>
Makes him mad (to make him happy again, apologize)
<h3>General Compliments</h3>
Makes him happy
<h3>Note</h3>
If you type the @ sign and then text, it will run the text like a voice command.
<br>
Example: typing "@ hello" is the equivalent of saying "hello" to Jimbot
<h2>How the AI works:</h2>
Jimbot does not have a very complex AI, as he is mainly there to assist you. How the AI works is modeled after human emotion. There is 6 numbers that determine Jimbot's mood. 1 and 4 are happy, 2 is chatty, 3 is neutral, 5 is angry, and 6 is serious. For each keyword in his system, a set of numbers is assigned. For example, if you say "Hello," the numbers 1,2,3 and 4 are assigned. A number is then randomly selected. Say 2, the chatty mood is selected. He will then give a third reply to your input that will encourage you to respond. As your next response, you say "How are you?" The set is 1, 1, 1, 2, 3, 4. There is now a higher likelyhood that he is happy. Also, because his mood from last time was 2, it will be added to the set, so the real set is 1, 1, 1, 2, 2, 2, 3, 4. Then the conversation continues on. There are two numbers left, 5 and 6. 6 is very simple. If you give a command, such as "Google search," then 6 will be added. Whenever the program detects a 6, it will cancel all 2 values in the list. 5 is also simple. When 5 is selected and becomes the mood, Jimbot will become angry. Now, when you give input, you will be locked in a seperate function that gives blunt responses and does not do any of your commands. For example, if you say "Open VLC media player," he will respond with "I'm still mad." The only way to get out of this loop is to apologize by saying "I'm sorry" or "Please forgive me."
