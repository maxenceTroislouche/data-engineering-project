import json

from pacemaker import PacemakerMeasure


def get_json_string_from_pacemaker_measure(measure: PacemakerMeasure) -> str:
    """
    Get a JSON string from a PacemakerMeasure
    :param measure: PacemakerMeasure
    :return: str
    """
    return json.dumps({
        'pacemakerId': measure.pacemaker.id,
        'date': measure.date.strftime('%Y-%m-%d %H:%M:%S'),
        'measureNature': measure.type.value,
        'alertLevel': measure.alert_level.value,
        'alertCode': measure.alert_code.value,
        'heartRate': measure.heart_rate,
        'bodyTemperature': measure.body_temperature
    })
