select
	`a`.*
from `account` as `a`
left join `account_history` as `ah`
	on `a`.`id` = `ah`.`account_id`
group by `a`.`id`
having max(
    `ah`.`id` is not null
    and `ah`.`reason_id` = 3
    and `ah`.`old_balance` > `ah`.`balance`
    and month(`ah`.`datetime`) = 03
    and year(`ah`.`datetime`) = 2017) = false
