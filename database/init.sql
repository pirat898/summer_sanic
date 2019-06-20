create table users (
    user_id serial primary key,
    name varchar(255) not null,
    age int,
    phone varchar(10)
);


insert into users (name, age, phone)
values
    ('Peter', 22, '2223334501'),
    ('Bob', 31, '2223334502'),
    ('Alice', 25, '2223334503'),
    ('Mark', 43, '2223334504'),
    ('Natasha', 36, '2223334505')
;

