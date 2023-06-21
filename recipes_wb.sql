SELECT * FROM users;

SELECT * FROM users
JOIN recipes
ON recipes.user_id = user.id
WHERE users.id = 4;