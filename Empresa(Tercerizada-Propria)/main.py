from Cadastro import JanelaInicial
from PySide6.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaInicial()
    janela.show()
    sys.exit(app.exec_())