"""empty message

Revision ID: 7597ee8b3fca
Revises: ba36fba603bf
Create Date: 2023-07-21 08:05:25.309529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7597ee8b3fca'
down_revision = 'ba36fba603bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###