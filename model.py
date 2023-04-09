from units import CONVERTER, Units


class Model:
    conversions = CONVERTER

    def __init__(self):
        pass

    def convert(self, convert_from: Units, convert_to: Units, value: float | int):
        return self.conversions[(convert_from, convert_to)](value)
    
    @property
    def units(self) -> list[Units]:
        return [f for f in Units]
    
    def match_units(self, user_unit: Units) -> list[Units]:
        allowed_units: list[Units] = []

        for units, _ in self.conversions.items():
            if user_unit in units:
                allowed_units.append(units)
        
        return allowed_units
    
    def check_units(self, unit1, unit2) -> bool:
        return (unit1, unit2) in self.conversions         

    def check_input_number(self, string: str) -> bool:
        return string.isnumeric()