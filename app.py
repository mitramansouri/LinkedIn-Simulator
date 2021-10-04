from PyQt5 import QtCore, QtGui, QtWidgets
from main import linkedin
import datetime

# The interface file

my_username = 5

class PageWindow(QtWidgets.QMainWindow): # Do not touch this
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)


class ViewProfile(PageWindow):

    def __init__(self):
        super().__init__()
        self.user_id = linkedin_database.contact_userid
        self.username = ""
        self.password = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        self.birth_day = ""
        self.email = ""
        self.about = ""
        self.gender = ""
        self.country = ""
        self.city = ""
        self.skill_list = []
        self.accomplishment_list = []
        self.featured_list = []
        self.initUI()

    def initUI(self):
        self.UiComponents()
        self.setWindowTitle("edit")

    def get_info(self):
        username = linkedin_database.get_username(linkedin_database.contact_userid)
        info = linkedin_database.get_user_information(username)
        if info != None:
            self.user_id = info[0][0]
            self.username = info[0][1]
            if info[0][3] != None:
                self.first_name = info[0][3]
            if info[0][4] != None:
                self.last_name = info[0][4]
            if info[0][5] != None:
                self.about = info[0][5]
            if info[0][6] != None:
                self.gender = info[0][6]
            if info[0][7] != None:
                self.birth_day = info[0][7]
            if info[0][8] != None:
                self.country = info[0][8]
            if info[0][9] != None:
                self.city = info[0][9]
            if info[0][10] != None:
                self.email = info[0][10]

            self.skill_list = linkedin_database.get_skills(int(self.user_id))
            self.accomplishment_list = linkedin_database.get_accomplishments(int(self.user_id))
            self.featured_list = linkedin_database.get_featureds(int(self.user_id))

    def clearlayout(self, layout):
         if layout is not None:
             while layout.count():
                 item = layout.takeAt(0)
                 widget = item.widget()
                 if widget is not None:
                     widget.deleteLater()
                 else:
                     clearlayout(item.layout())

    def endorse_skill(self, skill_id):
        linkedin_database.add_new_endorse(skill_id, self.user_id, 0)
        self.skill_printer()

    def unendorse_skill(self, skill_id):
        linkedin_database.remove_endorse(skill_id, self.user_id)
        self.skill_printer()

    def skill_printer(self):
        self.clearlayout(self.gridLayout_skill)
        if self.user_id != '':
            self.skill_list = linkedin_database.get_skills(int(self.user_id))
        for i in range(len(self.skill_list)):
            self.textBrowser_skill = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2skill)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.textBrowser_skill.sizePolicy().hasHeightForWidth())
            self.textBrowser_skill.setSizePolicy(sizePolicy)
            self.textBrowser_skill.setObjectName("textBrowser")
            self.textBrowser_skill.setSizePolicy(sizePolicy)
            self.textBrowser_skill.setText(str(self.skill_list[i][2]))
            self.textBrowser_skill.setMaximumSize(QtCore.QSize(200, 60))
            skillid = int(self.skill_list[i][0])
            if linkedin_database.is_endorsed(skillid, self.user_id) == 0:
                self.pushButton_sdel = QtWidgets.QPushButton("Endorse",self.textBrowser_skill)
                self.pushButton_sdel.clicked.connect(lambda ch, skillid=skillid : self.endorse_skill(skillid))
            else:
                self.pushButton_sdel = QtWidgets.QPushButton("Un-endorse",self.textBrowser_skill)
                self.pushButton_sdel.clicked.connect(lambda ch, skillid=skillid : self.unendorse_skill(skillid))

            self.pushButton_sdel.setGeometry(QtCore.QRect(120, 10, 80, 30))
            self.pushButton_sdel.setObjectName("pushButton_4")


            self.gridLayout_skill.addWidget(self.textBrowser_skill, i, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.scrollArea_skills.setWidget(self.scrollAreaWidgetContents_2skill)
        self.verticalLayout_skills.addWidget(self.scrollArea_skills)

    def accom_printer(self):
        self.clearlayout(self.gridLayout_accom)
        if self.user_id != '':
            self.accomplishment_list = linkedin_database.get_accomplishments(int(self.user_id))
        for i in range(len(self.accomplishment_list)):
            self.textBrowser_accom = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2accom)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.textBrowser_accom.sizePolicy().hasHeightForWidth())
            self.textBrowser_accom.setSizePolicy(sizePolicy)
            self.textBrowser_accom.setObjectName("textBrowser")
            self.textBrowser_accom.setSizePolicy(sizePolicy)
            self.textBrowser_accom.setText(str(self.accomplishment_list[i][2]))
            self.textBrowser_accom.setMaximumSize(QtCore.QSize(200, 60))

            self.gridLayout_accom.addWidget(self.textBrowser_accom, i, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.scrollArea_accom.setWidget(self.scrollAreaWidgetContents_2accom)
        self.verticalLayout_accom.addWidget(self.scrollArea_accom)

    def features_printer(self):
        self.clearlayout(self.gridLayout_feat)
        if self.user_id != '':
            self.featured_list = linkedin_database.get_featureds(int(self.user_id))
        for i in range(len(self.featured_list)):
            self.textBrowser_feat = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2feat)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.textBrowser_feat.sizePolicy().hasHeightForWidth())
            self.textBrowser_feat.setSizePolicy(sizePolicy)
            self.textBrowser_feat.setObjectName("textBrowser")
            self.textBrowser_feat.setSizePolicy(sizePolicy)
            self.textBrowser_feat.setText(str(self.featured_list[i][2]))
            self.textBrowser_feat.setMaximumSize(QtCore.QSize(200, 60))

            self.gridLayout_feat.addWidget(self.textBrowser_feat, i, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.scrollArea_feat.setWidget(self.scrollAreaWidgetContents_2feat)
        self.verticalLayout_feat.addWidget(self.scrollArea_feat)

    def goback(self):
        self.goto("main")


    def UiComponents(self):
        self.Skills_label = QtWidgets.QLabel("Skills", self)
        self.Skills_label.setGeometry(QtCore.QRect(210, 360, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Skills_label.setFont(font)
        self.Skills_label.setObjectName("Skills_label")
        self.accomplishments_label = QtWidgets.QLabel("Accomplishments", self)
        self.accomplishments_label.setGeometry(QtCore.QRect(610, 360, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.accomplishments_label.setFont(font)
        self.accomplishments_label.setObjectName("accomplishments_label")
        self.features_label = QtWidgets.QLabel("Featured", self)
        self.features_label.setGeometry(QtCore.QRect(1010, 360, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.features_label.setFont(font)
        self.features_label.setObjectName("features_label")
        self.profile_frame = QtWidgets.QFrame(self)
        self.profile_frame.setGeometry(QtCore.QRect(200, 100, 600, 200))
        self.profile_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.profile_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.profile_frame.setLineWidth(1)
        self.profile_frame.setObjectName("profile_frame")
        self.name_label = QtWidgets.QLabel(self.profile_frame)
        self.name_label.setText(str(self.first_name) + " " + str(self.last_name))
        self.name_label.setGeometry(QtCore.QRect(30, 20, 500, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")

        self.username_label = QtWidgets.QLabel("@ " + str(self.username) , self.profile_frame)
        self.username_label.setGeometry(QtCore.QRect(30, 60, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.contactinfo_label = QtWidgets.QLabel("Contact info. : " + str(self.email) , self.profile_frame)
        self.contactinfo_label.setGeometry(QtCore.QRect(300, 60, 250, 21))
        self.contactinfo_label.setObjectName("contactinfo_label")
        self.address_label = QtWidgets.QLabel("Address : " + str(self.country) + ", " + str(self.city), self.profile_frame)
        self.address_label.setGeometry(QtCore.QRect(300, 30, 200, 16))
        self.address_label.setObjectName("address_label")
        self.about_frame = QtWidgets.QFrame(self)
        self.about_frame.setGeometry(QtCore.QRect(900, 100, 350, 200))
        self.about_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.about_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.about_frame.setLineWidth(1)
        self.about_frame.setObjectName("about_frame")
        self.about_label = QtWidgets.QLabel("About", self.about_frame)
        self.about_label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.about_label.setObjectName("about_label")
        self.about_context = QtWidgets.QLabel(str(self.about), self.about_frame)
        self.about_context.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.about_context.setObjectName("about_label")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.about_label.setFont(font)

        self.widget_skill = QtWidgets.QWidget(self)
        self.widget_skill.setGeometry(QtCore.QRect(200, 400, 250, 250))
        self.widget_skill.setObjectName("widget")
        self.verticalLayout_skills = QtWidgets.QVBoxLayout(self.widget_skill)
        self.verticalLayout_skills.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_skills.setObjectName("verticalLayout")
        self.scrollArea_skills = QtWidgets.QScrollArea(self.widget_skill)
        self.scrollArea_skills.setWidgetResizable(True)
        self.scrollArea_skills.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2skill = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2skill.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.scrollAreaWidgetContents_2skill.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_skill = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2skill)
        self.gridLayout_skill.setObjectName("gridLayout")
        self.skill_printer()

        self.widget_accom = QtWidgets.QWidget(self)
        self.widget_accom.setGeometry(QtCore.QRect(600, 400, 250, 250))
        self.widget_accom.setObjectName("widget")
        self.verticalLayout_accom = QtWidgets.QVBoxLayout(self.widget_accom)
        self.verticalLayout_accom.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_accom.setObjectName("verticalLayout")
        self.scrollArea_accom = QtWidgets.QScrollArea(self.widget_accom)
        self.scrollArea_accom.setWidgetResizable(True)
        self.scrollArea_accom.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2accom = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2accom.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.scrollAreaWidgetContents_2accom.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_accom = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2accom)
        self.gridLayout_accom.setObjectName("gridLayout")
        self.accom_printer()

        self.widget_feat = QtWidgets.QWidget(self)
        self.widget_feat.setGeometry(QtCore.QRect(1000, 400, 250, 250))
        self.widget_feat.setObjectName("widget")
        self.verticalLayout_feat = QtWidgets.QVBoxLayout(self.widget_feat)
        self.verticalLayout_feat.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_feat.setObjectName("verticalLayout")
        self.scrollArea_feat = QtWidgets.QScrollArea(self.widget_feat)
        self.scrollArea_feat.setWidgetResizable(True)
        self.scrollArea_feat.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2feat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2feat.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.scrollAreaWidgetContents_2feat.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_feat = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2feat)
        self.gridLayout_feat.setObjectName("gridLayout")

        self.backButton = QtWidgets.QPushButton("back", self)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 100, 30))
        self.backButton.clicked.connect(self.goback)
        self.features_printer()



class EditPage(PageWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.UiComponents()
        self.setWindowTitle("edit")

    def UiComponents(self):
        info = linkedin_database.get_user_information(linkedin_database.username)
        self.firstname_label_e = QtWidgets.QLabel("First Name ", self)
        self.firstname_label_e.setGeometry(QtCore.QRect(80, 110, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstname_label_e.setFont(font)
        self.firstname_label_e.setObjectName("firstname_label")
        self.lineEdit_firstname_e = QtWidgets.QLineEdit(self)
        self.lineEdit_firstname_e.setGeometry(QtCore.QRect(80, 140, 201, 26))
        if info != None:
            self.lineEdit_firstname_e.setText(info[0][3])
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_firstname_e.setFont(font)
        self.lineEdit_firstname_e.setObjectName("lineEdit_firstname")
        self.lineEdit_lasrname_e = QtWidgets.QLineEdit(self)
        self.lineEdit_lasrname_e.setGeometry(QtCore.QRect(80, 230, 201, 26))
        if info != None:
            self.lineEdit_lasrname_e.setText(info[0][4])
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_lasrname_e.setFont(font)
        self.lineEdit_lasrname_e.setObjectName("lineEdit_lasrname")
        self.lastname_label_e = QtWidgets.QLabel("Last Name", self)
        self.lastname_label_e.setGeometry(QtCore.QRect(80, 200, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lastname_label_e.setFont(font)
        self.lastname_label_e.setObjectName("lastname_label")
        self.lineEdit_username_e = QtWidgets.QLineEdit(self)
        self.lineEdit_username_e.setGeometry(QtCore.QRect(470, 140, 201, 26))
        if info != None:
            self.lineEdit_username_e.setText(info[0][1])
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_username_e.setFont(font)
        self.lineEdit_username_e.setObjectName("lineEdit_username")
        self.username_label_e = QtWidgets.QLabel("Username", self)
        self.username_label_e.setGeometry(QtCore.QRect(470, 110, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_label_e.setFont(font)
        self.username_label_e.setObjectName("username_label")
        self.lineEdit_password_e = QtWidgets.QLineEdit(self)
        self.lineEdit_password_e.setGeometry(QtCore.QRect(470, 230, 201, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_password_e.setFont(font)
        self.lineEdit_password_e.setObjectName("lineEdit_password")
        self.password_label_e = QtWidgets.QLabel("Password", self)
        self.password_label_e.setGeometry(QtCore.QRect(470, 200, 201, 16))
        if info != None:
            self.lineEdit_password_e.setText(info[0][2])
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_label_e.setFont(font)
        self.password_label_e.setObjectName("password_label")
        self.country_label_e = QtWidgets.QLabel("Country", self)
        self.country_label_e.setGeometry(QtCore.QRect(80, 290, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.country_label_e.setFont(font)
        self.country_label_e.setObjectName("country_label")
        self.country_lineEdit_e = QtWidgets.QLineEdit(self)
        self.country_lineEdit_e.setGeometry(QtCore.QRect(80, 320, 201, 26))
        if info != None:
            self.country_lineEdit_e.setText(info[0][8])
        font = QtGui.QFont()
        font.setPointSize(10)
        self.country_lineEdit_e.setFont(font)
        self.country_lineEdit_e.setObjectName("country_lineEdit")
        self.city_label_e = QtWidgets.QLabel("City", self)
        self.city_label_e.setGeometry(QtCore.QRect(340, 290, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.city_label_e.setFont(font)
        self.city_label_e.setObjectName("city_label")
        self.city_lineEdit_e = QtWidgets.QLineEdit(self)
        self.city_lineEdit_e.setGeometry(QtCore.QRect(330, 320, 201, 26))
        if info != None:
            self.city_lineEdit_e.setText(info[0][9])
        font = QtGui.QFont()
        font.setPointSize(10)
        self.city_lineEdit_e.setFont(font)
        self.city_lineEdit_e.setObjectName("city_lineEdit")
        self.contact_info_label_e = QtWidgets.QLabel("Contact Info.", self)
        self.contact_info_label_e.setGeometry(QtCore.QRect(570, 290, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contact_info_label_e.setFont(font)
        self.contact_info_label_e.setObjectName("contact_info_label")
        self.contact_info_lineEdit_e = QtWidgets.QLineEdit(self)
        self.contact_info_lineEdit_e.setGeometry(QtCore.QRect(580, 320, 201, 26))
        if info != None:
            self.contact_info_lineEdit_e.setText(info[0][10])
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contact_info_lineEdit_e.setFont(font)
        self.contact_info_lineEdit_e.setObjectName("contact_info_lineEdit")
        self.about_label_e = QtWidgets.QLabel("About", self)
        self.about_label_e.setGeometry(QtCore.QRect(80, 500, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.about_label_e.setFont(font)
        self.about_label_e.setObjectName("about_label")
        self.save_btn_e = QtWidgets.QPushButton("Save Changes", self)
        self.save_btn_e.setGeometry(QtCore.QRect(390, 800, 120, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_btn_e.setFont(font)
        self.save_btn_e.setObjectName("save_btn")
        self.save_btn_e.clicked.connect(self.save_changes)
        self.about_textEdti_e = QtWidgets.QTextEdit(self)
        self.about_textEdti_e.setGeometry(QtCore.QRect(80, 550, 705, 195))
        self.about_textEdti_e.setObjectName("about_textEdti")
        if info != None:
            self.about_textEdti_e.setText(info[0][5])

        self.b_info_label_e = QtWidgets.QLabel("Birth Date", self)
        self.b_info_label_e.setGeometry(QtCore.QRect(80, 390, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_info_label_e.setFont(font)
        self.b_info_label_e.setObjectName("contact_info_label")

        self.bday_textEdti_e = QtWidgets.QLineEdit(self)
        self.bday_textEdti_e.setGeometry(QtCore.QRect(80, 420, 201, 26))
        self.bday_textEdti_e.setObjectName("about_textEdti")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bday_textEdti_e.setFont(font)
        if info != None:
            self.bday_textEdti_e.setText(info[0][7])

        self.frame_e = QtWidgets.QFrame(self)
        self.frame_e.setGeometry(QtCore.QRect(310, 640, 120, 80))
        self.frame_e.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_e.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_e.setObjectName("frame")

    def save_changes(self):
        username = self.lineEdit_username_e.text()
        password = self.lineEdit_password_e.text()
        fname = self.lineEdit_firstname_e.text()
        lname = self.lineEdit_lasrname_e.text()
        about = self.about_textEdti_e.toPlainText()
        country = self.country_lineEdit_e.text()
        city = self.city_lineEdit_e.text()
        email = self.contact_info_lineEdit_e.text()
        bday = self.bday_textEdti_e.text()

        linkedin_database.edit_profile(username, password, fname, lname, about, country, city, email, bday)
        self.goto("main")



class LoginPage(PageWindow):  # all the ui functions and widgets of login page sit in this class

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Login")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(9)
        self.setFont(font)
        self.setStyleSheet("color: rgb(80, 80, 80);")
        self.commandLinkButton = QtWidgets.QCommandLinkButton("Don\'t have an account? Signup", self)
        self.commandLinkButton.setGeometry(QtCore.QRect(780, 670, 291, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("color: rgb(73, 73, 109);")
        icon = QtGui.QIcon.fromTheme("none")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.login_button = QtWidgets.QPushButton("Login", self)
        self.login_button.setGeometry(QtCore.QRect(860, 580, 131, 41))
        self.login_button.setObjectName("login_button")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_username = QtWidgets.QLabel("Username", self)
        self.label_username.setGeometry(QtCore.QRect(810, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_username.setObjectName("label")
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setGeometry(QtCore.QRect(800, 330, 251, 51))
        self.username_input.setObjectName("username_input")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_input.setFont(font)
        self.label_password = QtWidgets.QLabel("Password", self)
        self.label_password.setGeometry(QtCore.QRect(810, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_password.setObjectName("label_3")
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setGeometry(QtCore.QRect(800, 460, 251, 51))
        self.password_input.setObjectName("password_input")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_input.setFont(font)

        self.label_2 = QtWidgets.QLabel("Login to your account", self)
        self.label_2.setGeometry(QtCore.QRect(790, 80, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(117, 117, 176);")
        self.label_2.setObjectName("label_2")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(700, 170, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.line.setFont(font)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")


        self.commandLinkButton.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.login)

    def signup(self):
        self.goto("signup")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if linkedin_database.login(username, password):
            linkedin_database.username = username
            self.goto("main")
        else:
            pass
            # should show a message that says username or password incorrect
            #print("Wrong username or password")

class SignupPage(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Signup")
        self.UiComponents()

    def UiComponents(self):
        self.signup_button = QtWidgets.QPushButton("Signup", self)
        self.signup_button.setGeometry(QtCore.QRect(860, 580, 131, 41))
        self.signup_button.setObjectName("login_button")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_username = QtWidgets.QLabel("Username", self)
        self.label_username.setGeometry(QtCore.QRect(810, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_username.setObjectName("label")
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setGeometry(QtCore.QRect(800, 330, 251, 51))
        self.username_input.setObjectName("username_input")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_input.setFont(font)
        self.label_password = QtWidgets.QLabel("Password", self)
        self.label_password.setGeometry(QtCore.QRect(810, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_password.setObjectName("label_3")
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setGeometry(QtCore.QRect(800, 460, 251, 51))
        self.password_input.setObjectName("password_input")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_input.setFont(font)

        self.label_2 = QtWidgets.QLabel("Create an account", self)
        self.label_2.setGeometry(QtCore.QRect(810, 80, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(117, 117, 176);")
        self.label_2.setObjectName("label_2")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(700, 170, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.line.setFont(font)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.signup_button.clicked.connect(self.signup)

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if linkedin_database.signup(username, password):
            self.goto("login")
        else:
            # should show a message that says this username is already taken
            pass


class MainPage(PageWindow):
    def __init__(self):
        super().__init__()
        self.user_id = ""
        self.username = ""
        self.password = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        self.birth_day = ""
        self.email = ""
        self.about = ""
        self.gender = ""
        self.country = ""
        self.city = ""

        self.my_network_list = []
        self.my_invitation_list = []
        self.my_post_list = [] # posts which of that I am the author
        self.my_home_posts = []
        self.notif_list = []

        self.skill_list = []
        self.accomplishment_list = []
        self.featured_list = []

        self.search1 = []
        self.search2 = []
        self.search_total = []

        self.contacts = []
        self.conv = []
        self.result_of_search_mssg = []
        self.result_of_search_users = []
        self.ppl_i_may_know = []
        self.archived = []
        self.selected_contact = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Home")
        self.UiComponents()

    def get_info(self):
        info = linkedin_database.get_user_information(linkedin_database.username)
        if info != None:
            self.user_id = info[0][0]
            self.username = info[0][1]
            if info[0][3] != None:
                self.first_name = info[0][3]
            if info[0][4] != None:
                self.last_name = info[0][4]
            if info[0][5] != None:
                self.about = info[0][5]
            if info[0][6] != None:
                self.gender = info[0][6]
            if info[0][7] != None:
                self.birth_day = info[0][7]
            if info[0][8] != None:
                self.country = info[0][8]
            if info[0][9] != None:
                self.city = info[0][9]
            if info[0][10] != None:
                self.email = info[0][10]

            self.my_network_list = linkedin_database.get_network(int(self.user_id))
            self.my_invitation_list = linkedin_database.get_my_invitations(int(self.user_id))
            self.my_post_list = linkedin_database.get_my_posts(int(self.user_id))
            self.my_home_posts = linkedin_database.get_home_posts(int(self.user_id))
            self.ppl_i_may_know = linkedin_database.get_people_you_may_know(int(self.user_id))
            self.notif_list = linkedin_database.get_notifications(int(self.user_id))
            self.skill_list = linkedin_database.get_skills(int(self.user_id))
            self.accomplishment_list = linkedin_database.get_accomplishments(int(self.user_id))
            self.featured_list = linkedin_database.get_featureds(int(self.user_id))
            todays_date = datetime.datetime.now()
            if (str(todays_date.strftime("%m")) == str(self.birth_day[5:7]) and str(todays_date.strftime("%d")) == str(self.birth_day[8:10])):
                for item in self.my_network_list:
                    if item[1] == self.user_id:
                        linkedin_database.add_notification(self.user_id, item[2], '1')
                    elif item[2] == self.user_id:
                        linkedin_database.add_notification(self.user_id, item[1], '1')

            network_temp = []
            for item in self.my_network_list:
                network_temp += [item[1]]
                network_temp += [item[2]]

            temp = []
            for i in range(len(self.ppl_i_may_know)):
                if self.ppl_i_may_know[i][1] not in network_temp:
                    temp += [self.ppl_i_may_know[i]]

            self.ppl_i_may_know = temp

            print("ppl:")
            print(self.ppl_i_may_know)
            print("my net:")
            print(self.my_network_list)
            # print(todays_date.strftime("%m"))
            # print(todays_date.strftime("%d"))
            # print(self.birth_day[0:4]) # year
            # print(self.birth_day[5:7]) # month
            # print(self.birth_day[8:10]) # day


    def clearlayout(self, layout):
         if layout is not None:
             while layout.count():
                 item = layout.takeAt(0)
                 widget = item.widget()
                 if widget is not None:
                     widget.deleteLater()
                 else:
                     clearlayout(item.layout())

    def get_a_conv(self, contact_name):
        n = len(self.contacts)
        contact_id = ""
        for j in range(n):
            if self.verticalLayout_2m.itemAt(j).widget().text() == contact_name :
                contact_id = int(self.verticalLayout_2m.itemAt(j).widget().objectName())

        #print("here")
        info = linkedin_database.get_a_conversation(self.user_id, contact_id)
        self.selected_contact = contact_id
        self.conv = info
        self.print_chat(self.conv)

    def delete_a_message(self, id):
        linkedin_database.physical_delete_a_message(int(id))
        self.conv = linkedin_database.get_a_conversation(self.user_id, self.selected_contact)
        self.print_chat(self.conv)

    def archive_mssg(self, mssg_id):
        linkedin_database.archive_a_message(int(mssg_id))
        self.conv = linkedin_database.get_a_conversation(self.user_id, self.selected_contact)
        self.print_chat(self.conv)

    def unarchive_mssg(self, mssg_id):
        print(mssg_id)
        linkedin_database.unarchive_a_message(int(mssg_id))
        self.conv = linkedin_database.get_a_conversation(self.user_id, self.selected_contact)
        self.print_chat(self.conv)

    def print_chat(self, chat_list):
        self.clearlayout(self.verticalLayout_2ch)
        num_of_chats = len(chat_list)
        for chat_index in range(num_of_chats):
            self.textBrowser_ch = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_ch)
            self.textBrowser_ch.setObjectName("textBrowser_2")
            self.del_chat_button = QtWidgets.QPushButton("Delete", self.textBrowser_ch)
            self.del_chat_button.setGeometry(QtCore.QRect(200, 0, 60, 30))
            self.del_chat_button.setObjectName(str(chat_list[chat_index][2]))
            ch_b_txt = self.del_chat_button.objectName()
            self.del_chat_button.clicked.connect(lambda ch, ch_b_txt=ch_b_txt : self.delete_a_message(ch_b_txt))

            self.arch_chat_button = QtWidgets.QPushButton(self.textBrowser_ch)
            self.arch_chat_button.setGeometry(QtCore.QRect(260, 0, 80, 30))
            self.arch_chat_button.setObjectName(str(chat_list[chat_index][2]))

            if len(chat_list[chat_index]) >= 8:
                full_text = str(linkedin_database.get_username(chat_list[chat_index][0]))
                full_text += " : \n   "
                full_text += str(chat_list[chat_index][8])
                if chat_list[chat_index][3] == '1':
                    self.arch_chat_button.setText("Un-Archive")
                    self.arch_chat_button.clicked.connect(lambda ch, ch_b_txt=ch_b_txt : self.unarchive_mssg(ch_b_txt))
                    full_text += "\n\nArchived"
                else:
                    self.arch_chat_button.setText("Archive")
                    self.arch_chat_button.clicked.connect(lambda ch, ch_b_txt=ch_b_txt : self.archive_mssg(ch_b_txt))
                    full_text += "\n\nUn-archived"
                if chat_list[chat_index][4] == '1':
                    full_text += " & Unread"
                else:
                    full_text += " & Read"
                self.textBrowser_ch.setText(full_text)
            self.verticalLayout_2ch.addWidget(self.textBrowser_ch)
            #self.verticalLayout_2ch.addWidget(self.del_chat_button)

        self.scrollArea_ch.setWidget(self.scrollAreaWidgetContents_ch)

    def send_mssg(self):
        mssg_text = self.textEdit.toPlainText()
        self.textEdit.clear()
        m = linkedin_database.add_new_message(mssg_text)
        linkedin_database.add_new_conversation(int(self.user_id), int(self.selected_contact), m)

        self.conv = linkedin_database.get_a_conversation(self.user_id, self.selected_contact)
        self.print_chat(self.conv)

    def search_mssg(self):
        if self.selected_contact != "":
            self.result_of_search_mssg = linkedin_database.search_in_messages(int(self.user_id), int(self.selected_contact), self.chat_search.text())
            self.print_chat(self.result_of_search_mssg)

    def message_to(self, userid):
        self.tabWidget.setCurrentIndex(2)
        username = linkedin_database.get_username(int(userid))
        if (str(username), int(userid)) not in self.contacts:
            self.contacts += [(str(username), int(userid))]

            self.textBrowser_m = QtWidgets.QPushButton(str(username), self.scrollAreaWidgetContents_m)
            self.textBrowser_m.setObjectName(str(userid))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.textBrowser_m.setFont(font)
            text = self.textBrowser_m.text()
            self.textBrowser_m.clicked.connect(lambda ch, text=text : self.get_a_conv(text))
            self.verticalLayout_2m.addWidget(self.textBrowser_m)

        self.get_a_conv(username)

    def go_to_their_profile(self, user_id):
        linkedin_database.contact_userid = int(user_id)
        linkedin_database.add_notification(int(self.user_id), int(user_id), '2')
        self.goto("view")

    def search_connection_num(self):
        self.search1 = linkedin_database.search_by_connection(int(self.user_id))
        self.search_total = linkedin_database.search_by_connection(int(self.user_id))
        for i in range(len(self.search1)):
            self.search1[i] = self.search1[i][0]
        # print("search1 : ")
        # print(self.search1)
        self.search2 = linkedin_database.get_all_users()
        for i in range(len(self.search2)):
            self.search2[i] = self.search2[i][0]
        # print("search2 : ")
        # print(self.search2)
        for item in self.search2:
            if item not in self.search1:
                self.search_total += [(item, 0)]
        # print("search total :")
        # print(self.search_total)

    def search_for_users(self):
        filter_choice = self.comboBox_net.currentText()
        if filter_choice == "Connection":
            self.search_connection_num()
            self.result_of_search_users = self.search_total
            self.search_for_users2()
        elif filter_choice == "Username":
            username_search = self.lineEdit_search_net.text()
            self.result_of_search_users = linkedin_database.search_in_users(username_search)
            self.search_for_users2()
        elif filter_choice == "Location":
            address_search = self.lineEdit_search_net.text()
            self.result_of_search_users = linkedin_database.search_in_users_location(address_search)
            self.search_for_users2()
        elif filter_choice == "Current Company":
            pass

    def search_for_users2(self):
        #self.result_of_search_users = linkedin_database.search_in_users(self.lineEdit_search_net.text())
        self.clearlayout(self.verticalLayout_2net_search)
        num_of_users_found = len(self.result_of_search_users)
        print(self.result_of_search_users)
        for user_search_index in range(num_of_users_found):
            self.textBrowser_net_search = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_net_search)
            self.textBrowser_net_search.setObjectName("textBrowser_search")
            userid = self.result_of_search_users[user_search_index][0]
            no_of_connection = self.result_of_search_users[user_search_index][1]
            text = str(linkedin_database.get_username(userid))
            filter_choice = self.comboBox_net.currentText()

            if filter_choice == "Connection":
                text += "\n" + str(no_of_connection) + " Mutual connection(s)"

            if filter_choice == "Location":
                if (self.result_of_search_users[user_search_index][8] != None):
                    text += "\nLocation : "
                    text += str(self.result_of_search_users[user_search_index][8])
                    text += ", "
                    text += str(self.result_of_search_users[user_search_index][9])

            self.textBrowser_net_search.setText(text)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.textBrowser_net_search.setFont(font)

            self.view_profile_button = QtWidgets.QPushButton("View",self.textBrowser_net_search)
            self.view_profile_button.setGeometry(QtCore.QRect(250, 0, 80, 30))
            self.view_profile_button.setObjectName(str(self.result_of_search_users[user_search_index][1]))
            searched_username_v = self.view_profile_button.objectName()
            user_id = self.result_of_search_users[user_search_index][0]
            self.view_profile_button.clicked.connect(lambda ch, user_id = user_id : self.go_to_their_profile(user_id))
            # if this button is pushed
            # send a view profile notif

            self.messsage_strabger_button = QtWidgets.QPushButton("Message",self.textBrowser_net_search)
            self.messsage_strabger_button.setGeometry(QtCore.QRect(250, 30, 80, 30))
            self.messsage_strabger_button.setObjectName(str(self.result_of_search_users[user_search_index][1]))
            searched_userid = self.result_of_search_users[user_search_index][0]
            self.messsage_strabger_button.clicked.connect(lambda ch, searched_userid=searched_userid : self.message_to(searched_userid))

            if linkedin_database.is_network(int(self.user_id), int(self.result_of_search_users[user_search_index][0])) == 1:
                self.network_button_3 = QtWidgets.QPushButton("Unfollow",self.textBrowser_net_search)
                self.network_button_3.setGeometry(QtCore.QRect(250, 60, 80, 30))
                self.network_button_3.setObjectName(str(self.result_of_search_users[user_search_index][0]))
                searched_username_n = self.network_button_3.objectName()
                self.network_button_3.clicked.connect(lambda ch, searched_username_n = searched_username_n : self.take_back_request(searched_username_n))
                # needs to be checked

            elif linkedin_database.is_pending(int(self.user_id), int(self.result_of_search_users[user_search_index][0])) == 1:
                self.network_button_3 = QtWidgets.QPushButton("Requested",self.textBrowser_net_search)
                self.network_button_3.setGeometry(QtCore.QRect(250, 60, 80, 30))
                self.network_button_3.setObjectName(str(self.result_of_search_users[user_search_index][0]))
                searched_username_n = self.network_button_3.objectName()
                self.network_button_3.clicked.connect(lambda ch, searched_username_n = searched_username_n : self.take_back_request(searched_username_n))
            else:
                # no record or rejected Invitation
                self.network_button_3 = QtWidgets.QPushButton("Connect",self.textBrowser_net_search)
                self.network_button_3.setGeometry(QtCore.QRect(250, 60, 80, 30))
                self.network_button_3.setObjectName(str(self.result_of_search_users[user_search_index][0]))
                searched_username_n = self.network_button_3.objectName()
                self.network_button_3.clicked.connect(lambda ch, searched_username_n = searched_username_n : self.send_invit(searched_username_n))

            self.verticalLayout_2net_search.addWidget(self.textBrowser_net_search)

        self.scrollArea_net_search.setWidget(self.scrollAreaWidgetContents_net_search)
        #self.verticalLayout_net_search.addWidget(self.scrollArea_net_search)

    def send_invit(self, userid):
        linkedin_database.send_invitation(int(self.user_id), int(userid))
        self.search_for_users()
        # call the function "search_for_users" again to refresh the page

    def accept_invi(self, userid):
        linkedin_database.accept_invitation(userid, self.user_id)
        self.invi_printer()
        self.network_printer()

    def reject_invi(self, userid):
        linkedin_database.reject_invitation(userid, self.user_id)
        self.invi_printer()
        self.network_printer()

    def invi_printer(self):
        self.clearlayout(self.verticalLayout_2invi)
        self.my_invitation_list = linkedin_database.get_my_invitations(int(self.user_id))
        num_of_invites = len(self.my_invitation_list)
        for i_invite in range(num_of_invites):
            self.textBrowser_invi = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_invi)
            self.textBrowser_invi.setObjectName(str(self.my_invitation_list[i_invite][1])) #sender_id
            sender_id_invite = self.textBrowser_invi.objectName()
            font = QtGui.QFont()
            font.setPointSize(10)
            self.textBrowser_invi.setFont(font)
            self.accept_btn = QtWidgets.QPushButton("Accept", self.textBrowser_invi)
            self.accept_btn.setGeometry(QtCore.QRect(100, 0, 60, 30))
            self.accept_btn.clicked.connect(lambda ch, sender_id_invite=sender_id_invite : self.accept_invi(sender_id_invite))

            self.reject_btn = QtWidgets.QPushButton("Reject", self.textBrowser_invi)
            self.reject_btn.setGeometry(QtCore.QRect(160, 0, 60, 30))
            self.reject_btn.clicked.connect(lambda ch, sender_id_invite=sender_id_invite : self.reject_invi(sender_id_invite))

            sender_name_invite = linkedin_database.get_username(sender_id_invite)
            self.UserName_label_i = QtWidgets.QLabel(sender_name_invite, self.textBrowser_invi)
            self.UserName_label_i.setGeometry(QtCore.QRect(10, 5, 60, 30))

            #self.textBrowser_invi.clicked.connect(lambda ch, text=text : self.get_a_conv(text))
            self.verticalLayout_2invi.addWidget(self.textBrowser_invi)

    def network_printer(self):
        self.clearlayout(self.verticalLayout_2net)
        self.my_network_list = linkedin_database.get_network(int(self.user_id))
        num_of_network = len(self.my_network_list)
        for i_network in range(num_of_network):
            self.textBrowser_net = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_net)
            self.textBrowser_net.setObjectName("textBrowser")
            network_user_id = int(self.my_network_list[i_network][1])
            if network_user_id != self.user_id:
                network_username = linkedin_database.get_username(network_user_id)
            else:
                network_user_id = int(self.my_network_list[i_network][2])
                network_username = linkedin_database.get_username(network_user_id)

            self.textBrowser_net.setText(str(network_username))
            self.verticalLayout_2net.addWidget(self.textBrowser_net)

    def take_back_request(self, userid):
        #print(userid)
        linkedin_database.reject_invitation(int(self.user_id), int(userid))
        linkedin_database.reject_invitation(int(userid), int(self.user_id))
        self.search_for_users()

    def get_contacts(self):
        info = linkedin_database.get_my_contacts(self.user_id)
        self.contacts = info

    def onChanged(self):
        filter_choice = self.comboBox.currentText()
        if filter_choice == "Archived":
            self.archived = linkedin_database.get_archived(self.user_id, self.selected_contact)
            self.print_chat(self.archived)
        elif filter_choice == "Not Archived":
            self.archived = linkedin_database.get_unarchived(self.user_id, self.selected_contact)
            self.print_chat(self.archived)
        elif filter_choice == "Read":
            pass
        elif filter_choice == "Unread":
            pass

    def like_post(self, post_id, user_id):
        linkedin_database.like_a_post(int(post_id), int(self.user_id))
        linkedin_database.add_notification(int(self.user_id), int(user_id), '3')
        self.post_printer()

    def unlike_post(self, post_id):
        linkedin_database.remove_a_like(int(post_id), int(self.user_id))
        self.post_printer()

    def like_a_com(self, comment_id):
        linkedin_database.like_a_comment(int(comment_id), int(self.user_id))
        self.post_printer()

    def remove_a_com_like(self, comment_id):
        linkedin_database.unlike_a_comment(int(comment_id), int(self.user_id))
        self.post_printer()

    def add_a_comment(self, post_id, user_id):
        comment_context = self.comment_edit_2.toPlainText()
        self.comment_edit_2.clear()
        comment_id = linkedin_database.add_new_comment(comment_context)
        linkedin_database.add_new_comment_detail(int(comment_id), int(self.user_id), int(post_id))
        linkedin_database.add_notification(int(self.user_id), int(user_id), '4')
        self.post_printer()

    def reply_a_com(self, comment_id, user_id):
        comment_context = self.comment_edit_2.toPlainText()
        self.comment_edit_2.clear()
        comment_id2 = linkedin_database.add_new_comment(comment_context)
        linkedin_database.add_new_reply(int(comment_id), int(comment_id2), int(self.user_id))
        linkedin_database.add_notification(int(self.user_id), int(user_id), '5')
        self.post_printer()

    def post_printer(self):
        self.clearlayout(self.gridLayout_2post)
        if self.user_id != "":
            self.my_home_posts = linkedin_database.get_home_posts(int(self.user_id))
        num_of_posts = len(self.my_home_posts)
        for index_post in range(num_of_posts):
            self.post_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_post)
            self.post_frame.setFrameShape(QtWidgets.QFrame.Box)
            self.post_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.post_frame.setObjectName("post_frame")
            self.gridLayout_3post = QtWidgets.QGridLayout(self.post_frame)
            self.gridLayout_3post.setObjectName("gridLayout_3")
            post_id_home = self.my_home_posts[index_post][0]
            user_id_home = self.my_home_posts[index_post][5]
            if linkedin_database.is_liked_a_post(int(post_id_home), int(self.user_id)) == 0:
                self.like_btn_post = QtWidgets.QPushButton("like", self.post_frame)
                self.like_btn_post.setObjectName(str(post_id_home))
                self.like_btn_post.clicked.connect(lambda ch, post_id_home=post_id_home, user_id_home=user_id_home : self.like_post(post_id_home, user_id_home))
            else:
                self.like_btn_post = QtWidgets.QPushButton("Unlike", self.post_frame)
                self.like_btn_post.setObjectName(str(post_id_home))
                self.like_btn_post.clicked.connect(lambda ch, post_id_home=post_id_home : self.unlike_post(post_id_home))

            self.gridLayout_3post.addWidget(self.like_btn_post, index_post+4, 6, 1, 1)
            self.comment_btn_post = QtWidgets.QPushButton("Comment", self.post_frame)
            self.comment_btn_post.setObjectName("comment_btn")
            self.comment_btn_post.clicked.connect(lambda ch, post_id_home=post_id_home, user_id_home=user_id_home : self.add_a_comment(post_id_home, user_id_home))
            self.gridLayout_3post.addWidget(self.comment_btn_post, index_post+4, 7, 1, 1)


            self.widget_comment_p = QtWidgets.QWidget(self.post_frame)
            self.widget_comment_p.setGeometry(QtCore.QRect(50, 50, 400, 300))
            self.widget_comment_p.setObjectName("widget")
            self.verticalLayout_comment_p = QtWidgets.QVBoxLayout(self.widget_comment_p)
            self.verticalLayout_comment_p.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_comment_p.setObjectName("verticalLayout")
            self.scrollArea_comment_p = QtWidgets.QScrollArea(self.widget_comment_p)
            self.scrollArea_comment_p.setWidgetResizable(True)
            self.scrollArea_comment_p.setObjectName("scrollArea")
            self.scrollAreaWidgetContents_2cmnt_p = QtWidgets.QWidget()
            self.scrollAreaWidgetContents_2cmnt_p.setGeometry(QtCore.QRect(0, 0, 50, 100))
            self.scrollAreaWidgetContents_2cmnt_p.setObjectName("scrollAreaWidgetContents_2")
            self.gridLayout_cmnt_p = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2cmnt_p)
            self.gridLayout_cmnt_p.setObjectName("gridLayout")
            comment_list = linkedin_database.get_a_posts_comments(int(post_id_home))
            k = 0
            for index_comm in range(len(comment_list)):
                self.textBrowser_cmnt_p = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2cmnt_p)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.textBrowser_cmnt_p.sizePolicy().hasHeightForWidth())
                self.textBrowser_cmnt_p.setSizePolicy(sizePolicy)
                self.textBrowser_cmnt_p.setObjectName("textBrowser")
                self.textBrowser_cmnt_p.setSizePolicy(sizePolicy)
                self.textBrowser_cmnt_p.setMaximumSize(QtCore.QSize(450, 60))
                self.textBrowser_cmnt_p.setMinimumSize(QtCore.QSize(450, 60))
                comment_composer = linkedin_database.get_username(int(comment_list[index_comm][1]))
                com_user = int(comment_list[index_comm][1])
                self.textBrowser_cmnt_p.setText(str(comment_composer) + " COMENTED : " + comment_list[index_comm][0] + "\nLikes: " + str(linkedin_database.number_of_likes_of_a_comment(int(comment_list[index_comm][2]))))
                self.comment_button_reply = QtWidgets.QPushButton( "Reply", self.textBrowser_cmnt_p)
                self.comment_button_reply.setGeometry(QtCore.QRect(380, 15, 60, 30))
                com_id = int(comment_list[index_comm][2])
                self.comment_button_reply.clicked.connect(lambda ch, com_id=com_id, com_user=com_user : self.reply_a_com(com_id, com_user))

                if linkedin_database.is_liked_a_comment(int(comment_list[index_comm][2]), int(self.user_id)) == 0:
                    self.comment_button_like = QtWidgets.QPushButton( "Like", self.textBrowser_cmnt_p)
                    self.comment_button_like.setGeometry(QtCore.QRect(320, 15, 60, 30))
                    com_id = int(comment_list[index_comm][2])
                    self.comment_button_like.clicked.connect(lambda ch, com_id=com_id : self.like_a_com(com_id))
                else:
                    self.comment_button_like = QtWidgets.QPushButton( "Unlike", self.textBrowser_cmnt_p)
                    self.comment_button_like.setGeometry(QtCore.QRect(320, 15, 60, 30))
                    com_id = int(comment_list[index_comm][2])
                    self.comment_button_like.clicked.connect(lambda ch, com_id=com_id : self.remove_a_com_like(com_id))

                self.gridLayout_cmnt_p.addWidget(self.textBrowser_cmnt_p, k , 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
                k += 1
                rely_list = linkedin_database.get_a_comments_replys(int(com_id))
                for rep_index in range(len(rely_list)):
                    self.textBrowser_cmnt_p = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2cmnt_p)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.textBrowser_cmnt_p.sizePolicy().hasHeightForWidth())
                    self.textBrowser_cmnt_p.setSizePolicy(sizePolicy)
                    self.textBrowser_cmnt_p.setObjectName("textBrowser")
                    self.textBrowser_cmnt_p.setSizePolicy(sizePolicy)
                    self.textBrowser_cmnt_p.setMaximumSize(QtCore.QSize(450, 60))
                    self.textBrowser_cmnt_p.setMinimumSize(QtCore.QSize(450, 60))
                    comment_composer = linkedin_database.get_username(int(rely_list[rep_index][1]))
                    com_user = int(rely_list[rep_index][1])
                    self.textBrowser_cmnt_p.setText( str(comment_composer) +  " REPLIED : " + rely_list[rep_index][0] + "\nLikes: " + str(linkedin_database.number_of_likes_of_a_comment(int(rely_list[rep_index][2]))))
                    self.comment_button_reply = QtWidgets.QPushButton( "Reply", self.textBrowser_cmnt_p)
                    self.comment_button_reply.setGeometry(QtCore.QRect(380, 15, 60, 30))
                    com_id = int(rely_list[rep_index][2])
                    self.comment_button_reply.clicked.connect(lambda ch, com_id=com_id, com_user=com_user : self.reply_a_com(com_id, com_user))
                    if linkedin_database.is_liked_a_comment(int(rely_list[rep_index][2]), int(self.user_id)) == 0:
                        self.comment_button_like = QtWidgets.QPushButton( "Like", self.textBrowser_cmnt_p)
                        self.comment_button_like.setGeometry(QtCore.QRect(320, 15, 60, 30))
                        com_id = int(rely_list[rep_index][2])
                        self.comment_button_like.clicked.connect(lambda ch, com_id=com_id : self.like_a_com(com_id))
                    else:
                        self.comment_button_like = QtWidgets.QPushButton( "Unlike", self.textBrowser_cmnt_p)
                        self.comment_button_like.setGeometry(QtCore.QRect(320, 15, 60, 30))
                        com_id = int(rely_list[rep_index][2])
                        self.comment_button_like.clicked.connect(lambda ch, com_id=com_id : self.remove_a_com_like(com_id))

                    self.gridLayout_cmnt_p.addWidget(self.textBrowser_cmnt_p, k , 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
                    k += 1

            self.scrollArea_comment_p.setWidget(self.scrollAreaWidgetContents_2cmnt_p)
            self.verticalLayout_comment_p.addWidget(self.scrollArea_comment_p)

            self.gridLayout_3post.addWidget(self.widget_comment_p, 5+index_post, 0, 7, 10)
            total_com_number = k
            self.label_cooments = QtWidgets.QLabel("Comments : " + str(total_com_number), self.post_frame)
            self.label_cooments.setObjectName("label_cooments")
            self.gridLayout_3post.addWidget(self.label_cooments, 4+index_post, 0, 1, 1)
            self.Author_label = QtWidgets.QLabel(str(linkedin_database.get_username(self.my_home_posts[index_post][5])) , self.post_frame)
            self.Author_label.setObjectName("Author_label")
            self.caption_label = QtWidgets.QLabel(str(self.my_home_posts[index_post][2]), self.post_frame)
            self.caption_label.setObjectName("caption_label")
            self.gridLayout_3post.addWidget(self.caption_label, 1+index_post, 0, 1, 1)
            self.gridLayout_3post.addWidget(self.Author_label, index_post, 0, 1, 1)
            self.likes_label = QtWidgets.QLabel(self.post_frame)
            self.likes_label.setObjectName("likes_label")
            #self.gridLayout_3post.addWidget(self.likes_label, 100+index_post , 0, 1, 1)
            self.likes_count = QtWidgets.QLabel(" Likes : " + str(linkedin_database.number_of_likes_of_a_post(self.my_home_posts[index_post][0])), self.post_frame)
            self.likes_count.setObjectName("likes_count")
            self.gridLayout_3post.addWidget(self.likes_count, 3+index_post , 0, 1, 1)
            self.gridLayout_2post.addWidget(self.post_frame, 0+index_post, 0, 1, 1)

        self.scrollArea_post.setWidget(self.scrollAreaWidgetContents_post)
        self.gridLayout_post.addWidget(self.scrollArea_post, 0, 0, 1, 1)

    def add_skill(self):
        text = self.textEdit_add_skill.toPlainText()
        linkedin_database.add_new_skill(int(self.user_id), text)
        self.textEdit_add_skill.clear()
        self.skill_printer()

    def add_acc(self):
        text = self.textEdit_add_acc.toPlainText()
        linkedin_database.add_new_accomplishment(int(self.user_id), text)
        self.textEdit_add_acc.clear()
        self.accom_printer()

    def add_feat(self):
        text = self.textEdit_add_feat.toPlainText()
        linkedin_database.add_new_featured(int(self.user_id), text)
        self.textEdit_add_feat.clear()
        self.features_printer()

    def skill_printer(self):
        self.clearlayout(self.gridLayout_skill)
        if self.user_id != '':
            self.skill_list = linkedin_database.get_skills(int(self.user_id))

    def del_accom(self, accomid):
        linkedin_database.remove_an_accomplishment(int(self.user_id), int(accomid))
        self.accom_printer()

    def del_skill(self, skillid):
        linkedin_database.remove_a_skill(int(self.user_id), int(skillid))
        self.skill_printer()

    def del_feat(self, featid):
        linkedin_database.remove_a_featured(int(self.user_id), int(featid))
        self.features_printer()

    def skill_printer(self):
        self.clearlayout(self.gridLayout_skill)
        if self.user_id != '':
            self.skill_list = linkedin_database.get_skills(int(self.user_id))
        for i in range(len(self.skill_list)):
            self.textBrowser_skill = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2skill)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.textBrowser_skill.sizePolicy().hasHeightForWidth())
            self.textBrowser_skill.setSizePolicy(sizePolicy)
            self.textBrowser_skill.setObjectName("textBrowser")
            self.textBrowser_skill.setSizePolicy(sizePolicy)
            self.textBrowser_skill.setText(str(self.skill_list[i][2]))
            self.textBrowser_skill.setMaximumSize(QtCore.QSize(200, 60))
            self.pushButton_sdel = QtWidgets.QPushButton("Delete",self.textBrowser_skill)
            self.pushButton_sdel.setGeometry(QtCore.QRect(140, 10, 50, 30))
            self.pushButton_sdel.setObjectName("pushButton_4")
            skillid = int(self.skill_list[i][0])
            self.pushButton_sdel.clicked.connect(lambda ch, skillid=skillid : self.del_skill(skillid))
            self.gridLayout_skill.addWidget(self.textBrowser_skill, i, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.scrollArea_skills.setWidget(self.scrollAreaWidgetContents_2skill)
        self.verticalLayout_skills.addWidget(self.scrollArea_skills)

    def accom_printer(self):
        self.clearlayout(self.gridLayout_accom)
        if self.user_id != '':
            self.accomplishment_list = linkedin_database.get_accomplishments(int(self.user_id))
        for i in range(len(self.accomplishment_list)):
            self.textBrowser_accom = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2accom)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.textBrowser_accom.sizePolicy().hasHeightForWidth())
            self.textBrowser_accom.setSizePolicy(sizePolicy)
            self.textBrowser_accom.setObjectName("textBrowser")
            self.textBrowser_accom.setSizePolicy(sizePolicy)
            self.textBrowser_accom.setText(str(self.accomplishment_list[i][2]))
            self.textBrowser_accom.setMaximumSize(QtCore.QSize(200, 60))
            self.pushButton_adel = QtWidgets.QPushButton("Delete",self.textBrowser_accom)
            self.pushButton_adel.setGeometry(QtCore.QRect(140, 10, 50, 30))
            self.pushButton_adel.setObjectName("pushButton_4")
            accomid = int(self.accomplishment_list[i][0])
            self.pushButton_adel.clicked.connect(lambda ch, accomid=accomid : self.del_accom(accomid))

            self.gridLayout_accom.addWidget(self.textBrowser_accom, i, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.scrollArea_accom.setWidget(self.scrollAreaWidgetContents_2accom)
        self.verticalLayout_accom.addWidget(self.scrollArea_accom)

    def features_printer(self):
        self.clearlayout(self.gridLayout_feat)
        if self.user_id != '':
            self.featured_list = linkedin_database.get_featureds(int(self.user_id))
        for i in range(len(self.featured_list)):
            self.textBrowser_feat = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2feat)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.textBrowser_feat.sizePolicy().hasHeightForWidth())
            self.textBrowser_feat.setSizePolicy(sizePolicy)
            self.textBrowser_feat.setObjectName("textBrowser")
            self.textBrowser_feat.setSizePolicy(sizePolicy)
            self.textBrowser_feat.setText(str(self.featured_list[i][2]))
            self.textBrowser_feat.setMaximumSize(QtCore.QSize(200, 60))
            self.pushButton_fdel = QtWidgets.QPushButton("Delete",self.textBrowser_feat)
            self.pushButton_fdel.setGeometry(QtCore.QRect(140, 10, 50, 30))
            self.pushButton_fdel.setObjectName("pushButton_4")
            featid = int(self.featured_list[i][0])
            self.pushButton_fdel.clicked.connect(lambda ch, featid=featid : self.del_feat(featid))

            self.gridLayout_feat.addWidget(self.textBrowser_feat, i, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.scrollArea_feat.setWidget(self.scrollAreaWidgetContents_2feat)
        self.verticalLayout_feat.addWidget(self.scrollArea_feat)

    def notif_printer(self):
        self.widget_notif = QtWidgets.QWidget(self.notifications)
        self.widget_notif.setGeometry(QtCore.QRect(600, 150, 400, 600))
        self.widget_notif.setObjectName("widget")
        self.verticalLayout_notif = QtWidgets.QVBoxLayout(self.widget_notif)
        self.verticalLayout_notif.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_notif.setObjectName("verticalLayout")
        self.scrollArea_notif = QtWidgets.QScrollArea(self.widget_notif)
        self.scrollArea_notif.setWidgetResizable(True)
        self.scrollArea_notif.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2notif = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2notif.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.scrollAreaWidgetContents_2notif.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_notif = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2notif)
        self.gridLayout_notif.setObjectName("gridLayout")
        for i in range(len(self.notif_list)):
            self.textBrowser_notif = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2notif)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.textBrowser_notif.sizePolicy().hasHeightForWidth())
            self.textBrowser_notif.setSizePolicy(sizePolicy)
            self.textBrowser_notif.setObjectName("textBrowser")
            self.textBrowser_notif.setSizePolicy(sizePolicy)
            self.textBrowser_notif.setMaximumSize(QtCore.QSize(300, 60))
            self.textBrowser_notif.setMinimumSize(QtCore.QSize(300, 60))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.textBrowser_notif.setFont(font)
            username = linkedin_database.get_username(int(self.notif_list[i][1]))
            type = self.notif_list[i][3]
            if type == '1':
                self.textBrowser_notif.setText(str(username) + "'s birthday is today")
            if type == '2':
                self.textBrowser_notif.setText(str(username) + " Visited your profile")
            if type == '3':
                self.textBrowser_notif.setText(str(username) + " Liked your Post")
            if type == '4':
                self.textBrowser_notif.setText(str(username) + " Commneted on your Post")
            if type == '5':
                self.textBrowser_notif.setText(str(username) + " Replied your comment")
            if type == '6':
                self.textBrowser_notif.setText(str(username) + " Endorsed your skill")
            if type == '7':
                self.textBrowser_notif.setText(str(username) + " Changed their job")

            self.gridLayout_notif.addWidget(self.textBrowser_notif, i, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.scrollArea_notif.setWidget(self.scrollAreaWidgetContents_2notif)
        self.verticalLayout_notif.addWidget(self.scrollArea_notif)

    def make_a_post(self):
        linkedin_database.add_new_post(None, self.post_maker_input.toPlainText(), None, None, int(self.user_id))
        self.post_maker_input.clear()
        self.post_printer()

    def goToEdit(self):
        self.goto("edit")

    def goToMain(self):
        self.goto("login")

    def UiComponents(self):
        # self.backButton = QtWidgets.QPushButton("BackButton", self)
        # self.backButton.setGeometry(QtCore.QRect(450, 5, 100, 20))
        # self.backButton.clicked.connect(self.goToMain)

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 1780, 900))
        self.tabWidget.setObjectName("tabWidget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(71, 71, 71);")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.tabWidget.addTab(self.home, "Home")

        self.label90 = QtWidgets.QLabel("Make a new Post", self.home)
        self.label90.setGeometry(QtCore.QRect(70, 200, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label90.setFont(font)
        self.label90.setObjectName("label")
        self.label_290 = QtWidgets.QLabel("Type your commnet here", self.home)
        self.label_290.setGeometry(QtCore.QRect(70, 550, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_290.setFont(font)
        self.label_290.setObjectName("label_2")
        self.label91 = QtWidgets.QLabel("People you may know", self.home)
        self.label91.setGeometry(QtCore.QRect(1250, 30, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label91.setFont(font)
        self.label91.setObjectName("label")

        self.centralwidget_post = QtWidgets.QWidget(self.home)
        self.centralwidget_post.setObjectName("centralwidget")
        self.centralwidget_post.setGeometry(QtCore.QRect(500, 100, 600, 700))
        self.gridLayout_post = QtWidgets.QGridLayout(self.centralwidget_post)
        self.gridLayout_post.setObjectName("gridLayout")
        self.scrollArea_post = QtWidgets.QScrollArea(self.centralwidget_post)
        self.scrollArea_post.setWidgetResizable(True)
        self.scrollArea_post.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_post = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_post.setGeometry(QtCore.QRect(0, 0, 674, 360))
        self.scrollAreaWidgetContents_post.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2post = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_post)
        self.gridLayout_2post.setObjectName("gridLayout_2")
        self.comment_edit_2 = QtWidgets.QTextEdit(self.home)
        self.comment_edit_2.setGeometry(QtCore.QRect(55, 600, 320, 70))
        self.post_printer()

        self.people_you_may_know = QtWidgets.QTextBrowser(self.home)
        self.people_you_may_know.setGeometry(QtCore.QRect(1240, 80, 400, 720))
        self.verticalLayout_people = QtWidgets.QVBoxLayout(self.people_you_may_know)
        self.verticalLayout_people.setObjectName("verticalLayout")
        self.scrollArea_people = QtWidgets.QScrollArea(self.home)
        self.scrollArea_people.setWidgetResizable(True)
        self.scrollArea_people.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_people = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_people.setGeometry(QtCore.QRect(0, 0, 651, 508))
        self.scrollAreaWidgetContents_people.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2people = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_people)
        self.verticalLayout_2people.setObjectName("verticalLayout_2")

        num_of_people_you_may_know = len(self.ppl_i_may_know)
        for i in range(num_of_people_you_may_know):
            self.textBrowser_people = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_people)
            self.textBrowser_people.setObjectName("textBrowser")
            person_username = linkedin_database.get_username(int(self.ppl_i_may_know[i][1]))
            self.textBrowser_people.setText("User : " + str(person_username) + " ( " + str(self.ppl_i_may_know[i][2]) + " Mutuals )")
            self.verticalLayout_2people.addWidget(self.textBrowser_people)

        self.scrollArea_people.setWidget(self.scrollAreaWidgetContents_people)
        self.verticalLayout_people.addWidget(self.scrollArea_people)


        self.post_maker_input = QtWidgets.QTextEdit(self.home)
        self.post_maker_input.setGeometry(QtCore.QRect(50, 250, 331, 131))
        self.post_maker_input.setObjectName("post_maker_input")
        self.post_maker_button = QtWidgets.QPushButton("Post", self.home)
        self.post_maker_button.setGeometry(QtCore.QRect(160, 400, 93, 28))
        self.post_maker_button.setObjectName("post_maker_button")
        self.post_maker_button.setStyleSheet("color: rgb(30, 30, 30);")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.post_maker_button.setFont(font)
        self.post_maker_button.clicked.connect(self.make_a_post)

        # My network Tab
        self.my_network = QtWidgets.QWidget()
        self.my_network.setObjectName("my_network")
        self.tabWidget.addTab(self.my_network, "My Network")

        self.label_net0 = QtWidgets.QLabel("Search Users", self.my_network)
        self.label_net0.setGeometry(QtCore.QRect(220, 70, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_net0.setFont(font)
        self.label_net0.setObjectName("label_net")

        self.label_net = QtWidgets.QLabel("Filter results by :", self.my_network)
        self.label_net.setGeometry(QtCore.QRect(150, 160, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_net.setFont(font)
        self.label_net.setObjectName("label_net")
        self.comboBox_net = QtWidgets.QComboBox(self.my_network)
        self.comboBox_net.setGeometry(QtCore.QRect(330, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_net.setFont(font)
        self.comboBox_net.setObjectName("comboBox_net")
        self.comboBox_net.addItem("Connection")
        self.comboBox_net.addItem("Username")
        self.comboBox_net.addItem("Location")
        self.comboBox_net.addItem("Current Company")

        self.label_mynet = QtWidgets.QLabel("My Network", self.my_network)
        self.label_mynet.setGeometry(QtCore.QRect(780, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_mynet.setFont(font)
        self.label_mynet.setObjectName("label_net")

        self.network_holder = QtWidgets.QWidget(self.my_network)
        self.network_holder.setGeometry(QtCore.QRect(600, 80, 500, 720))
        self.verticalLayout_net = QtWidgets.QVBoxLayout(self.network_holder)
        self.verticalLayout_net.setObjectName("verticalLayout")
        self.scrollArea_net = QtWidgets.QScrollArea(self.my_network)
        self.scrollArea_net.setWidgetResizable(True)
        self.scrollArea_net.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_net = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_net.setGeometry(QtCore.QRect(0, 0, 651, 508))
        self.scrollAreaWidgetContents_net.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2net = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_net)
        self.verticalLayout_2net.setObjectName("verticalLayout_2")

        num_of_network = len(self.my_network_list)
        # All the people in my connection sit here
        for i_network in range(num_of_network):
            self.textBrowser_net = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_net)
            self.textBrowser_net.setObjectName("textBrowser")
            network_user_id = int(self.my_network_list[i_network][1])
            if network_user_id != self.user_id:
                network_username = linkedin_database.get_username(network_user_id)
            else:
                network_user_id = int(self.my_network_list[i_network][2])
                network_username = linkedin_database.get_username(network_user_id)

            self.textBrowser_net.setText(str(network_username))
            self.verticalLayout_2net.addWidget(self.textBrowser_net)

        self.scrollArea_net.setWidget(self.scrollAreaWidgetContents_net)
        self.verticalLayout_net.addWidget(self.scrollArea_net)

        self.lineEdit_search_net = QtWidgets.QLineEdit(self.my_network)
        self.lineEdit_search_net.setGeometry(QtCore.QRect(115, 231, 260, 41))
        self.lineEdit_search_net.setObjectName("lineEdit_search")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_search_net.setFont(font)
        self.pushButton_search_net = QtWidgets.QPushButton("Search", self.my_network)
        self.pushButton_search_net.setGeometry(QtCore.QRect(388, 230, 101, 41))
        self.pushButton_search_net.setStyleSheet("color: rgb(30, 30, 30);")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_net.setFont(font)
        self.pushButton_search_net.setObjectName("pushButton_search")
        self.pushButton_search_net.clicked.connect(self.search_for_users)

        self.network_holder_search = QtWidgets.QWidget(self.my_network)
        self.network_holder_search.setGeometry(QtCore.QRect(100, 300, 400, 500))
        self.verticalLayout_net_search = QtWidgets.QVBoxLayout(self.network_holder_search)
        self.verticalLayout_net_search.setObjectName("verticalLayout")
        self.verticalLayout_net_search.setSpacing(5)
        self.verticalLayout_net_search.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea_net_search = QtWidgets.QScrollArea(self.network_holder_search)
        self.scrollArea_net_search.setWidgetResizable(True)
        self.scrollArea_net_search.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_net_search = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_net_search.setGeometry(QtCore.QRect(0, 0, 651, 508))
        self.scrollAreaWidgetContents_net_search.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2net_search = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_net_search)
        self.verticalLayout_2net_search.setObjectName("verticalLayout_2")
        self.verticalLayout_2net_search.setSpacing(5)
        self.verticalLayout_2net_search.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_2net_search.setContentsMargins(20, 20, 20, 20)
        self.scrollArea_net_search.setWidget(self.scrollAreaWidgetContents_net_search)
        self.verticalLayout_net_search.addWidget(self.scrollArea_net_search)

        # my network -> my invitations
        self.label_mynet2 = QtWidgets.QLabel("My Invitations", self.my_network)
        self.label_mynet2.setGeometry(QtCore.QRect(1300, 140, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_mynet2.setFont(font)
        self.label_mynet2.setObjectName("label_net")

        self.invi_holder =  QtWidgets.QWidget(self.my_network)
        self.invi_holder.setGeometry(QtCore.QRect(1200, 200, 350, 600))
        self.verticalLayout_invi = QtWidgets.QVBoxLayout(self.invi_holder)
        self.verticalLayout_invi.setObjectName("verticalLayout_m")
        self.verticalLayout_invi.setSpacing(5)
        self.verticalLayout_invi.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea_invi = QtWidgets.QScrollArea(self.invi_holder)
        self.scrollArea_invi.setWidgetResizable(True)
        self.scrollArea_invi.setObjectName("scrollArea_m")
        self.scrollAreaWidgetContents_invi = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_invi.setGeometry(QtCore.QRect(100, 100, 50, 50))
        self.scrollAreaWidgetContents_invi.setObjectName("scrollAreaWidgetContents_m")
        self.verticalLayout_2invi = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_invi)
        self.verticalLayout_2invi.setObjectName("verticalLayout_2m")
        self.verticalLayout_2invi.setSpacing(5)
        self.verticalLayout_2invi.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_2invi.setContentsMargins(20, 20, 20, 20)

        num_of_invites = len(self.my_invitation_list)
        for i_invite in range(num_of_invites):
            self.textBrowser_invi = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_invi)
            self.textBrowser_invi.setObjectName(str(self.my_invitation_list[i_invite][1])) #sender_id
            sender_id_invite = self.textBrowser_invi.objectName()
            font = QtGui.QFont()
            font.setPointSize(10)
            self.textBrowser_invi.setFont(font)
            self.accept_btn = QtWidgets.QPushButton("Accept", self.textBrowser_invi)
            self.accept_btn.setGeometry(QtCore.QRect(100, 0, 60, 30))
            self.accept_btn.clicked.connect(lambda ch, sender_id_invite=sender_id_invite : self.accept_invi(sender_id_invite))

            self.reject_btn = QtWidgets.QPushButton("Reject", self.textBrowser_invi)
            self.reject_btn.setGeometry(QtCore.QRect(160, 0, 60, 30))
            self.reject_btn.clicked.connect(lambda ch, sender_id_invite=sender_id_invite : self.reject_invi(sender_id_invite))

            sender_name_invite = linkedin_database.get_username(sender_id_invite)
            self.UserName_label_i = QtWidgets.QLabel(sender_name_invite, self.textBrowser_invi)
            self.UserName_label_i.setGeometry(QtCore.QRect(10, 5, 60, 30))

            #self.textBrowser_invi.clicked.connect(lambda ch, text=text : self.get_a_conv(text))
            self.verticalLayout_2invi.addWidget(self.textBrowser_invi)

        self.scrollArea_invi.setWidget(self.scrollAreaWidgetContents_invi)
        self.verticalLayout_invi.addWidget(self.scrollArea_invi)


        # mssging tab
        self.messaging = QtWidgets.QWidget()
        self.messaging.setObjectName("messaging")
        self.tabWidget.addTab(self.messaging, "Messaging")

        self.label92 = QtWidgets.QLabel("My Contacts", self.messaging)
        self.label92.setGeometry(QtCore.QRect(250, 150, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label92.setFont(font)
        self.label92.setObjectName("label")

        self.temp =  QtWidgets.QWidget(self.messaging)
        self.temp.setGeometry(QtCore.QRect(140, 200, 350, 400))
        self.verticalLayout_m = QtWidgets.QVBoxLayout(self.temp)
        self.verticalLayout_m.setObjectName("verticalLayout_m")
        self.verticalLayout_m.setSpacing(5)
        self.verticalLayout_m.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea_m = QtWidgets.QScrollArea(self.temp)
        self.scrollArea_m.setWidgetResizable(True)
        self.scrollArea_m.setObjectName("scrollArea_m")
        self.scrollAreaWidgetContents_m = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_m.setGeometry(QtCore.QRect(100, 100, 50, 50))
        self.scrollAreaWidgetContents_m.setObjectName("scrollAreaWidgetContents_m")
        self.verticalLayout_2m = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_m)
        self.verticalLayout_2m.setObjectName("verticalLayout_2m")
        self.verticalLayout_2m.setSpacing(5)
        self.verticalLayout_2m.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_2m.setContentsMargins(20, 20, 20, 20)

        num_of_contacts = len(self.contacts)
        for i in range(num_of_contacts):
            self.textBrowser_m = QtWidgets.QPushButton(self.contacts[i][0], self.scrollAreaWidgetContents_m)
            self.textBrowser_m.setObjectName(str(self.contacts[i][1]))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.textBrowser_m.setFont(font)
            text = self.textBrowser_m.text()
            self.textBrowser_m.clicked.connect(lambda ch, text=text : self.get_a_conv(text))
            self.verticalLayout_2m.addWidget(self.textBrowser_m)

        self.scrollArea_m.setWidget(self.scrollAreaWidgetContents_m)
        self.verticalLayout_m.addWidget(self.scrollArea_m)

        self.textEdit = QtWidgets.QTextEdit(self.messaging)
        self.textEdit.setGeometry(QtCore.QRect(770, 610, 421, 100))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton("Send",self.messaging)
        self.pushButton_4.setGeometry(QtCore.QRect(920, 750, 121, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.send_mssg)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(30, 30, 30);")

        self.scrollArea_ch = QtWidgets.QScrollArea(self.messaging)
        self.scrollArea_ch.setGeometry(QtCore.QRect(770, 200, 421, 400))
        self.scrollArea_ch.setWidgetResizable(True)
        self.scrollArea_ch.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_ch = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_ch.setGeometry(QtCore.QRect(0, 0, 278, 50))
        self.scrollAreaWidgetContents_ch.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2ch = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_ch)
        self.verticalLayout_2ch.setObjectName("verticalLayout_2")

        self.chat_search = QtWidgets.QLineEdit(self.messaging)
        self.chat_search.setGeometry(QtCore.QRect(780, 80, 281, 41))

        self.search_chat_button = QtWidgets.QPushButton("Search",self.messaging)
        self.search_chat_button.setGeometry(QtCore.QRect(1080, 80, 101, 41))
        self.search_chat_button.clicked.connect(self.search_mssg)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_chat_button.setFont(font)
        self.search_chat_button.setStyleSheet("color: rgb(30, 30, 30);")

        #Filtering chats
        self.label_filter = QtWidgets.QLabel("Filter your chats by : ", self.messaging)
        self.label_filter.setGeometry(QtCore.QRect(825, 154, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_filter.setFont(font)
        self.label_filter.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.messaging)
        self.comboBox.setGeometry(QtCore.QRect(1010, 150, 141, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("All")
        self.comboBox.addItem("Archived")
        self.comboBox.addItem("Not Archived")
        self.comboBox.addItem("Read")
        self.comboBox.addItem("Unread")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)

        self.comboBox.activated.connect(self.onChanged)

        # Notifications Tab
        self.notifications = QtWidgets.QWidget()
        self.notifications.setObjectName("notifications")
        self.tabWidget.addTab(self.notifications, "Notifications")
        self.notif_printer()

        self.label93 = QtWidgets.QLabel("Notifications", self.notifications)
        self.label93.setGeometry(QtCore.QRect(730, 80, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label93.setFont(font)
        self.label93.setObjectName("label")

        # Profile Tab
        self.editprof = QtWidgets.QWidget()
        self.editprof.setObjectName("editprof")
        self.tabWidget.addTab(self.editprof, "Profile")

        self.Skills_label = QtWidgets.QLabel("Skills", self.editprof)
        self.Skills_label.setGeometry(QtCore.QRect(210, 360, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Skills_label.setFont(font)
        self.Skills_label.setObjectName("Skills_label")
        self.accomplishments_label = QtWidgets.QLabel("Accomplishments", self.editprof)
        self.accomplishments_label.setGeometry(QtCore.QRect(610, 360, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.accomplishments_label.setFont(font)
        self.accomplishments_label.setObjectName("accomplishments_label")
        self.features_label = QtWidgets.QLabel("Featured", self.editprof)
        self.features_label.setGeometry(QtCore.QRect(1010, 360, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.features_label.setFont(font)
        self.features_label.setObjectName("features_label")
        self.profile_frame = QtWidgets.QFrame(self.editprof)
        self.profile_frame.setGeometry(QtCore.QRect(200, 100, 600, 200))
        self.profile_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.profile_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.profile_frame.setLineWidth(1)
        self.profile_frame.setObjectName("profile_frame")
        self.profile_edit_btn = QtWidgets.QPushButton("Edit", self.profile_frame)
        self.profile_edit_btn.setGeometry(QtCore.QRect(540, 170, 60, 30))
        self.profile_edit_btn.clicked.connect(self.goToEdit)
        self.name_label = QtWidgets.QLabel(str(self.first_name) + " " + str(self.last_name), self.profile_frame)
        self.name_label.setGeometry(QtCore.QRect(30, 20, 500, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.username_label = QtWidgets.QLabel("@ " + str(self.username) , self.profile_frame)
        self.username_label.setGeometry(QtCore.QRect(30, 60, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.contactinfo_label = QtWidgets.QLabel("Contact info. : " + str(self.email) , self.profile_frame)
        self.contactinfo_label.setGeometry(QtCore.QRect(300, 60, 250, 21))
        self.contactinfo_label.setObjectName("contactinfo_label")
        self.address_label = QtWidgets.QLabel("Address : " + str(self.country) + ", " + str(self.city), self.profile_frame)
        self.address_label.setGeometry(QtCore.QRect(300, 30, 200, 16))
        self.address_label.setObjectName("address_label")
        self.about_frame = QtWidgets.QFrame(self.editprof)
        self.about_frame.setGeometry(QtCore.QRect(900, 100, 350, 200))
        self.about_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.about_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.about_frame.setLineWidth(1)
        self.about_frame.setObjectName("about_frame")
        self.about_edit_btn = QtWidgets.QPushButton("Edit", self.about_frame)
        self.about_edit_btn.setGeometry(QtCore.QRect(290, 170, 60, 30))
        self.about_label = QtWidgets.QLabel("About", self.about_frame)
        self.about_label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.about_label.setObjectName("about_label")
        self.about_context = QtWidgets.QLabel(str(self.about), self.about_frame)
        self.about_context.setGeometry(QtCore.QRect(20, 50, 200, 16))
        self.about_context.setObjectName("about_label")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.about_label.setFont(font)

        self.widget_skill = QtWidgets.QWidget(self.editprof)
        self.widget_skill.setGeometry(QtCore.QRect(200, 400, 250, 250))
        self.widget_skill.setObjectName("widget")
        self.verticalLayout_skills = QtWidgets.QVBoxLayout(self.widget_skill)
        self.verticalLayout_skills.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_skills.setObjectName("verticalLayout")
        self.scrollArea_skills = QtWidgets.QScrollArea(self.widget_skill)
        self.scrollArea_skills.setWidgetResizable(True)
        self.scrollArea_skills.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2skill = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2skill.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.scrollAreaWidgetContents_2skill.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_skill = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2skill)
        self.gridLayout_skill.setObjectName("gridLayout")
        self.skill_printer()

        self.widget_accom = QtWidgets.QWidget(self.editprof)
        self.widget_accom.setGeometry(QtCore.QRect(600, 400, 250, 250))
        self.widget_accom.setObjectName("widget")
        self.verticalLayout_accom = QtWidgets.QVBoxLayout(self.widget_accom)
        self.verticalLayout_accom.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_accom.setObjectName("verticalLayout")
        self.scrollArea_accom = QtWidgets.QScrollArea(self.widget_accom)
        self.scrollArea_accom.setWidgetResizable(True)
        self.scrollArea_accom.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2accom = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2accom.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.scrollAreaWidgetContents_2accom.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_accom = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2accom)
        self.gridLayout_accom.setObjectName("gridLayout")
        self.accom_printer()

        self.widget_feat = QtWidgets.QWidget(self.editprof)
        self.widget_feat.setGeometry(QtCore.QRect(1000, 400, 250, 250))
        self.widget_feat.setObjectName("widget")
        self.verticalLayout_feat = QtWidgets.QVBoxLayout(self.widget_feat)
        self.verticalLayout_feat.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_feat.setObjectName("verticalLayout")
        self.scrollArea_feat = QtWidgets.QScrollArea(self.widget_feat)
        self.scrollArea_feat.setWidgetResizable(True)
        self.scrollArea_feat.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2feat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2feat.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.scrollAreaWidgetContents_2feat.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_feat = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2feat)
        self.gridLayout_feat.setObjectName("gridLayout")
        self.features_printer()

        self.textEdit_add_skill = QtWidgets.QTextEdit(self.editprof)
        self.textEdit_add_skill.setGeometry(QtCore.QRect(200, 670, 250, 50))
        self.textEdit_add_skill.setObjectName("textEdit")
        self.pushButton_41 = QtWidgets.QPushButton("Add",self.editprof)
        self.pushButton_41.setGeometry(QtCore.QRect(260, 750, 121, 41))
        self.pushButton_41.setObjectName("pushButton_4")
        self.pushButton_41.clicked.connect(self.add_skill)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setStyleSheet("color: rgb(30, 30, 30);")

        self.textEdit_add_acc = QtWidgets.QTextEdit(self.editprof)
        self.textEdit_add_acc.setGeometry(QtCore.QRect(600, 670, 250, 50))
        self.textEdit_add_acc.setObjectName("textEdit")
        self.pushButton_42 = QtWidgets.QPushButton("Add",self.editprof)
        self.pushButton_42.setGeometry(QtCore.QRect(660, 750, 121, 41))
        self.pushButton_42.setObjectName("pushButton_4")
        self.pushButton_42.clicked.connect(self.add_acc)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setStyleSheet("color: rgb(30, 30, 30);")

        self.textEdit_add_feat = QtWidgets.QTextEdit(self.editprof)
        self.textEdit_add_feat.setGeometry(QtCore.QRect(1000, 670, 250, 50))
        self.textEdit_add_feat.setObjectName("textEdit")
        self.pushButton_43 = QtWidgets.QPushButton("Add",self.editprof)
        self.pushButton_43.setGeometry(QtCore.QRect(1060, 750, 121, 41))
        self.pushButton_43.setObjectName("pushButton_4")
        self.pushButton_43.clicked.connect(self.add_feat)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("color: rgb(30, 30, 30);")


        #self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)


class Window(QtWidgets.QMainWindow): # Just add the new pages to this, don't delete anything
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Modified
        self.resize(1800, 950)
        self.m_pages = {}

        # Register all the pages of app
        self.register(EditPage(), "edit")
        self.register(LoginPage(), "login")
        self.register(MainPage(), "main")
        self.register(SignupPage(), "signup")
        self.register(ViewProfile(), "view")

        # Fisrt page to be
        self.goto("login")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            if name == 'main':
                # refreshing
                widget.get_info()
                widget.get_contacts()
            if name == "view":
                widget.get_info()
            widget.UiComponents()
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    import sys

    linkedin_database = linkedin()
    #linkedin_database.signup("admin","admin")

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
