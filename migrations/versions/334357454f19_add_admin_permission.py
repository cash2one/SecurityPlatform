"""add admin permission

Revision ID: 334357454f19
Revises: 41ffd3aafc90
Create Date: 2016-10-29 21:52:26.999000

"""

# revision identifiers, used by Alembic.
revision = '334357454f19'
down_revision = '41ffd3aafc90'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('permissions', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'permissions')
    ### end Alembic commands ###