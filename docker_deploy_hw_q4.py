# Week 2 | Homework
# from prefect orion
# import
from prefect.infrastructure.docker import DockerContainer
from prefect.deployments import Deployment
from parametric_web_to_gcs_hw import etl_parent_flow
from prefect.filesystems import GitHub 
from prefect.infrastructure.process import Process

# Set-up Infrastructure
github_block = GitHub.load("prefect-github-block")
docker_block = DockerContainer.load("prefectdockerblock")


# https://docs.prefect.io/api-ref/prefect/deployments/#prefect.deployments.Deployment.build_from_flow
process_block = Process.load("anonymous-89ee9bd3-8200-4882-89a9-6324720b9451")

gsc_git_dep = Deployment.build_from_flow(
    flow=etl_parent_flow,
    name="github-flow-hw-q4",
    storage=github_block,
    infrastructure=docker_block
)

print(
    "Successfully deployed Prefect Github Block. Check Prefect Orion [127.0.0.1:4200] then Deployments"
)

# execute
if __name__ == "__main__":
    gsc_git_dep.apply()

# prefect deployment run etl-web-to-gcs/github-flow-hw-q4 --params '{"color":"green", "year":2019, "month":11}'
