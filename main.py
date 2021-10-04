
import sqlite3


class linkedin:
    def __init__(self):
        self.connection = sqlite3.connect("./myDB.db")
        self.cursor = self.connection.cursor()
        self.username = ""
        self.contact_userid = ""

    def set_myusername(self, username):
        self.username = username

    def create_user_table(self):
        self.cursor.execute("""CREATE TABLE User (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username VARCHAR(50),
                            password VARCHAR(50),
                            fname VARCHAR(50),
                            lname VARCHAR(50),
                            about VARCHAR(500),
                            gender CHAR(1),
                            bday DATE,
                            country VARCHAR(50),
                            city VARCHAR(50),
                            email VARCHAR(50),
                            joining DATE
                            );""")

    def create_conversation_table(self):
        self.cursor.execute("""CREATE TABLE Conversation (
                            sender_id INTEGER,
                            receiver_id INTEGER,
                            message_id INTEGER,
                            archived VARCHAR(1),
                            unread VARCHAR(1),
                            deleted VARCHAR(1),
                            joining DATE
                            );""")
        self.connection.commit()

    def create_message_table(self):
        self.cursor.execute("""CREATE TABLE Message (
                            message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            text VARCHAR(500),
                            joining DATE
                            );""")

    def create_skill_table(self):
        self.cursor.execute("""CREATE TABLE Skill (
                            skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            skill_name VARCHAR(100),
                            joining DATE
                            );""")

    def create_accomplishment_table(self):
        self.cursor.execute("""CREATE TABLE Accomplishment (
                            accomplishment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            accomplishment_name VARCHAR(100),
                            joining DATE
                            );""")

    def create_featured_table(self):
        self.cursor.execute("""CREATE TABLE Featured (
                            featured_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            featured_name VARCHAR(100),
                            joining DATE
                            );""")

    def create_endorse_table(self):
        self.cursor.execute("""CREATE TABLE Endorse (
                            skill_id INTEGER,
                            user_id INTEGER,
                            endorsement_id INTEGER,
                            joining DATE
                            );""")

    def create_endorsement_table(self):
        self.cursor.execute("""CREATE TABLE Endorsement (
                            endorsement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            message VARCHAR(100),
                            joining DATE
                            );""")

    def create_invitation_table(self):
        self.cursor.execute("""CREATE TABLE Invitation (
                            invitation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sender_id INTEGER,
                            receiver_id INTEGER,
                            result VARCHAR(1),
                            joining DATE
                            );""")

    def add_new_user(self, username, password, first_name, last_name, gender, bday):
        try:
            self.create_user_table()
        except:
            print("table already existed!")

        command = "INSERT INTO User (username, password, fname, lname, gender, bday) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');".format(username, password, first_name, last_name, gender, bday)
        self.cursor.execute(command)
        self.connection.commit()

    def add_new_message(self, text):
        try:
            self.create_message_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Message (text) VALUES ('{0}');".format(text)
        self.cursor.execute(command)
        self.connection.commit()

        command = "SELECT * FROM Message ORDER BY message_id DESC LIMIT 1;"

        self.cursor.execute(command)
        message_id = self.cursor.fetchall()
        return message_id[0][0]


    def add_new_conversation(self, sender, receiver, message_id):
        # AKA send a message
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Conversation (sender_id, receiver_id, message_id, archived, unread, deleted) VALUES ('{0}', '{1}', '{2}', 0, 0, 0 );".format(sender, receiver, message_id)
        self.cursor.execute(command)
        self.connection.commit()

    def add_new_skill(self, user_id, skill_name):
        try:
            self.create_skill_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Skill (user_id, skill_name) VALUES ('{0}', '{1}');".format(user_id, skill_name)
        self.cursor.execute(command)
        self.connection.commit()

    def add_new_accomplishment(self, user_id, accomplishment_name):
        try:
            self.create_accomplishment_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Accomplishment (user_id, accomplishment_name) VALUES ('{0}', '{1}');".format(user_id, accomplishment_name)
        self.cursor.execute(command)
        self.connection.commit()

    def add_new_featured(self, user_id, featured_name):
        try:
            self.create_featured_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Featured (user_id, featured_name) VALUES ('{0}', '{1}');".format(user_id, featured_name)
        self.cursor.execute(command)
        self.connection.commit()

    def add_new_endorse(self, skill_id, user_id, endorsement_id): #should create an Endorsement first then pass its  id to this function
        try:
            self.create_endorse_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Endorse (skill_id, user_id, endorsement_id) VALUES ('{0}', '{1}', '{2}');".format(skill_id, user_id, endorsement_id)
        self.cursor.execute(command)
        self.connection.commit()

    def remove_endorse(self, skill_id, user_id):
        try:
            self.create_endorse_table()
        except:
            print("table already existed!")
        command = "DELETE FROM Endorse WHERE skill_id = '{0}' AND user_id = '{1}'".format(skill_id, user_id)
        self.cursor.execute(command)
        self.connection.commit()

    def is_endorsed(self, skill_id, user_id):
        try:
            self.create_endorse_table()
        except:
            print("table already existed!")

        command = "SELECT * FROM Endorse WHERE skill_id = '{0}' AND user_id = '{1}'".format(skill_id, user_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return len(res)

    def add_new_endorsement(self, mssg):
        try:
            self.create_endorsement_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Endorsement (message) VALUES ('{0}');".format(mssg)
        self.cursor.execute(command)
        self.connection.commit()

    def get_skills(self, userid):
        try:
            self.create_skill_table()
        except:
            print("table already existed!")

        command = "SELECT * FROM Skill WHERE user_id = '{0}'".format(userid)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def get_accomplishments(self, userid):
        try:
            self.create_accomplishment_table()
        except:
            print("table already existed!")

        command = "SELECT * FROM Accomplishment WHERE user_id = '{0}'".format(userid)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def get_featureds(self, userid):
        try:
            self.create_featured_table()
        except:
            print("table already existed!")

        command = "SELECT * FROM Featured WHERE user_id = '{0}'".format(userid)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def remove_a_skill(self, userid, skill_id):
        try:
            self.create_skill_table()
        except:
            print("table already existed!")
        command = "DELETE FROM Skill WHERE user_id = '{0}' AND skill_id = '{1}';".format(userid, skill_id)
        self.cursor.execute(command)
        self.connection.commit()

    def remove_an_accomplishment(self, userid, accomplishment_id):
        try:
            self.create_accomplishment_table()
        except:
            print("table already existed!")
        command = "DELETE FROM Accomplishment WHERE user_id = '{0}' AND accomplishment_id = '{1}';".format(userid, accomplishment_id)
        self.cursor.execute(command)
        self.connection.commit()

    def remove_a_featured(self, userid, featured_id):
        try:
            self.create_featured_table()
        except:
            print("table already existed!")
        command = "DELETE FROM Featured WHERE user_id = '{0}' AND featured_id = '{1}';".format(userid, featured_id)
        self.cursor.execute(command)
        self.connection.commit()

    def login(self, username, password):
        try:
            self.create_user_table()
        except:
            print("table already existed!")

        command = "SELECT * FROM User WHERE username = '{0}' and password = '{1}';".format(username, password)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        if len(res) == 1: # change this to == pls
            return True
        else:
            return False

    def signup(self, username, password):
        try:
            self.create_user_table()
        except:
            print("table already existed!")
        command = "SELECT * FROM User WHERE username = '{0}' and password = '{1}';".format(username, password)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        if len(res) == 0:
            # This username is available
            command = "INSERT INTO User (username, password) VALUES ('{0}', '{1}');".format(username, password)
            self.cursor.execute(command)
            self.connection.commit()
            return True
        else:
            #This username is taken
            return False

    def get_user_information(self, username):
        try:
            self.create_user_table()
        except:
            print("table already existed!")
        command = "SELECT * FROM User WHERE username = '{0}';".format(username)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        if len(res) == 1:
            return res

    def get_username(self, user_id):
        try:
            self.create_user_table()
        except:
            print("table already existed!")
        command = "SELECT * FROM User WHERE user_id = '{0}';".format(user_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        if len(res) == 1:
            return res[0][1]

    def open_conversation(self, sender_id, receiver_id):
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")
        command = "SELECT * FROM Conversation WHERE sender_id = '{0}' and receiver_id = '{1}';".format(sender_id, receiver_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        # returns mssg ids
        return res

    def get_my_contacts(self, user_id):
        try:
            self.create_user_table()
        except:
            print("table already existed!")
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")
        command = "SELECT DISTINCT username, user_id FROM Conversation JOIN User ON Conversation.receiver_id = User.user_id WHERE sender_id = '{0}'".format(user_id)
        command += " UNION  "
        command += "SELECT DISTINCT username, user_id FROM Conversation JOIN User ON Conversation.sender_id = User.user_id WHERE receiver_id = '{0}';".format(user_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def get_a_conversation(self, user_id1, user_id2):
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")
        try:
            self.create_message_table()
        except:
            print("table already existed!")
        command = "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{0}' AND sender_id = '{1}'".format(user_id1, user_id2)
        command += " UNION "
        command += "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{1}' AND sender_id = '{0}'".format(user_id1, user_id2)
        command += " ORDER BY message_id"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def get_archived(self, user_id1, user_id2):
        try:
            self.create_message_table()
        except:
            print("table already existed!")
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")

        command = "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{0}' AND sender_id = '{1}' AND archived = '1'".format(user_id1, user_id2)
        command += " UNION "
        command += "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{1}' AND sender_id = '{0}' AND archived = '1'".format(user_id1, user_id2)
        command += " ORDER BY message_id"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def get_unarchived(self, user_id1, user_id2):
        try:
            self.create_message_table()
        except:
            print("table already existed!")
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")
        command = "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{0}' AND sender_id = '{1}' AND archived = '0'".format(user_id1, user_id2)
        command += " UNION "
        command += "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{1}' AND sender_id = '{0}' AND archived = '0'".format(user_id1, user_id2)
        command += " ORDER BY message_id"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def archive_a_message(self, message_id):
        try:
            self.create_message_table()
        except:
            print("table already existed!")
        command = "UPDATE Conversation SET archived = '1' WHERE message_id = '{0}' ".format(message_id)
        self.cursor.execute(command)
        self.connection.commit()

    def unarchive_a_message(self, message_id):
        try:
            self.create_message_table()
        except:
            print("table already existed!")
        command = "UPDATE Conversation SET archived = '0' WHERE message_id = '{0}'".format(message_id)
        self.cursor.execute(command)
        self.connection.commit()

    def search_in_messages(self, user_id1, user_id2, message_subset):
        try:
            self.create_message_table()
        except:
            print("table already existed!")
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")
        command = "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{0}' AND sender_id = '{1}' AND Message.text like '%{2}%'".format(user_id1, user_id2, message_subset)
        command += " UNION "
        command += "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{1}' AND sender_id = '{0}' AND Message.text like '%{2}%'".format(user_id1, user_id2, message_subset)
        command += " ORDER BY message_id"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def search_in_users(self, username):
        try:
            self.create_user_table()
        except:
            print("table already existed!")
        command = "SELECT * from User WHERE username like '%{0}%'".format(username)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def search_in_users_location(self, location):
        try:
            self.create_user_table()
        except:
            print("table already existed!")
        command = "SELECT * from User WHERE country like '%{0}%' OR City like '%{0}%'".format(location)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def physical_delete_a_message(self, message_id):
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")
        command = "DELETE FROM Conversation WHERE Conversation.message_id = '{0}';".format(message_id)
        self.cursor.execute(command)
        self.connection.commit()

    def add_connection(self, user_id1, user_id2):
        try:
            self.create_invitation_table()
        except:
            print("Table already existed!")

        command = "INSERT INTO Invitation (sender_id, receiver_id, result) VALUES ('{0}', '{1}', 1);".format(user_id1, user_id2)
        self.cursor.execute(command)
        self.connection.commit()

    def send_invitation(self, sender, receiver):
        try:
            self.create_invitation_table()
        except:
            print("Table already existed!")

        command = "INSERT INTO Invitation (sender_id, receiver_id, result) VALUES ('{0}', '{1}', 0);".format(sender, receiver)
        self.cursor.execute(command)
        self.connection.commit()

    def accept_invitation(self, sender_id, receiver_id):
        try:
            self.create_invitation_table()
        except:
            print("Table already existed!")
        command = "UPDATE Invitation SET result = 1 WHERE sender_id = '{0}' AND receiver_id = '{1}'".format(sender_id, receiver_id)
        self.cursor.execute(command)
        self.connection.commit()

    def edit_profile(self, username, password, fname, lname, about, country, city, email, bday):
        try:
            self.create_user_table()
        except:
            print("Table already existed!")
        command = "UPDATE User SET password = '{1}', fname = '{2}', lname = '{3}', about = '{4}', country = '{5}', city = '{6}', email = '{7}', bday = '{8}'  WHERE username = '{0}'".format( username, password, fname, lname, about, country, city, email, bday)
        self.cursor.execute(command)
        self.connection.commit()

    def reject_invitation(self, sender_id, receiver_id):
        try:
            self.create_invitation_table()
        except:
            print("Table already existed!")
        command = "DELETE FROM Invitation WHERE sender_id = '{0}' AND receiver_id = '{1}'".format(sender_id, receiver_id)
        self.cursor.execute(command)
        self.connection.commit()

    def get_my_invitations(self, user_id):
        try:
            self.create_invitation_table()
        except:
            print("Table already existed!")
        command = "SELECT * FROM Invitation WHERE receiver_id = '{0}' AND result = '0'".format(user_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def get_network(self, userid):
        try:
            self.create_invitation_table()
        except:
            print("Table already existed!")

        command = "SELECT * FROM Invitation WHERE sender_id = '{0}' AND result = 1".format(userid)
        command += " UNION "
        command += "SELECT * FROM Invitation WHERE receiver_id = '{0}' AND result = 1".format(userid)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def is_network(self, user_id1, user_id2):
        try:
            self.create_invitation_table()
        except:
            print("Table already existed!")
        command = "SELECT * FROM Invitation WHERE sender_id = '{0}' AND receiver_id = '{1}' AND result = 1 ".format(user_id1, user_id2)
        command += " UNION "
        command += "SELECT * FROM Invitation WHERE sender_id = '{0}' AND receiver_id = '{1}' AND result = 1 ".format(user_id2, user_id1)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return len(res)

    def is_pending(self, user_id1, user_id2):
        try:
            self.create_invitation_table()
        except:
            print("Table already existed!")
        command = "SELECT * FROM Invitation WHERE sender_id = '{0}' AND receiver_id = '{1}' AND result = 0 ".format(user_id1, user_id2)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return len(res)

    def print_user_table(self):
        self.cursor.execute("SELECT * FROM User")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

    def print_message_table(self):
        self.cursor.execute("SELECT * FROM Message")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

    def print_conversation_table(self):
        self.cursor.execute("SELECT * FROM Conversation")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

    def print_invitation_table(self):
        self.cursor.execute("SELECT * FROM Invitation")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

    #Negin start

    def create_post_table(self):
        self.cursor.execute("""CREATE TABLE Post (
                            post_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            image IMAGE,
                            caption TEXT,
                            releaseDate DATE,
                            releaseTime TIME,
                            author_id INTEGER,
                            share_id INTEGER
                            );""")


    def create_comment_table(self):
        self.cursor.execute("""CREATE TABLE Comment (
                            comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            commentText VARCHAR(100),
                            releaseDate DATE,
                            releaseTime TIME
                            );""")


    def create_comment_detail_table(self):
        self.cursor.execute("""CREATE TABLE CommentDetail (
                            CommentPost_id INTEGER,
                            UserID INTEGER,
                            PostID INTEGER
                            );""")

    def delete_comment_tables(self):
        command = "DROP TABLE Comment"
        self.cursor.execute(command)
        self.connection.commit()
        command = "DROP TABLE CommentDetail"
        self.cursor.execute(command)
        self.connection.commit()


    def create_reply_table(self):
        self.cursor.execute("""CREATE TABLE Reply (
                            parentComment_id INTEGER,
                            childComment_id INTEGER,
                            userid INTEGER
                            );""")


    def create_likes_table(self):
        self.cursor.execute("""CREATE TABLE Likes (
                                    user_id INTEGER,
                                    post_id INTEGER
                                    );""")


    def like_a_post(self, post_id, user_id):
        try:
            self.create_likes_table()
        except:
            print("table already existed")
        command = "INSERT INTO Likes (user_id, post_id) VALUES ('{0}', '{1}');".format(user_id, post_id)
        self.cursor.execute(command)
        self.connection.commit()

    def remove_a_like(self, post_id, user_id):
        try:
            self.create_likes_table()
        except:
            print("table already existed")
        command = "DELETE FROM likes WHERE post_id = '{0}' AND user_id = '{1}'".format(post_id, user_id)
        self.cursor.execute(command)
        self.connection.commit()

    def is_liked_a_post(self, post_id, user_id):
        try:
            self.create_likes_table()
        except:
            print("table already existed")
        command = "SELECT * FROM Likes WHERE user_id = '{0}' AND post_id = '{1}'".format(user_id, post_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return len(res)

    def print_likes_table(self):
        command = "SELECT * FROM Likes"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        for rec in res:
            print(rec)

    def share_post(self, post, user1, user2):
        pass


    def add_new_post(self, image, caption, releaseDate, releaseTime, user_id):
        try:
            self.create_post_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Post (image, caption, releaseDate, releaseTime, author_id) VALUES ('{0}', '{1}', '{2}', '{3}', {4});".format(image, caption, releaseDate, releaseTime, user_id)
        self.cursor.execute(command)
        self.connection.commit()

    def get_my_posts(self, user_id):
        try:
            self.create_post_table()
        except:
            print("table already existed!")

        command = "SELECT * FROM Post WHERE author_id = '{0}'".format(user_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def print_post_table(self):
        self.cursor.execute("SELECT * FROM Post")
        table = self.cursor.fetchall()
        for record in table:
            print(record)


        #  ***  NEGIN  ***

    def create_likedComment_table(self):
        self.cursor.execute("""CREATE TABLE LikedComment (
                                    comment_id INTEGER,
                                    userid INTEGER
                                    );""")

    def number_of_likes_of_a_post(self, post_id):
        try:
            self.create_likes_table()
        except:
            print("table already existed")
        command = "SELECT user_id FROM Likes WHERE Likes.post_id = '{0}';".format(post_id)
        self.cursor.execute(command)
        table = self.cursor.fetchall()
        return len(table)

    def add_new_comment(self, text):
        try:
            self.create_comment_table()
        except:
            print("table already existes!")

        command = "INSERT INTO Comment (commentText) VALUES ('{0}');".format(text)
        self.cursor.execute(command)
        self.connection.commit()

        command = "SELECT * FROM Comment ORDER BY comment_id DESC LIMIT 1;"
        self.cursor.execute(command)
        comment_id = self.cursor.fetchall()
        return comment_id[0][0]

    def add_new_comment_detail(self, CommentPost_id, UserID, PostID):
         try:
             self.create_comment_detail_table()
         except:
             print("table already exists!")

         command = "INSERT INTO CommentDetail (CommentPost_id, UserID, PostID) VALUES ('{0}', '{1}', '{2}');".format(CommentPost_id, UserID, PostID)
         self.cursor.execute(command)
         self.connection.commit()

    def add_new_reply(self, parentComment_id, childComment_id, userid):
        try:
            self.create_reply_table()
        except:
            print("table already exists!")

        command = "INSERT INTO Reply (parentComment_id, childComment_id, userid) VALUES ('{0}', '{1}', '{2}');".format(parentComment_id, childComment_id, userid)
        self.cursor.execute(command)
        self.connection.commit()

    def get_a_posts_comments(self, post_id):
        try:
            self.create_comment_table()
        except:
            print("table already existed")
        try:
            self.create_comment_detail_table()
        except:
            print("table already existed")
        command = "SELECT Comment.commentText, CommentDetail.UserID, Comment.comment_id  FROM Comment JOIN CommentDetail ON Comment.comment_id = CommentDetail.CommentPost_id WHERE CommentDetail.PostId = '{0}';".format(post_id)
        self.cursor.execute(command)
        table = self.cursor.fetchall()
        return table

    def get_a_comments_replys(self, comment_id):
        try:
            self.create_comment_table()
        except:
            print("table already existed")
        try:
            self.create_reply_table()
        except:
            print("table already existed")
        command = "SELECT Comment.commentText, Reply.userid, Comment.comment_id FROM Comment JOIN Reply ON Comment.comment_id = Reply.childComment_id WHERE Reply.parentComment_id = '{0}';".format(comment_id)
        self.cursor.execute(command)
        table = self.cursor.fetchall()
        return table

    def is_liked_a_comment(self, comment_id, user_id):
        try:
            self.create_likedComment_table()
        except:
            print("table already exists")
        command = "SELECT * FROM LikedComment WHERE userid = '{0}' AND comment_id = '{1}'".format(user_id, comment_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return len(res)


    def like_a_comment(self, comment_id, user_id):
        try:
            self.create_likedComment_table()
        except:
            print("table already exists")
        command = "INSERT INTO LikedComment (comment_id, userid) VALUES ('{0}', '{1}');".format(comment_id, user_id)
        self.cursor.execute(command)
        self.connection.commit()

    def unlike_a_comment(self, comment_id, user_id):
        try:
            self.create_likedComment_table()
        except:
            print("table already exists")
        command = "DELETE FROM likedComment WHERE comment_id = '{0}' AND userid = '{1}'".format(comment_id, user_id)
        self.cursor.execute(command)
        self.connection.commit()

    def number_of_likes_of_a_comment(self, comment_id):
        try:
            self.create_likedComment_table()
        except:
            print("table already exists")
        command = "SELECT userid FROM LikedComment WHERE LikedComment.comment_id = '{0}';".format(comment_id)
        self.cursor.execute(command)
        table = self.cursor.fetchall()
        return (len(table))

    def get_home_posts(self, user_id):
        try:
            self.create_post_table()
        except:
            print("table already exists")
        try:
            self.create_invitation_table()
        except:
            print("table already exists")
        try:
            self.create_likes_table()
        except:
            print("table already exists")
        try:
            self.create_comment_table()
        except:
            print("table already exists")
        try:
            self.create_comment_detail_table()
        except:
            print("table already exists")

        try:
            command = "CREATE VIEW tmp AS SELECT * FROM Invitation WHERE (sender_id = '{0}' OR receiver_id = '{0}') AND result = 1 ".format(user_id)
            self.cursor.execute(command)
            self.connection.commit()
        except:
            print("table already existed")
        try:
            command = "CREATE VIEW network AS SELECT sender_id FROM tmp UNION SELECT receiver_id FROM tmp"
            self.cursor.execute(command)
            self.connection.commit()
        except:
            print("table already existed")

        command = "DROP VIEW tmp"
        self.cursor.execute(command)
        self.connection.commit()

        command = "DROP VIEW network"
        self.cursor.execute(command)
        self.connection.commit()

        command = "CREATE VIEW tmp AS SELECT * FROM Invitation WHERE (sender_id = '{0}' OR receiver_id = '{0}') AND result = 1 ".format(user_id)
        self.cursor.execute(command)
        self.connection.commit()
        command = "CREATE VIEW network AS SELECT sender_id FROM tmp UNION SELECT receiver_id FROM tmp"
        self.cursor.execute(command)
        self.connection.commit()
        command = "SELECT * FROM network"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        #print(res)
        if len(res) == 0:
            command = "SELECT Post.* FROM Post WHERE author_id = '{0}'".format(user_id)
        else:
            command = "SELECT Post.* FROM network JOIN post ON sender_id = author_id"
        command += " UNION "
        command += "SELECT Post.* FROM network JOIN Likes ON network.sender_id = Likes.user_id JOIN Post ON likes.post_id = Post.post_id"
        command += " UNION "
        command += "SELECT Post.* FROM network JOIN CommentDetail ON network.sender_id = CommentDetail.UserID JOIN Post ON CommentDetail.PostID = Post.post_id"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res


        #  ***  MITRA  ***

    def create_notification_table(self):
        # A table having 3 columns:
        # sender_id, receiver_id, type
        # type -> VARCHAR(1)
        # '1' -> birthday
        # '2' -> profile visit
        # '3' -> like a post
        # '4' -> received comment
        # '5' -> liked or replied comment
        # '6' -> endorsed you
        # '7' -> someone's job changes
        self.cursor.execute("""CREATE TABLE Notification (
                            notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sender_id INTEGER ,
                            receiver_id INTEGER,
                            type VARCHAR(1)
                            );""")

    def add_notification(self, sender_id, receiver_id, type):
        # sender is the one causing the notification
        try:
            self.create_notification_table()
        except:
            print("Table already existed!")

        command = "INSERT INTO Notification (sender_id, receiver_id, type) VALUES ('{0}', '{1}', '{2}');".format(sender_id, receiver_id, type)
        self.cursor.execute(command)
        self.connection.commit()

    def get_notifications(self, user_id):
        try:
            self.create_notification_table()
        except:
            print("Table already existed!")
        try:
            self.create_invitation_table()
        except:
            print("Table already existed!")

        command = "SELECT * FROM Notification WHERE receiver_id = '{0}' ORDER BY notification_id DESC".format(user_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def print_notif_table(self):
        command = "SELECT * FROM Notification"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        for rec in res:
            print(rec)

    def get_people_you_may_know(self, user_id):
        try:
            self.create_invitation_table()
        except:
            print("table already exists")
        try:
            command = "CREATE VIEW tmp AS SELECT * FROM Invitation WHERE (sender_id = '{0}' OR receiver_id = '{0}') AND result = 1 ".format(user_id)
            self.cursor.execute(command)
            self.connection.commit()
        except:
            print("table already existed")
        try:
            command = "CREATE VIEW friendship AS SELECT sender_id, result FROM tmp UNION SELECT receiver_id, result FROM tmp"
            self.cursor.execute(command)
            self.connection.commit()
        except:
            print("table already existed")

        command = "DROP VIEW tmp"
        self.cursor.execute(command)
        self.connection.commit()

        command = "DROP VIEW friendship"
        self.cursor.execute(command)
        self.connection.commit()

        command = "CREATE VIEW tmp AS SELECT * FROM Invitation WHERE result = 1 ".format(user_id)
        self.cursor.execute(command)
        self.connection.commit()
        command = "CREATE VIEW friendship AS SELECT sender_id, receiver_id, result FROM tmp UNION SELECT receiver_id, sender_id, result FROM tmp".format(user_id)
        self.cursor.execute(command)
        self.connection.commit()

        command = "select * from friendship"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        print("\n\nfriendship : ")
        for rec in res:
            print(rec)

        command = """select friendship.sender_id, f2.receiver_id, count(f2.receiver_id) as c
                        from friendship, friendship as f2
                        where friendship.result = 1 and f2.result = 1 and friendship.receiver_id = f2.sender_id and friendship.sender_id != f2.receiver_id
                        and friendship.sender_id = '{0}'
                        Group by friendship.sender_id, f2.receiver_id
                        order by c desc""".format(user_id)

        self.cursor.execute(command)
        res = self.cursor.fetchall()
        # index(0) -> your UserID
        # index(1) -> person you may know user_id
        # index(2) -> number of mutual connections
        print("\n\nPPL U MAY KNOW : ")
        for rec in res:
            print(rec)
        return res

    def search_by_connection(self, user_id):
        # complete it later
        try:
            command = "CREATE VIEW tmp AS SELECT * FROM Invitation WHERE sender_id = '{0}' OR receiver_id = '{0}'".format(user_id)
            self.cursor.execute(command)
            self.connection.commit()
        except:
            print("table already existed")
        try:
            command = "CREATE VIEW friendship AS SELECT sender_id, result FROM tmp UNION SELECT receiver_id, result FROM tmp"
            self.cursor.execute(command)
            self.connection.commit()
        except:
            print("table already existed")

        command = "DROP VIEW tmp"
        self.cursor.execute(command)
        self.connection.commit()

        command = "DROP VIEW friendship"
        self.cursor.execute(command)
        self.connection.commit()

        command = "CREATE VIEW tmp AS SELECT * FROM Invitation WHERE (sender_id = '{0}' OR receiver_id = '{0}')".format(user_id)
        #maybe you have to change this ^

        self.cursor.execute(command)
        self.connection.commit()
        command = "CREATE VIEW friendship AS SELECT sender_id, receiver_id, result FROM tmp UNION SELECT receiver_id, sender_id, result FROM tmp".format(user_id)
        self.cursor.execute(command)
        self.connection.commit()

        command = """select friendship.sender_id, count(friendship.receiver_id) as c
                        from friendship
                        where receiver_id = '{0}'
                        Group by friendship.sender_id
                        order by c desc""".format(user_id)

        self.cursor.execute(command)
        res = self.cursor.fetchall()
        # index(0) -> connected UserID
        # index(1) -> number of mutual connections
        return res

    def get_all_users(self):
        command = "SELECT user_id FROM User"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def search_by_location(self, user_id, location):
        # Have to alter the User table first
        pass



if __name__ == "__main__":
    l = linkedin()
    l.print_user_table()
    # print(l.search_in_users(""))
    # print(l.search_by_connection(2))
    # print(l.get_all_users())
    # l.print_notif_table()
    # print(l.get_notifications(1))
    #print(l.get_skills(1))
    #l.remove_a_skill(1,1)
    # print("invi table :")
