from typing import Iterable, Tuple
def temperature_tuple_v2(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    h = ()
    for item in temperatures:
        if input_unit_of_measurement == 'a':
            h+= (item,float('{:.2f}'.format((item - 32) * 5 / 9 + 273.15))),
    return h