[![Actions Status](https://github.com/Attendance-System-G14/SATS-Backend/workflows/Django%20CI/badge.svg)](https://github.com/Attendance-System-G14/SATS-Backend/actions)

## Student Attendance Tracking System(Backend)

The Student Attendance Tracking System is a complete package to mark the attendance of students enrolled in a course using camera clicked picture of the class.
- The attendance marking process would be simpler and less time consuming.
- Development of a transparent system with no scope for proxies.
- Scope for marking attendance manually if the application does not mark it itself.
	* The student raises a ticket to show that he was there in the picture of the class that was uploaded on the application.
	*  The TA(Teaching Assistant) to comment Yes/No for the faculty to mark attendance manually.
	* The faculty accepts/rejects the token, thereby marking the student present/absent.

The Backend is made in Django, a Python based web framework. Using this, the communications would be made to the frontend application (to be made in [Flutter](https://flutter.dev/)) using Django's [REST Framework](https://www.django-rest-framework.org/). 