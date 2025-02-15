"""
This file configures the Apache Airflow DAG to ingest Statens museum data.

We do this by running `provider_api_scripts.staten_museum.main`
"""
import logging

# airflow DAG (necessary for Airflow to find this file)
from datetime import datetime, timedelta

from common.dag_factory import create_provider_api_workflow
from providers.provider_api_scripts import staten_museum


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s:  %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

DAG_ID = "staten_museum_workflow"
START_DATE = datetime(2020, 1, 1)
DAGRUN_TIMEOUT = timedelta(hours=24)

globals()[DAG_ID] = create_provider_api_workflow(
    DAG_ID,
    staten_museum.main,
    start_date=START_DATE,
    schedule_string="@monthly",
    dated=False,
    dagrun_timeout=DAGRUN_TIMEOUT,
)
