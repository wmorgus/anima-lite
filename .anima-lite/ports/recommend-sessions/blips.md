# Blips: recommend-sessions

## Blip: "open slots" has no backing data in prod (CLAIM-2 rank input, CLAIM-4 display field)
Severity: CONTRACT-BREAK
Location: java/source/edu/cmu/pl2/item/SessionItem.java, GroupItem.java; java/source/edu/cmu/pl2/service/impl/TutorSessionServiceImpl.java (capacity logic)
What happened: CLAIM-2 (amended) specifies the candidate set as "open sessions ...
with free slots" ranked by "soonest start + most open slots," and CLAIM-4 says to
show "open-slots" alongside title/time. Probing SessionItem, GroupItem, and every
"capacity"-named code path in TutorSessionServiceImpl confirms there is no
student-side capacity/slot concept anywhere in prod: every existing "capacity" /
"slots needed" mechanism (ShiftItem.numTutorsNeeded, IndividualShiftDto capacity
tracking) is TUTOR staffing capacity, not room for a student to join a session.
There is no maxStudents/studentCapacity field on SessionItem or GroupItem, and no
service method that answers "how many more students can this session hold."
Why: This is the same class of gap as the subject-field blocker that the plan
already caught and got amended (dropped) before execution — a contract term
written against something that does not exist in the real schema. Unlike
subject, this one was not caught during ari-argue/ari-port planning (plan.md's
blockers section asserted "Free-slot count... derivable from existing prod
data," which this probe shows is incorrect).
Resolution taken (did not invent a proxy): implemented CLAIM-2's candidate
filter + rank using only the parts backed by real data — institution match,
excluding sessions the student is already in, and sorting by soonest
sessionStart. Did NOT implement "most open slots" as a filter or tiebreak, and
did NOT show an open-slots field in CLAIM-4's display. No student-capacity
proxy was invented (e.g. reusing GroupItem.lessons or tutor capacity) without
confirmation, per the same discipline the subject blocker required.
Downstream consequence: the shipped rank rule is narrower than the frozen,
amended contract text literally states ("soonest start" only, not "+ most open
slots"). The candidate list may include sessions that are already at whatever
informal capacity the tutoring team manages out-of-band (e.g. via Zoom
room limits), since prod has no way to know. CLAIM-4's displayed fields are
title/time only — no slots figure is shown because none exists to show.
Contracting failure?: Yes — ari-argue/ari-port planning should have verified
every literal-schema reference in the contract against prod (not just the one
the user flagged), the same way subject was verified. Recommend: before
freezing a contract, grep for every noun phrase in a claim's rule text
("subject," "open slots," "capacity," etc.) against the real item/dto/service
classes it depends on, not just the naming the proto's mock UI happened to use.
Candidate resolution paths (mirrors the subject blocker's framing, for
whoever revisits this): (a) leave dropped permanently — soonest-start-only is
a defensible, honest heuristic; (b) add a real student-capacity field to
GroupItem/SessionItem (schema change, out of this port's scope); (c) derive a
coarse proxy from tutor:student ratio via ShiftItem.numTutorsNeeded (would
need product confirmation that this ratio is meaningful — not verified here).

## Blip: CLAIM-6 — no student-facing notification wired (record-only)
Severity: review-suggested
Location: java/docroot/javascript/pl2/schedule/tutor_schedule_recommend.js (renderConfirmStep copy)
What happened: The proto's confirm-step copy said "This will be shared with the
student." The port's copy was changed to "This will be recorded with the
recommendation" — no student-facing notification channel is wired up. Per
CLAIM-6, this port is record-only: SessionRecommendationItem is persisted
server-side, but nothing pushes a notification, email, or in-app alert to the
student. A student has no way to learn about the recommendation from the
product today.
Why: The contract explicitly decided this (CLAIM-6, confirmed 2026-07-07) —
prod's student-facing notification channel is unconfirmed, so this port does
not invent one.
Downstream consequence: the feature is only useful if the tutor separately
tells the student (e.g. verbally, or the tutor dashboard surfaces this
elsewhere). If the product wants the proto's promised "shared with the
student" behavior, that is a follow-on port once a notification channel is
confirmed.
Contracting failure?: n/a — already named and accepted in the contract.

## Blip: CLAIM-2/CLAIM-7 split leaves a transient authorization gap between commits
Severity: info
Location: java/source/edu/cmu/pl2/servlet/TutorScheduleServlet.java (getRecommendCandidates)
What happened: Per the plan's commit sequence, CLAIM-2 (ranking) and CLAIM-7
(gating to the tutor's own advisor-students + institution) are separate
commits. In the commit-2 state (after CLAIM-2, before CLAIM-7),
getRecommendCandidates resolves the given studentId to a PL2StudentItem and
queries their institution without yet checking that the requesting tutor is
actually that student's advisor. This state exists only on this feature branch
between two commits in the same PR — it is not a deployable intermediate
state — but is worth flagging for anyone bisecting the branch.
Why: The plan deliberately separates ranking (CLAIM-2) from authorization
(CLAIM-7) so each is independently auditable/revertable, matching how an
auditor would want to see "who can see what" isolated from "what gets shown."
Downstream consequence: none in the shipped PR (both commits land together
before merge/deploy); flagged only so a future `git bisect` or partial cherry-
pick doesn't accidentally ship CLAIM-2 without CLAIM-7.
Contracting failure?: n/a — intentional plan structure, not a gap.

## Blip: subject dropped from candidate filter/rank and UI (context, already resolved)
Severity: info
Location: java/docroot/javascript/pl2/schedule/tutor_schedule_recommend.js (renderCriteriaStep); java/docroot/jsp_pl2/tutor_schedule.jsp
What happened: The proto's criteria-select step had a student dropdown AND a
subject dropdown (hardcoded Math/English). The port's criteria-select step has
only the student dropdown. This was resolved before execution via the
contract's CLAIM-2 amendment (2026-07-07): prod has no subject field on
SessionItem/GroupItem/ShiftItem/InstitutionItem, so subject was dropped from
both the filter/rank input and the UI.
Why: Recorded here for completeness since it's a visible UI difference from
the proto, not because it's a new decision.
Downstream consequence: none beyond what the amendment already accepted.
Contracting failure?: n/a — already resolved.
