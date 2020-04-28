from django.db import models
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.conf import settings
from django.db import transaction
from django.contrib.auth.models import (
    AbstractBaseUser,
)

# from phonenumber_field.modelfields import PhoneNumberField
# from datetime import datetime


class User(AbstractBaseUser):
    """
    Defines the base user class, useable in every app

    This is almost the same as the auth module AbstractUser since it inherits from it,
    but some fields are required, and the username is generated automatically with the
    name of the user (see generate_username()).

    Added field: nick_name, date_of_birth
    Required fields: email, first_name, last_name, date_of_birth
    """

    username = models.CharField(
        _("username"),
        max_length=254,
        unique=True,
        help_text=_(
            "Required. 254 characters or fewer. Letters, digits and ./+/-/_ only."
        ),
        validators=[
            validators.RegexValidator(
                r"^[\w.+-]+$",
                _(
                    "Enter a valid username. This value may contain only "
                    "letters, numbers "
                    "and ./+/-/_ characters."
                ),
            )
        ],
        error_messages={"unique": _("A user with that username already exists.")},
    )
    first_name = models.CharField(_("first name"), max_length=64)
    last_name = models.CharField(_("last name"), max_length=64)
    email = models.EmailField(_("email address"), unique=True)
    nick_name = models.CharField(_("nick name"), max_length=64, null=True, blank=True)
    address = models.CharField(_("address"), max_length=128, blank=True, default="")

    """profile_pict = models.OneToOneField(
        "SithFile",
        related_name="profile_of",
        verbose_name=_("profile"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )"""
    sex = models.CharField(
        _("sex"),
        max_length=10,
        choices=[("MAN", _("Man")), ("WOMAN", _("Woman"))],
        default="MAN",
    )
    tshirt_size = models.CharField(
        _("tshirt size"),
        max_length=5,
        choices=[
            ("-", _("-")),
            ("XS", _("XS")),
            ("S", _("S")),
            ("M", _("M")),
            ("L", _("L")),
            ("XL", _("XL")),
            ("XXL", _("XXL")),
            ("XXXL", _("XXXL")),
        ],
        default="-",
    )

    is_superuser = models.BooleanField(
        _("superuser"),
        default=False,
        help_text=_("Designates whether this user is a superuser. "),
    )

    # REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        create = False
        with transaction.atomic():
            if self.id:
                old = User.objects.filter(id=self.id).first()
                if old and old.username != self.username:
                    self._change_username(self.username)
            else:
                create = True
            super(User, self).save(*args, **kwargs)
            if (
                create and settings.IS_OLD_MYSQL_PRESENT
            ):
                raise ValidationError( ("ERROR"))

    def _change_username(self, new_name):
        u = User.objects.filter(username=new_name).first()
        if u is None:
            if self.home:
                self.home.name = new_name
                self.home.save()
        else:
            raise ValidationError(_("A user with that username already exists"))

    def get_profile(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "nick_name": self.nick_name,
        }

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_nick_name(self):
        if self.nick_name:
            return self.nick_name
        return "No nick name"

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        if from_email is None:
            from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, from_email, [self.email], **kwargs)
