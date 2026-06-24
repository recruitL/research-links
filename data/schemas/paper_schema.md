# Paper CSV Schema

推荐字段：

| Field | Meaning |
| --- | --- |
| `arxiv_id` | arXiv identifier, including old prefixes such as `gr-qc/9811091` |
| `title` | Paper title |
| `authors` | Semicolon-separated author list |
| `year` | Publication or arXiv year |
| `published` | arXiv published date if available |
| `updated` | arXiv updated date if available |
| `primary_category` | Main arXiv category |
| `categories` | All known categories |
| `abstract` | Abstract text when harvested |
| `url` | arXiv abstract URL or official page |
| `pdf_url` | PDF URL |
| `topic` | Research topic |
| `technical_tags` | Semicolon-separated technical tags |
| `technical_role` | Why this paper matters technically |
| `relevance` | Relation to current research route |
| `status` | Candidate, selected, reading, reviewed, reproduced, blocked |
| `ai_rating` | A/B/C/D/X initial AI rating |
| `human_checked` | no, partial, yes, needs expert check |
| `notes` | Free-form notes and provenance |

Existing source-specific fields should be preserved when possible.
