# EPAM Delivery Platform (EDP) Cluster Add-ons Repository

This repository contains a collection of pre-configured solutions (add-ons) for Kubernetes cluster. It follows the GitOps methodology and utilizes the ArgoCD App of Apps pattern for streamlined configuration and deployment.

The repository offers a variety of Kubernetes add-ons that can be easily integrated into Kubernetes cluster, whether running on Openshift or any other Managed Kubernetes distribution. These add-ons enhance cluster capabilities and provide additional functionalities for the EPAM Delivery Platform (EDP).

Using ArgoCD, one can leverage the repository to expedite the setup process of the EPAM Delivery Platform (EDP) and cluster components. The repository provides ready-to-use configurations for add-ons, simplifying deployment and reducing complexity.

Explore this repository to access a comprehensive collection of Kubernetes add-ons for your Kubernetes. Simplify deployment, enhance cluster capabilities, and stay up-to-date with the evolving landscape of Kubernetes.

## Repository structure

* `add-ons` - contains the source code of the Add Ons in the form of the Helm charts
* `chart` - contains the Helm chart that uses Apps of Apps pattern and contains ArgoCD Application CRs

```bash
.
├── add-ons
│   ├── argocd
│   ├── aws-efs-csi-driver
│   ├── cert-manager
...
│   ├── tekton
│   └── vault
└── chart
    ├── Chart.yaml
    ├── README.md
    ├── templates
    │   ├── argocd.yaml
    │   ├── aws-efs-csi-driver.yaml
    │   ├── cert-manager.yaml
...
    │   ├── tekton.yaml
    │   └── vault.yaml
    └── values.yaml
    └── values.yaml
```

## Available add-ons

Check out the list of available add-ons in the [chart](./chart/README.md) directory.

```bash
make update-readme
```

<!-- AUTOGENERATED CONTENT BELOW -->
| Component              | createNamespace   | enable   |
|:-----------------------|:------------------|:---------|
| argo-cd                | False             | False    |
| aws-efs-csi-driver     | N/A               | False    |
| capsule                | False             | False    |
| capsule-tenant         | N/A               | False    |
| certmanager            | False             | False    |
| defectdojo             | False             | False    |
| dependency-track       | False             | False    |
| edp                    | False             | False    |
| extensions-oidc        | False             | False    |
| external-secrets       | False             | False    |
| fluent-bit             | False             | False    |
| harbor                 | False             | False    |
| harbor-ha              | False             | False    |
| harbor-ha-okd          | False             | False    |
| ingress-nginx          | False             | False    |
| jaeger-operator        | False             | False    |
| keycloak               | False             | False    |
| keycloak-postgresql    | False             | False    |
| minio-operator         | False             | False    |
| nexus                  | False             | False    |
| nexus-operator         | False             | False    |
| opensearch             | False             | False    |
| opentelemetry-operator | False             | False    |
| postgres-operator      | False             | False    |
| prometheus-operator    | False             | False    |
| redis-operator         | False             | False    |
| sonar                  | False             | False    |
| sonar-operator         | False             | False    |
| storage-class          | N/A               | False    |
| tekton-cache           | True              | True     |
| tekton                 | False             | False    |
| vault                  | False             | False    |
| vault-kms              | False             | False    |
| vault-okd              | False             | False    |
