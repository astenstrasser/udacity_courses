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
       having num = 1
```


**Using Join:**

```sql
select this, that from Table1 join Table2 on condition
```
or using simple join
```sql
select this, that from Table1, Table2 where condition
```

Ex.:

 List all the taxonomic orders, using their common names, sorted by the number of animals of that order that the zoo has. The animals table has (name, species, birthdate) for each individual. The taxonomy table has (name, species, genus, family, t_order) for each species. The ordernames table has (t_order, name) for each order.

```sql
select ordernames.name, count(taxonomy.t_order) as num 
    from animals join taxonomy join ordernames
    on (animals.species = taxonomy.name) and (ordernames.t_order = taxonomy.t_order)
    group by ordernames.name
    order by num desc
```

**Using Distinct:**
In order to avoid listing duplicates

```sql
select distinct .... from .... where ...
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
update my_table set column = 'safe words' where column like '%spam%'
```

### delete:

The syntax:

```sql
 delete from my_table where restriction 
```