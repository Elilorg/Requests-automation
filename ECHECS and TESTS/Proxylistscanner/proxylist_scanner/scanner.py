
import undetected_chromedriver as uc 
import time
import bs4
import pandas as pd
import json
import requests
import base64
import logging
from .scanners import FreeProxyczScaner, HideMyNameScaner
class Portocols : 
    HTTP = "http"
    HTTPS = "https"
    SOCKET4 = "socket4"
    SOCKET5 = "socket5"
    
class Security : 
    NO = "1"
    LOW = "2"
    AVERAGE = "3"
    HIGH = "4"

user_agent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1847.137 Safari/537.36"

class Scaner : 
    using_selenium  : bool
    using_requests  : bool
    proxylist_url   : str
    proxylist_name  : str

    def scan(self) -> list[dict]: #On veut une liste homogène 
    

        pass

class Proxy(object):
    """
        Proxy is the class for proxy.

        Attributes:
            ip: ip address of proxy
            port: port of proxy
            protocol: protocol of proxy
            speed: speed of proxy
            ping: ping of proxy
            security: security of proxy {1 : Transparant, 2 : Anonymous, 3 : Undetected}



    """

    def __init__(self, ip=None, port=None, protocol=None, speed = None, ping = None, security = None):
        """
        Initialization of the proxy class
        :param ip: ip address of proxy
        :param port: port of proxy
        """
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.speed = speed
        self.ping = ping  
        self.securitty = security
        
   






