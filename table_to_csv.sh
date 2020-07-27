#!/bin/bash
 
dir=tables
rm -rf ${dir}/
mkdir -p ${dir}
mysql --skip-column-names -e"select concat(TABLE_SCHEMA,'.',TABLE_NAME) from information_schema.tables where table_schema in ('edmbuild','db1') and table_type='BASE TABLE'">${dir}.txt
while IFS=. read -r  schema item_name xxx; do
    echo ${schema} ./${dir}/${schema}.${item_name}.csv ${xxx}
    #mysql -e"select group_concat(column_name order by ordinal_position) from information_schema.columns where table_schema='${schema}' and table_name='${item_name}'" >./${dir}/${schema}.${item_name}.csv
    mysql --raw db1 -e"select * from ${schema}.${item_name};" | sed 's/\t/,/g' >>./${dir}/${schema}.${item_name}.csv
    #mysql --skip-column-names --raw db1 -e"select * from ${schema}.${item_name};" | sed 's/\t/,/g' >>./${dir}/${schema}.${item_name}.csv
    #sqlformat --reindent --keywords upper  _tmp.sql >./${dir}/${item_name}.sql
done <${dir}.txt 
