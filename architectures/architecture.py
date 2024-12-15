from diagrams import Cluster, Diagram
from diagrams.aws.analytics import AmazonOpensearchService
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.general import User
from diagrams.aws.network import APIGateway

with Diagram('', filename='./images/architecture', show=False):
    user = User('User')
    with Cluster('LocalStack'):
        api = APIGateway('Amazon\nAPI Gateway')
        function = LambdaFunction('AWS\nLambda Function')
        opensearch = AmazonOpensearchService('Amazon\nOpenSearch Service')

    user >> api >> function >> opensearch
