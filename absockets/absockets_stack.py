from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    #aws_s3 as s3, # Get S3
    aws_servicecatalog_alpha as servicecatalog, # Get Service Catalog Construct from Construct Hub
    aws_iam as iam
)
import aws_cdk
from constructs import Construct

# Resource Name
import os
current_user = os.getlogin()
resourcename = current_user + "-absockets"

class AbsocketsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AbsocketsQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        #
        # bucket = s3.Bucket(self, resourcename, versioned=True,
        #    removal_policy=aws_cdk.RemovalPolicy.DESTROY,
        #    auto_delete_objects=True)
        
        portfolio =servicecatalog.Portfolio(self, "MyFirstPortfolio",
            display_name="MyFirstPortfolio",
            provider_name="MyTeam",
            description="Portfolio for a project",
            message_language=servicecatalog.MessageLanguage.EN
        )

        role = iam.Role(self, "Admin",
            assumed_by=iam.AccountRootPrincipal()
        )
        portfolio.give_access_to_role(role)

        product = servicecatalog.CloudFormationProduct(self, "MyFirstProduct",
            product_name="My Product",
            owner="Product Owner",
            product_versions=[servicecatalog.CloudFormationProductVersion(
                product_version_name="v1",
                cloud_formation_template=servicecatalog.CloudFormationTemplate.from_url("https://raw.githubusercontent.com/awslabs/aws-cloudformation-templates/master/aws/services/ServiceCatalog/Product.yaml")
            )
            ]
        )

