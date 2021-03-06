"""empty message

Revision ID: b7d09e7e34f4
Revises: ad73e72a62f4
Create Date: 2021-01-16 16:32:40.671154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7d09e7e34f4'
down_revision = 'ad73e72a62f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('last_edit', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_post', 'last_edit')
    # ### end Alembic commands ###
