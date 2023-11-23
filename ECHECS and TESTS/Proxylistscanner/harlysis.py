import json

def crer_communications(filename) : 
    with open(filename, "r") as file : 
        list_of_communications = json.load(file)["log"]["entries"]

    return [Communication(dic) for dic in list_of_communications]

if __name__ == "__main__":

    file1 = open("./HAR Files\YOPMAILHAR1", "rb")
    file2 = open("./HAR Files\YOPMAILHAR2", "rb")

    list_of_communications1 = json.load(file1)["log"]["entries"]
    list_of_communications2 = json.load(file2)["log"]["entries"]

    #str_requests1 = str(list_requests1)
    #str_requests1 = str(list_requests2)

    # clear le fichier
    output = open("output.txt", "w")
    output.close()

    # ouvre le fichier
    output = open("output.txt", "a")

    # pour la transfo de la string cooke en dict


def format_cookies(cookies_str : str) -> dict: 
    """Parses a string of cookies and returns a dictionary of cookie key-value pairs.

    Args:
        cookies_str: A string of cookies in the format "key1=value1; key2=value2; ..."

    Returns:
        A dictionary of cookie key-value pairs.

    Example:
        >>> format_cookies("name=John; age=30; location=New York")
        {'name': 'John', 'age': '30', 'location': 'New York'}
    """

    new_cookies = {}
    for cookie in cookies_str.split(";"):
        cookie = cookie.split("=")
        new_cookies[cookie[0]] = cookie[1]
    return new_cookies

# transforme la liste de header en dictionnaire cle/valeur


def traitement_dictionnaire(header: list[dict]) -> dict:
    """
    Take a list of dictionary headers and return a new dictionary with formatted cookies.

    Args:
        header (list[dict]): A list of dictionaries where each dictionary represents a header.

    Returns:
        dict: A new dictionary with formatted cookies.

    Example:
        >>> header = [{"name": "Cookie", "value": "flavor=chocolate; brand=Oreo"},
                      {"name": "User-Agent", "value": "Mozilla/5.0"}]
        >>> traitement_dictionnaire(header)
        {'Cookie': 'flavor=chocolate; brand=Oreo', 'User-Agent': 'Mozilla/5.0'}
    """
    
    new_headers = {}
    for i in header:
        if i["name"] == "Cookie" or i["name"] == "cookies":
            new_headers[i["name"]] = format_cookies(i["value"])
        else:
            new_headers[i["name"]] = i["value"]
    return new_headers


requests = True
response = False
only_requests = True
only_response = False

# On choisis si on ne veux analiser que les requetes ou seulement les réponses etc...
# On applique le traitement des headers et autres

class Communication() : 
    def __init__(self, raw_dic) :
        self.request = Request(raw_dic["request"])
        self.response = Response(raw_dic["response"])

        self.dic_rep = raw_dic
        self.dic_rep["request"] = self.request.dic_rep
        self.dic_rep["response"] = self.response.dic_rep

class Request() : 
    def __init__(self, raw_dic) : 
        self.dic_rep = self.format_dic(raw_dic)
        self.method = self.dic_rep["method"]
        self.url = self.dic_rep["url"]

    


    def format_dic(self, dic):
        request_headers = traitement_dictionnaire(dic["headers"])
        request_querys = traitement_dictionnaire(dic["queryString"])
        request_cookies = traitement_dictionnaire(dic["cookies"])

        dic["headers"] = request_headers
        dic["queryString"] = request_querys
        dic["cookies"] = request_cookies
        

        return dic
    

class Response() : 
    def __init__(self, raw_dic) : 
        self.dic_rep = self.format_dic(raw_dic)
        self.status = self.dic_rep["status"]
        self.content = self.dic_rep["content"]

    
    def format_dic(self, dic):
        request_headers = traitement_dictionnaire(dic["headers"])
        request_cookies = traitement_dictionnaire(dic["cookies"])

        dic["headers"] = request_headers
        dic["cookies"] = request_cookies
        

        return dic

        







class List_of_communications() : 
    def __init__(self, list_of_communications, requests=True, response=True, only_requests=False, only_response=False):
        self.requests = requests
        self.response = response
        self.only_requests = only_requests
        self.only_response = only_response
        self.list_requests = list_of_communications 
        self.traitement()

    def compare(self, list2):
        list_comparaison(self.list_requests, list2)


    def traiter_communication(self, communication):

        communication_instance = Communication(communication)


        if self.only_requests:
            communication_instance.dic_rep = communication_instance.dic_rep["request"]
            return communication_instance
        
        if self.only_response:
            communication_instance.dic_rep =  {'request':  
                        {'url': communication_instance.request.url, 
                        'method': communication_instance.request.method}, 
                    'response': communication_instance.response.dic_rep} 
            return communication_instance
        if not self.requests : 
            communication_instance.dic_rep["request"] = None


        if not self.response:
            communication_instance.dic_rep["response"] = None

        return communication_instance

    def traitement(self):
        self.list_of_communication_objects= []

        for index, communication in enumerate(self.list_requests):

            communication_object = self.traiter_communication(communication)
            self.list_of_communication_objects.append(communication_object)

    








########### INUTILE #############


def list_comparaison(list1, list2):
    for index, requete1 in enumerate(list1):
        requete2 = list2[index]
        url1 = requete1["request"]["url"]
        url2 = requete2["request"]["url"]

        compare_dict(requete1, requete2, [index])

# On a 2 valeurs différente


def different_values_comparaison(value1, value2, new_path):
    if type(value1) == type(value2) == type({}):

        compare_dict(value1, value2, new_path)

    elif type(value1) == type(value2) == type([]):
        compare_list(value1, value2, new_path)

    else:
        if len(str(value1)) < 1000 and len(str(value2)) < 1000:
            print(f"{value1}, {value2}, {new_path}")
            output.write(f"{value1}, {value2}, {new_path}\n")
        else:
            print(new_path)
            output.write(str(new_path) + '\n')


def compare_dict(dic1, dic2, path):
    every_keys = list(set(list(dic1.keys()) + list(dic2.keys())))
    # print(every_keys)
    for key in every_keys:
        value1 = dic1.get(key)
        value2 = dic2.get(key)
        new_path = path + [key]
        if value2 == value1:
            pass
            
        else:
            different_values_comparaison(value1, value2, new_path)


def compare_list(list1, list2, path=[]):
    # A améliorer si il y a une longeur de liste différente
    for index in range(min(len(list1), len(list2))):
        value1 = list1[index]
        value2 = list2[index]
        new_path = path + [index]
        if value2 == value1:
            #print("RAS",  new_path)
            pass
        else:
            different_values_comparaison(value1, value2, new_path)







if __name__ == "__main__":
    list_requests1, list_requests2 = [], []
    for n, communication_object in enumerate(list_requests1.list_of_communication_objects):
        communication_object1 = communication_object
        communication_object2 = list_requests2.list_of_communication_objects[n]

        string_enter = f"Requete n° {n}, avec url : {communication_object1.request.url} ou {communication_object2.request.url}"
        print(string_enter)
        output.write(string_enter + '\n')

        print()
        output.write('\n')

        compare_dict(communication_object1.dic_rep, communication_object2.dic_rep, [])

        print()
        output.write("\n")



