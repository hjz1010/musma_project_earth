from datetime import datetime, timedelta
from django import views
from pytz     import timezone, utc

from django.http       import JsonResponse
from django.views      import View
from django.db.models  import Q
from django.db.models import Avg, Min, Max, Count, F, Sum

from detections.models import Detection, State, Area

KST = timezone('Asia/Seoul')


class AnalysisView(View):
    def get(self, request):        
        select  = request.GET.get('select')  

        now            = datetime.utcnow()
        today_datetime = utc.localize(now).astimezone(KST)

        q = Q()

        if select == 'daily' or not select:
            q &= Q(datetime__date=today_datetime)
            working_time = 8*60*60

        elif select == 'weekly':
            weekday = today_datetime.weekday() # 0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일
            mon_datetime = today_datetime - timedelta(days=weekday)
            q &= Q(datetime__date__gte=mon_datetime)
            working_time = 5* 8*60*60
            
        elif select == 'monthly':
            month = today_datetime.month 
            q &= Q(datetime__month=month) 
            working_time = 20 * 5 * 8*60*60

        else :
            return JsonResponse({'message': 'Query Parameter Error'}, status=400)

        detection_by_period = Detection.objects.filter(q)  
        # print('기간내 데이터:',detection_by_period.count(),'개','\n','쿼리셋:',detection_by_period)

         ##### 이제 시리얼 넘버로 #########
        truck = detection_by_period.filter(detection_type__name = 'truck').values('area','serial_number').annotate(Count('serial_number'))
        equips = detection_by_period.exclude(detection_type__name = 'truck').values('serial_number').annotate(Count('serial_number'))
        equips_state = detection_by_period.exclude(detection_type__name = 'truck').values('serial_number', 'state').annotate(count=Count('state'))

        results = {
            'truck_count' : {
                area.name : truck.filter(area_id=area.id).count() 
                for area in Area.objects.all()
                }
            }

        for equip in equips:
            results[equip['serial_number']] = {
                state.equipment_state : equips_state.filter(state_id=state.id).count()*10 
                for state in State.objects.all()
                }
            serial_number = results[equip['serial_number']]
            serial_number['utilization_rate'] = (serial_number['travel'] + serial_number['load'] + serial_number['unload']) /working_time

        # results = {
        #     a: {
        #         state.equipment_state : equips_state.filter(state_id=state.id).count()*10 
        #         for state in State.objects.all()
        #         }
        #     equip['serial_number']['utilization_rate'] = (equip['serial_number']['travel'] + equip['serial_number']['load'] + equip['serial_number']['unload']) /working_time
        # for equip in equips
        # }
        
        # results['truck_count'] = {
        #     area.name : truck.filter(area_id=area.id).count()
        # for area in Area.objects.all()
        # }
        

        return JsonResponse({'message': 'SUCCESS', 'results': results},  status=200)
  