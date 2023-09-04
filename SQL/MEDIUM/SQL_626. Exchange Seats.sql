SELECT 
    CASE
        WHEN mod(id, 2) = 0 AND id != (SELECT max(id) FROM Seat) THEN id - 1
        WHEN mod(id, 2) = 1 AND id != (SELECT max(id) FROM Seat) THEN id + 1
        WHEN mod(id, 2) = 0 AND id = (SELECT max(id) FROM Seat) THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id asc;