"""create post table

Revision ID: c526c8dfe3e3
Revises: 
Create Date: 2023-09-27 09:05:20.287557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c526c8dfe3e3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
                    , sa.Column('title', sa.String(),nullable =False ))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
