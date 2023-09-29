"""add last few columns to posts table

Revision ID: f8021c228004
Revises: c2e77034dcdd
Create Date: 2023-09-27 22:00:06.895700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8021c228004'
down_revision: Union[str, None] = 'c2e77034dcdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
