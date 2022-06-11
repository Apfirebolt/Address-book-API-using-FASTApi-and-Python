"""create task table

Revision ID: c0d3bf99bbad
Revises: 
Create Date: 2022-06-11 07:13:15.221890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0d3bf99bbad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('task')
    
