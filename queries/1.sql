select
	month(`datetime`) as `month`,
    count(*) as `transactions`
from `transaction_history`
where year(`datetime`) = 2020
order by `month`
