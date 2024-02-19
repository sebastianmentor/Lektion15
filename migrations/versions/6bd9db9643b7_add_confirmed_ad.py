"""Add confirmed_ad

Revision ID: 6bd9db9643b7
Revises: b638fc48543b
Create Date: 2024-02-19 09:58:27.659121

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6bd9db9643b7'
down_revision = 'b638fc48543b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed_at', sa.Boolean(), nullable=True))
        batch_op.drop_column('confirmed')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
        batch_op.drop_column('confirmed_at')

    # ### end Alembic commands ###
