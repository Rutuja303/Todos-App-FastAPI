"""add apt num col

Revision ID: 1cc0740549c0
Revises: 6a5725f5533c
Create Date: 2025-07-08 18:36:36.881263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cc0740549c0'
down_revision: Union[str, Sequence[str], None] = '6a5725f5533c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
