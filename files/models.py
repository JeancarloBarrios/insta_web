from django.db import models
from django.conf import settings
import boto3
from django.dispatch import receiver


# Create your models here.
def _gen_signed_url(self, key, bucket):
    exp_time = settings.get('FILE_EXPIRATION_TIME', 3600)
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_ACCESS_KEY_SECRET
    )
    try:
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket,
                'Key': key
            },
            # ExpiresIn=exp_time
            ExpiresIn=63072000
        )
    except:
        url = None
    return url


class File(models.Model):
    UUID = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    extension = models.CharField(max_length=100)

    @property
    def key(self):
        return 'files/{}/{}'.format(self.UUID, self.name)

    @property
    def url(self):
        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_ACCESS_KEY_SECRET
        )
        return s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': settings.S3_BUCKET_NAME,
                'Key': self.key
            },
            ExpiresIn=3600*24*7
        )


@receiver(models.signals.post_delete, sender=File)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    client = boto3.client('s3')
    client.delete_object(Bucket=settings.S3_BUCKET_NAME, Key=instance.key)
