# Migrating Applications<a name="cce_01_9995"></a>

This section describes how to create a Deployment with the same specifications as that in CCE 1.0 on the CCE 2.0 console.

It is advised to delete the applications on CCE 1.0 only after you have successfully created these applications on CCE 2.0.

## Before Migration<a name="section468148175110"></a>

Common Kubernetes resources include Deployments, StatefulSets, jobs, DaemonSets, pods, ConfigMaps, secrets, and Services. To migrate applications, export the Kubernetes resources from CCE 1.0 and create them on the CCE 2.0 clusters.

## Procedure<a name="section18998418513"></a>

1.  <a name="li156087595210"></a>Export resource files from CCE 1.0.

    **kubectl get **_\{resource\} \{name\}_** -n **_\{namespace\}_** -oyaml --export \> **_\{namespace\}\_\{resource\}\_\{name\}_**.yaml**

    Assume that the following resource files are exported:

    **kubectl get svc app-svc-test -ndefault -oyaml --export \> default\_svc\_app-svc-test.yaml**

    **kubectl get secret secret-test -ndefault -oyaml --export \> default\_secret\_secret-test.yaml**

    **kubectl get cm cm-test -ndefault -oyaml --export \> default\_cm\_cm-test.yaml**

2.  Switch to the CCE 2.0 clusters and run the following kubectl command to create the resources exported in  [1](#li156087595210).

    **kubectl create -f**_\{namespace\}\_\{resource\}\_\{name\}_**.yaml**

    Examples of creating resource files:

    **kubectl create -f default\_svc\_app-svc-test.yaml**

    **kubectl create -f default\_secret\_secret-test.yaml**

    **kubectl create -f default\_cm\_cm-test.yaml**

3.  In CCE 1.0, the application type is ReplicationController, which needs to be changed into Deployment in CCE 2.0.

    To change the application type, replace ReplicationController in the ReplicationController YAML file exported from CCE 1.0 with Deployment.

    Assume that the ReplicationController YAML file exported is as follows:

    ```
    apiVersion: v1
    kind: ReplicationController
    metadata:
    annotations:
    cce/app-createTimestamp: 2019-09-09-08-59-13
    cce/app-description: ""
    cce/app-updateTimestamp: 2019-09-09-08-59-13
    creationTimestamp: null
    generation: 1
    labels:
    cce/appgroup: app-test
    name: ssss
    rollingupdate: "false"
    name: ssss
    selfLink: /api/v1/namespaces/default/replicationcontrollers/ssss
    spec:
    replicas: 1
    selector:
    cce/appgroup: app-test
    name: ssss
    rollingupdate: "false"
    template:
    metadata:
    annotations:
    scheduler.alpha.kubernetes.io/affinity: '{"nodeAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":{"nodeSelectorTerms":[{"matchExpressions":[{"key":"failure-domain.beta.kubernetes.io/zone","operator":"In","values":["eu-de-02","eu-de-01"]}]}]}}}'
    creationTimestamp: null
    labels:
    cce/appgroup: app-test
    name: ssss
    rollingupdate: "false"
    spec:
    affinity:
    nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    nodeSelectorTerms:
    - matchExpressions:
    - key: failure-domain.beta.kubernetes.io/zone
    operator: In
    values:
    - eu-de-02
    - eu-de-01
    containers:
    - args:
    - "360000"
    command:
    - sleep
    image: 10.125.1.72:6443/otc00000000001000010000/busybox:latest
    imagePullPolicy: Always
    name: container01
    ports:
    - containerPort: 80
    protocol: TCP
    resources: {}
    securityContext:
    privileged: true
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    dnsPolicy: ClusterFirst
    imagePullSecrets:
    - name: myregistry
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    terminationGracePeriodSeconds: 30
    status:
    replicas: 0
    ```

    Replace the content in bold in the preceding YAML file to generate a YAML file for Deployments in CCE 2.0.

    ```
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      annotations:
        cce/app-createTimestamp: 2019-09-09-08-59-13
        cce/app-description: ""
        cce/app-updateTimestamp: 2019-09-09-08-59-13
      creationTimestamp: null
      generation: 1
      labels:
        cce/appgroup: app-test
        name: ssss
        rollingupdate: "false"
      name: ssss
      selfLink: /api/v1/namespaces/default/replicationcontrollers/ssss
    spec:
      replicas: 1
      selector:
      matchLabels:
        cce/appgroup: app-test
      template:
      metadata:
        annotations:
          scheduler.alpha.kubernetes.io/affinity: '{"nodeAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":{"nodeSelectorTerms":[{"matchExpressions":[{"key
    ":"failure-domain.beta.kubernetes.io/zone","operator":"In","values":["eu-de-02","eu-de-01"]}]}]}}}'
        creationTimestamp: null
        labels:
          cce/appgroup: app-test
        name: ssss
        rollingupdate: "false"
      spec:
        affinity:
          nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
              - matchExpressions:
                - key: failure-domain.beta.kubernetes.io/zone
                  operator: In
                  values:
                    - eu-de-02
                    - eu-de-01
        containers:
            - args:
          - "360000"
        command:
          - sleep
        image: 10.125.7.25:20202/otc00000000001000010000/busybox:latest
        imagePullPolicy: Always
        name: container01
        ports:
            - containerPort: 80
        protocol: TCP
        resources: {}
        securityContext:
        privileged: true
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        imagePullSecrets:
            - name: default-secret
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
        status:
          replicas: 0
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Rectify errors as prompted during cluster upgrading. If you have any questions, contact O&M personnel.  


