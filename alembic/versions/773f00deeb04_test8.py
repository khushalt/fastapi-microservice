"""test8

Revision ID: 773f00deeb04
Revises: 8b0ea93e7a10
Create Date: 2023-04-13 15:43:05.059744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '773f00deeb04'
down_revision = '8b0ea93e7a10'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('email', sa.String(length=255), nullable=False), schema='customer')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'email', schema='customer')
    # ### end Alembic commands ###