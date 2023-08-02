# Qt GUI app entry file

import sys
import traceback
from types import TracebackType

from PySide6.QtWidgets import QApplication, QMessageBox

from pyside_app.utils import logger
from pyside_app.views import MainWindow


def handleException(
    _type: type[BaseException],
    _value: BaseException,
    _traceback: TracebackType,
) -> None:
    logger.exception(
        "Unhandled exception:",
        exc_info=(_type, _value, _traceback),
    )
    error_details = "".join(
        traceback.format_exception(_type, _value, _traceback),
    )
    QMessageBox.critical(
        None,  # type: ignore reportGeneralTypeIssues
        "Unhandled Exception",
        "An unhandled exception occurred.\n\n" + error_details,
    )
    QApplication.quit()


def main() -> None:
    # Start Qt application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Exception handler
    sys.excepthook = handleException

    logger.info("Starting Qt application")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
