CREATE DATABASE weatherdb;

DROP TABLE weather;

CREATE TABLE weather (
    Date                    date,
    Location                varchar,
    MinTemp                 real,
    MaxTemp                 real,
    Rainfall                real,
    Evaporation             real,
    Sunshine                real,
    WindGustDir             varchar,
    WindGustSpeed           real,
    WindDir9am              varchar,
    WindDir3pm              varchar,
    WindSpeed9am            real,
    WindSpeed3pm            real,
    Humidity9am             real,
    Humidity3pm             real,
    Pressure9am             real,
    Pressure3pm             real,
    Cloud9am                real,
    Cloud3pm                real,
    Temp9am                 real,
    Temp3pm                 real,
    RainToday               varchar,
    RainTomorrow            varchar);

\copy weather FROM 'data/weatherAUS.csv' DELIMITER ',' CSV HEADER;