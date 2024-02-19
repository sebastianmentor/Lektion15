"""Add confirmed_ad corrected

Revision ID: a1aa76029cb1
Revises: 6bd9db9643b7
Create Date: 2024-02-19 09:59:23.865537

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a1aa76029cb1'
down_revision = '6bd9db9643b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('confirmed_at',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('confirmed_at',
               existing_type=sa.DateTime(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)

    # ### end Alembic commands ###