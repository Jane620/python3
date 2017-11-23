create table proxy(
    id int unsigned not null auto_increment primary key,
    ip varchar(20) not null,
    port varchar(8) not null,
    type varchar(6) not null,
    is_valid char(1) not null,
    test_date date
);


--创建表 省市区
--表 province

create table province
(
   pro_id int unsigned primary key ,
   pro_code varchar(6) NOT NULL,
   pro_name varchar(20) NOT NULL
)
DEFAULT CHARSET = UTF8;
--表 city
CREATE TABLE city
(
  city_id int unsigned   PRIMARY KEY ,
  city_code varchar(6) NOT NULL,
  city_name varchar(40) NOT NULL,
  pro_code varchar(6) NOT NULL
)
DEFAULT CHARSET = UTF8;
--表 `area`
CREATE TABLE area (
   are_id int unsigned primary key ,
   are_code varchar(6) NOT NULL,
   are_name varchar(50) NOT NULL,
   city_code varchar(6) NOT NULL
)
DEFAULT CHARSET = UTF8;