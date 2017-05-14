Introduction:

In this project, I have written a  Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

Code Templates:
The templates for this project are in the tournament subdirectory of VM’s /vagrant directory. 
There are three files there: tournament.sql, tournament.py, and tournament_test.py.

The template file tournament.sql is where has the database schema, in the form of SQL create table commands. 
The template file tournament.py contains the code of your module. 
Finally, the file tournament_test.py contains unit tests that will test the functions that are written in tournament.py. You can run the tests from the command line, using the command python tournament_test.py.

How to Run:
1.	Import the database scheme into PostgreSQL database and then execute the following commands:
psql -> create database tournament;
 -> \c tournament 
-> \i tournament.sql 
-> \q
2.	Run the tests of this project by executing the command:
python tournament_test.py

If all the tests are executed successfully, the following message will be displayed:

1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!

