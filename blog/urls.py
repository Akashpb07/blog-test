from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.admin.views.decorators import staff_member_required
from posts.views import (
    index,
    search,
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    IndexView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from stories.views import (StoryListView,story_list,searchstory,IndexStorieView,contactUs,view_profile,searchstory)
from marketing.views import email_list_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),index_1
    path('contact_us/', contactUs.as_view(), name="contact_us"),
    path('', IndexView.as_view(), name='home'),
    path('', IndexStorieView.as_view(), name='home'),
    path('blog/', post_list, name='post-list'),
    path('story/', story_list, name='story-list'),
    path('accounts/signup/blog/', PostListView.as_view(), name='post-list'),
    path('accounts/signup/blog/', PostListView.as_view(), name='post-list'),
    path('accounts/login/blog/', StoryListView.as_view(), name='Story-list'),
    # path('search/', searchstory, name='searchstory'),
    path('search/', search, name='search'),
    path('searchstory/', searchstory, name='searchstory'),
    path('email-signup/', email_list_signup, name='email-list-signup'),
    # path('create/', post_create, name='post-create'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    # path('post/<id>/', post_detail, name='post-detail'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/<id>/update/', post_update, name='post-update'),
    path('post/<pk>/update/', staff_member_required(PostUpdateView.as_view()), name='post-update'),
    # path('post/<id>/delete/', post_delete, name='post-delete'),
    path('post/<pk>/delete/', staff_member_required(PostDeleteView.as_view()), name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path("view_profile/", view_profile, name="view_profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
