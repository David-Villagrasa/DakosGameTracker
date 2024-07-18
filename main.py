import sys
import json
import os
import re 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox
from main_window import Ui_MainWindow
from table import TableWindow

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
        self.actionNew_Year.triggered.connect(self.add_new_year)  # connect the New Year action

        self.check_folder_selected()

    def check_folder_selected(self):
        if not self.selected_folder:
            QtWidgets.QMessageBox.warning(self, "No Folder Selected", "Please go to Options > Select Folder to configure the application by selecting a folder.")

    def open_dialog(self):
        if not self.selected_folder:
            QtWidgets.QMessageBox.warning(self, "No Folder Selected", "Please select a folder first.")
            return

        selected_year = self.cbYears.currentText()
        if selected_year in self.files:
            file_path = self.files[selected_year]
            dialog = TableWindow(self, file_path)
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
        # get all .txt files that match the pattern "YYYYpg.txt"
        files = [f for f in os.listdir(self.selected_folder) if f.endswith('.txt') and re.match(r'\d{4}pg\.txt$', f)]
        self.lbl_numberOf.setText(str(len(files)))  # update the label with the number of files
        self.cbYears.clear()  # clear existing items in the combo box
        self.files = {f[:4]: os.path.join(self.selected_folder, f) for f in files}  # map years to file paths
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
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
        else:
            config = {}

        config['selected_folder'] = self.selected_folder

        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)

    def add_new_year(self):
        if not self.selected_folder:
            QtWidgets.QMessageBox.warning(self, "No Folder Selected", "Please select a folder first.")
            return

        year, ok = QInputDialog.getText(self, "New Year", "Enter the year:")
        if ok and year:
            if re.match(r'^\d{4}$', year) and year not in self.files:
                new_file_path = os.path.join(self.selected_folder, f"{year}pg.txt")
                with open(new_file_path, 'w') as f:
                    f.write("")  # create an empty file
                self.update_file_info()  # update the file list
                QMessageBox.information(self, "Success", f"File {year}pg.txt created successfully.")
            else:
                QMessageBox.warning(self, "Error", "The year is invalid or already exists.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
