-- Table definitions for the tournament project.
--

-- Delete the players and matches tables if they currently exist.
drop table if exists players;
drop table if exists matches;

-- Create a table to store the players of the tournament.
create table players (
    name    text,
    ID  serial
);

-- Create a table to store the match results.
create table matches (
    Winner_ID   integer,
    Loser_ID    integer,
    Match_ID    serial
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