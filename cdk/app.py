#!/usr/bin/env python3

from aws_cdk import core

from stack.api_stack import MyAPIService


app = core.App()
MyAPIService(app, "stack")

app.synth()
