# Creating an AS Group<a name="EN-US_TOPIC_0129640296"></a>

## Application Scenarios<a name="section0724445183614"></a>

This template is used to perform the following operations:

-   Create an AS group that contains 1 to 2 ECSs.
-   Create a security group in which ECSs in the AS group are created.

## Example Template<a name="section9684125914360"></a>

```
heat_template_version: 2014-10-16
description: Create an AS instance.
resources:
  auto_scaling_config:
    type: OSE::AS::ScalingConfig
    properties:
      scaling_configuration_name: Scaling Configuration Name
      instance_config:
        key_name: Key Pair
        flavorRef: Flavor ID
        imageRef: Image ID
        disk:
         - disk_type: SYS
           size: 200
           volume_type: SATA
         - disk_type: DATA
           size: 100
           volume_type: SATA
        personality:
         - path: /etc/sample.txt
           content: input_sample_content
        public_ip:
          eip:
            ip_type: 5_bgp
            bandwidth:
              size: 5
              share_type: PER
              charging_mode: traffic
        user_data: sampleTest
        metadata: #NA
          test: sampleTest
  auto_scaling_group:
    type: OSE::AS::ScalingGroup
    properties:
      scaling_group_name: Scaling Group Name
      scaling_configuration_id: { get_resource: auto_scaling_config }
      desire_instance_number: 1
      min_instance_number: 1
      max_instance_number: 2
      cool_down_time: 900
      available_zones:
        - AZ Name
      networks:
        - id: Network ID
      security_groups:
        - id: Security Groups ID
      vpc_id: VPC ID
      health_periodic_audit_method: NOVA_AUDIT
      health_periodic_audit_time: 15
      instance_terminate_policy: OLD_INSTANCE
      delete_publicip: true
```

