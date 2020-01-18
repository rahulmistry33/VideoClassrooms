drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null,
    contact text not null,
    email text not null,
    usertype text not null
);