from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import MemberForm
from .models import Member
from members.decorators import active_member_required
from django.shortcuts import render


def is_instructor(user):
    return user.is_authenticated and user.is_instructor

def home(request):
    return render(request, "home.html")

@active_member_required
def duty_roster(request):
    return render(request, 'members/duty_roster.html')

@active_member_required
@user_passes_test(is_instructor)
def instructors_only(request):
    return render(request, 'members/instructors.html')

@active_member_required
def members_list(request):
    return render(request, 'members/members.html')

@active_member_required
def log_sheets(request):
    return render(request, 'members/log_sheets.html')

@active_member_required
def member_list(request):
    members = Member.objects.all()
    return render(request, "members/member_list.html", {"members": members})

@active_member_required
def member_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if not (request.user.is_staff or request.user == member):
        return render(request, "403.html", status=403)

    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect("member_list")
        else:
            print("Form errors:", form.errors)  # 🔍 Debug!
    else:
        form = MemberForm(instance=member)
    print("FILES received:", request.FILES)
    return render(request, "members/member_edit.html", {"form": form})

from django.http import HttpResponse
from .utils import generate_vcard_qr
import base64

@active_member_required
def member_view(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    qr_png = generate_vcard_qr(member)
    qr_base64 = base64.b64encode(qr_png).decode('utf-8')
    return render(request, "members/member_view.html", {
        "member": member,
        "qr_base64": qr_base64
    })

def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", status=403)

from .models import Badge

@login_required
@active_member_required
def badge_board(request):
    badges = Badge.objects.prefetch_related('memberbadge_set__member')
    return render(request, "members/badges.html", {"badges": badges})

