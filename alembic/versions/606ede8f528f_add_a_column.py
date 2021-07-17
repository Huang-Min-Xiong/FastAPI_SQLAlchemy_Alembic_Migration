"""Add a column

Revision ID: 606ede8f528f
Revises: 
Create Date: 2021-07-08 09:56:50.466752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '606ede8f528f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('records', sa.Column('aaa', sa.Integer))

def downgrade():
    pass
