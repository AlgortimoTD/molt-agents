# Certifications

<!-- FICTIONAL DOCUMENT: invented production company for the directorio-freelancers plugin demo. No person, company or client is real. -->

The certifications North Beacon recognizes, with the name the team uses. The expiry tracker
compares the cards against this list and the tiers below; a certification that appears on a
card and is not here gets reported so the team decides whether it enters.

<!-- Current since 2026-09-15 (origin: installation interview) -->

## Catalog

| Certification (as the team says it) | Who requires it | Typical validity | Document kept |
|---|---|---|---|
| heights course | construction sites and industrial clients | 1 year | photo of the card or PDF |
| construction safety course | construction companies | 1 year | PDF |
| drone license | every shoot with a drone | 2 years | PDF |

## Notice tiers

The weekly sweep classifies every certification of every card into exactly one of these
tiers, counting from the day of the sweep:

| Tier | Means |
|---|---|
| expired | the date has passed |
| expires within 7 days | expires in the next 7 days |
| expires within 30 days | expires between 8 and 30 days from now |
| expires within 60 days | expires between 31 and 60 days from now |
| undated | the card names it but does not say when it expires; never counts as valid |
| no supporting document | has a date but there is no document in `freelancers/documents/` |

What expires after 60 days is not reported; it stays on the card.

## Validity rule

For a shoot, a certification is valid if its expiry date is after the date of the shoot, not
after today. A person whose course expires on November 10 does not enter a shoot on the 15th.

## History

No entries. This file is born on 2026-09-15 with the installation.
