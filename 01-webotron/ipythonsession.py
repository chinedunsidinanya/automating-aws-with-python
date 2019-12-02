import boto3
session = boto3.session.Session(profile_name='chinedu')
s3 = session.resource('s3')
if __name__ == '__main__':
    for bucket in s3.buckets.all():
        print(bucket)
