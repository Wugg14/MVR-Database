"""empty message

Revision ID: 3ef6e3e24b8b
Revises: 9e463b131e5b
Create Date: 2019-08-21 12:26:54.516890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ef6e3e24b8b'
down_revision = '9e463b131e5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('report_CT',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor', sa.String(length=24), nullable=True),
    sa.Column('docSerialNum', sa.String(length=20), nullable=True),
    sa.Column('patient', sa.String(length=24), nullable=True),
    sa.Column('species', sa.String(length=6), nullable=True),
    sa.Column('owner', sa.String(length=24), nullable=True),
    sa.Column('CT_Image_Date', sa.String(length=12), nullable=True),
    sa.Column('CT_NumImages', sa.Integer(), nullable=True),
    sa.Column('CTView', sa.String(length=24), nullable=True),
    sa.Column('CT_Findings', sa.String(length=360), nullable=True),
    sa.Column('CT_Conclusions', sa.String(length=360), nullable=True),
    sa.Column('Clinic_Phone', sa.String(length=20), nullable=True),
    sa.Column('date', sa.String(length=12), nullable=True),
    sa.Column('clinicSerialNum', sa.Integer(), nullable=True),
    sa.Column('clinic', sa.String(length=24), nullable=True),
    sa.Column('mvr4seasons', sa.String(length=24), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('report_CT')
    # ### end Alembic commands ###