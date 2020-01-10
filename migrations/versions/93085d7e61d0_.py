"""empty message

Revision ID: 93085d7e61d0
Revises: 655dd2f05704
Create Date: 2019-10-11 13:59:20.424157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93085d7e61d0'
down_revision = '655dd2f05704'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('report__echo', sa.Column('mvr4seasons', sa.String(length=24), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('report__echo', 'mvr4seasons')
    # ### end Alembic commands ###