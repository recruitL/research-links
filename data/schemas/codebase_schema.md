# Codebase CSV Schema

推荐字段：

| Field | Meaning |
| --- | --- |
| `name` | Codebase name |
| `url` | Repository, documentation, or project URL |
| `language` | Main implementation language |
| `main_use` | What the codebase is used for |
| `status` | Active, archived, paper-level only, unknown |
| `installation_difficulty` | low, medium, high, unknown |
| `theory_transparency` | Whether formulas and model choices are easy to trace |
| `modifiable` | Whether it can be modified for diagnostics |
| `relation_to_my_work` | Why it matters for current work |
| `ai_evaluation` | Initial AI assessment |
| `human_check` | Manual verification status |
| `notes` | Known caveats |

Do not mark a codebase as suitable for production use until it has been installed and tested locally.
