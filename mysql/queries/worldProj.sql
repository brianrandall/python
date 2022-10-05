-- select name, language, percentage from languages
-- join countries on countries.id = languages.country_id
-- where language = 'Slovene'
-- order by percentage desc

select name, count(
from countries join cities
on country_id = country.id


-- join countries on countries.id = cities.country_id
