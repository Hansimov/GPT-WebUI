# %%
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.programming.framework import Flask, Vue

with Diagram("architecture", show=False):
    flask = Flask("Flask")
    vue = Vue("Vue")

    flask >> vue
