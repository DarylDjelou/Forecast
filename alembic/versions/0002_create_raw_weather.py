""" Raw Weather table migration
REVISION ID: 0002_create_raw_weather
Revises: 0001_create_location
Created: 2026-08-31 17:45:00.000000
"""

from alembic import op
import sqlalchemy as sa

def upgrade() -> None:
    op.create_table(
        'raw_weather',
        sa.Column('location_id', sa.Integer, sa.ForeignKey('location.location_id'), nullable=False),
        sa.Column('forecast_timestamp', sa.DateTime, nullable=False),
        sa.Column('temperature_2m', sa.Double, nullable=True),
        sa.Column('relative_humidity_2m', sa.Double, nullable=True),
        sa.Column('apparent_temperature', sa.Float, nullable=True),
        sa.Column('retrieved_at', sa.DateTime, nullable=False),
        sa.PrimaryKeyConstraint('location_id', 'forecast_timestamp','retrieved_at', name='raw_weather_pk'),
    )

def downgrade() -> None:
    op.drop_table('raw_weather')