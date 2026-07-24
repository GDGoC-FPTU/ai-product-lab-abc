@startuml
skinparam roundcorner 10
skinparam ActivityBorderThickness 1.5
skinparam defaultTextAlignment center

title Current-State Workflow: Transshipment Dispatching

start

#LightBlue:Request Received via System/Radio\n**[Handoff]**;

:Dispatcher Reads Request;

while (Is Request Clear?) is (No)
  :Contact Requester for Details;
  :Dispatcher Reads Request;
endwhile (Yes)

#Pink:🔴 **BOTTLENECK**\nManually search dashboard\nfor available vehicles\n*(Time: ~5 mins)*;

:Calculate ETA and Route manually\n*(Time: ~3 mins)*;

:Select Driver;

#Moccasin:Call/Message Driver with details\n**[Handoff]**;

:Update Excel/ERP status;

stop
@enduml
