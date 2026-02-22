{{ config(
			materialized='table',
			tags=['tier1']
		) }}

select
  c.customer_id,
  c.customer_name,
  c.segment,
  coalesce(m.order_count, 0) as order_count,
  coalesce(m.lifetime_value, 0) as lifetime_value
from {{ ref('stg_customers') }} c
left join {{ ref('int_customer_order_metrics') }} m
  on c.customer_id = m.customer_id
