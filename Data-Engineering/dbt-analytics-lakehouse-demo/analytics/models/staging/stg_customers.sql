{{ config(materialized='view') }}

select
  cast(customer_id as integer) as customer_id,
  cast(customer_name as varchar) as customer_name,
  cast(segment as varchar) as segment,
  cast(loaded_at as timestamp) as loaded_at
from {{ source('raw', 'raw_customers') }}
