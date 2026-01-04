        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()