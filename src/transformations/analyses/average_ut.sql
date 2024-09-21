SELECT * EXCLUDE state FROM (UNPIVOT (FROM {{ ref('state_averages') }} WHERE state = 'UT')
ON COLUMNS (* EXCLUDE state)
INTO NAME 'Test' VALUE "UT Average");