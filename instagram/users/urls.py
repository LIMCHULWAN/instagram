from django.urls import path
from . import views

# from instagram.users.views import (
#     user_list_view,
#     user_redirect_view,
#     user_update_view,
#     user_detail_view,
# )

app_name = "users"
urlpatterns = [
    path("explore/", view=views.ExploreUsers.as_view(), name="explore_users"),
    path("<int:user_id>/follow/", view=views.FollowUser.as_view(), name="follow_user"),
    path("<int:user_id>/unfollow/", view=views.UnFollowUser.as_view(), name="follow_user"),
    path("<username>/followers/", view=views.UserFollowers.as_view(), name="user_followers"),
    path("<username>/following/", view=views.UserFollowing.as_view(), name="user_following"),
    path("search/", view=views.Search.as_view(), name="user_following"),
    path("<username>/", view=views.UserProfile.as_view(), name="user_profile"),

    # function base view example
    # path("<username>/following/", view=views.UserFollowingFBV, name="user_following"),

    # path("", view=user_list_view, name="list"),
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
