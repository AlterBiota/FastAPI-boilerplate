import uuid

from sqlalchemy import Boolean, Column, DateTime, Double, Integer, LargeBinary, String
from sqlalchemy.dialects.postgresql import ARRAY, UUID

from ..core.db.database import Base


class RawProcessedData(Base):
    __tablename__ = 'raw_processed_data'
    particle_id = Column(Integer, primary_key=True)
    img_id = Column(UUID(as_uuid=True), nullable=False)
    trigger_id = Column(UUID(as_uuid=True), nullable=False)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    volume = Column(Double)
    flatness = Column(Double)
    angularity = Column(Double)
    roughness = Column(Double)
    roundness = Column(Double)
    sphericity = Column(Double)
    mask_area = Column('mask area', Double)
    equivalent_circular_diameter = Column('equivalent circular diameter', Double)
    major_diameter_eq_ellipse = Column('major diameter eq ellipse', Double)
    minor_diameter_eq_ellipse = Column('minor diameter eq ellipse', Double)
    min_bounding_rectangle_width = Column('minimum bounding rectangle width', Double)
    min_bounding_rectangle_height = Column('minimum bounding rectangle height', Double)
    min_enclosing_circle_diameter = Column('min enclosing circle diameter', Double)


class TriggerRegister(Base):
    __tablename__ = 'trigger_register'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    camera_id = Column(String, nullable=False)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    start_ts = Column(DateTime, nullable=False)
    end_ts = Column(DateTime, nullable=False)
    is_ended = Column(Boolean, default=False)


class Img(Base):
    __tablename__ = 'img'
    img_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    trigger_id = Column(UUID(as_uuid=True), nullable=False)
    raw_img = Column(LargeBinary, nullable=False)


class InferenceMetadata(Base):
    __tablename__ = 'inference_metadata'
    img_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    particle_id = Column(Integer, primary_key=True)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    camera_id = Column(UUID(as_uuid=True), nullable=False)
    model_id = Column(String, nullable=False)
    bit_mask = Column(ARRAY(Integer), nullable=False)
    image_ts = Column(DateTime, nullable=False)
    inference_speed_ms = Column(Integer)
