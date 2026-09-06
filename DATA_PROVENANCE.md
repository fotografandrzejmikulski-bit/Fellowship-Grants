# Data Provenance Standard

Current benchmark inputs and outputs are synthetic/model-generated and must never be described as physical measurements.

Every future experimental dataset must record:

- acquisition timestamp;
- raw-file hash;
- instrument make/model and relevant settings;
- calibration status;
- ambient/device temperature;
- optical source settings;
- software/firmware versions;
- scenario identifier;
- random seed where applicable;
- evidence level;
- operator notes and known anomalies.

Measured data should be immutable once released, with derived tables and plots generated from the archived raw dataset.
