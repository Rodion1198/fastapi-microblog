"""Second

Revision ID: 36108e4e15a8
Revises: c8dab045753a
Create Date: 2022-04-07 17:38:38.741036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36108e4e15a8'
down_revision = 'c8dab045753a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    op.add_column('mictroblog_posts', sa.Column('user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'mictroblog_posts', 'user', ['user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mictroblog_posts', type_='foreignkey')
    op.drop_column('mictroblog_posts', 'user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
