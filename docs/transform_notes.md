# Data Notes

Design decisions and data quirks that affect how this data should be used.

## Filtering

All dashboard views filter to individual providers (RNDRNG_PRVDR_ENT_CD = 'I'). The billing data includes organizations (labs, group practices, health systems) that bill under a single NPI.

## MIPS Score Resolution

Providers can have multiple MIPS records from different scoring pathways (individual, group, APM). The provider_profile_view resolves this to one score per NPI using MAX(FINAL_MIPS_SCORE), consistent with how CMS determines payment adjustments. Any analysis comparing MIPS scores across providers should account for the source type.

## Billing Data

Submitted charges (AVG_SBMTD_CHRG) are set by the provider and average roughly 4x what Medicare allows. They are not meaningful for comparison. Use AVG_MDCR_STDZD_AMT for analysis as it adjusts for geographic cost differences.

TOT_BENES is per service line. Summing it across services for a provider overcounts because the same patient appears in multiple service lines. It works as a rough volume indicator but is not a unique patient count. No unique patient count is derivable from these datasets.

## Hospital Quality Standardization

The COMPARED_TO_NATIONAL column uses different phrasing across source tables. The hospital_quality_summary_view standardizes all values to: Better, Worse, No Different, Not Available, or Number of Cases Too Small.

## HAI Sub-measures

The raw HAI table has 36 rows per facility — 6 infection types with 6 component measures each. The hospital_quality_summary_view filters to only the summary measures.

## Credentials Column

RNDRNG_PRVDR_CRDNTLS is free-text with no standardization. Not usable for filtering without cleanup. Cleanup not performed as the metric was not used in this project.

## Medicare Only

This data covers Medicare fee-for-service billing only. Provider revenue from commercial insurance and Medicaid is not represented. Specialties that appear low-revenue here may be well-compensated overall through other payers. Similarly, MIPS eligibility requires minimum Medicare billing thresholds. This accounts for the high null rate for individual providers in the data.
