from django.shortcuts import render
import serial
import time
from django.http import HttpResponseRedirect
from django.views import View


class Home(View):
      def get(self, request, *args, **kwargs):
        return render(request, 'Home.html')
"""     


# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        ser=serial.Serial("com9",9600)
        data = []
        for i in range(10):
            b = ser.readline()
            string_n = b.decode()
            string =string_n.rstrip()
            flt = string
            data.append(string)
            time.sleep(0.1)
        ser.close()
        print(data)
        ser.close()
        return render(request, 'Home.html', { 'read':data })
"""    