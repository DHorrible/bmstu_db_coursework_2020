select
    *
from `client`
where `birthday` = (select max(`c`.`birthday`) from `client` as `c`)
