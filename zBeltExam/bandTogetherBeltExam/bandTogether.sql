select * from users 
left join recipes on users.id = recipes.user_id
where users.id = 1;

select first_name from recipes
join users on recipes.user_id = users.id
where recipes.id = 2;

select * from recipes left join users on users.id = recipes.user_id where recipes.id = 2;

select * from users;

select * from recipes left join users on users.id = recipes.user_id where recipes.id = 3;

