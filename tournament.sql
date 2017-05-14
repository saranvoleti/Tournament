-- Table definitions for the tournament project.
-- Import using PostgreSQL
CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE matches(
    match_id SERIAL PRIMARY KEY,
    winner_id INTEGER REFERENCES players(id),
    loser_id INTEGER REFERENCES players(id)
);

-- Create the "player_wins" view
CREATE  VIEW player_wins AS
    (SELECT players.id AS player, count(matches.match_id) AS wins
    FROM players LEFT JOIN matches
    ON players.id = matches.winner_id
    GROUP BY players.id, matches.winner_id
    ORDER BY players.id);

-- Create the "player_losses" view
CREATE  VIEW player_losses AS
    (SELECT players.id AS player, count(matches.match_id) AS losses
    FROM players LEFT JOIN matches
    ON players.id = matches.loser_id
    GROUP BY players.id, matches.loser_id
    ORDER BY players.id);

-- Create the "player_matches" view
CREATE  VIEW player_matches AS
    (SELECT players.id AS player, count(matches.match_id) AS matches
    FROM players LEFT JOIN matches
    ON(players.id=matches.winner_id) OR(players.id=matches.loser_id)
    GROUP BY players.id
    ORDER BY players.id ASC);
