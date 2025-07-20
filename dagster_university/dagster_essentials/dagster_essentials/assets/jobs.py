import dagster as dg

trips_by_week = dg.AssetSelection.assets(["trips_by_week"])

weekly_update_job = dg.define_asset_job(
    name="weekly_update_job",
    selection=trips_by_week,
)

