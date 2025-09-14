
from typing import Dict, List, Set
def score_roles(found_skills: Set[str], roles: Dict[str, Dict[str, List[str]]]) -> List[Dict]:
    results = []
    f = set([s.lower() for s in found_skills])
    for role, cfg in roles.items():
        req = set([s.lower() for s in cfg.get("required_skills", [])])
        nice = set([s.lower() for s in cfg.get("nice_to_have", [])])
        req_hit = len(req & f)
        nice_hit = len(nice & f)
        score = (req_hit / max(len(req),1))*0.8 + ((nice_hit / max(len(nice),1))*0.2 if len(nice) else 0)
        missing_req = sorted([s for s in req if s not in f])
        suggested = sorted([s for s in nice if s not in f])
        results.append({
            "role": role,
            "score": round(score*100,1),
            "matched_required": req_hit,
            "total_required": len(req),
            "matched_nice": nice_hit,
            "total_nice": len(nice),
            "missing_required": missing_req,
            "suggested_skills": suggested,
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
