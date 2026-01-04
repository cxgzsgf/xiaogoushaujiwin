if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)

    if hasattr(sys, '_MEIPASS'):
        splash_image_path = os.path.join(sys._MEIPASS, 'background.png')
    else:
        splash_image_path = 'background.png'

    splash_pixmap = QtGui.QPixmap(splash_image_path)
    splash = SplashScreen(splash_pixmap)
    splash.show()