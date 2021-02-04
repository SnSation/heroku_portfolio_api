"""empty message

Revision ID: 6aa5a52de032
Revises: 1fd7d8e75e07
Create Date: 2021-01-30 17:23:19.254629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aa5a52de032'
down_revision = '1fd7d8e75e07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'v3__navbar', 'v3__image', ['icon'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'v3__navbar', type_='foreignkey')
    # ### end Alembic commands ###
