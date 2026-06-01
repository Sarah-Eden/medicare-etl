CREATE OR REPLACE VIEW provider_profile_view AS (
    SELECT
        d.rndrng_npi AS npi,
        d.rndrng_prvdr_last_org_name AS last_name,
        d.rndrng_prvdr_first_name AS first_name,
        d.rndrng_prvdr_crdntls AS credentials,
        d.rndrng_prvdr_type AS provider_type,
        d.rndrng_prvdr_st1 AS address,
        d.rndrng_prvdr_city AS city,
        d.rndrng_prvdr_state_abrvtn AS state, 
        d.rndrng_prvdr_ruca AS ruca,
        m.max_individual_mips_score
    FROM provider_demographics d
    LEFT JOIN (
        SELECT npi, MAX(final_mips_score) AS max_individual_mips_score
        FROM mips_performance
        WHERE source = 'individual'
        GROUP BY npi
    ) m ON m.npi = d.rndrng_npi
    WHERE d.rndrng_prvdr_ent_cd = 'I'
);

CREATE OR REPLACE VIEW hospital_quality_summary_view AS (
    SELECT
        facility_id,
        'HAI' as source,
        measure_id,
        measure_name,
        compared_to_national,
        score,
    CASE 
        WHEN compared_to_national LIKE 'Better%'  THEN 'Better'
        WHEN compared_to_national LIKE 'Worse%' THEN 'Worse'
        WHEN compared_to_national LIKE 'No Different%' THEN 'No Different'
        ELSE 'Not Available'
    END AS compared_to_national_category
    FROM hospital_hai
    WHERE measure_id LIKE '%SIR'

    UNION ALL

    SELECT
        facility_id,
        'Complications Deaths' AS SOURCE,
        measure_id,
        measure_name,
        compared_to_national,
        score,
    CASE
        WHEN compared_to_national LIKE 'Better%' THEN 'Better'
        WHEN compared_to_national LIKE 'Worse%' THEN 'Worse'
        WHEN compared_to_national LIKE 'No Different%' THEN 'No Different'
        WHEN compared_to_national LIKE 'Number%' THEN 'Number of Cases Too Small'
        ELSE 'Not Available'
    END AS compared_to_national_category
    FROM hospital_complications_deaths

    UNION ALL

    SELECT
        facility_id,
        'Unplanned Visits' AS SOURCE,
        measure_id,
        measure_name,
        compared_to_national,
        score,
    CASE
        WHEN compared_to_national LIKE 'Better%' 
            OR compared_to_national LIKE 'Fewer%' THEN 'Better'
        WHEN compared_to_national LIKE 'Worse%' 
            OR compared_to_national LIKE 'More Days%' THEN 'Worse'
        WHEN compared_to_national LIKE 'No Different%' 
            OR compared_to_national LIKE 'Average%' THEN 'No Different'
        WHEN compared_to_national LIKE 'Number%' THEN 'Number of Cases Too Small'
        ELSE 'Not Available'
    END AS compared_to_national_category
    FROM hospital_unplanned_visits   
);

CREATE OR REPLACE VIEW hcahps_summary_view AS (
    SELECT
        facility_id,
        hcahps_measure_id,
        hcahps_question,
        patient_survey_star_rating,
        number_of_completed_surveys,
        survey_response_rate_percent     
    FROM hospital_hcahps
    WHERE hcahps_question LIKE '%star%'
);


CREATE OR REPLACE VIEW hcahps_detailed_view AS (
    SELECT
        facility_id,
        hcahps_measure_id,
        hcahps_question,
        hcahps_answer_description,
        hcahps_answer_percent
    FROM hospital_hcahps
    WHERE hcahps_question NOT LIKE '%star%'
        AND hcahps_question NOT LIKE '%linear%'
);
