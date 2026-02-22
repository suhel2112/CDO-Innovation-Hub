{{ config(
    materialized='incremental',
    unique_key='order_id',
    incremental_strategy='delete+insert',
	tags=['tier1']
) }}

select
  order_id,
  customer_id,
  order_date,
  amount
from {{ ref('stg_orders') }}

{% if is_incremental() %}
  where order_date >= (select max(order_date) - interval 3 day from {{ this }})
{% endif %}
