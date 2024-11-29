import aws_cdk as core
import aws_cdk.assertions as assertions

from 29112024.29112024_stack import 29112024Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in 29112024/29112024_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 29112024Stack(app, "29112024")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
