# Creating a Load Balancer<a name="EN-US_TOPIC_0129640297"></a>

## Application Scenarios<a name="section3371113418372"></a>

This template is used to create ECSs and a load balancer and add all ECSs to the load balancer.

## Example Template<a name="section2886194303710"></a>

```
heat_template_version: 2014-10-16
description: Create an ELB instance.
resources:
  elb_loadbalancer:
    type: OSE::ELB::LoadBalancer
    properties:
      name: loadbalancer
      vpc_id: VPC ID
      type: External
      bandwidth: 300
      admin_state_up: true
  elb_listener:
    type: OSE::ELB::Listener
    properties:
      name: elb_listener
      loadbalancer_id: { get_resource: elb_loadbalancer }
      protocol: HTTP
      port: 8080
      backend_protocol: HTTP
      backend_port: 8080
      lb_algorithm: leastconn
      sticky_session_type: insert
  elb_healthcheck:
    type: OSE::ELB::HealthCheck
    properties:
      listener_id: { get_resource: elb_listener }
      healthcheck_protocol: HTTP
      healthcheck_timeout: 2
      unhealthy_threshold: 3
      healthcheck_interval: 5
      healthy_threshold: 3
      healthcheck_connect_port: 8080
      healthcheck_uri: /
  elb_member:
    type: OSE::ELB::Member
    properties:
      listener_id: { get_resource: elb_listener }
      members:
        - server_id: { get_resource: nova_server1 }
          address: { get_attr: [nova_server1, first_address] }
  server_port:
    type: OS::Neutron::Port
    properties:
      network: Network Name or ID
  nova_server1:
    type: OS::Nova::Server
    properties:
      name: ECS Name
      image: Image Name or ID
      flavor: Flavor Name
      networks:
        - port: { get_resource: server_port }
      availability_zone: AZ Name
```

