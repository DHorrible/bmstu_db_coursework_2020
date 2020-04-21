select
	month(`datetime`) as `month`,
    count(*) as `transactions`
from `transaction_history`
where year(`datetime`) = 2017
order by `month`
