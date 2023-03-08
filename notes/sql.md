# SQL

## Table Creation

- Sample:

```sql
CREATE TABLE TerminalUnits (
    Id    INT NOT NULL PRIMARY KEY IDENTITY,
    AhuId INT NULL,
    Name NVARCHAR(MAX) NOT NULL,
    AirflowCfm float,
    DuctAreaFt2 FLOAT,
    AreaServed NVARCHAR(MAX),
    SquareFootageServed INT,
    Type NVARCHAR(MAX),

    CONSTRAINT FK_AhuTerminalUnitFOREIGN FOREIGN KEY (AhuId) REFERENCES Ahus (Id)
);
```

## Adding a Column

```
ALTER TABLE dbo.TerminalUnits ADD [Floor] INT NULL
```

## Insert data

```sql
INSERT INTO Table (Column1, Column2, ...) VALUES (Value1, Value2, ...);
```

## Converting from UTC to Time Zone

SELECT CONVERT(datetime2, [UTC Datetime Column] at time zone 'UTC' at time zone 'Central Standard Time')

## Update

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

## Operations

String concatenation: `+`.

## Recursion

<https://medium.com/swlh/recursion-in-sql-explained-graphically-679f6a0f143b>
