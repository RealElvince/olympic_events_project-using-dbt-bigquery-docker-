{{ % test assert_column_postive(model,column_name) %}}
     
    SELECT *
    FROM {{ model }}
    WHERE {{ column_name }} <= 0
{{ % endtest %}}
