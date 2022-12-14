select name, language, percentage from languages
join countries on countries.id = languages.country_id
where language = 'Slovene'
order by percentage desc;

select countries.name, count(cities.id) as count from countries 
join cities
on cities.country_id = countries.id
group by countries.id
order by count desc;

select cities.name, cities.population from cities
join countries on cities.country_id = countries.id
where countries.name = 'mexico' and cities.population > 500000
order by cities.population desc;

select countries.name, languages.language, languages.percentage from languages 
join countries on countries.id = languages.country_id
where languages.percentage > 89
order by languages.percentage desc;

select countries.name, countries.surface_area, countries.population from countries
where surface_area < 501 and population > 100000;

select countries.name, countries.government_form, countries.capital, countries.life_expectancy from countries
where government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75;

select countries.name, cities.name, cities.district, cities.population from cities
join countries on countries.id = cities.country_id
where cities.district = 'buenos aires' and cities.population > 500000;

select countries.region, count(countries.id) as countries from countries
group by countries.region
order by countries desc;
