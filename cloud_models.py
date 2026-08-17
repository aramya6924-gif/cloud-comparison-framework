from dataclasses import dataclass


@dataclass
class CloudModel:
    name: str
    description: str
    customer_control: int
    scalability: int
    maintenance: int
    deployment_speed: int
    flexibility: int
    security_control: int
    management_effort: int


IaaS = CloudModel(
    name="IaaS",
    description=(
        "Infrastructure as a Service provides virtual machines, "
        "networking, storage and other infrastructure resources."
    ),
    customer_control=5,
    scalability=4,
    maintenance=2,
    deployment_speed=2,
    flexibility=5,
    security_control=5,
    management_effort=5
)


PaaS = CloudModel(
    name="PaaS",
    description=(
        "Platform as a Service provides a managed platform "
        "for developing and deploying applications."
    ),
    customer_control=3,
    scalability=5,
    maintenance=4,
    deployment_speed=5,
    flexibility=4,
    security_control=4,
    management_effort=2
)


SaaS = CloudModel(
    name="SaaS",
    description=(
        "Software as a Service provides ready-to-use software "
        "through the internet."
    ),
    customer_control=1,
    scalability=4,
    maintenance=5,
    deployment_speed=5,
    flexibility=2,
    security_control=3,
    management_effort=1
)


CLOUD_MODELS = {
    "IaaS": IaaS,
    "PaaS": PaaS,
    "SaaS": SaaS
}