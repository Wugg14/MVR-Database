"""empty message

Revision ID: 655dd2f05704
Revises: f92987044805
Create Date: 2019-10-11 13:12:40.155855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '655dd2f05704'
down_revision = 'f92987044805'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('report__echo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=12), nullable=True),
    sa.Column('doctor', sa.String(length=24), nullable=True),
    sa.Column('docSerialNum', sa.String(length=20), nullable=True),
    sa.Column('clinicSerialNum', sa.Integer(), nullable=True),
    sa.Column('clinicName', sa.String(length=24), nullable=True),
    sa.Column('patient', sa.String(length=24), nullable=True),
    sa.Column('breed', sa.String(length=24), nullable=True),
    sa.Column('owner', sa.String(length=24), nullable=True),
    sa.Column('sexPatient', sa.String(length=2), nullable=True),
    sa.Column('agePatient', sa.String(length=24), nullable=True),
    sa.Column('weightPatient', sa.Float(), nullable=True),
    sa.Column('clinicalHistory', sa.String(length=360), nullable=True),
    sa.Column('LVFW_Distolic_Thickness', sa.Float(), nullable=True),
    sa.Column('lower_range_LV_wall_D', sa.Float(), nullable=True),
    sa.Column('upper_range_LV_wall_D', sa.Float(), nullable=True),
    sa.Column('LVFW_DT_result', sa.String(length=5), nullable=True),
    sa.Column('LVFW_Systolic_Thickness', sa.Float(), nullable=True),
    sa.Column('lower_range_LV_wall_S', sa.Float(), nullable=True),
    sa.Column('upper_range_LV_wall_S', sa.Float(), nullable=True),
    sa.Column('LVFW_ST_result', sa.String(length=5), nullable=True),
    sa.Column('Left_Vent_Diastolic', sa.Float(), nullable=True),
    sa.Column('lower_range_LV_Chamber_D', sa.Float(), nullable=True),
    sa.Column('upper_range_LV_Chamber_D', sa.Float(), nullable=True),
    sa.Column('LV_DD_result', sa.String(length=5), nullable=True),
    sa.Column('Left_Vent_Systolic', sa.Float(), nullable=True),
    sa.Column('lower_range_LV_Chamber_S', sa.Float(), nullable=True),
    sa.Column('upper_range_LV_Chamber_S', sa.Float(), nullable=True),
    sa.Column('LV_SD_result', sa.String(length=5), nullable=True),
    sa.Column('Shortening_Fraction', sa.Float(), nullable=True),
    sa.Column('lower_range_fractional_shortening', sa.Float(), nullable=True),
    sa.Column('upper_range_fractional_shortening', sa.Float(), nullable=True),
    sa.Column('SF_result', sa.String(length=5), nullable=True),
    sa.Column('IVS_Diastolic_Thickness', sa.Float(), nullable=True),
    sa.Column('lower_range_septum_d', sa.Float(), nullable=True),
    sa.Column('upper_range_septum_d', sa.Float(), nullable=True),
    sa.Column('IVS_DT_result', sa.String(length=5), nullable=True),
    sa.Column('IVS_Systolic_Thickness', sa.Float(), nullable=True),
    sa.Column('lower_range_septum_s', sa.Float(), nullable=True),
    sa.Column('upper_range_septum_s', sa.Float(), nullable=True),
    sa.Column('IVS_ST_result', sa.String(length=5), nullable=True),
    sa.Column('Aortic_Root', sa.Float(), nullable=True),
    sa.Column('lower_range_aorta', sa.Float(), nullable=True),
    sa.Column('upper_range_aorta', sa.Float(), nullable=True),
    sa.Column('AR_result', sa.String(length=5), nullable=True),
    sa.Column('Left_Atrium', sa.Float(), nullable=True),
    sa.Column('lower_range_left_atrium', sa.Float(), nullable=True),
    sa.Column('upper_range_left_atrium', sa.Float(), nullable=True),
    sa.Column('LA_result', sa.String(length=5), nullable=True),
    sa.Column('Left_Atrium_over_AO', sa.Float(), nullable=True),
    sa.Column('lower_range_la_over_ao', sa.Float(), nullable=True),
    sa.Column('upper_range_la_over_ao', sa.Float(), nullable=True),
    sa.Column('la_over_ao_result', sa.Float(), nullable=True),
    sa.Column('EPSS', sa.Float(), nullable=True),
    sa.Column('upper_range_epss', sa.Float(), nullable=True),
    sa.Column('epss_result', sa.Float(), nullable=True),
    sa.Column('mMode_comments', sa.String(length=360), nullable=True),
    sa.Column('echo_doppler_findings', sa.String(length=450), nullable=True),
    sa.Column('Echo_B_mode_findings', sa.String(length=450), nullable=True),
    sa.Column('Echo_Conclusions', sa.String(length=450), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('report__echo')
    # ### end Alembic commands ###
