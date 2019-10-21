"""computation task columns modification

Revision ID: b1056134dfb4
Revises: a615c14b885c
Create Date: 2019-10-21 18:20:42.626007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1056134dfb4'
down_revision = 'a615c14b885c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ComputationAccount', 'password')
    op.add_column('ComputationTask', sa.Column('app_id', sa.Integer(), nullable=False))
    op.alter_column('ComputationTask', 'end_time',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('ComputationTask', 'start_time',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ComputationTask', 'start_time',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('ComputationTask', 'end_time',
               existing_type=sa.DATE(),
               nullable=False)
    op.drop_column('ComputationTask', 'app_id')
    op.add_column('ComputationAccount', sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###