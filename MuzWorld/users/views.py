from django.http import HttpResponse

def user(request, question_id):
	return HttpResponse("Here will be user %s" % question_id)

def music(request, question_id):
	return HttpResponse("Here will be music of user %s" % question_id)

def registration(request):
	return HttpResponse("Here will be registration")