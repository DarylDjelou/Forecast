from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
)

metadata = MetaData()

location = Table(
    "location",
    metadata,

    Column("location_id", Integer, primary_key=True),
    Column("city", String, nullable=False),
    Column("latitude", Float, nullable=False),
    Column("longitude", Float, nullable=False),
    Column("timezone", String, nullable=False),
)

raw_weather = Table(
    "raw_weather",
    metadata,

    Column(
        "location_id",
        Integer,
        ForeignKey("location.location_id"),
        nullable=False,
    ),
    Column("timestamp", DateTime, nullable=False),
    Column("temperature_2m", Float),
    Column("relative_humidity_2m", Float),
    Column("apparent_temperature", Float),
    Column("retrieved_at", DateTime, nullable=False),
)