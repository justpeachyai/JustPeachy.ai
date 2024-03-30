"""
worker profile image generator
has a base prompt, and uses info from worker config to create image

def generate_profile_pic(name, role, goal, personality, backstory)"
    {{prompt}}
    upload to s3
    return s3 file_id
"""