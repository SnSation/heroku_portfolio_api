"""empty message

Revision ID: 1fd7d8e75e07
Revises: 3056872665e8
Create Date: 2021-01-30 17:21:44.233243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fd7d8e75e07'
down_revision = '3056872665e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('v3__navbar', sa.Column('icon', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('v3__navbar', 'icon')
    # ### end Alembic commands ###
