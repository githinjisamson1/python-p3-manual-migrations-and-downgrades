"""Renaming students to scholars

Revision ID: ef2e9a804978
Revises: f7a1a78ba777
Create Date: 2023-12-11 05:46:11.360925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef2e9a804978'
down_revision = 'f7a1a78ba777'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
