"""1  Migration

Revision ID: efb7db437467
Revises: 9a69fc288c6f
Create Date: 2022-08-19 01:59:35.924338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efb7db437467'
down_revision = '9a69fc288c6f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('FBPAGE', 'post_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('FBPAGE', sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
