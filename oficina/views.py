from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


from django.views.generic import TemplateView

# Create your views here.
class OfinaView(TemplateView):
	template_name = "oficina.html"

	@method_decorator(staff_member_required)
	def dispatch(self, *args, **kwargs):
		return super(OfinaView, self).dispatch(*args, **kwargs)

@staff_member_required
def ofina_views(request):
	context = {}
	return render(request, 'oficina.html', context)