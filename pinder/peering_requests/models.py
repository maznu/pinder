from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Request(models.Model):

    STATE_WAITING = "waiting"
    STATE_ACCEPTED = "accepted"
    STATE_REJECTED = "rejected"

    STATES = (
        (STATE_WAITING, "Waiting"),
        (STATE_ACCEPTED, "Accepted"),
        (STATE_REJECTED, "Rejected"),
    )

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="requests_received")
    receiver = models.ForeignKey("users.Isp", related_name="requests_sent")
    ixlan_id = models.PositiveIntegerField()

    state = models.CharField(
        choices=STATES, default=STATE_WAITING, max_length=8)

    sender_is_ready = models.BooleanField(default=False)
    receiver_is_ready = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Peering request from {} to {}".format(
            self.sender, self.receiver)
