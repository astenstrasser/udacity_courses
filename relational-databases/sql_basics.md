# SQL basics 

## Data types:

### Text and string types

    text — a string of any length, like Python str or unicode types.
    char(n) — a string of exactly n characters.
    varchar(n) — a string of up to n characters.

### Numeric types
    integer — an integer value, like Python int.
    real — a floating-point value, like Python float. Accurate up to six decimal places.
    double precision — a higher-precision floating-point value. Accurate up to 15 decimal places.
    decimal — an exact decimal value.

### Date and time types
    date — a calendar date; including year, month, and day.
    time — a time of day.
    timestamp — a date and time together.


## Query Syntax:

### select: 
The syntax of the select statement with a where clause:

```sql
select columns from tables where condition;
```

Boolean operators and logic operators can be used on condition!
Columns are separated by commas, * select all columns.

Ex.:

```sql
select name form animals where (not species = 'gorilla') and (not name = 'Max');
    
select name form animals where species != 'gorilla' and name != 'Max';   (just like python operator) 
```

In exceptions we can use commands like:
 - order by  (desc? asc?) - can be used with more than one parameter 
 - limit n offset n (could use for pagination)  
 - group by 
 - having
 - char_length() 
 'Group by' runs before running the other commands in line. The command 'having' filter the results after running the search.
 

Ex.:
```sql
select name, food, count(animals.name) as num 
       from diet, animals 
       where animals.species = diet.species group by food 
       having num = 1;
```


**Using Join:**

```sql
select this, that from Table1 join Table2 on condition;
```
or using simple join
```sql
select this, that from Table1, Table2 where condition;
```

Ex.:

 List all the taxonomic orders, using their common names, sorted by the number of animals of that order that the zoo has. The animals table has (name, species, birthdate) for each individual. The taxonomy table has (name, species, genus, family, t_order) for each species. The ordernames table has (t_order, name) for each order.

```sql
select ordernames.name, count(taxonomy.t_order) as num 
    from animals join taxonomy join ordernames
    on (animals.species = taxonomy.name) and (ordernames.t_order = taxonomy.t_order)
    group by ordernames.name
    order by num desc;
```

**Self Join:**

It is possible to join one table with it self if we are looking for similarities in the rows of this table. 

ex.: Find out which pets have the same owner and the same appointment time.

```sql
select a.name, b.name, a.owner, a.appointment_time
from pets as a, pets as b
where a.appointment_time = b.appointment_time 
and a.owner = b.owner
and a.id < b.id; 
```

**Left Join / Right Join**


The words “left” and “right” refer to the tables to the left and right of the join operator. 

A regular (inner) join returns only those rows where the two tables have entries matching the join condition. 
A left join returns all those rows, plus the rows where the left table has an entry but the right table doesn’t. 
And a right join does the same but for the right table.



**Using Distinct:**

In order to avoid listing duplicates

```sql
select distinct .... from .... where ...;
```

**Using Regexp**

Regexp performs a pattern match of a string expression against a pattern. Using '^anypattern' you test the first letter. 
Using 'anypattern$' you test the word end.

ex.: Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION.

```sql
SELECT CITY FROM STATION WHERE CITY REGEXP '[aeuio]$';
```


### insert: 
    
The basic syntax for the insert statement:
    
```sql
insert into my_table ( column1, column2, ... ) values ( val1, val2, ... );
```

### update:

The syntax of the update statement:

```sql
update my_table set column = my_value where restriction ;
```

**Using Like:**
 A simple form of text pattern-matching.
 The pattern is an SQL text string (so it's in 'single quotes') and can use the % sign to match any sub-string, including the empty string.

ex.: 
```sql
update my_table set column = 'safe words' where column like '%spam%';
```

### delete:

The syntax:

```sql
 delete from my_table where restriction;
```


### Subqueries:

It is possible to use the output of one query to do a new one.

If we have the query:
```sql
select max(grade) as highest_grade from students group by stud_class;
```
and we want to find out the average highest grade of all classes, we can use this output on a new query.

```sql
select avg(highest_grade) from (
    select max(grade) as highest_grade from students group by stud_class
) as class_average;
```


## Creating database

To create a database, the following command can be used:
```sql
create database my_database_name [options];
```

The database can also be dropped with following command:
```sql
drop database my_database_name [options];
```

### Psql commands:

- \c database_name - change to this database
- \dt - list all tables in one database 
- \l - list all databases on your machine


## Creating tables

### Normalized tables:

Rules:
- Every row has the same number of columns.
- There is a unique key, everything in the row is related to the key.
- what is not related to key should be in another table.
- Tables shouldnt imply relationships that are not true. Better create more tables.

### Sintax:

- To create a table:
```sql
create table my_table (
    column1 var_type [my_constraints],
    column2 var_type [my_constraints],
    [row_constraints]);
```

Examples with primary keys:
```sql
create table students (
    stud_id serial primary key,
    name text,
    birthdate date);    
```
```sql
create table postal_places (
    postal_code text,
    country text,
    name text,
    primary key (postal_code, country)
);    
```

- To delete a table:
```sql
drop table my_table_name [options];
```

### Foreing Keys - Defining relationships between tables:

To assure that one column will only have values that are present in other table we need to refer to it:

```sql
create table grades( 
    stud_id references students(stud_id),
    course_id text,
    grade real
);
```

This way we can only add grades of registered students to this new table. 

