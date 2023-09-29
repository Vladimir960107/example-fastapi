"""add content column to posts table

Revision ID: ab3d7701f914
Revises: c526c8dfe3e3
Create Date: 2023-09-27 10:03:05.841208

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab3d7701f914'
down_revision: Union[str, None] = 'c526c8dfe3e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
