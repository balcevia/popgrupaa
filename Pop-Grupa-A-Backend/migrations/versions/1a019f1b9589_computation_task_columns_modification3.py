"""computation task columns modification3

Revision ID: 1a019f1b9589
Revises: b1056134dfb4
Create Date: 2019-10-21 18:41:04.122763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a019f1b9589'
down_revision = 'b1056134dfb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ComputationTask', sa.Column('end_date', sa.DateTime(), nullable=True))
    op.add_column('ComputationTask', sa.Column('start_date', sa.DateTime(), nullable=True))
    op.drop_column('ComputationTask', 'start_time')
    op.drop_column('ComputationTask', 'end_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ComputationTask', sa.Column('end_time', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('ComputationTask', sa.Column('start_time', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('ComputationTask', 'start_date')
    op.drop_column('ComputationTask', 'end_date')
    # ### end Alembic commands ###