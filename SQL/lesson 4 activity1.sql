create table of not exists book (
    book_id  integer primary key,
    title    text    not null,
    genre    text    not null,
    rating   real    not null,
    pages    integer not null,
    pub_year integer not NULL
);

insert into book values (1, 'Dragon Quest',   'Fantasy',   9.2, 312, 2021);
insert into book values (2, 'Code Wizards',   'Sci-fi',    8.5, 280, 2020);
insert into book values (3, 'Ocean Deep',     'Adventure', 7.8, 195, 2022);
insert into book values (4, 'Star Rangers',   'Sci-fi',    9.5, 340, 2019);
insert into book values (5, 'Forest Secrets', 'Fantasy',   8.1, 228, 2023);
insert into book values (6, 'Robot City',     'Sci-fi',    7.2, 260, 2021);
insert into book values (7, 'Time Jumpers',   'Adventure', 8.9, 175, 2022);
insert into book values (8,'Magic Academy',   'Fantasy',   9.0, 398, 2020);

select from book;

select title, rating from book order by rating asc;
select title, rating from book order by rating desc;
select title, genre, rating from book order by genre asc, rating desc;

select title, rating from book order by rating desc limit 3;
select title, pub_year from book order by pub_year asc limit 5;

select genre, count(*) as book_count from book group by genre;
select genre, sum(pages) as total_page, avg(rating) as avg_rating
from book
group by genre;

select genre, count(*) as book_count
from book
group by genre
having count(*) > 2;

select genre, avg(rating) as avg_rating
from book
group by genre
having avg_rating >= 8.5
