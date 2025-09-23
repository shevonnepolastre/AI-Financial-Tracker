targetScope = 'resourceGroup'

@description('Deployment location')
param location string = resourceGroup().location

@description('Container App name')
param containerAppName string = 'financialapp'

@description('ACR name (must be globally unique)')
param acrName string = 'aifinancialregistry'

@description('ACR SKU')
@allowed([
  'Basic'
  'Standard'
  'Premium'
])
param acrSku string = 'Basic'

@description('Container image tag')
param imageTag string = 'latest'

@description('CPU cores for container')
param cpuCores int = 1

@description('Memory for container (GiB)')
param memory string = '2Gi'

// Deploy Azure Container Registry
module acr './modules/acr.bicep' = {
  name: 'deploy-acr'
  params: {
    acrName: acrName
    location: location
    acrSku: acrSku
  }
}

// Reference the ACR as an existing resource for role assignment scope
resource acrResource 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' existing = {
  name: acrName
}

// Deploy Managed Environment for Container Apps
resource containerEnv 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: '${containerAppName}-env'
  location: location
  properties: {}
}

// Deploy Container App with system-assigned identity
resource containerApp 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    managedEnvironmentId: containerEnv.id
    configuration: {
      registries: [
        {
          server: acr.outputs.loginServer
          identity: 'system'
        }
      ]
      ingress: {
        external: true
        targetPort: 8000
      }
    }
    template: {
      containers: [
        {
          name: containerAppName
          image: '${acr.outputs.loginServer}/financial-tracker:${imageTag}'
          resources: {
            cpu: cpuCores
            memory: memory
          }
        }
      ]
    }
  }
}

// Role assignment so Container App can pull from ACR
resource acrRoleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(containerApp.id, 'acrpull')
  scope: acrResource
  properties: {
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      '7f951dda-4ed3-4680-a7ca-43fe172d538d' // AcrPull built-in role
    )
    principalId: containerApp.identity.principalId
    principalType: 'ServicePrincipal'
  }
}

// Output Container App FQDN for convenience
output containerAppUrl string = containerApp.properties.configuration.ingress.fqdn
