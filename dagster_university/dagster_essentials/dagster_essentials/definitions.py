import dagster as dg

from dagster_essentials.assets import metrics, trips
from dagster_essentials.resources import database_resource
from dagster_essentials.jobs import (
    weekly_update_job
)

from dagster_essentials.schedules import (
    weekly_update_schedule
)

trip_assets = dg.load_assets_from_modules([trips])
metric_assets = dg.load_assets_from_modules([metrics])

defs = dg.Definitions(
    assets=[*trip_assets, *metric_assets],
    resources={
        "database": database_resource,
    },
    jobs=[weekly_update_job],
    schedules=[weekly_update_schedule],
)
