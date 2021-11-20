"""create posts table

Revision ID: 82df6bbba91f
Revises: 
Create Date: 2021-11-20 16:56:49.805977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82df6bbba91f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
     sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
