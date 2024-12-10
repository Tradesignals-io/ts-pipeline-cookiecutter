"""
This module contains the pipeline for the {{ cookiecutter.pipeline_name }} pipeline.
"""

import json
import logging
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union

from dotenv_derive import dotenv
from lib.consumer import AvroMessageConsumer
from lib.pipeline import PipelineApplication
from lib.producer import AvroMessageProducer
from lib.serializer import AvroMessageSerializer

logger = logging.getLogger({{ cookiecutter.pipeline_name }})
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

@dotenv(coerce_values=True, extras="ignore", env_file="./.env")
class EnvObject:
    kafka_bootstrap_servers: str
    kafka_sasl_password: str
    kafka_sasl_username: str
    kafka_sasl_mechanism: str
    kafka_group_id: str
    kafka_enable_idempotence: bool
    output_type: str
    output_name: str
    output_key_serializer: str
    output_value_serializer: str
    input_type: str
    input_name: str
    input_key_deserializer: str
    input_value_deserializer: str
    schema_registry_url: str
    schema_registry_auth_info: str
    cloud_region: str
    cloud_provider: str
    flink_org_id: str
    flink_env_id: str
    flink_compute_pool: str
    flink_job_name: str
    log_level: str
    log_format: str

print(EnvObject())

# env_object = EnvObject(
#     kafka_bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
#     kafka_sasl_password=os.getenv('KAFKA_SASL_PASSWORD'),
#     kafka_sasl_username=os.getenv('KAFKA_SASL_USERNAME'),
#     kafka_sasl_mechanism=os.getenv('KAFKA_SASL_MECHANISM'),
#     kafka_group_id=os.getenv('KAFKA_GROUP_ID'),
#     kafka_enable_idempotence=os.getenv('KAFKA_ENABLE_IDEMPOTENCE') == 'True',
#     output_type=os.getenv('OUTPUT_TYPE'),
#     output_name=os.getenv('OUTPUT_NAME'),
#     output_key_serializer=os.getenv('OUTPUT_KEY_SERIALIZER'),
#     output_value_serializer=os.getenv('OUTPUT_VALUE_SERIALIZER'),
#     input_type=os.getenv('INPUT_TYPE'),
#     input_name=os.getenv('INPUT_NAME'),
#     input_key_deserializer=os.getenv('INPUT_KEY_DESERIALIZER'),
#     input_value_deserializer=os.getenv('INPUT_VALUE_DESERIALIZER'),
#     schema_registry_url=os.getenv('SCHEMA_REGISTRY_URL'),
#     schema_registry_auth_info=os.getenv('SCHEMA_REGISTRY_AUTH_INFO'),
#     cloud_region=os.getenv('CLOUD_REGION'),
#     cloud_provider=os.getenv('CLOUD_PROVIDER'),
#     flink_org_id=os.getenv('FLINK_ORG_ID'),
#     flink_env_id=os.getenv('FLINK_ENV_ID'),
#     flink_compute_pool=os.getenv('FLINK_COMPUTE_POOL'),
#     flink_job_name=os.getenv('FLINK_JOB_NAME'),
#     log_level=os.getenv('LOG_LEVEL'),
#     log_format=os.getenv('LOG_FORMAT')
# )

app = PipelineApplication({{ cookiecutter.pipeline_name }})
app.set_logger(logger)
app.set_log_level({{ cookiecutter.log_level }})
app.set_config(env_object)

if __name__ == "__main__":
    logger.info("Starting {{ cookiecutter.pipeline_name }} pipeline")
