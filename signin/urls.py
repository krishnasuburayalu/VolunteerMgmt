from django.conf.urls import url

from .views import SignInView, PostSignIn, signInView


urlpatterns = [

url( 
		r'^submit/',PostSignIn.as_view(), name='submit'
		),
url(
        r'^$',signInView, name = 'my-ajax-url'#SignInView.as_view()
        ),

]
