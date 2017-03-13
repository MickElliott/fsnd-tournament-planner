###############################################################################
                   Tournament Planner Application
###############################################################################

1. What Is It?
   -----------
   The Tournament Planner Application is a Python application that keeps track
   of players and matches in a Swiss-system tournament. The application uses a
   PostgreSQL database to keep track of the players and matches in the 
   tournament. 
   This application was created as partial fulfillment of the Udacity Full 
   Stack Web Developer Nanodegree. Specifically, it is Project 4: Tournament 
   Results.

2. Installation
   ------------
   The source code for this application can be obtained from the following
   GitHub repository:
      https://github.com/MickElliott/fsnd-tournament-planner

   The application consists of the following files:
      tournament.py
      tournament.sql
      tournament_test.py
      readme.txt

3. Python Version
   --------------
   This application was developed using Python version 2.7.13

4. Usage
   -----
   The user needs to have Python installed with the psycopg2 DB-API library.
   The psql PostGreSQL database also needs to be installed. 
   The PostGreSQL database needs to contain a database called tournament.
   The included SQL file needs to be used to create the required tables and
   views. Execute the following command:
      psql \i tournament.sql

   This SQL file will overwrite any existing tables from previous tournaments.

   The tournament.py module contains a set of method definitions which can be 
   used to register players for the tournament, record match results, produce
   the player standings and determine the pairings for the next round. The user
   can write code to use this interface to customise their own Swiss-system
   tournament.
   The tournament_test.py module contains a set of test methods which serve
   as examples to the user of how to use this interface.