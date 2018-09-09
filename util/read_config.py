from ConfigParser import ConfigParser
def read_config(filename,section):
    """
    Input:
    filename(string):  config filename
    section(string):  section inside the config file
    Description : retrives values under the section
    Output(dictioanry): returns full details in the form of dictionary
    """
    config_dic={}
    try:
        config=ConfigParser()
        config.read(filename)
        print config.items(section)
        config_dic=dict(config.items(section))
        print config_dic
    except Exception,e:
        print e
    return config_dic

data = read_config("config.ini","Information").get("name")
print data
