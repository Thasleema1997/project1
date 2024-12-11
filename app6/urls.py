from django.urls import path
from . import views

urlpatterns=[ path("",views.run,name="run"),
             path("p1",views.register,name="register"),
             path("p2",views.signin,name="signin"),
              path("p3",views.login,name="login"),
              path("p4",views.userdata,name="userdata"),
              path("p6",views.welcome,name="welcome"),
              path("p5",views.lod,name="lod")
            ]