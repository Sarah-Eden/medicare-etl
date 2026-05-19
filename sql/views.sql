CREATE OR REPLACE VIEW provider_profile_view AS (
    SELECT
        d.rndrng_npi,
        d.rndrng_prvdr_last_org_name,
        d.rndrng_prvdr_first_name,
        d.rndrng_prvdr_type,
        d.rndrng_prvdr_city,
        d.rndrng_prvdr_state_abrvtn, 
        m.max_mips_score
    FROM provider_demographics d
    LEFT JOIN (
        SELECT npi, MAX(final_mips_score) as max_mips_score
        FROM mips_performance
        GROUP BY npi
    ) m ON m.npi = d.rndrng_npi
    WHERE d.rndrng_prvdr_ent_cd = 'I'
);

CREATE OR REPLACE VIEW provider_hospital_info_view AS (
    SELECT
        d.rndrng_npi,
        h.facility_id,
        h.facility_name,
        h.hospital_overall_rating
    FROM hospital_general_information h
    INNER JOIN provider_hospital_affiliation a 
        ON a.facility_affiliations_certification_number = h.facility_id
    INNER JOIN provider_demographics d ON d.rndrng_npi = a.npi
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
