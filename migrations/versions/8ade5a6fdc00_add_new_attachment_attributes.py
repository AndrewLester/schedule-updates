"""Add new attachment attributes

Revision ID: 8ade5a6fdc00
Revises: 5a0eb5916ecc
Create Date: 2021-03-24 14:54:34.400845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ade5a6fdc00'
down_revision = '5a0eb5916ecc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attachment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(length=5), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=300), nullable=False),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('icon', sa.Text(), nullable=True),
    sa.Column('update_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['update_id'], ['update.id'], name='fk_attachment_update_id'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('update', schema=None) as batch_op:
        batch_op.drop_column('attachments')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('update', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attachments', sa.VARCHAR(), nullable=False))

    op.drop_table('attachment')
    # ### end Alembic commands ###
