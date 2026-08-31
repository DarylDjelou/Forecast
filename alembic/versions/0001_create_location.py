""" Location table creation migration

REVISION ID: 0001_create_location
Revises: None
Created: 2026-08-31 17:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

def upgrade() -> None:
    op.create_table(
        'location',
        sa.Column('location_id', sa.Integer,
                  sa.Identity(always=True)
                  ,primary_key=True),
                sa.Column('city', sa.String(length=255),
                          nullable=False),
                sa.Column('country', sa.String(length=255),
                          nullable=False),
                sa.Column('latitude', sa.Double,
                          nullable=False),
                sa.Column('longitude', sa.Double,
                          nullable=False),
                sa.Column('timezone', sa.String(length=255),
                          nullable=False),
        sa.CheckConstraint('latitude >= -90 AND latitude <= 90', name='latitude_range'),
        sa.CheckConstraint('longitude >= -180 AND longitude <= 180', name='longitude_range'),
        sa.UniqueConstraint('city', 'country'),
    )

def downgrade() -> None:
    op.drop_table('location')