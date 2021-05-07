from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Value, CharField, IntegerField
from django.db.models.functions import TruncDate
from django.shortcuts import render, redirect
from .forms import responses, Responses_Form
from django.contrib import messages
from .models import Responses, Profile
import time
from datetime import date
from .utils import motivation_data


# Create your views here.
@login_required
def form_view(request):
    # users = User.objects.all()
    form = responses()
    current_user = request.user
    resp = Responses.objects
    if current_user.is_superuser:
        return redirect('responses:dashboard')
    else:
        if request.method == 'POST':
            form = responses(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                # collect responses and save
                resp = Responses(
                    morale=data.get('rating'), top_goal=data.get('goal'), highlights=data.get('highlights'),
                    lowlights=data.get('lowlights'),
                    w_load=data.get('wload'), goal_obs=data.get('goal_obst'), m_tip=data.get('m_tip'),
                    employee=current_user,
                )
                resp.save()
                # messages.add_message(request, messages.INFO, )
                messages.success(request, 'Responses submitted successfully')
            else:
                form = responses()
                return redirect("/responses")
        # check if current month is filled

        try:
            last_update = Responses.objects.filter(employee=current_user). \
                latest('date').date.date().month
            if last_update == date.today().month:
                resp_status = True
        except:
            resp_status = False

        context = {
            'form': form,
            'resp_status': resp_status,
            'user_id': current_user.id
        }
        return render(request, "responses/form_index.html", context)

@login_required
def admin_view(request):
    current_user = request.user
    if current_user.is_superuser:
        user = request.user
        context = {
            'user': user
        }
        return render(request, "responses/admin_index.html", context)
    else:
        return redirect('responses:my_responses')


@login_required
def team_view(request):
    profiles = Profile.objects.all().values()
    # users = User.objects
    current_user = request.user
    if current_user.is_superuser:
        context = {
            'profile': profiles,
            'var2': 67
        }
        print(context)
        return render(request, "responses/team.html", context)
    else:
        return redirect('responses:my_responses')

@login_required
def team_member(request, pk):
    resps = Responses.objects.filter(employee_id=pk).values()
    team_member = Profile.objects.filter(id=pk).values()

    def team_member_name(team_member):
        if team_member.values_list()[0][3] is not None:
            name = f"Name: {team_member.values_list()[0][3]} {team_member.values_list()[0][4]}"
        else:
            name = f"Member ID:{team_member.values_list()[0][0]} ; "
        return name

    context = {
        'team_member': team_member_name(team_member),
        'resps': {
            'morale': resps.values()
        }
    }
    return render(request, "responses/single_team.html", context)

@login_required
def all_responses(request):
    resp = Responses.objects.all()
    current_user = request.user
    if current_user.is_superuser:
        context = {
            'profile_info': resp
        }
        return render(request, "responses/all_resp.html", context)
    else:
        return redirect('responses:my_responses')

@login_required
def analytics(request):
    current_user = request.user
    if current_user.is_superuser:
        all_users = len(User.objects.all())
        use_resp = Responses.objects.filter(date__year=date.today().year)
        groups, motivated, not_motivated = motivation_data(use_resp.values())
        arrow = lambda x: 'up' if x[-2] < x[-1] else 'down'

        context = {
            'user_count': all_users - 1,
            'month': [i for i in groups.Month],
            'morale': [i for i in groups.morale],
            'atm': groups.morale.to_list()[-1],
            'mot_arrow': arrow(groups.morale.to_list()),
            'motivated': motivated.shape[0],
            'not_motivated': not_motivated.shape[0]
        }
        return render(request, "responses/analytics.html", context)
    else:
        return redirect('responses:my_responses')

@login_required
def top_highlights(request):
    highligh = Responses.objects.all()
    context = {
        'highlight': highligh.values()
    }
    return render(request, "responses/highlights.html", context)


def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html")
