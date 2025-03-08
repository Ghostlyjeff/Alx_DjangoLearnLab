from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden

# Function to check if a user is an Admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# View that only Admin users can access
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_dashboard.html')
