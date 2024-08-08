"""empty message

Revision ID: 0f6b0991e995
Revises: 72c12b41582d
Create Date: 2024-08-07 08:18:36.319058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f6b0991e995'
down_revision = '72c12b41582d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('allergies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('allergies', schema=None) as batch_op:
        batch_op.drop_column('img')

    # ### end Alembic commands ###
