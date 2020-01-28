"""empty message

Revision ID: 25c846a6302c
Revises: 
Create Date: 2020-01-08 15:31:04.286769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25c846a6302c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clinic',
    sa.Column('clinicSerialNum', sa.String(length=64), nullable=False),
    sa.Column('company', sa.String(length=64), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('street', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=10), nullable=True),
    sa.Column('zip', sa.Integer(), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('note', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('clinicSerialNum'),
    sa.UniqueConstraint('company'),
    sa.UniqueConstraint('nickname')
    )
    op.create_table('misc_service',
    sa.Column('serviceID', sa.String(length=20), nullable=False),
    sa.Column('serviceType', sa.String(length=20), nullable=True),
    sa.Column('serviceAbbr', sa.String(length=10), nullable=True),
    sa.Column('reportType', sa.String(length=5), nullable=True),
    sa.Column('description', sa.String(length=144), nullable=True),
    sa.Column('servicePrice', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('serviceID')
    )
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
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_report_CT_timestamp'), 'report_CT', ['timestamp'], unique=False)
    op.create_table('report_US',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('docSerialNum', sa.String(length=20), nullable=True),
    sa.Column('patient', sa.String(length=24), nullable=True),
    sa.Column('owner', sa.String(length=24), nullable=True),
    sa.Column('species', sa.String(length=6), nullable=True),
    sa.Column('breed', sa.String(length=24), nullable=True),
    sa.Column('sexPatient', sa.String(length=2), nullable=True),
    sa.Column('agePatient', sa.String(length=24), nullable=True),
    sa.Column('clinicalHistory', sa.String(length=360), nullable=True),
    sa.Column('SF_Liver', sa.String(length=12), nullable=True),
    sa.Column('SF_Spleen', sa.String(length=12), nullable=True),
    sa.Column('SF_Stomach', sa.String(length=12), nullable=True),
    sa.Column('SF_Pancreas', sa.String(length=12), nullable=True),
    sa.Column('SF_Intestines', sa.String(length=12), nullable=True),
    sa.Column('SF_Adrenals', sa.String(length=12), nullable=True),
    sa.Column('SF_LKidney', sa.String(length=12), nullable=True),
    sa.Column('SF_RKidney', sa.String(length=12), nullable=True),
    sa.Column('SF_Bladder', sa.String(length=12), nullable=True),
    sa.Column('SF_Sublum', sa.String(length=12), nullable=True),
    sa.Column('SF_Prostate', sa.String(length=12), nullable=True),
    sa.Column('SF_Uterus', sa.String(length=12), nullable=True),
    sa.Column('Conclusions_ALL', sa.String(length=360), nullable=True),
    sa.Column('FINDAS_ALL', sa.String(length=360), nullable=True),
    sa.Column('date', sa.String(length=12), nullable=True),
    sa.Column('clinicSerialNum', sa.Integer(), nullable=True),
    sa.Column('clinicName', sa.String(length=24), nullable=True),
    sa.Column('doctor', sa.String(length=24), nullable=True),
    sa.Column('mvr4seasons', sa.String(length=24), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_report_US_timestamp'), 'report_US', ['timestamp'], unique=False)
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
    sa.Column('mvr4seasons', sa.String(length=24), nullable=True),
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
    sa.Column('la_over_ao_result', sa.String(length=5), nullable=True),
    sa.Column('EPSS', sa.Float(), nullable=True),
    sa.Column('upper_range_epss', sa.Float(), nullable=True),
    sa.Column('epss_result', sa.String(length=5), nullable=True),
    sa.Column('mMode_comments', sa.String(length=360), nullable=True),
    sa.Column('echo_doppler_findings', sa.String(length=450), nullable=True),
    sa.Column('Echo_B_mode_findings', sa.String(length=450), nullable=True),
    sa.Column('Echo_Conclusions', sa.String(length=450), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_report__echo_timestamp'), 'report__echo', ['timestamp'], unique=False)
    op.create_table('report__misc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor', sa.String(length=24), nullable=True),
    sa.Column('docSerialNum', sa.String(length=20), nullable=True),
    sa.Column('clinicSerialNum', sa.Integer(), nullable=True),
    sa.Column('clinicName', sa.String(length=24), nullable=True),
    sa.Column('mvr4seasons', sa.String(length=24), nullable=True),
    sa.Column('patient', sa.String(length=24), nullable=True),
    sa.Column('owner', sa.String(length=24), nullable=True),
    sa.Column('service', sa.String(length=24), nullable=True),
    sa.Column('SvcTotal', sa.Numeric(), nullable=True),
    sa.Column('Misc_Service_Description', sa.String(length=300), nullable=True),
    sa.Column('date', sa.String(length=12), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_report__misc_timestamp'), 'report__misc', ['timestamp'], unique=False)
    op.create_table('report__radiographic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor', sa.String(length=24), nullable=True),
    sa.Column('docSerialNum', sa.String(length=20), nullable=True),
    sa.Column('patient', sa.String(length=24), nullable=True),
    sa.Column('species', sa.String(length=6), nullable=True),
    sa.Column('owner', sa.String(length=24), nullable=True),
    sa.Column('Rad_Image_Date', sa.String(length=12), nullable=True),
    sa.Column('Rad_NumImages', sa.Integer(), nullable=True),
    sa.Column('RadView', sa.String(length=24), nullable=True),
    sa.Column('Rad_Findings', sa.String(length=360), nullable=True),
    sa.Column('Rad_Conclusions', sa.String(length=360), nullable=True),
    sa.Column('Clinic_Phone', sa.String(length=20), nullable=True),
    sa.Column('date', sa.String(length=12), nullable=True),
    sa.Column('clinicSerialNum', sa.Integer(), nullable=True),
    sa.Column('clinic', sa.String(length=24), nullable=True),
    sa.Column('mvr4seasons', sa.String(length=24), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_report__radiographic_timestamp'), 'report__radiographic', ['timestamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('doctor',
    sa.Column('doctorSerialNum', sa.String(length=64), nullable=False),
    sa.Column('first', sa.String(length=24), nullable=True),
    sa.Column('middle', sa.String(length=3), nullable=True),
    sa.Column('last', sa.String(length=24), nullable=True),
    sa.Column('cell', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('note', sa.String(length=140), nullable=True),
    sa.Column('salutation', sa.String(length=4), nullable=True),
    sa.Column('clinicName', sa.String(length=20), nullable=True),
    sa.Column('clinicSerialNum', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['clinicSerialNum'], ['clinic.clinicSerialNum'], ),
    sa.PrimaryKeyConstraint('doctorSerialNum')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_table('doctor')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_report__radiographic_timestamp'), table_name='report__radiographic')
    op.drop_table('report__radiographic')
    op.drop_index(op.f('ix_report__misc_timestamp'), table_name='report__misc')
    op.drop_table('report__misc')
    op.drop_index(op.f('ix_report__echo_timestamp'), table_name='report__echo')
    op.drop_table('report__echo')
    op.drop_index(op.f('ix_report_US_timestamp'), table_name='report_US')
    op.drop_table('report_US')
    op.drop_index(op.f('ix_report_CT_timestamp'), table_name='report_CT')
    op.drop_table('report_CT')
    op.drop_table('misc_service')
    op.drop_table('clinic')
    # ### end Alembic commands ###