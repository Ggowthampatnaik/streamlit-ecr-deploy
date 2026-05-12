from aws_cdk import App, Stack

app = App()

Stack(app, "TestStack")

app.synth()
