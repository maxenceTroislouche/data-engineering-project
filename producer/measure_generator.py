import datetime
import random

from pacemaker import PacemakerMeasure, Pacemaker, PacemakerMeasureType, PacemakerAlertLevel, PacemakerAlertCode


def _generate_random_number_between_1_and_100() -> int:
    """
    Generate a random number between 1 and 100
    :return: int
    """
    return random.randint(1, 100)


def _generate_random_measure_type() -> PacemakerMeasureType:
    """
    Generate a random measure type
    :return: PacemakerMeasureType
    """
    generated_number = _generate_random_number_between_1_and_100()

    if generated_number <= 70:
        return PacemakerMeasureType.STANDARD
    if generated_number <= 90:
        return PacemakerMeasureType.INCIDENT
    return PacemakerMeasureType.ALERT


def _generate_random_alert_level(type: PacemakerMeasureType) -> PacemakerAlertLevel:
    """
    Generate a random alert level
    :return: PacemakerAlertLevel
    """
    if type == PacemakerMeasureType.STANDARD:
        return PacemakerAlertLevel.LOW

    if type == PacemakerMeasureType.INCIDENT:
        generated_number = _generate_random_number_between_1_and_100()

        if generated_number <= 70:
            return PacemakerAlertLevel.MEDIUM
        return PacemakerAlertLevel.HIGH

    # ALERT
    return PacemakerAlertLevel.CRITICAL

def _generate_alert_code(alert_level: PacemakerAlertLevel) -> PacemakerAlertCode:
    """
    Generate a random alert code
    :return: str
    """
    if alert_level == PacemakerAlertLevel.LOW:
        return PacemakerAlertCode.STANDARD

    if alert_level in (PacemakerAlertLevel.MEDIUM, PacemakerAlertLevel.HIGH):
        generated_number = _generate_random_number_between_1_and_100()
        if generated_number <= 25:
            return PacemakerAlertCode.HEART_RATE_LOW
        if generated_number <= 50:
            return PacemakerAlertCode.HEART_RATE_HIGH
        if generated_number <= 75:
            return PacemakerAlertCode.BODY_TEMPERATURE_LOW
        return PacemakerAlertCode.BODY_TEMPERATURE_HIGH

    generated_number = _generate_random_number_between_1_and_100()
    if generated_number <= 13:
        return PacemakerAlertCode.HEART_RATE_VERY_HIGH
    if generated_number <= 25:
        return PacemakerAlertCode.HEART_RATE_VERY_LOW
    if generated_number <= 38:
        return PacemakerAlertCode.BODY_TEMPERATURE_VERY_HIGH
    if generated_number <= 50:
        return PacemakerAlertCode.BODY_TEMPERATURE_VERY_LOW

    return PacemakerAlertCode.BATTERY_LOW


def _generate_heart_rate(alert_code: PacemakerAlertCode) -> int:
    """
    Generate a random heart rate
    :return: int
    """
    if alert_code == PacemakerAlertCode.HEART_RATE_LOW:
        return random.randint(40, 60)

    if alert_code == PacemakerAlertCode.HEART_RATE_HIGH:
        return random.randint(100, 180)

    if alert_code == PacemakerAlertCode.HEART_RATE_VERY_LOW:
        return random.randint(30, 40)

    if alert_code == PacemakerAlertCode.HEART_RATE_VERY_HIGH:
        return random.randint(180, 220)

    return random.randint(60, 100)

def _generate_body_temperature(alert_code: PacemakerAlertCode) -> float:
    """
    Generate a random body temperature
    :return: float
    """
    if alert_code == PacemakerAlertCode.BODY_TEMPERATURE_LOW:
        return random.uniform(34.0, 36.0)

    if alert_code == PacemakerAlertCode.BODY_TEMPERATURE_HIGH:
        return random.uniform(38.0, 40.0)

    if alert_code == PacemakerAlertCode.BODY_TEMPERATURE_VERY_LOW:
        return random.uniform(30.0, 34.0)

    if alert_code == PacemakerAlertCode.BODY_TEMPERATURE_VERY_HIGH:
        return random.uniform(40.0, 42.0)

    return random.uniform(36.0, 38.0)

def generate_measure_for_pacemaker(pacemaker: Pacemaker) -> PacemakerMeasure:
    """
    Generate a random measure for a pacemaker
    :param pacemaker: Pacemaker
    :return: PacemakerMeasure
    """
    current_datetime = datetime.datetime.now()
    measure_type = _generate_random_measure_type()
    alert_level = _generate_random_alert_level(measure_type)
    alert_code = _generate_alert_code(alert_level)
    heart_rate = _generate_heart_rate(alert_code)
    body_temperature = _generate_body_temperature(alert_code)

    return PacemakerMeasure(
        pacemaker=pacemaker,
        date=current_datetime,
        type=measure_type,
        alert_level=alert_level,
        alert_code=alert_code,
        heart_rate=heart_rate,
        body_temperature=body_temperature
    )
