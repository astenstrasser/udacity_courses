# SQL basics 

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
 order by  (desc?), limit n offset n (could use for pagination), group by.

### insert 
    
The basic syntax for the insert statement:
    
```sql
insert into table ( column1, column2, ... ) values ( val1, val2, ... );
```

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

