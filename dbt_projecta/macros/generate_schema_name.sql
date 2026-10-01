-- generate_schema_name.sql overrides dbt's default schema naming behavior
-- when dbt creates a table it calls a built-in macro called generate_schema_name to decide which schema to write to
-- by default that macro combines the target schema from profiles.yml (public) with the custom schema from dbt_project.yml (silver or gold)
-- resulting in public_silver and public_gold instead of silver and gold
-- placing this file in macros/ overrides the built-in macro since dbt checks macros/ first

-- the macro takes two arguments:
-- custom_schema_name: the schema defined in dbt_project.yml for that model folder (silver or gold), None if not set
-- node: the current model being processed, not used here but required by dbt's macro signature

-- if custom_schema_name is None (no custom schema set) fall back to target.schema which is public from profiles.yml
-- if custom_schema_name is set use it directly with trim() to strip any whitespace, giving silver or gold without any prefix

{% macro generate_schema_name(custom_schema_name, node) -%}
    {%- if custom_schema_name is none -%}
        {{ target.schema }}
    {%- else -%}
        {{ custom_schema_name | trim }}
    {%- endif -%}
{%- endmacro %}
