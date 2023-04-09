from PyQt5 import QtWidgets
from units import Units


class View(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 400, 400)
        self.setWindowTitle("Units Converter")
        self.create_ui()
    
    def create_ui(self) -> None:
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.create_top_layout())
        self.main_layout.addLayout(self.create_bottom_layout())

        self.setLayout(self.main_layout)
    
    def create_top_layout(self):
        layout = QtWidgets.QHBoxLayout()

        self.convert_from = QtWidgets.QComboBox()
        layout.addWidget(self.convert_from)

        self.convert_to = QtWidgets.QComboBox()
        layout.addWidget(self.convert_to)

        return layout 

    def create_bottom_layout(self) -> QtWidgets.QHBoxLayout:
        layout = QtWidgets.QHBoxLayout()

        self.number_entry = QtWidgets.QLineEdit()
        self.number_entry.setPlaceholderText("Enter the number you want to convert")
        layout.addWidget(self.number_entry)

        self.convert = QtWidgets.QPushButton("Convert")
        layout.addWidget(self.convert)

        self.output_value = QtWidgets.QLabel()
        layout.addWidget(self.output_value)

        return layout
    
    def _get_mapped_unit(self, text: str) -> Units:
        for unit in Units:
            if unit.value == text:
                return Units[unit.name]
    
    def get_from_unit(self) -> Units:
        user_input = self.convert_from.currentText()
        return self._get_mapped_unit(user_input)
    
    def get_to_unit(self) -> Units:
        user_input = self.convert_to.currentText()
        return self._get_mapped_unit(user_input)
    
    def get_number_input(self) -> str:
        text = self.number_entry.text()
        return text
    
    def show_output(self, string: str) -> None:
        self.output_value.setText(string)
    
    def clear_putput(self) -> None:
        self.output_value.setText("")
    
    def list_units(self, units: list[Units]) -> None:
        for unit in units:
            self.convert_from.addItem(unit.value)
            self.convert_to.addItem(unit.value)
        