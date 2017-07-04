#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    
    c.execute(query)
    DB.commit()
    DB.close()



def deletePlayers():
    """Remove all player records from the database."""
    DB = connect()
    c = DB.cursor()
    query = "DELETE from players WHERE id NOTNULL;"
    c.execute(query)
    DB.commit()
    DB.close()



def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    query = "SELECT count(id) as num FROM players;"
    c.execute(query)
    count = int(c.fetchone()[0])
    DB.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
    name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    query = "INSERT INTO players (name) values (%s)"
    c.execute(query, (name,))
    DB.commit()
    DB.close()



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
    A list of tuples, each of which contains (id, name, wins, matches):
    id: the player's unique id (assigned by the database)
    name: the player's full name (as registered)
    wins: the number of matches the player has won
    matches: the number of matches the player has played
    """

    DB = connect()
    c = DB.cursor()
    query = """
		SELECT players.id, players.name, player_wins.wins, player_matches.matches
		FROM players
		LEFT JOIN player_wins ON players.id = player_wins.player
		LEFT JOIN player_matches ON players.id = player_matches.player
		GROUP BY players.id, players.name, player_wins.wins, player_matches.matches
		ORDER BY player_wins.wins DESC;
	"""
    c.execute(query)
    standings = c.fetchall()
    DB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
    winner:  the id number of the player who won
    loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    query = "INSERT INTO matches (winner_id, loser_id) values (%s, %s);"
    c.execute(query, (int(winner), int(loser)))
    DB.commit()
    DB.close()




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
    standings = playerStandings()
    total_players = len(standings)
    result = []
    for player in range(0, total_players, 2):

            pairing = (standings[player][0],
                        standings[player][1],
                        standings[player+1][0],
                        standings[player+1] [1],                )
            result.append(pairing)
    return result

