from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import CrystalForm
import subprocess
from shutil import copyfile
import os
from os.path import join, isfile, isdir, exists


WORK_DIR = settings.WORK_DIR
CCTBX_ENV = settings.CCTBX_ENV
SCRIPT_DIR = settings.SCRIPT_DIR


# Create your views here.
def index(request):
    if not exists(WORK_DIR):
        os.mkdir(WORK_DIR)
    os.chmod(WORK_DIR, 0o777)
    if request.method == 'POST':
        form = CrystalForm(request.POST)
        if form.is_valid():
            a = str(form.cleaned_data['a'])
            b = str(form.cleaned_data['b'])
            c = str(form.cleaned_data['c'])
            alpha = str(form.cleaned_data['alpha'])
            beta = str(form.cleaned_data['beta'])
            gamma = str(form.cleaned_data['gamma'])
            space_group = str(form.cleaned_data['space_group'])
            low_res = str(form.cleaned_data['low_res'])
            high_res = str(form.cleaned_data['high_res'])
            # check if scripts exist in work_dir
            if not isfile(join(WORK_DIR, 'gen_sf.sh')):
                copyfile(join(SCRIPT_DIR, 'gen_sf.sh'), join(WORK_DIR, 'gen_sf.sh'))
            if not isfile(join(WORK_DIR, 'gen_sf.py')):
                copyfile(join(SCRIPT_DIR, 'gen_sf.py'), join(WORK_DIR, 'gen_sf.py'))
            subprocess.check_output(
                ['bash', join(WORK_DIR, 'gen_sf.sh'), CCTBX_ENV, WORK_DIR, space_group, a, b, c, alpha, beta, gamma, low_res,
                 high_res])
            with open('%s/sf.hkl' % WORK_DIR) as f:
                content = f.read()
            response = HttpResponse(content, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="sf.hkl"'
            return response
        else:
            return HttpResponse('%s' % str(form.errors))
    else:
        form = CrystalForm()
        template = 'crystal/index.html'
        return render(request, template, {'form': form})
