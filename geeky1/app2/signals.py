'''
# built-in signals

from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

# ani ya sarv func sathi url define karychi garaj nhi
# user_logged_in

@receiver(user_logged_in,sender=User)
def login_succ(sender,request,user,**kwargs):
    print("-----------------------------------")
    print("logged-in signal....Run Intro..")
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print("user password:",user.password)     # asa additional use kartat signals cha
    print(f"kwargs: {kwargs}") # kwargs f string madhe dya lagte
# or   user_logged_in.connect(login_succ,sender=User)


# user_logged_out

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("-------------------------------------")
    print("logged-out signal.......run outro...")
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print(f"kwargs:{kwargs}")


# user_login_failed

@receiver(user_login_failed)
def log_out(sender,credentials,request,**kwargs):
    print("-------------------------------------")
    print("login failed signal.......")
    print("sender:",sender)
    print("request:",request)
    print("credentials:",credentials)
    print(f"kwargs:{kwargs}")

from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete

# pre_save

@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("-------------------------------------")
    print("pre save signal.......")
    print("sender:",sender)
    print("instance:",instance)
    print(f"kwargs:{kwargs}")


# post_save

@receiver(post_save,sender=User)
def at_beginning_save(sender,instance,created,**kwargs):
    if created:
        print("-------------------------------------")
        print("post save signal.......")
        print("new record")
        print("sender:",sender)
        print("instance:",instance)
        print("created:",created)
        print(f"kwargs:{kwargs}")
    else:
        print("-------------------------------------")
        print("post save signal.......")
        print("update")
        print("sender:",sender)
        print("instance:",instance)
        print("created:",created)
        print(f"kwargs:{kwargs}")

# pre_delete

@receiver(pre_delete,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("-------------------------------------")
    print("pre delete.......")
    print("sender:",sender)
    print("instance:",instance)
    print(f"kwargs:{kwargs}")

# post delete

@receiver(post_delete,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("-------------------------------------")
    print("post delete.......")
    print("sender:",sender)
    print("instance:",instance)
    print(f"kwargs:{kwargs}")

# pre init

@receiver(pre_init,sender=User)
def at_beginning_save(sender,*args,**kwargs):
    print("-------------------------------------")
    print("pre init.......")
    print("sender:",sender)
    print(f"args:{args}")
    print(f"kwargs:{kwargs}")

# post init

@receiver(post_init,sender=User)
def at_beginning_save(sender,*args,**kwargs):
    print("-------------------------------------")
    print("post init.......")
    print("sender:",sender)
    print(f"args:{args}")
    print(f"kwargs:{kwargs}")

from django.core.signals import request_started,request_finished,got_request_exception

# request_started

@receiver(request_started)
def at_beginning_save(sender,environ,**kwargs):
    print("-------------------------------------")
    print("request started.......")
    print("sender:",sender)
    print("environ:",environ)
    print(f"kwargs:{kwargs}")

# request_finished

@receiver(request_finished)
def at_beginning_save(sender,**kwargs):
    print("-------------------------------------")
    print("request finished.......")
    print("sender:",sender)
    print(f"kwargs:{kwargs}")

# got_request_exception

@receiver(got_request_exception)
def at_beginning_save(sender,request,**kwargs):
    print("-------------------------------------")
    print("got exception.......")
    print("sender:",sender)
    print("request:",request)
    print(f"kwargs:{kwargs}")

from django.db.models.signals import pre_migrate,post_migrate

# pre_migrate

@receiver(pre_migrate)
def at_beginning_save(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("-------------------------------------")
    print("before migrate.......")
    print("sender:",sender)
    print("app_config::",app_config)
    print("verbosity:",verbosity)
    print("interactive:",interactive)
    print("using:",using)
    print("plan:",plan)
    print("apps:",apps)
    print(f"kwargs:{kwargs}")


# post_migrate

@receiver(post_migrate)
def at_beginning_save(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("-------------------------------------")
    print("after migrate.......")
    print("sender:",sender)
    print("app_config::",app_config)
    print("verbosity:",verbosity)
    print("interactive:",interactive)
    print("using:",using)
    print("plan:",plan)
    print("apps:",apps)
    print(f"kwargs:{kwargs}")


from django.db.backends.signals import connection_created

@receiver(connection_created)
def at_beginning_save(sender,connection,**kwargs):
    print("-------------------------------------")
    print("initial connection to the database.......")
    print("sender:",sender)
    print("connection:",connection)
    print(f"kwargs:{kwargs}")

    '''
