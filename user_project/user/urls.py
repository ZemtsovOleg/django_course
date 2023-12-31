from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-url'),
    path('feedback/', views.FeedbackFormView.as_view(), name='feedback-url'),
    path('sign-up/', views.SignUpCreateView.as_view(), name='sign-up-url'),
    path('password-reset/', views.CustomPasswordResetView.as_view(),
         name="password-reset-url"),
    path('confirm-email/', views.ConfirmEmail.as_view(), name='confirm-email-url'),
    path('email-confirmed/<token>/', views.ConfirmedEmail.as_view(),
         name='email-confirmed-url'),
    # path('verify_email/<uidb64>/<token>/',
    #      views.EmailVerify.as_view(), name='verify-email'),
    path('', include('django.contrib.auth.urls')),
    path('<slug:slug_user>/', views.ProfilePageView.as_view(), name='profile-url'),
]

''' Для избежания коллизий и обеспечения уникальности слагов, можно принять несколько подходов:

Использовать другое поле для идентификации пользователей в URL: Вместо slug можно использовать другое уникальное поле, например, id, для идентификации пользователей в URL. В таком случае, URL мог бы выглядеть как: https://home.com/user/1/, где 1 - это id пользователя. Такой подход гарантирует уникальность URL и избежание коллизий.

Добавить префикс к URL: Вы можете добавить уникальный префикс к URL, чтобы обеспечить его уникальность. Например, URL может выглядеть так: https://home.com/u/slug_user/, где /u/ - это префикс, а slug_user - слаг пользователя. Такой подход также поможет избежать коллизий и обеспечить уникальность URL.

Ограничить выбор слагов: Вы можете ограничить выбор слагов пользователями, чтобы они не могли использовать зарезервированные имена, такие как admin, user, profile и т.д. Вы можете проверять выбранный слаг и отображать сообщение об ошибке, если пользователь пытается использовать недопустимый слаг.

Независимо от выбранного подхода, главной задачей является обеспечение уникальности URL и предотвращение коллизий, чтобы пользователи могли свободно выбирать и использовать слаги для своих страниц. '''
