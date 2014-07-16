#!/usr/bin/python

# TrayIcon

# Access to various monitoring capabilities (HIDS, dashboard, ip configuration, network recognition, etc.)
# Alerting plugin (IM notifications, irssi, OSSEC) that can help to display and monitor notification informations)
# Deamon plugin (sort of tail -f over selected files, RSS gathering, correlation)
# Knowledge base: regex, xpath and pattern recognition for classification
# Correlation and (help to the alerting plugin) some rules to notify additional messages (security, twitter)
# Social feeds integration (at least for Twitter) and we can imagine some sort of lexicometric tricks over it with correlation and alerting


# import sys
# from PyQt4 import QtGui
#
# class SystemTrayIcon(QtGui.QSystemTrayIcon):
#     def __init__(self, icon, parent=None):
#         QtGui.QSystemTrayIcon.__init__(self, icon, parent)
#         self.menu = QtGui.QMenu(parent)
#         exitAction = self.menu.addAction("Exit")
#         self.setContextMenu(self.menu)
#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     style = app.style()
#     icon = QtGui.QIcon(style.standardPixmap(QtGui.QStyle.SP_FileIcon))
#     trayIcon = SystemTrayIcon(icon)
#
#     trayIcon.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

# TO BE CONTINUED... ?
