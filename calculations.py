from cloud_models import CLOUD_MODELS


def calculate_score(model_name, weights):
    """
    Calculate the weighted technical score
    for a cloud service model.
    """

    model = CLOUD_MODELS[model_name]

    attributes = [
        "customer_control",
        "scalability",
        "maintenance",
        "deployment_speed",
        "flexibility",
        "security_control",
        "management_effort"
    ]

    total_score = 0
    total_weight = 0

    for attribute in attributes:
        value = getattr(model, attribute)
        weight = weights.get(attribute, 1)

        total_score += value * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return round(total_score / total_weight, 2)


def calculate_cost(cost_data):
    """
    Calculate total estimated monthly cost.
    """

    return sum(cost_data.values())


def calculate_all_scores(weights):
    """
    Calculate scores for IaaS, PaaS and SaaS.
    """

    scores = {}

    for model_name in CLOUD_MODELS:
        scores[model_name] = calculate_score(
            model_name,
            weights
        )

    return scores


def get_best_model(scores):
    """
    Return the model with the highest technical score.
    """

    return max(
        scores,
        key=scores.get
    )