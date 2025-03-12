import io
from zipfile import ZipFile
from django.shortcuts import render, redirect, get_object_or_404
from .models import Day
from django.utils import timezone
from datetime import timedelta
from .forms import DayForm  # Make sure you have this import
from django.http import HttpResponse, Http404
import datetime
from pytz import UTC
def index(request):
    today = timezone.now()
    nearest_days = Day.objects.filter(date_time__lte=today).order_by('-date_time')[:7]
    
    if request.method == "POST":
        form = DayForm(request.POST)
        if form.is_valid():
            # Extract the date from the submitted form
            date_time = form.cleaned_data['date_time']
            alias = form.cleaned_data['alias']
            day = date_time.day
            day_month = date_time.month
            day_year = date_time.year
            new_date_time = timezone.make_aware(datetime.datetime(day_year, day_month, day, 12, 0, 0), timezone.get_default_timezone())
            existing_alias = Day.objects.filter(alias = alias).first()
            # Check if a Day with the same day, month, and year already exists
            existing_day = Day.objects.filter(date_time__day = day, date_time__month=day_month, date_time__year=day_year).first()
            if existing_day:
                # Redirect to the edit page of the existing Day
                return redirect('edit_day', day_id=existing_day.id)
            elif existing_alias:
                # Redirect to the edit page of the existing Day with the same alias
                return redirect('edit_day', day_id=existing_alias.id)
            else:
                # Create a new Day object manually
                new_day = Day(
                    alias=form.cleaned_data['alias'],
                    date_time=new_date_time,
                    activities=form.cleaned_data['activities'],
                    workout=form.cleaned_data['workout'],
                    academic=form.cleaned_data['academic'],
                    sr=form.cleaned_data['sr'],
                    economics=form.cleaned_data['economics']
                )
                new_day.save()
    else:
        form = DayForm()

    return render(request, 'days/index.html', {'nearest_days': nearest_days, 'form': form})

def search(request):
    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')
    days = Day.objects.none()  # Start with an empty queryset

    if month and year:
        # Filter Days based on the provided month and year
        days = Day.objects.filter(date_time__day = day, date_time__month=month, date_time__year=year)
    
    return render(request, 'days/search.html', {'days': days})

def edit_day(request, day_id):
    day = get_object_or_404(Day, id=day_id)
    if request.method == "POST":
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DayForm(instance=day)
    
    return render(request, 'days/edit_day.html', {'form': form, 'day': day})

def export(request):
    if request.method == "POST":
        # Specific date inputs
        specific_day = request.POST.get('specific_day')
        specific_month = request.POST.get('specific_month')
        specific_year = request.POST.get('specific_year')

        # Range date inputs
        start_day = request.POST.get('start_day')
        start_month = request.POST.get('start_month')
        start_year = request.POST.get('start_year')
        end_day = request.POST.get('end_day')
        end_month = request.POST.get('end_month')
        end_year = request.POST.get('end_year')

        zip_buffer = io.BytesIO()
        zip_filename = ""

        with ZipFile(zip_buffer, 'w') as zip_file:
            if specific_day and specific_month and specific_year:
                # Construct specific datetime
                specific_date_str = f"{specific_year}-{specific_month.zfill(2)}-{specific_day.zfill(2)}"
                specific_datetime = datetime.datetime.strptime(specific_date_str, '%Y-%m-%d')
                specific_datetime = UTC.localize(specific_datetime)
                specific_datetime = specific_datetime.astimezone(timezone.get_default_timezone())
                # Attempt to fetch the specific Day object
                try:
                    day = get_object_or_404(Day, date_time__day=specific_day, date_time__month=specific_month, date_time__year=specific_year)

                except Http404:
                    return render(request, 'days/export.html', {
                        'error': f"No Day found for {specific_date_str}."
                    })
                
                # Prepare the content for the specific day
                filename = f"Day({specific_date_str}).txt"
                content = (f"Alias: {day.alias}\n"
                           f"Date: {day.date_time}\n"
                           f"Activities: {day.activities}\n"
                           f"Workout: {day.workout}\n"
                           f"Academic: {day.academic}\n"
                           f"SR: {day.sr}\n"
                           f"Economics: {day.economics}\n")
                zip_file.writestr(filename, content)

                zip_filename = f"Day({specific_date_str}).zip"
    # Set the buffer to the beginning
                zip_buffer.seek(0)

                # Prepare the response for file download
                response = HttpResponse(zip_buffer.read(), content_type='application/zip')
                response['Content-Disposition'] = f'attachment; filename={zip_filename}'

                # Return the response immediately
                return response

            elif (start_day and start_month and start_year and
                  end_day and end_month and end_year):
                # Construct start and end datetime
                start_date_str = f"{start_year}-{start_month.zfill(2)}-{start_day.zfill(2)}"
                end_date_str = f"{end_year}-{end_month.zfill(2)}-{end_day.zfill(2)}"
                
                start_datetime = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
                start_datetime = UTC.localize(start_datetime)
                start_datetime = start_datetime.astimezone(timezone.get_default_timezone())

                end_datetime = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')
                end_datetime = UTC.localize(end_datetime)
                end_datetime = end_datetime.astimezone(timezone.get_default_timezone())
                end_datetime = end_datetime.replace(hour=23, minute=59, second=59)

                # Filter Days that match the full datetime range
                days = Day.objects.filter(date_time__range=[start_datetime, end_datetime])
                
                if not days.exists():
                    return render(request, 'days/export.html', {
                        'error': f"No Days found between {start_date_str} and {end_date_str}."
                    })

            for day in days:
                local_date_time = day.date_time.astimezone(timezone.get_default_timezone())
                filename = f"{local_date_time.strftime('%Y-%m-%d')}.txt"
                content = (f"Alias: {day.alias}\n"
                        f"Date: {local_date_time}\n"
                        f"Activities: {day.activities}\n"
                        f"Workout: {day.workout}\n"
                        f"Academic: {day.academic}\n"
                        f"SR: {day.sr}\n"
                        f"Economics: {day.economics}\n")
                zip_file.writestr(filename, content)

            zip_filename = f"Days({start_date_str} - {end_date_str}).zip"

        zip_buffer.seek(0)

        # Prepare the response for file download
        response = HttpResponse(zip_buffer.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={zip_filename}'

        return response

    return render(request, 'days/export.html')
