select
	`a`.`id`,
    count(*) AS `transactions`
from `account` as `a` inner join `account_history` as `ah`
	on `a`.`id` = `ah`.`account_id`
    and `ah`.`reason_id` = 3
inner join `client` as `c`
	on `c`.`id` = `a`.`client_id`
	and `c`.`secondname` = 'Petrov'
group by `a`.`id`
