import configparser

def load(confPath,profileName):
    # Read the profile file
    profile = configparser.ConfigParser()
    profile.read(confPath + '/profiles/' + profileName[0] + '.conf')
    return profile