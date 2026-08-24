CREATE TABLE Location
(
    location_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    city        TEXT             NOT NULL,
    country     TEXT             NOT NULL,
    latitude    DOUBLE PRECISION NOT NULL,
    longitude   DOUBLE PRECISION NOT NULL,
    timezone TEXT NOT NULL

        CONSTRAINT latitude_range
            CHECK (latitude BETWEEN -90 AND 90),

        CONSTRAINT longitude_range
            CHECK (longitude BETWEEN -180 AND 180),

        CONSTRAINT unique_city_country
            UNIQUE (city, country)
);