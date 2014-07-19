# -*- coding: utf-8 -*-
from ..Node import Node
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
from .common import *
from pyqtgraph.SRTTransform import SRTTransform
from pyqtgraph.Point import Point
from pyqtgraph.widgets.TreeWidget import TreeWidget
from pyqtgraph.graphicsItems.LinearRegionItem import LinearRegionItem

from . import functions


class EvalNode(Node):
    """Return the output of a string evaluated/executed by the python interpreter.
    The string may be either an expression or a python script, and inputs are accessed as the name of the terminal. 
    For expressions, a single value may be evaluated for a single output, or a dict for multiple outputs.
    For a script, the text will be executed as the body of a function."""
    nodeName = 'PythonEval'
    
    def __init__(self, name):
        Node.__init__(self, name, 
            terminals = {
                'input': {'io': 'in', 'renamable': True},
                'output': {'io': 'out', 'renamable': True},
            },
            allowAddInput=True, allowAddOutput=True)
        
        self.ui = QtGui.QWidget()
        self.layout = QtGui.QGridLayout()
        #self.addInBtn = QtGui.QPushButton('+Input')
        #self.addOutBtn = QtGui.QPushButton('+Output')
        self.text = QtGui.QTextEdit()
        self.text.setTabStopWidth(30)
        self.text.setPlainText("# Access inputs as args['input_name']\nreturn {'output': None} ## one key per output terminal")
        #self.layout.addWidget(self.addInBtn, 0, 0)
        #self.layout.addWidget(self.addOutBtn, 0, 1)
        self.layout.addWidget(self.text, 1, 0, 1, 2)
        self.ui.setLayout(self.layout)
        
        #QtCore.QObject.connect(self.addInBtn, QtCore.SIGNAL('clicked()'), self.addInput)
        #self.addInBtn.clicked.connect(self.addInput)
        #QtCore.QObject.connect(self.addOutBtn, QtCore.SIGNAL('clicked()'), self.addOutput)
        #self.addOutBtn.clicked.connect(self.addOutput)
        self.text.focusOutEvent = self.focusOutEvent
        self.lastText = None
        
    def ctrlWidget(self):
        return self.ui
        
    #def addInput(self):
        #Node.addInput(self, 'input', renamable=True)
        
    #def addOutput(self):
        #Node.addOutput(self, 'output', renamable=True)
        
    def focusOutEvent(self, ev):
        text = str(self.text.toPlainText())
        if text != self.lastText:
            self.lastText = text
            self.update()
        return QtGui.QTextEdit.focusOutEvent(self.text, ev)
        
    def process(self, display=True, **args):
        l = locals()
        l.update(args)
        ## try eval first, then exec
        try:  
            text = str(self.text.toPlainText()).replace('\n', ' ')
            output = eval(text, globals(), l)
        except SyntaxError:
            fn = "def fn(**args):\n"
            run = "\noutput=fn(**args)\n"
            text = fn + "\n".join(["    "+l for l in str(self.text.toPlainText()).split('\n')]) + run
            exec(text)
        except:
            print("Error processing node: %s" % self.name())
            raise
        return output
        
    def saveState(self):
        state = Node.saveState(self)
        state['text'] = str(self.text.toPlainText())
        #state['terminals'] = self.saveTerminals()
        return state
        
    def restoreState(self, state):
        Node.restoreState(self, state)
        self.text.clear()
        self.text.insertPlainText(state['text'])
        self.restoreTerminals(state['terminals'])
        self.update()

