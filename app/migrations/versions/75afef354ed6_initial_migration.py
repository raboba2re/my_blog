"""Initial migration.

Revision ID: 75afef354ed6
Revises: 
Create Date: 2023-03-11 12:22:28.732665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75afef354ed6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=140), nullable=False),
    sa.Column('slug', sa.VARCHAR(length=140), nullable=False),
    sa.Column('body', sa.TEXT(), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###
