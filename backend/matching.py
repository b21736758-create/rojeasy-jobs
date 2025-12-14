def match_jobs(candidate_skills, jobs):
    ranked = []
    for job in jobs:
        score = len(set(candidate_skills.split(","))
                    & set(job.skills.split(",")))
        ranked.append({"job": job.title, "score": score})
    return sorted(ranked, key=lambda x: x["score"], reverse=True)
