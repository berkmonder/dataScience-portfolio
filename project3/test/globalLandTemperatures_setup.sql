DROP TABLE global_temperatures;
DROP TABLE global_by_country;
DROP TABLE global_by_state;
DROP TABLE global_by_city;
DROP TABLE global_by_major_city;


CREATE TABLE global_temperatures (
    dt                                        timestamp without time zone,
    LandAverageTemperature                    numeric,
    LandAverageTemperatureUncertainty         numeric,
    LandMaxTemperature                        numeric,
    LandMaxTemperatureUncertainty             numeric,
    LandMinTemperature                        numeric,
    LandMinTemperatureUncertainty             numeric,
    LandAndOceanAverageTemperature            numeric,
    LandAndOceanAverageTemperatureUncertainty numeric);

CREATE TABLE global_by_country (
    dt                               timestamp without time zone,
    AverageTemperature               numeric,
    AverageTemperatureUncertainty    numeric,
    Country                          varchar);

CREATE TABLE global_by_state (
    dt                               timestamp without time zone,
    AverageTemperature               numeric,
    AverageTemperatureUncertainty    numeric,
    State                            varchar,
    Country                          varchar);

CREATE TABLE global_by_city (
    dt                               timestamp without time zone,
    AverageTemperature               numeric,
    AverageTemperatureUncertainty    numeric,
    City                             varchar,
    Country                          varchar,
    Latitude                         varchar,
    Longitude                        varchar);

CREATE TABLE global_by_major_city (
    dt                               timestamp without time zone,
    AverageTemperature               numeric,
    AverageTemperatureUncertainty    numeric,
    City                             varchar,
    Country                          varchar,
    Latitude                         varchar,
    Longitude                        varchar);

\copy global_temperatures FROM 'data/GlobalTemperatures.csv' DELIMITER ',' CSV HEADER;

\copy global_by_country FROM 'data/GlobalLandTemperaturesByCountry.csv' DELIMITER ',' CSV HEADER;

\copy global_by_state FROM 'data/GlobalLandTemperaturesByState.csv' DELIMITER ',' CSV HEADER;

\copy global_by_city FROM 'data/GlobalLandTemperaturesByCity.csv' DELIMITER ',' CSV HEADER;

\copy global_by_major_city FROM 'data/GlobalLandTemperaturesByMajorCity.csv' DELIMITER ',' CSV HEADER;