{{ config(materialized='ephemeral') }}

select
  customer_id,
  count(*) as order_count,
  sum(amount) as lifetime_value
from {{ ref('stg_orders') }}
group by 1
