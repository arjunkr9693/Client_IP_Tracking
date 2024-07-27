from django.shortcuts import render
import ipinfo


def visitor_ip_info(request):
    # Extract IP address
    visitor_ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR')
    
    # Access token for ipinfo
    access_token = get_access_token()
    handler = ipinfo.getHandler(access_token)
    
    # Get IP details
    ip_details = handler.getDetails(visitor_ip)
    # Render details
    context = {
        'visitor_ip': visitor_ip,
        'ip_details': ip_details.all
    }
    return render(request, 'ipdetails/ip_info.html', context)


def get_access_token():
    try:
        with open('AccessToken.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("AccessToken.txt file not found.")
        return None
