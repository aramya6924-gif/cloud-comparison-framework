USE_CASES = {
    "Custom Web Application": {
        "description": (
            "A company wants to develop, deploy and maintain "
            "a custom web application."
        ),
        "recommended": "PaaS",

        "weights": {
            "customer_control": 3,
            "scalability": 5,
            "maintenance": 4,
            "deployment_speed": 5,
            "flexibility": 5,
            "security_control": 4,
            "management_effort": 3
        }
    },

    "Off-the-Shelf CRM": {
        "description": (
            "A company wants to use an existing Customer Relationship "
            "Management system without developing the software itself."
        ),
        "recommended": "SaaS",

        "weights": {
            "customer_control": 1,
            "scalability": 4,
            "maintenance": 5,
            "deployment_speed": 5,
            "flexibility": 2,
            "security_control": 3,
            "management_effort": 1
        }
    },

    "Custom Network Infrastructure": {
        "description": (
            "A company needs complete control over servers, networking, "
            "storage, firewalls and infrastructure configuration."
        ),
        "recommended": "IaaS",

        "weights": {
            "customer_control": 5,
            "scalability": 4,
            "maintenance": 2,
            "deployment_speed": 2,
            "flexibility": 5,
            "security_control": 5,
            "management_effort": 5
        }
    }
}


# Illustrative monthly cost estimates in USD.
# These are not live AWS/Azure/GCP prices.

COSTS = {
    "Custom Web Application": {
        "IaaS": {
            "compute": 180,
            "storage": 50,
            "network": 40,
            "management": 120
        },

        "PaaS": {
            "compute": 150,
            "storage": 40,
            "network": 25,
            "management": 40
        },

        "SaaS": {
            "compute": 0,
            "storage": 0,
            "network": 0,
            "management": 0
        }
    },

    "Off-the-Shelf CRM": {
        "IaaS": {
            "compute": 250,
            "storage": 70,
            "network": 50,
            "management": 150
        },

        "PaaS": {
            "compute": 200,
            "storage": 60,
            "network": 40,
            "management": 80
        },

        "SaaS": {
            "compute": 0,
            "storage": 0,
            "network": 0,
            "management": 100
        }
    },

    "Custom Network Infrastructure": {
        "IaaS": {
            "compute": 300,
            "storage": 120,
            "network": 100,
            "management": 200
        },

        "PaaS": {
            "compute": 200,
            "storage": 80,
            "network": 60,
            "management": 100
        },

        "SaaS": {
            "compute": 0,
            "storage": 0,
            "network": 0,
            "management": 150
        }
    }
}