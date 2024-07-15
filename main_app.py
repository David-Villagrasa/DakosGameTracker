import sys
import csv
import os
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main import Ui_MainWindow
from table import Ui_Dialog

CONFIG_FILE = 'config.json'

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.selected_folder = ""  # attribute to store the selected folder path
        self.files = {}  # dictionary to store the mapping of years to files
        self.load_config()  # load configuration from JSON file

        self.btnOpenYear.clicked.connect(self.open_dialog)
        self.actionExit.triggered.connect(self.close_application)
        self.actionSet_Folder.triggered.connect(self.set_folder)  # connect the Set Folder action
        self.actionLoad_Files.triggered.connect(self.reload_files)  # connect the Load Files action

    def open_dialog(self):
        selected_year = self.cbYears.currentText()
        if selected_year in self.files:
            file_path = self.files[selected_year]
            dialog = SecondDialog(self, file_path)
            dialog.exec_()

    def close_application(self):
        self.save_config()  # save configuration before closing
        self.close()

    def set_folder(self):
        # open the dialog to select a folder
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.selected_folder = folder
            self.update_file_info()
            self.save_config()  # save configuration after setting the folder

    def reload_files(self):
        # reload the files as if pressing F5
        if self.selected_folder:
            self.update_file_info()

    def update_file_info(self):
        # get all .txt files that match the pattern "YYYY juegos jugados"
        files = [f for f in os.listdir(self.selected_folder) if f.endswith('.txt') and 'juegos jugados' in f]
        self.lbl_numberOf.setText(str(len(files)))  # update the label with the number of files
        self.cbYears.clear()  # clear existing items in the combo box
        self.files = {f.split(' ')[0]: os.path.join(self.selected_folder, f) for f in files if f.split(' ')[0].isdigit()}
        years = sorted(self.files.keys())
        self.cbYears.addItems(years)  # add years to the combo box

    def load_config(self):
        # load configuration from JSON file
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                self.selected_folder = config.get('selected_folder', '')
                if self.selected_folder:
                    self.update_file_info()

    def save_config(self):
        # save configuration to JSON file
        config = {
            'selected_folder': self.selected_folder
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f)


class SecondDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None, file_path=""):
        super(SecondDialog, self).__init__(parent)
        self.setupUi(self)
        self.file_path = file_path
        self.load_data()
        self.saveButton.clicked.connect(self.save_data)
        self.refreshButton.clicked.connect(self.load_data)

    def load_data(self):
        self.tableWidget.setRowCount(0)
        if not self.file_path:
            return
        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Juego", "Fechas", "Nota sobre 10", "Comentarios adicionales"])
            for row_data in reader:
                row_number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(data))

    def save_data(self):
        if not self.file_path:
            return
        with open(self.file_path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            for row in range(self.tableWidget.rowCount()):
                row_data = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    row_data.append(item.text() if item else '')
                writer.writerow(row_data)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())