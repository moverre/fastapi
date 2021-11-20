"""add content to posts table

Revision ID: 879c59357c54
Revises: 82df6bbba91f
Create Date: 2021-11-20 17:10:54.480446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '879c59357c54'
down_revision = '82df6bbba91f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
