"""empty message

Revision ID: ecb5cbcf4f99
Revises: None
Create Date: 2016-11-09 10:02:59.117000

"""

# revision identifiers, used by Alembic.
revision = 'ecb5cbcf4f99'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('visitNum', sa.Integer(), nullable=True),
    sa.Column('updatedTime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('about', sa.Text(), nullable=False),
    sa.Column('logo', sa.String(length=128), nullable=True),
    sa.Column('topicNum', sa.Integer(), nullable=True),
    sa.Column('createdTime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stocks',
    sa.Column('code', sa.String(length=16), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('is_password_reset_link_valid', sa.Boolean(), nullable=True),
    sa.Column('is_valid_registered', sa.Boolean(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=False),
    sa.Column('avatar_url', sa.String(length=64), nullable=True),
    sa.Column('telephone', sa.String(length=32), nullable=True),
    sa.Column('personal_id', sa.String(length=32), nullable=True),
    sa.Column('personal_profile', sa.Text(), nullable=True),
    sa.Column('topicNum', sa.Integer(), nullable=False),
    sa.Column('postNum', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('visitNum', sa.Integer(), nullable=True),
    sa.Column('postNum', sa.Integer(), nullable=True),
    sa.Column('groupID', sa.Integer(), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('createdTime', sa.DateTime(), nullable=True),
    sa.Column('updatedTime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['groupID'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('stock_id', sa.String(length=16), nullable=True),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('is_buy', sa.Boolean(), nullable=True),
    sa.Column('tradeTime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['stock_id'], ['stocks.code'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_stock',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('stock_id', sa.String(length=16), nullable=False),
    sa.Column('average_price', sa.Float(), nullable=True),
    sa.Column('own_num', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['stock_id'], ['stocks.code'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'stock_id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=1024), nullable=False),
    sa.Column('topicID', sa.Integer(), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('createdTime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['topicID'], ['topics.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('user_stock')
    op.drop_table('trades')
    op.drop_table('topics')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('stocks')
    op.drop_table('groups')
    op.drop_table('articles')
    ### end Alembic commands ###
