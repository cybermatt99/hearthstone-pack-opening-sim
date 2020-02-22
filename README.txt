
HEARTHSTONE PACK OPENING SIMULATOR

By Matthew  Thibodeau 2/22/2020

OVERVIEW
--------
This program allows you to simulate opening a Hearthstone Pack
and receive 5 cards based on actual Blizzard-provided odds.
You have the option to continue opening indefinitely, as well
as check the statistics of the cards you have already opened.


HOW TO USE
----------

Download the 'hearthstone.py' file and all of the .txt files.
The 'ultimate.txt' file is not currently implemented in this
build so you do not need it.

This program works off of the command line so put all of the
.txt files and the 'hearthstone.py' file in the same directory.

Make sure that you have Python3 installed and then run

"python [directory_name]\hearthstone.py"

in the command-line. You can also use it with basically
any program that compiles and runs .py programs like IDLE.


CONTROLS
--------

Press 'a' when prompted to open a new pack.
Press 's' when prompted to check the statistics of your
current session.

PLANNED FEATURES
----------------

Currently (as of 2/22/2020) this features up to the 
Journey to Un'Goro update so I would like to add all 
the way up to the current update. 

I would like to add an export feature to allow you
to save your session to a .txt file.

I would like to add a feature where you can import a
previous session from a .txt file to continue where
you left off.

I would like to add in Golden cards. I haven't determined
exactly how I want to do that yet.

I would like to add in a GUI and move away from the text-based
implementation. This would of course require changing the
whole project but it is doable. Also, I would need to add in
pictures for it to be any good.

I want to separate into different sets, so that you can choose
to open from "all sets" or just open a 'classic' pack or just
Curse of Naxxramas, etc.

Down the road once I start experimenting with GUI's I can 
possibly add in sound effects which would be AWESOME

I would like to include the cost of cards so that you can look
at that in the Statistics as well. This would require
editing of the .txt files however.

I would like to implement the total amount of real-world money
that this opening would have cost. Possibly include that in
the statistics. The only difficulty is that packs range 
anywhere from about $1.495 a pack to $1.167 a pack depending
on how many you buy at once. Perhaps I can either average
these numbers and go with that, or calculate the cost based
on total packs opened.
