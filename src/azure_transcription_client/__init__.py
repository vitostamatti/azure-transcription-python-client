# coding: utf-8

# flake8: noqa

"""
    Speech to Text API v3.0

    Speech to Text API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

__version__ = "0.1.0"
# import apis into sdk package
from azure_transcription_client.api.default_api import DefaultApi

# import ApiClient
from azure_transcription_client.api_client import ApiClient
from azure_transcription_client.configuration import Configuration

# import models into sdk package
from azure_transcription_client.models.api_speechtotext_v30_datasets_locales_get200_application_json_response import (
    ApiSpeechtotextV30DatasetsLocalesGet200ApplicationJsonResponse,
)
from azure_transcription_client.models.api_speechtotext_v30_endpoints_locales_get200_application_json_response import (
    ApiSpeechtotextV30EndpointsLocalesGet200ApplicationJsonResponse,
)
from azure_transcription_client.models.api_speechtotext_v30_evaluations_locales_get200_application_json_response import (
    ApiSpeechtotextV30EvaluationsLocalesGet200ApplicationJsonResponse,
)
from azure_transcription_client.models.api_speechtotext_v30_models_locales_get200_application_json_response import (
    ApiSpeechtotextV30ModelsLocalesGet200ApplicationJsonResponse,
)
from azure_transcription_client.models.api_speechtotext_v30_projects_locales_get200_application_json_response import (
    ApiSpeechtotextV30ProjectsLocalesGet200ApplicationJsonResponse,
)
from azure_transcription_client.models.api_speechtotext_v30_transcriptions_locales_get200_application_json_response import (
    ApiSpeechtotextV30TranscriptionsLocalesGet200ApplicationJsonResponse,
)
from azure_transcription_client.models.component import Component
from azure_transcription_client.models.dataset import Dataset
from azure_transcription_client.models.dataset_properties import DatasetProperties
from azure_transcription_client.models.dataset_update import DatasetUpdate
from azure_transcription_client.models.endpoint import Endpoint
from azure_transcription_client.models.endpoint_links import EndpointLinks
from azure_transcription_client.models.endpoint_properties import EndpointProperties
from azure_transcription_client.models.endpoint_properties_update import (
    EndpointPropertiesUpdate,
)
from azure_transcription_client.models.endpoint_update import EndpointUpdate
from azure_transcription_client.models.entity_error import EntityError
from azure_transcription_client.models.entity_reference import EntityReference
from azure_transcription_client.models.error import Error
from azure_transcription_client.models.error_content import ErrorContent
from azure_transcription_client.models.error_detail import ErrorDetail
from azure_transcription_client.models.evaluation import Evaluation
from azure_transcription_client.models.evaluation_properties import EvaluationProperties
from azure_transcription_client.models.evaluation_update import EvaluationUpdate
from azure_transcription_client.models.file import File
from azure_transcription_client.models.file_links import FileLinks
from azure_transcription_client.models.file_properties import FileProperties
from azure_transcription_client.models.health_status import HealthStatus
from azure_transcription_client.models.inner_error import InnerError
from azure_transcription_client.models.inner_error_v2 import InnerErrorV2
from azure_transcription_client.models.internal_model import InternalModel
from azure_transcription_client.models.links import Links
from azure_transcription_client.models.management_model import ManagementModel
from azure_transcription_client.models.management_model_array import (
    ManagementModelArray,
)
from azure_transcription_client.models.management_model_properties import (
    ManagementModelProperties,
)
from azure_transcription_client.models.model import Model
from azure_transcription_client.models.model_copy import ModelCopy
from azure_transcription_client.models.model_deprecation_dates import (
    ModelDeprecationDates,
)
from azure_transcription_client.models.model_file import ModelFile
from azure_transcription_client.models.model_links import ModelLinks
from azure_transcription_client.models.model_manifest import ModelManifest
from azure_transcription_client.models.model_properties import ModelProperties
from azure_transcription_client.models.model_update import ModelUpdate
from azure_transcription_client.models.paginated_datasets import PaginatedDatasets
from azure_transcription_client.models.paginated_endpoints import PaginatedEndpoints
from azure_transcription_client.models.paginated_evaluations import PaginatedEvaluations
from azure_transcription_client.models.paginated_files import PaginatedFiles
from azure_transcription_client.models.paginated_models import PaginatedModels
from azure_transcription_client.models.paginated_projects import PaginatedProjects
from azure_transcription_client.models.paginated_transcriptions import (
    PaginatedTranscriptions,
)
from azure_transcription_client.models.paginated_web_hooks import PaginatedWebHooks
from azure_transcription_client.models.project import Project
from azure_transcription_client.models.project_links import ProjectLinks
from azure_transcription_client.models.project_properties import ProjectProperties
from azure_transcription_client.models.project_update import ProjectUpdate
from azure_transcription_client.models.transcription import Transcription
from azure_transcription_client.models.transcription_properties import (
    TranscriptionProperties,
)
from azure_transcription_client.models.transcription_update import TranscriptionUpdate
from azure_transcription_client.models.web_hook import WebHook
from azure_transcription_client.models.web_hook_events import WebHookEvents
from azure_transcription_client.models.web_hook_events1 import WebHookEvents1
from azure_transcription_client.models.web_hook_links import WebHookLinks
from azure_transcription_client.models.web_hook_properties import WebHookProperties
from azure_transcription_client.models.web_hook_properties_update import (
    WebHookPropertiesUpdate,
)
from azure_transcription_client.models.web_hook_update import WebHookUpdate
