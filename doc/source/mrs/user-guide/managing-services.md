# Managing Services<a name="EN-US_TOPIC_0125375581"></a>

## Scenario<a name="section5382474819236"></a>

On MRS Manager, users can perform the following operations:

-   Start a service that is in the  **Stopped**, **Stopped\_Failed**, or **Start\_Failed**  state.
-   Stop unused or abnormal services.
-   Restart abnormal services or configure expired services to restore or enable the services.

## Procedure<a name="section554138901949"></a>

1.  On MRS Manager, click  **Service**.
2.  Locate the row that contains the target service, click  **Start**, **Stop**,  or **Restart**  to start, stop, or restart the service.

    Services are interrelated. If a service is started, stopped, or restarted, services dependent on it will be affected.

    The services will be affected in the following ways:

    -   If a service is to be started, the lower-layer services dependent on it must be started first.
    -   If a service is stopped, the upper-layer services dependent on it are unavailable.
    -   If a service is restarted, the running upper-layer services dependent on it must be restarted.


