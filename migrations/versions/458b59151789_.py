"""empty message

Revision ID: 458b59151789
Revises: b7d09e7e34f4
Create Date: 2021-01-16 17:20:49.281514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '458b59151789'
down_revision = 'b7d09e7e34f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('last_edit', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'last_edit')
    # ### end Alembic commands ###
