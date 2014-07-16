# -*- coding: utf-8 -*-

import os
import inspect
import intelwiz

INTELWIZ_PATH = os.path.dirname(inspect.getfile(intelwiz))
CONFIG_PATH = os.path.join(INTELWIZ_PATH, 'config')
