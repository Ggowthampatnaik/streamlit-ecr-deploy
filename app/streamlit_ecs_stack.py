from aws_cdk import (
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct


class StreamlitEcsStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        env_name: str,
        instance_count: int,
        image_uri: str,
        **kwargs
    ):
        super().__init__(scope, construct_id, **kwargs)

        if not image_uri:
            raise ValueError("imageUri context is required. Pass it using -c imageUri=<ECR_IMAGE_URI>")

        vpc = ec2.Vpc(
            self,
            "StreamlitVpc",
            max_azs=2
        )

        cluster = ecs.Cluster(
            self,
            "StreamlitCluster",
            vpc=vpc
        )

        service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "StreamlitService",
            cluster=cluster,
            cpu=256,
            memory_limit_mib=512,
            desired_count=instance_count,
            public_load_balancer=True,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry(image_uri),
                container_port=8501
            )
        )

        service.target_group.configure_health_check(
            path="/",
            port="8501"
        )

        CfnOutput(
            self,
            "AppURL",
            value=f"http://{service.load_balancer.load_balancer_dns_name}"
        )
