<! DOCTYPE html>
<html>
<head>
<link href="/css/bootstrap.css" rel="stylesheet">
<title>Meeting Rollcall</title>
</head>
<body>
<div class="container">
<p>
<a href="/show/done">Report</a>
</p>
<table class="table table-striped">
<tr>
    <th>Day</th>
    <th>Meeting Name</th>
    <th>Meeting Number</th>
    <th>Present?</th>
    <th>Notes</th>
</tr>
% for item in meetings:
% if item['present'] == 0:
%    presentstr = "icon-remove"
%  elif item['present'] == 1:
%    presentstr = "icon-ok"
% end
<tr>
    <td>{{ item['day'] }}</td>
    <td><a href="/show/{{ item['id'] }}">{{ item['name'] }}</a></td>
    <td>{{ item['number'] }}</td>
    <td><i class="{{ presentstr }}"</i></td>
    <td>{{ item['notes'] }}</td>
</tr>

%end
</div>
</body>
</html>
