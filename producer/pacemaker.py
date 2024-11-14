import datetime
import enum
from dataclasses import dataclass

@dataclass
class Pacemaker:
    """
    Base class for a Pacemaker
    """
    id: int

class PacemakerMeasureType(enum.Enum):
    """
    Enum for the type of measure
    """
    STANDARD = "STANDARD"
    INCIDENT = "INCIDENT"
    ALERT = "ALERT"


class PacemakerAlertLevel(enum.Enum):
    """
    Enum for the alert level
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class PacemakerAlertCode(enum.Enum):
    """
    Enum for the alert codes
    """
    # STANDARD
    STANDARD = "standard"
    # INCIDENT
    HEART_RATE_LOW = "heart rate low"
    HEART_RATE_HIGH = "heart rate high"
    BODY_TEMPERATURE_LOW = "body temperature low"
    BODY_TEMPERATURE_HIGH = "body temperature high"
    # ALERT
    BATTERY_LOW = "battery low"
    HEART_RATE_VERY_LOW = "heart rate very low"
    HEART_RATE_VERY_HIGH = "heart rate very high"
    BODY_TEMPERATURE_VERY_LOW = "body temperature very low"
    BODY_TEMPERATURE_VERY_HIGH = "body temperature very high"


@dataclass
class PacemakerMeasure:
    pacemaker: Pacemaker
    date: datetime.datetime
    type: PacemakerMeasureType
    alert_level: PacemakerAlertLevel
    alert_code: PacemakerAlertCode
    heart_rate: int
    body_temperature: float
