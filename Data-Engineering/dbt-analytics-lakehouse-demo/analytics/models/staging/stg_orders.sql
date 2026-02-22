{{ config(materialized='view') }}

select
  cast(order_id as integer) as order_id,
  cast(customer_id as integer) as customer_id,
  cast(order_date as date) as order_date,
  cast(amount as double) as amount,
  cast(loaded_at as timestamp) as loaded_at
from {{ source('raw', 'raw_orders') }}
