rollcaller
==========

This is a small stand-alone web application that lets you take roll for a large class or meeting. It provides large text for readability in a large room with a projector. It does not require network access and can run stand alone on Windows or Linux (the only two platforms I have tested it on)


### Requirements

 - Python - I'm running it on 2.7.1
 - [bottle.py](http://bottlepy.org/docs/dev/), the awesome single file python framework.
 - bottle_sqlite - for connecting bottle to SQLite
 - sqlite3 - Database for the roll information
 - Twitter bootstrap, although I'm including it in the /css and /img directories.

(Twitter bootstrap is awesome! Keep up with it at http://twitter.github.com/bootstrap/) 


### Installation

Decompress the archive into a directory. Make sure you have the requirements installed. Then, run rollcall.py and open a web browser. Connect to localhost:9090, and you're ready to go!


### Using Rollcall

The main page is a list of all workshop/meeting names, their ID Numbers, their present/absent status, and any notes. Click on whatever name is at the top to start taking roll. 

Each rollcall page will have the person's name in very large font at the top. Click 'Absent' to toggle their present/absent status, put in any notes that you need, hit submit, then hit 'next' to go the next person.

After the last person is called, you will see an Attendance Report page with the number of people present/absent, a percentage, and whether or not a Quorum has been reached. (Quorum is defined as 50% present, you can change that in the code though.)

It's very, very simple!


### License

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.