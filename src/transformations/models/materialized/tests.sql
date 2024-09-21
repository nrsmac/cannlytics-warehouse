SELECT column_name AS test_name
FROM information_schema.columns 
WHERE table_name = 'raw_test_results'
AND column_name NOT IN (
        'producer_license_number',
        'lab',
        'label',
        'product_type',
        'is_on_hold',
        'overall_passed',
        'test_passed',
        'producer',
        'images',
        'analyses',
        'results',
        'serving_size',
        'metrc_source_id',
        'metrc_manifest_number',
        'batch_size',
        'sum_of_cannabinoids',
        'notes',
        'distributor_city',
        'distributor_zipcode',
        'producer_city',
        'producer_zipcode',
        'metrc_ids',
        'status',
        'product_size',
        'results_hash',
        'batch_number',
        'distributor',
        'distributor_license_number',
        'source',
        'year',
        'error',
        'week',
        'month',
        'classification',
        'processor',
        'state',
        'city',
        'standard_product_type',
        'id',
        'code',
        'market',
        'license_number',
    )
AND column_name NOT LIKE 'package%' 
AND column_name NOT LIKE 'unit%' 
AND column_name NOT LIKE 'coa%' 
AND column_name NOT LIKE 'mertc%' 
AND column_name NOT LIKE '%$_id'
AND column_name NOT LIKE 'date%'
AND column_name NOT LIKE 'lab%'
AND column_name NOT LIKE '%name' 
AND column_name NOT LIKE 'city%' 
AND column_name NOT LIKE '%city' 
AND column_name NOT LIKE 'name%' 
AND column_name NOT LIKE '%method%'
AND column_name NOT LIKE 'sample%'
AND column_name NOT LIKE '%url'
AND column_name NOT LIKE 'product%'
AND column_name NOT LIKE 'lab%'
AND column_name NOT LIKE 'distributor%'
AND column_name NOT LIKE 'producer%'
AND column_name NOT LIKE 'address%' 
AND column_name NOT LIKE 'Unnamed%' 
AND column_name NOT LIKE '%datetime' 
AND column_name NOT LIKE '%$_date$_%' 
AND column_name NOT LIKE '%$_date%' ESCAPE '$'
AND column_name NOT LIKE 'date$_%' ESCAPE '$'
AND column_name NOT LIKE 'is$_%' ESCAPE '$'
AND column_name NOT LIKE '%$_at' ESCAPE '$'
AND column_name NOT LIKE '%$_code' ESCAPE '$'
AND column_name NOT LIKE '%$_address' ESCAPE '$'
AND column_name NOT LIKE '%$_date' ESCAPE '$'
AND column_name NOT LIKE '%$_by' ESCAPE '$'
AND column_name NOT LIKE '%$_id' ESCAPE '$'