select
	`ah`.`account_id`,
	`c`.`name` as `currency_name`,
	sum(`ah`.`balance` - `ah`.`old_balance`) as `income`
from `account_history` as `ah`
inner join `account` as `a`
	on `a`.`id` = `ah`.`account_id`
inner join `currency` as `c`
	on `c`.`id` = `a`.`currency_id`
where `ah`.`account_id` = '{}'
	and `ah`.`old_balance` < `ah`.`balance`
