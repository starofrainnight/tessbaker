'''

@date: 2015-5-17
@author: Hong-She Liang <starofrainnight@gmail.com>

'''

from .Ui_QTBMainWindow import Ui_QTBMainWindow
from PySide import QtCore
from PySide import QtGui

class QTBMainWindow(QtGui.QMainWindow):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(QTBMainWindow, self).__init__(parent)
        self.ui = Ui_QTBMainWindow()
        self.ui.setupUi(self)