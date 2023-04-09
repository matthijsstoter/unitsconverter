import sys

from model import Model
from presenter import Presenter
from view import View
from PyQt5 import QtWidgets


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.run()

    app.setApplicationName("Units Converter")
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()