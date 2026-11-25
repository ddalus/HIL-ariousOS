import uuid

job_id = f"Job ID: {uuid.uuid4().hex[:8]}"

print(job_id)