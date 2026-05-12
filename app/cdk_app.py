#!/usr/bin/env python3

import aws_cdk as cdk
from streamlit_ecs_stack import StreamlitEcsStack

app = cdk.App()

env_name = app.node.try_get_context("env") or "dev"
instance_count = int(app.node.try_get_context("instanceCount") or "1")
image_uri = app.node.try_get_context("imageUri")

StreamlitEcsStack(
    app,
    "StreamlitEcsStack",
    env_name=env_name,
    instance_count=instance_count,
    image_uri=image_uri,
    env=cdk.Environment(
        account="493272324412",
        region="us-east-1"
    )
)

app.synth()
