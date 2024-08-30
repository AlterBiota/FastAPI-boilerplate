"""empty message

Revision ID: ea64bee06815
Revises: 466399921e39
Create Date: 2024-08-30 10:03:13.138267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ea64bee06815'
down_revision: Union[str, None] = '466399921e39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('img',
    sa.Column('img_id', sa.UUID(), nullable=False),
    sa.Column('customer_id', sa.UUID(), nullable=False),
    sa.Column('trigger_id', sa.UUID(), nullable=False),
    sa.Column('raw_img', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('img_id')
    )
    op.create_table('inference_metadata',
    sa.Column('img_id', sa.UUID(), nullable=False),
    sa.Column('particle_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.UUID(), nullable=False),
    sa.Column('camera_id', sa.UUID(), nullable=False),
    sa.Column('model_id', sa.String(), nullable=False),
    sa.Column('bit_mask', postgresql.ARRAY(sa.Integer()), nullable=False),
    sa.Column('image_ts', sa.DateTime(), nullable=False),
    sa.Column('inference_speed_ms', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('img_id', 'particle_id')
    )
    op.create_table('raw_processed_data',
    sa.Column('particle_id', sa.Integer(), nullable=False),
    sa.Column('img_id', sa.UUID(), nullable=False),
    sa.Column('trigger_id', sa.UUID(), nullable=False),
    sa.Column('customer_id', sa.UUID(), nullable=False),
    sa.Column('volume', sa.Double(), nullable=True),
    sa.Column('flatness', sa.Double(), nullable=True),
    sa.Column('angularity', sa.Double(), nullable=True),
    sa.Column('roughness', sa.Double(), nullable=True),
    sa.Column('roundness', sa.Double(), nullable=True),
    sa.Column('sphericity', sa.Double(), nullable=True),
    sa.Column('mask area', sa.Double(), nullable=True),
    sa.Column('equivalent circular diameter', sa.Double(), nullable=True),
    sa.Column('major diameter eq ellipse', sa.Double(), nullable=True),
    sa.Column('minor diameter eq ellipse', sa.Double(), nullable=True),
    sa.Column('minimum bounding rectangle width', sa.Double(), nullable=True),
    sa.Column('minimum bounding rectangle height', sa.Double(), nullable=True),
    sa.Column('min enclosing circle diameter', sa.Double(), nullable=True),
    sa.PrimaryKeyConstraint('particle_id')
    )
    op.create_table('trigger_register',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('camera_id', sa.String(), nullable=False),
    sa.Column('customer_id', sa.UUID(), nullable=False),
    sa.Column('start_ts', sa.DateTime(), nullable=False),
    sa.Column('end_ts', sa.DateTime(), nullable=False),
    sa.Column('is_ended', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trigger_register')
    op.drop_table('raw_processed_data')
    op.drop_table('inference_metadata')
    op.drop_table('img')
    # ### end Alembic commands ###
