#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(db_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname=%s" % db_name)
        cursor = db.cursor()
        return db, cursor
    except:
        print "Could not connect to database: %s" % db_name


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()

    cursor.execute("truncate table matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()

    cursor.execute("truncate table players cascade")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()

    cursor.execute("select count(*) from players")

    count = int(cursor.fetchone()[0])
    db.commit()
    db.close()

    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()

    query = "insert into players values (%s)"
    param = (name,)
    cursor.execute(query, param)

    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()

    query = "select * from player_standings"
    cursor.execute(query)

    result = cursor.fetchall()
    db.commit()
    db.close()

    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()

    query = "insert into matches values (%s,%s)"
    param = (winner, loser)
    cursor.execute(query, param)

    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # Get the current player standings.
    standings = playerStandings()
    numPlayers = len(standings)
    matchList = []

    if numPlayers % 2 != 0:
        # We assume that there are an even number of players in the tournament
        raise ValueError("Odd number of players in standings.")
    else:
        # Determine the number of pairings to create
        numMatches = numPlayers / 2

        # Make a list of pairings. For each pairing needed, make a tuple of
        # consecutive players from the player standings list.
        index = 0
        for i in range(0, numMatches):
            matchList.append((standings[index][0],
                              standings[index][1],
                              standings[index + 1][0],
                              standings[index + 1][1]))
            index += 2

    return matchList
