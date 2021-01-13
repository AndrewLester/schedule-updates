"""Create Models

Revision ID: 1995b16d172f
Revises: 
Create Date: 2021-01-12 21:45:47.182152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1995b16d172f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('update',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('realm', sa.String(), nullable=False),
    sa.Column('realm_id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('attachments', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('timezone', sa.String(length=120), nullable=True),
    sa.Column('profile_picture_url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('o_auth1_token',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('oauth_token', sa.String(length=48), nullable=False),
    sa.Column('oauth_token_secret', sa.String(length=48), nullable=True),
    sa.Column('user_id', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_user_id'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('scheduled_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scheduled_at', sa.DateTime(), nullable=False),
    sa.Column('scheduled_for', sa.DateTime(), nullable=False),
    sa.Column('update_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['update_id'], ['update.id'], name='fk_update_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scheduled_job')
    op.drop_table('o_auth1_token')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    op.drop_table('update')
    # ### end Alembic commands ###
