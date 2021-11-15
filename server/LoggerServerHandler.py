from server.LogWritter import LogWritter
from server.UserGetter import UserGetter

class LoggerServerHandler:
    def __init__(self) -> None:
        self.usersLogged = []

    def validateMessageStructure(self, message) -> dict:
        structuredMessage = {
            "user": None,
            "message": None
        }
        splitted = message.split()
        if (len(splitted) == 2 and splitted[0] == 'helloiam'):
            structuredMessage = {
                "user": splitted[1],
                "message": None
            }
        elif (len(splitted) > 2):                    
            structuredMessage = {
                "user": splitted[0],
                "message": ' '.join(splitted[1:])
            }
        
        return structuredMessage

    def validateUserAndWriteLog(self, userMessage, protocol, userAddress) -> str:
        # Validating the user exists
        structuredMessage = self.validateMessageStructure(userMessage)
        if (not structuredMessage['user'] and not structuredMessage['message']):
            return 'Formato de mensaje incorrecto'
        userGetter = UserGetter()
        msgFromServer = userGetter.searchUser(structuredMessage['user'])
        if (msgFromServer == 'OK'):
            # Verifies if user is logged or not
            try:
                self.usersLogged.index(structuredMessage['user'])
                # The user exists
                print('The user is already logged')
                if not structuredMessage['message']:
                    return 'Formato de mensaje incorrecto'
                # Write a LOG file with message
                logger = LogWritter()
                logger.writeProtocolLog(structuredMessage['user'], structuredMessage['message'], userAddress, protocol)
                return 'Mensaje escrito en logs con exito'
            except ValueError as e:
                # Save the user as logged in
                self.usersLogged.append(structuredMessage['user'])
                print('The user is now logged')
                return 'OK'
        else:
            # Write error log file
            logger = LogWritter()
            error = 'Usuario inexistente'
            logger.writeProtocolLog(structuredMessage['user'], 'Usuario inexistente', userAddress, protocol, True)
            return error