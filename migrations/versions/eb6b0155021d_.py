"""empty message

Revision ID: eb6b0155021d
Revises: 9bc04a919347
Create Date: 2021-01-16 15:02:24.201915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb6b0155021d'
down_revision = '9bc04a919347'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('author', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blog_post', 'user', ['author'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blog_post', type_='foreignkey')
    op.drop_column('blog_post', 'author')
    # ### end Alembic commands ###
