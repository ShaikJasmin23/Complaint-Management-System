



from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name, email, phone, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)  # Normalizing email

        user = self.model(
            email=email,
            phone=phone,
            name=name,
            is_active=True  # Ensure the user is active by default
        )

        user.set_password(password)  # Setting the hashed password
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, password=None):
        user = self.create_user(
            name=name,
            email=email,
            phone=phone,
            password=password,
        )
        # Setting additional fields for the superuser
        user.is_admin = True
        user.is_staff = True  # Make sure this user is considered a staff member
        user.is_superuser = True  # Required for superuser privileges in Django admin
        user.role = "admin"  # Assign role as admin
        user.save(using=self._db)
        return user





























# from django.contrib.auth.models import BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self,name, email, phone, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")

#         user = self.model(
#             email=self.normalize_email(email),
#             phone=phone,
#             name=name
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,name, email, phone, password=None):
#         user = self.create_user(
#             name=name,
#             email=email,
#             password=password,
#             phone=phone,
#         )
#         user.is_admin = True
#         user.role = "admin"
#         user.save(using=self._db)
#         return user





from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name, email, phone, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)  # Normalizing email

        user = self.model(
            email=email,
            phone=phone,
            name=name,
            is_active=True  # Ensure the user is active by default
        )

        user.set_password(password)  # Setting the hashed password
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, password=None):
        user = self.create_user(
            name=name,
            email=email,
            phone=phone,
            password=password,
        )
        # Setting additional fields for the superuser
        user.is_admin = True
        user.is_staff = True  # Make sure this user is considered a staff member
        user.is_superuser = True  # Required for superuser privileges in Django admin
        user.role = "admin"  # Assign role as admin
        user.save(using=self._db)
        return user




