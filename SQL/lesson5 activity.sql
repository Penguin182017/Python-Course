create table if not exists Restaurant (
    name text,
    neighborhood text,
    cuisine text,
    review real,
    price text,
    health text
);
INSERT INTO Restaurant (name, neighborhood, cuisine, review, price, health)
VALUES
    ('Peter', 'Brooklyn', 'steak', 4.4, '$$$$', 'A'),
    ('Jongro', 'Midtown', 'korean', 3.5, '$$', 'A'),
    ('Pocha', 'Midtown', 'Pizza', 4.0, '$$$', 'B'),
    ('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
    ('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
    ('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
    ('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
    ('DI Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$', 'A'),
    ('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');

select distinct neighborhood
from Restaurant;

select distinct cuisine
from Resaurant;

Select *
From Resaurant
where cuisine = 'Chinese';

Select *
from Restaurant
where review >= 4.0;

Select *
from Restaurant
where cuisine = 'Italian'
    and price in ('$$', '$$$');

select *
from Restaurant
where price = '$$$';

Select *
from Restaurant
where name like '%Candy%';

select *
from Restaurant
where neighborhood in ('Midtown', 'Downtown', 'Chinatown');

select *
from Restaurant
where health = '' or health is null;

Select *
from Restaurant
order by review DESC
limit 4;

