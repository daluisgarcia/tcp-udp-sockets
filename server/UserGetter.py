import os

class UserGetter:
    def __init__(self) -> None:
        self.filename = os.path.abspath('server\\usuarios mini aplicacion.txt')
        pass

    def searchUser(self, userName) -> str:
        # Read the users file
        usersFile = open(self.filename, 'r', encoding = 'utf8')
        # Convert file to an array of strings
        usersArray = usersFile.read().splitlines() #puts the file into an array
        usersFile.close()
        # Validate if the user name exists
        try:
            usersArray.index(userName)
            return "OK"
        except ValueError as e:
            return "Usuario inexistente"