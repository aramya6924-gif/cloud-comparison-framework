# SaaS vs PaaS vs IaaS — Cloud Service Model Decision Framework

An interactive cloud service-model evaluation and decision-support application that helps organizations compare **IaaS, PaaS, and SaaS** based on technical requirements, operational factors, and estimated monthly cost.

The application uses a weighted scoring system to evaluate each cloud service model for different business scenarios and combines technical analysis with cost estimation to generate a practical recommendation.

---

## 🚀 Project Overview

Selecting the right cloud service model is an important architectural decision for modern organizations.

Different applications require different levels of:

- Infrastructure control
- Customization
- Scalability
- Security control
- Development flexibility
- Deployment speed
- Maintenance effort
- Operational responsibility
- Cost efficiency

Instead of evaluating cloud models only by price, this project provides a multi-criteria comparison framework that considers both **technical suitability and estimated cost**.

The application allows users to select a business scenario, evaluates IaaS, PaaS, and SaaS using predefined criteria and weights, and presents the results through interactive tables and visualizations.

---

## 🎯 Key Goals

The project is designed to:

- Understand the architecture and characteristics of IaaS, PaaS, and SaaS.
- Compare cloud service models using multiple technical parameters.
- Apply different importance weights depending on the business scenario.
- Generate a technical suitability score for each model.
- Estimate the expected monthly cost.
- Compare technical performance with financial considerations.
- Visualize the comparison using interactive charts.
- Recommend the most suitable cloud service model.
- Provide a reusable framework that can be extended to additional scenarios.

---

## ☁️ Cloud Models Evaluated

### 1. Infrastructure as a Service (IaaS)

IaaS provides organizations with configurable computing infrastructure through the cloud.

Typical resources include:

- Virtual machines
- Computing resources
- Storage
- Networking
- Operating systems
- Virtual infrastructure

#### ✅ Strengths

- Maximum infrastructure-level control
- High customization
- Flexible networking
- Support for specialized environments
- Suitable for applications requiring custom infrastructure

#### ⚠️ Limitations

- Higher administrative responsibility
- More infrastructure configuration
- Greater maintenance requirements
- Requires technical expertise
- Higher operational management effort

---

### 2. Platform as a Service (PaaS)

PaaS provides a managed environment for developing, deploying, and running applications.

The cloud provider handles much of the underlying infrastructure, allowing developers to focus on application development.

#### ✅ Strengths

- Faster application development
- Simplified deployment
- Reduced infrastructure management
- Automatic scaling capabilities
- Developer-focused environment

#### ⚠️ Limitations

- Less infrastructure control than IaaS
- Platform-specific limitations
- Potential vendor lock-in
- Migration can become difficult for platform-dependent applications

---

### 3. Software as a Service (SaaS)

SaaS delivers complete software applications through the internet.

Users generally consume the software without managing the underlying infrastructure, operating system, or application platform.

#### ✅ Strengths

- Minimal infrastructure management
- Quick implementation
- Easy accessibility
- Low maintenance requirements
- Suitable for standardized business requirements

#### ⚠️ Limitations

- Limited customization
- Minimal infrastructure control
- Dependence on the service provider
- Recurring subscription costs
- Limited control over application architecture

---

## 📊 Evaluation Framework

The application evaluates each cloud model using multiple technical criteria.

| Criterion | Description |
|---|---|
| Infrastructure Control | Level of control over underlying infrastructure |
| Scalability | Ability to handle changing workloads |
| Flexibility | Ability to customize the environment |
| Deployment Speed | Time and effort required for deployment |
| Maintenance | Infrastructure management responsibility |
| Security Control | Level of control over security configuration |
| Management Effort | Operational effort required |
| Cost | Estimated monthly expenditure |

Each criterion receives a score and an importance weight based on the selected scenario.

---

## 🧮 Weighted Scoring System

The framework uses weighted scoring to calculate technical suitability.

### Formula

```text
Technical Score = Σ (Criterion Score × Criterion Weight)
