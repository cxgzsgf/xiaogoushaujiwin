        QtWidgets.QMessageBox.information(self, title, message)
        if url:
            webbrowser.open(url)
        QtCore.QTimer.singleShot(0, self.close_application)
