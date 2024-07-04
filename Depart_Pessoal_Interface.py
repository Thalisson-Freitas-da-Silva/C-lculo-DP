import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QDialog

class GanhoDiario(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cálculo de Ganho Diário')
        self.setFixedSize(300, 150)

        # Definindo o estilo da janela
        self.setStyleSheet("background-color: #81f2fc;")

        # Layout principal
        main_layout = QVBoxLayout()

        # Entrada para Ganho Mensal
        self.label_ganho_mensal = QLabel('Digite o valor ganho por mês: R$', self)
        main_layout.addWidget(self.label_ganho_mensal)
        self.input_ganho_mensal = QLineEdit(self)
        self.input_ganho_mensal.setStyleSheet("background-color: white;")
        main_layout.addWidget(self.input_ganho_mensal)

        # Botão para calcular
        self.calc_button = QPushButton('Calcular', self)
        self.calc_button.setStyleSheet("background-color: #2ad4c3; color: black;")
        self.calc_button.clicked.connect(self.calculate)
        main_layout.addWidget(self.calc_button)

        # Configura o layout principal
        self.setLayout(main_layout)

    def calculate(self):
        try:
            ganho_mensal = float(self.input_ganho_mensal.text())
        except ValueError:
            QMessageBox.warning(self, 'Erro', 'Por favor, insira um valor válido.')
            return

        # Ganho Diário
        ganho_diario = ganho_mensal / 30
        QMessageBox.information(self, 'Resultado', f'Ganho Diário: R$ {ganho_diario:.2f}')

class DepartamentoPessoal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Departamento Pessoal')
        self.setFixedSize(300, 200)

        # Definindo o estilo da janela
        self.setStyleSheet("background-color: #81f2fc;")

        # Layout principal
        main_layout = QVBoxLayout()

        # Combobox para selecionar a operação
        self.operation_combo = QComboBox(self)
        self.operation_combo.addItem("Selecione uma operação")
        self.operation_combo.addItem("Cálculo de Férias")
        self.operation_combo.addItem("Cálculo do 13° Salário")

        # Definindo o background do ComboBox como branco e aumentando a altura
        self.operation_combo.setStyleSheet("background-color: white; min-height: 20px;")
        main_layout.addWidget(self.operation_combo)

        # Entrada para Ganho Mensal
        self.label_ganho_mensal = QLabel('Digite o valor ganho por mês: R$', self)
        main_layout.addWidget(self.label_ganho_mensal)
        self.input_ganho_mensal = QLineEdit(self)
        self.input_ganho_mensal.setStyleSheet("background-color: white;")
        main_layout.addWidget(self.input_ganho_mensal)

        # Entrada para Meses Trabalhados
        self.label_meses_trabalhados = QLabel('Digite a quantidade de meses trabalhados:', self)
        main_layout.addWidget(self.label_meses_trabalhados)
        self.input_meses_trabalhados = QLineEdit(self)
        self.input_meses_trabalhados.setStyleSheet("background-color: white;")
        main_layout.addWidget(self.input_meses_trabalhados)

        # Botão para calcular
        self.calc_button = QPushButton('Calcular', self)
        self.calc_button.setStyleSheet("background-color: #2ad4c3; color: black;")
        self.calc_button.clicked.connect(self.calculate)
        main_layout.addWidget(self.calc_button)

        # Botão para abrir a janela de Ganho Diário
        self.ganho_diario_button = QPushButton('Calcular Ganho Diário', self)
        self.ganho_diario_button.setStyleSheet("background-color: #2ad4c3; color: black;")
        self.ganho_diario_button.clicked.connect(self.openGanhoDiarioWindow)
        main_layout.addWidget(self.ganho_diario_button)

        # Configura o layout principal
        self.setLayout(main_layout)

    def openGanhoDiarioWindow(self):
        self.ganho_diario_window = GanhoDiario()
        self.ganho_diario_window.exec_()

    def calculate(self):
        opc = self.operation_combo.currentIndex()
        try:
            ganho_mensal = float(self.input_ganho_mensal.text())
            meses_trabalhados = int(self.input_meses_trabalhados.text())
        except ValueError:
            QMessageBox.warning(self, 'Erro', 'Por favor, insira valores válidos.')
            return

        if opc == 1:
            # Cálculo de Férias
            proporcional_ferias = (ganho_mensal / 12) * meses_trabalhados
            ferias_total = (proporcional_ferias / 3) + proporcional_ferias
            QMessageBox.information(self, 'Resultado', f'Férias: R$ {ferias_total:.2f}')
        elif opc == 2:
            # Cálculo do 13° Salário
            decimo_terceiro = (ganho_mensal / 12) * meses_trabalhados
            QMessageBox.information(self, 'Resultado', f'13° Salário: R$ {decimo_terceiro:.2f}')
        else:
            QMessageBox.warning(self, 'Erro', 'Por favor, selecione uma operação válida.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DepartamentoPessoal()
    window.show()
    sys.exit(app.exec_())
