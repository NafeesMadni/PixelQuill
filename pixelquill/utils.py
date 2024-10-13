from django.contrib.auth.models import User
from authentication.models import Profile
from core.models import Category

categories = Category.objects.prefetch_related('category_blogs').all()

# btn_text_cols = {
#      "Fashion": " bg-rose-100/95 text-rose-500 ",
#      "Technology": " bg-blue-100/95 text-blue-500 ",
#      "Economy": " bg-green-100/95 text-green-500 ",
#      "Business": " bg-indigo-100/95 text-indigo-500 ",
#      "Travel": " bg-teal-100/95 text-teal-600 ",
#      "Lifestyle": " bg-yellow-100/95 text-yellow-500 ",
#      "Sports": " bg-cyan-100/95 text-cyan-500 ", 
# }

category_imgs = {
     "Fashion": "img/categories/fashion.jpg",
     "Technology": "img/categories/technology.jpg",
     "Economy": "img/categories/economy.jpg",
     "Business": "img/categories/business.jpg",
     "Travel": "img/categories/travel.jpg",
     "Lifestyle": "img/categories/lifestyle.jpg",
     "Sports": "img/categories/sports.jpg", 
}

btn_cols = {
     "Fashion": " bg-rose-500 ",
     "Technology": " bg-blue-500 ",
     "Economy": " bg-green-500 ",
     "Business": " bg-indigo-500 ",
     "Travel": " bg-teal-500 ",
     "Lifestyle": " bg-yellow-500 ",
     "Sports": " bg-cyan-500 ", 
}

def getUserProfile(request):
     # if there is no user login or login user is a admin
     if not request.user.is_authenticated :
          profile = None
          return profile
     if request.user.is_superuser or request.user.is_staff:
          profile = None
     else:
          user = User.objects.prefetch_related('profile').get(pk=request.user.pk)
          profile = user.profile
     print(profile)
     return profile
