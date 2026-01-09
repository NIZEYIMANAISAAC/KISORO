from .models import SiteInfo


def site_info(request):
    """Provide SiteInfo globally to templates (may be None until set in admin)."""
    site = SiteInfo.objects.first()
    return {'siteinfo': site}