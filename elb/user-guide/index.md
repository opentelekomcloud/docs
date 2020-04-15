# Elastic Load Balance User Guide \(Elastic Load Balancing User Guide\)

-   [Service Overview]
    -   [What Is Elastic Load Balancing?](what-is-elastic-load-balancing.md)
    -   [Product Advantages](product-advantages.md)
    -   [Application Scenarios](application-scenarios.md)
    -   [Differences Between Classic and Enhanced Load Balancers](differences-between-classic-and-enhanced-load-balancers.md)
    -   [How ELB Works](how-elb-works.md)
    -   [Network Type](network-type.md)
    -   [ELB and Other Services](elb-and-other-services.md)
    -   [Product Concepts]
        -   [Basic Concepts](basic-concepts.md)
        -   [Region and AZ](region-and-az.md)


-   [Getting Started]
    -   [Overview](overview.md)
    -   [Using Enhanced Load Balancers — Entry Level](using-enhanced-load-balancers-entry-level.md)
    -   [Using Enhanced Load Balancers — Advanced Level](using-enhanced-load-balancers-advanced-level.md)

-   [Load Balancer]
    -   [Network Type](network-type-0.md)
    -   [Preparing for Creation](preparing-for-creation.md)
    -   [Creating a Load Balancer](creating-a-load-balancer.md)
    -   [Deleting a Load Balancer](deleting-a-load-balancer.md)
    -   [Binding or Unbinding an EIP](binding-or-unbinding-an-eip.md)

-   [Listener]
    -   [Overview](overview-1.md)
    -   [Protocols and Ports](protocols-and-ports.md)
    -   [Load Balancing Algorithms](load-balancing-algorithms.md)
    -   [Sticky Session](sticky-session.md)
    -   [Access Control](access-control.md)
    -   [Adding a Listener](adding-a-listener.md)
    -   [Modifying or Deleting a Listener](modifying-or-deleting-a-listener.md)
    -   [Advanced Settings for HTTP or HTTPS Listeners]
        -   [Forwarding Policy](forwarding-policy.md)
        -   [Mutual Authentication](mutual-authentication.md)
        -   [HTTP Redirection to HTTPS](http-redirection-to-https.md)
        -   [Security Policy](security-policy.md)
        -   [SNI](sni.md)


-   [Backend Server]
    -   [Overview](overview-2.md)
    -   [Configuring Security Group Rules](configuring-security-group-rules.md)
    -   [Adding or Removing Backend Servers from an Enhanced Load Balancer](adding-or-removing-backend-servers-from-an-enhanced-load-balancer.md)
    -   [Adding or Removing Backend Servers from a Classic Load Balancer](adding-or-removing-backend-servers-from-a-classic-load-balancer.md)

-   [Health Check]
    -   [Configuring a Health Check](configuring-a-health-check.md)
    -   [Disabling Health Checks](disabling-health-checks.md)

-   [Certificate]
    -   [Certificate and Private Key Format](certificate-and-private-key-format.md)
    -   [Converting Certificate Formats](converting-certificate-formats.md)
    -   [Creating a Certificate](creating-a-certificate.md)

-   [Tag](tag.md)
-   [Access Logging](access-logging.md)
-   [Monitoring]
    -   [ELB Metrics](elb-metrics.md)
    -   [Setting an Alarm Rule]
        -   [Adding an Alarm Rule](adding-an-alarm-rule.md)
        -   [Modifying an Alarm Rule](modifying-an-alarm-rule.md)

    -   [Viewing Metrics](viewing-metrics.md)

-   [Auditing]
    -   [Key Operations Recorded by CTS](key-operations-recorded-by-cts.md)
    -   [Viewing Traces](viewing-traces.md)

