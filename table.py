import sys
import csv
from PyQt5 import QtWidgets
from table_window import Ui_Dialog

class TableWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None, file_path=""):
        super(TableWindow, self).__init__(parent)
        self.setupUi(self)
        self.file_path = file_path
        self.load_data()
        self.addButton.clicked.connect(self.add_row)
        self.saveButton.clicked.connect(self.save_data)
        self.refreshButton.clicked.connect(self.load_data)
        self.deleteRowButton.clicked.connect(self.delete_row)
        
        # adjust table size with window
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        
        # connect signals for row selection
        self.tableWidget.itemSelectionChanged.connect(self.update_delete_button_state)
        self.update_delete_button_state()

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
        with open(self.file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for row in range(self.tableWidget.rowCount()):
                row_data = []
                empty_row = True
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    text = item.text() if item else ''
                    if text.strip():  # check if the cell is not empty
                        empty_row = False
                    row_data.append(text)
                if not empty_row:  # write row only if it's not empty
                    writer.writerow(row_data)

    def add_row(self):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        for column in range(self.tableWidget.columnCount()):
            self.tableWidget.setItem(row_position, column, QtWidgets.QTableWidgetItem(""))

    def delete_row(self):
        indices = self.tableWidget.selectionModel().selectedRows()
        for index in sorted(indices):
            self.tableWidget.removeRow(index.row())
        self.update_delete_button_state()

    def update_delete_button_state(self):
        self.deleteRowButton.setEnabled(bool(self.tableWidget.selectionModel().selectedRows()))
