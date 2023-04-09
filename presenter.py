from model import Model
from view import View
from units import Units


class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
    
    def _connect(self) -> None:
        self.view.convert_from.activated.connect(self.handle_from_unit)
        self.view.convert_to.activated.connect(self.handle_to_unit)
        self.view.number_entry.textChanged.connect(self.handle_input_number)
        self.view.convert.clicked.connect(self.handle_compute_output)
    
    def handle_from_unit(self) -> None:
        self.view.get_from_unit()

    def handle_to_unit(self) -> None:
        self.view.get_to_unit()

    def handle_input_number(self) -> None:
        self.view.get_number_input()

    def handle_compute_output(self) -> None:
        from_unit = self.view.get_from_unit()
        to_unit = self.view.get_to_unit()
        input_text = self.view.get_number_input()

        if self.model.check_input_number(string=input_text) and self.model.check_units(unit1=from_unit, unit2=to_unit):
            input_number = float(input_text)
            output = self.model.convert(convert_from=from_unit, convert_to=to_unit, value=input_number)
            string = f"{output} {to_unit.value}"
            self.view.show_output(string)
        
        if not self.model.check_input_number(string=input_text):
            print(f"{input_text} is not a number")
            self.view.clear_putput()

        if not self.model.check_units(unit1=from_unit, unit2=to_unit):
            print(f"Unable to convert {from_unit.value} to {to_unit.value}")
            self.view.clear_putput()
    
    def run(self) -> None:
        self.view.list_units(self.model.units)
        self._connect()
        self.view.show()