-   [FAQs]
    -   [Questions Summary](questions-summary.md)
    -   [Load Balancer]
        -   [ELB Functionality]
            -   [Should I Adjust the Bandwidth of a Load Balancer Based on the Bandwidth of the Backend Server?](should-i-adjust-the-bandwidth-of-a-load-balancer-based-on-the-bandwidth-of-the-backend-server.md)
            -   [Will I Be Billed for Both the Bandwidth of a Load Balancer and of Backend Servers?](will-i-be-billed-for-both-the-bandwidth-of-a-load-balancer-and-of-backend-servers.md)
            -   [Can ELB Be Used Separately?](can-elb-be-used-separately.md)
            -   [Is the EIP Assigned to a Load Balancer Exclusive?](is-the-eip-assigned-to-a-load-balancer-exclusive.md)
            -   [How Many Load Balancers Can I Create?](how-many-load-balancers-can-i-create.md)
            -   [Can I Adjust the Number of Backend Servers When the Load Balancer is Running?](can-i-adjust-the-number-of-backend-servers-when-the-load-balancer-is-running.md)
            -   [Does ELB Support Servers Running Different OSs?](does-elb-support-servers-running-different-oss.md)
            -   [What Is the Impact of Deleting a Load Balancer?](what-is-the-impact-of-deleting-a-load-balancer.md)
            -   [Can I Adjust the Bandwidth of a Load Balancer?](can-i-adjust-the-bandwidth-of-a-load-balancer.md)
            -   [What Types of Sticky Sessions Does ELB Support?](what-types-of-sticky-sessions-does-elb-support.md)
            -   [How Can I Obtain the Real IP Address of a Client?](how-can-i-obtain-the-real-ip-address-of-a-client.md)

        -   [Service Configuration]
            -   [How Does ELB Distribute Traffic?](how-does-elb-distribute-traffic.md)
            -   [How Can I Create a Public or Private Network Load Balancer?](how-can-i-create-a-public-or-private-network-load-balancer.md)

        -   [Service Abnormality]
            -   [How Can I Rectify the Issue that Sticky Sessions Fail to Take Effect?](how-can-i-rectify-the-issue-that-sticky-sessions-fail-to-take-effect.md)
            -   [How Can I Check that the Traffic from the Frontend and to the Backend Is Inconsistent?](how-can-i-check-that-the-traffic-from-the-frontend-and-to-the-backend-is-inconsistent.md)
            -   [What Should I Do If the Traffic Is Unbalanced?](what-should-i-do-if-the-traffic-is-unbalanced.md)
            -   [What Should I Do If the ELB Performance Fails the Stress Test?](what-should-i-do-if-the-elb-performance-fails-the-stress-test.md)


    -   [Listener]
        -   [What Is the Relationship Between Load Balancing Algorithms and Sticky Session Types?](what-is-the-relationship-between-load-balancing-algorithms-and-sticky-session-types.md)
        -   [How Can ELB Support Multiple Certificates?](how-can-elb-support-multiple-certificates.md)
        -   [How Can I Use WebSocket?](how-can-i-use-websocket.md)

    -   [Backend Server]
        -   [Why Is the Interval That Backend Servers Receive Health Check Packets Is Different from the Configured Interval?](why-is-the-interval-that-backend-servers-receive-health-check-packets-is-different-from-the-configur.md)
        -   [Can Backend Servers Access the Public Network After ELB Is Used?](can-backend-servers-access-the-public-network-after-elb-is-used.md)
        -   [How Can I Check the Network Conditions of a Backend ECS?](how-can-i-check-the-network-conditions-of-a-backend-ecs.md)
        -   [How Can I Check the Network Configuration of a Backend ECS?](how-can-i-check-the-network-configuration-of-a-backend-ecs.md)
        -   [How Can I Check the Status of a Backend ECS?](how-can-i-check-the-status-of-a-backend-ecs.md)
        -   [When Is a Backend Server Considered Healthy?](when-is-a-backend-server-considered-healthy.md)

    -   [Health Check]
        -   [How Do I Troubleshoot an Unhealthy Backend Server?](how-do-i-troubleshoot-an-unhealthy-backend-server.md)
        -   [What Are the Precautions of Using UDP?](what-are-the-precautions-of-using-udp.md)
        -   [Why Does ELB Frequently Send Detection Requests to Backend Servers During Health Checks?](why-does-elb-frequently-send-detection-requests-to-backend-servers-during-health-checks.md)


-   [Appendix]
    -   [Configuring the TOA Plug-in](configuring-the-toa-plug-in.md)
