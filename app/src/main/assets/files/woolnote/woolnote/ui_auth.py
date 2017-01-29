from woolnote import util
from woolnote import config

# UI authentication helper
##########################

class WoolnoteUIAuth():
    def __init__(self):
        # TODO docstring
        self.authenticated_cookie = util.create_id_task()
        self.one_time_pwd = util.generate_one_time_pwd()
        self.one_time_pwd_tries_left = 0
        self.ONE_TIME_PWD_TRIES = 5

    def return_cookie_authenticated(self):
        # TODO docstring
        return self.authenticated_cookie

    def create_new_one_time_pwd(self):
        # TODO docstring
        """Creates a new one-time password and sets how many tries are left."""
        self.one_time_pwd = util.generate_one_time_pwd()
        self.one_time_pwd_tries_left = self.ONE_TIME_PWD_TRIES
        return self.one_time_pwd

    def check_one_time_pwd(self, user_supplied_pwd):
        # TODO docstring
        x = """Checks whether the supplied one-time password is correct, only if tries are left.
            Password is disabled after 1st successful use.
        """
        self.one_time_pwd_tries_left -= 1
        if self.one_time_pwd_tries_left > 0:
            ret = util.safe_string_compare(user_supplied_pwd, self.one_time_pwd)
            if ret is True:  # explicitly checking for boolean True
                # successful use, prohibit subsequent (e.g. attacker reading screen)
                self.one_time_pwd_tries_left = 0
                return True
            return False
        return False

    def check_permanent_pwd(self, user_supplied_pwd):
        # TODO docstring
        ret = util.safe_string_compare(user_supplied_pwd, config.LOGIN_PASSWORD)
        if ret is True:  # explicitly checking for boolean True
            return True
        return False


        # TODO: method for checking the permanent password
        # TODO: save the permanent password as a hash?
