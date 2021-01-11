from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import requests
from subprocess import Popen, PIPE, STDOUT


def create_directory():
    # ["python","easyaslinux/scripts/your_script_name.py","argument_here" ]
    command = ["bash", "django_script/scripts/test.sh", "create"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exitstatus = process.poll()
        if (exitstatus == 0):
            return {"status": "Success", "output": str(output)}
        else:
            return {"status": "Failed", "output": str(output)}
    except Exception as e:
        return {"status": "failed", "output": str(e)}


def delete_directory():

    command = ["bash", "django_script/scripts/test.sh", "delete"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exitstatus = process.poll()
        if (exitstatus == 0):
            return {"status": "Success", "output": str(output)}
        else:
            return {"status": "Failed", "output": str(output)}
    except Exception as e:
        return {"status": "failed", "output": str(e)}


@csrf_exempt
def file_maniputer(request):

    if request.method == 'POST':
        request_data = json.loads(request.body)

        if request_data["action"] == "create":
            data = create_directory()
        elif request_data["action"] == "delete":
            data = delete_directory()
        else:
            data = {"status": "not defined", "output": "not defined"}

        response = HttpResponse(json.dumps(
            data), content_type='application/json', status=200)
        return response
