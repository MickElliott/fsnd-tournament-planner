-- Table definitions for the tournament project.
--

-- Delete the tournament database if it currently exists.
drop database if exists tournament;
create database tournament;
\c tournament;

-- Create a table to store the players of the tournament.
create table players (
    name    text,
    ID  serial primary key
);

-- Create a table to store the match results.
create table matches (
    Winner_ID   integer references players(ID),
    Loser_ID    integer references players(ID),
    Match_ID    serial primary key
);

-- Create views to assist SQL queries used in Python code.
--
-- Create a view that determines the number of wins for each player.
create view win_total as
    select players.ID, count(winner_id) as wins
        from players left join matches on
            players.id = matches.winner_id
        group by players.id order by wins DESC;

-- Create a view that determines the number of losses for each player.
create view loss_total as
    select players.ID, count(loser_id) as losses
        from players left join matches on
            players.id = matches.loser_id
        group by players.id order by losses DESC;

-- Create a view that determines the total number of matches played for each
-- player.
create view match_total as
    select players.ID, count(match_id) as player_matches
        from players left join matches on
            players.id = matches.loser_id or players.id = matches.winner_id
        group by players.id order by player_matches DESC;

-- Create a view that generates a table of players in the order of their
-- number of wins.
create view player_standings as
    select players.ID, players.name,
            win_total.wins, match_total.player_matches from
        players left join win_total on
            players.id = win_total.id join match_total on
                players.id=match_total.id
        order by win_total.wins DESC;
