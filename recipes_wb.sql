SELECT * FROM users;

SELECT * FROM users
LEFT JOIN recipes
ON recipes.user_id = user.id
WHERE users.id = id;

SELECT * FROM recipes;

INSERT INTO recipes (name, description, instructions, date_cooked, under_30_minutes, user_id)
VALUES ('Brown Sugar Pop-Tarts','Easy to make breakfast food, or an on-the-go snack!',"Toast them... but not for too long.", NOW(),'1','1');

