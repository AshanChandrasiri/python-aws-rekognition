import boto3

client = boto3.client('batch')

job_name = "job-image-label-v1"
job_queue = "arn:aws:batch:us-east-1:265484233567:job-queue/mac-job-queue"
job_definition = "arn:aws:batch:us-east-1:265484233567:job-definition/image-label-app:2"
url = "https://images.pexels.com/videos/854671/free-video-854671.jpg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200"

response = client.submit_job(
    jobName=job_name,
    jobQueue=job_queue,
    jobDefinition=job_definition,
    parameters={
        'url': url,
        'extension': "jpg"
    }
)
