from py2neo import Graph

class App:
    def __init__(self, uri, username, password):
        self.uri = uri
        self.username = username
        self.password = password

    def create_driver(self):

        graph = Graph(self.uri, password=self.password)
        return graph

    def execute_query(self, query):

        return None