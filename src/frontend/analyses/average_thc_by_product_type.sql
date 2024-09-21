SELECT product_type, avg(total_thc) AS average_thc FROM test_results
GROUP BY product_type;